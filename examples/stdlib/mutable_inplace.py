"""
This example is concerned with the difficulty of typing binary operators.

When augmented assignment is performed on a mutable collection, the collection
is mutated in-place. In other words, `x += y` and `x = x + y` are not necessarily the same.
It depends on the specific implementation of the runtime type (whether it implements
__iadd__ or not). Therefore it is not safe to make assumptions on the abstract level:

```py
xs = [1, 2, 3]
ys = xs
ys += [4]
assert xs == [1, 2, 3 ,4]

# whereas:
xs = [1, 2, 3]
ys = xs
ys = ys + [4]
assert xs == [1, 2, 3]
```

Yet, despite this, both mypy and pyright allow the use of in-place operators for types that implement `__OP__`, even if they
don't implement `iOP`. While it is true at runtime that the presence of `__OP__` suffices to be able to use the `<OP>=`
operator, it's only statically sound iff the in-place `__iOP__` in subclasses has the same interface as the (not in-place)
`__OP__` in the superclass (because of the duality of `<OP>=` and the Liskov substitution principle).

Mypy (and I'm assuming pyright) do in fact implement a consistency guard between `__OP__` and `__iOP__` to guarantee this soundness.
However, this consistency guard in turn is way to restrictive, because it simply doesn't allow *any* covariant types to define
any operators that do any sort of addition (in the general sense off the word: to add something to the object, e.g. `+=`, `|=`,
...), with concrete types that implement the in-place operators. Because the signature of `__iOP__` would have to accept `T`,
where `T` is the covariant type var (otherwise adding the value can not be allowed), but `__OP__` *must not* accept `T` if it
is covariant. This is a direct contradiction with the consistency check implemented by the type checkers.

The above shows that the assumption that `__OP__` implies that `<OP>=` is supported, makes it impossible to correctly define
covariant types such as `collections.abc.Set`, as proven by the necessary type ignores in the built-in `set` signature in `typeshed`.

These type ignores in turn, break the assumption about `__OP__` and `__iOP__` consistency, which causes the unsoundness in this
example.

What follows below is a more elaborate and detailed analysis of this situation, that should serve to confirm the statements made
above. It was (mostly) copied from a comment is the discussion thread for JelleZijlstra/unsoundness#20, and included here to
have a full and centralized overview of the cause for the unsoundness in this example.

# Overview

We'll start with the facts, without getting into motivation or consequences:
1. Mypy doesn't allow you to use the generic type var or `Self` in argument types for `__OP__` on covariant types.
2. Mypy requires the signature for `__OP__` and `__iOP__` to be compatible. In practice I think that means the same or more generic, as if `__iOP__` is an override of `__OP__`.
3. `collections.abc.Set.__or__` is [defined broadly](https://github.com/python/typeshed/blob/df3b5f3cdd7736079ad3124db244e4553625590c/stdlib/typing.pyi#L684) as `__or__[_T](self, other: AbstractSet[_T]) -> AbstractSet[_T_co | _T]` (3.12 syntax for clarity). It takes another set of some type, and returns a set that contains either / both type(s).
4. stdlib's `set` refines `__or__`'s return type to be a concrete set, but otherwise keeps it the same. It has a [narrow definition](https://github.com/python/typeshed/blob/df3b5f3cdd7736079ad3124db244e4553625590c/stdlib/builtins.pyi#L1244) for `__ior__`: `__ior__(self, value: AbstractSet[_T], /) -> Self`, where `_T` is `set`'s own type var. It takes a set of its own type, and returns itself (modified, though that's not expressed in the signature of course.
5. stdlib has a type ignore on `set`'s `__ior__`.
6. mypy reasons that if a type defines `__or__`, it supports both `|` and `|=`, because according to the Python docs, it does (at least at runtime).

# Analysis

Before we dive into the specifics of these six facts, let's look at how all this plays together to result in the unsound behavior. `collections.abc.Set`'s definition of `set.__or__` (3), in combination with 6, leads mypy to accept `|=` with differently typed sets on the left and right side of the operator. For runtime sets that do not implement `__ior__`, that works out great because it would return a new set. But for the builtin `set`, this results in the left-hand set being updated, and stepping out of its type constraints. stdlib's `set` tries to mitigate this through its signature for `__ior__`: it only allows its own type for the right hand side. But of course, the abstract base type does not see or have this signature, so mypy does not see it.

So, let's deep a bit deeper into each of the above:
1. Makes perfect sense, and is a broadly applied rule.
2. In a way, `__iOP__` is indeed an override of `__OP__`, in the sense that it refines the definition of the `<OP>=` operator. But there is one huge issue with this, and the consistency requirement is somewhat arbitrary. Let's cover the other points first, and then get back to this with a better overall view on the situation.
3. Makes sense. Both because it has to be defined such due to 1, and because conceptually, a union could be multi-type, no problem there.
4. Makes perfect sense (except that it breaks 2, but we'll get to that). You can not expect an in-place update method to accept anything but a set of the same type. That would allow you to insert unsound values (hmm, that sounds familiar...).
5. It shouldn't, but it has to because of 4 and 2.
6. I still see issue with this, but we'll get to that.

# Conclusions

Ok, now that we've covered the bases, let's have a critical look at all this.

I think we can safely conclude that 2 and 6 are tightly coupled. 2 is required because 6 exists. If we were to change 2 without changing 6, we'd end up with more unsoundness, and vice versa (as proven by the type ignore). 2 is not required by itself, because the two definitions only need to be consistent if `<OP>=` is supported *and* `__iOP__` is not implemented but refined by a subtype. That is the mode that 6 exposes. Without that mode, this scenario could never exist.

Another conclusion I think we can safely draw is that a broad definition, as in 3, is *always* the appropriate definition for `__OP__`, both due to 1, and simply because if we're returning a new object, there's really no reason to be restrictive.

A final conclusion is that a narrow definition for `__iOP__`, as in 4, is *always* the appropriate definition for `__iOP__` (the ones that extend the object. The others are already defined broadly, as is appropriate, see e.g. `set.__isub__`): you can't extend the object with something of a different type. I mean, you can at runtime, but it's not sound in a static type system.

Huh, that's interesting. These are contradictory conclusions. We conclude that 3 and 4 are always appropriate. So that must mean that 2 is simply too restrictive: it doesn't allow *any* sound definition of a covariant base type that offers `__OP__`, with concrete types that expand it with `__iOP__`. It will have got to go. And we can only get rid of 2 if we also get rid of 6. If we do both, we end up with a system that allows both 3 and 4, without ignores, and without the unsoundness that this whole thread is about.

So, while the type ignores are indeed a problem, I also think they are very much required. The real problem stems from the fact that they will always be required. And therefore the type checkers' assumption in 6 simply can not hold. Or at least that it essentially prohibits abstract covariant types from defining any operators at all.

# Solutions

The obvious solution seems to be to update mypy (and pyright I'm assuming) to drop the assumption that if `__OP__` is defined, the type supports `<OP>=`. As a bonus, it would also ensure that supposedly immutable types may be mutated, because that could be implemented now even without type ignores.

I should disclaim, what I propose would be a solution to *this* problem. I do not know for sure if it might create other problems elsewhere, and if those can be soundly solved. This is something that would need to be investigated and discussed further. But I think that the first step has to be that this premise is accepted and acknowledged: the way mypy handles this know is simply broken for covariant abstract types like `collections.abc.Set`. And not in some subjective way that could be addressed by a strict mode, but objectively, in all such cases.

But for certain other types, we have to make sure that `<OP>+` keeps on working. e.g. consider `int`'s `+=`. We'll have to find a way to drop the broken assumption, without breaking types like `int` in the meantime. It is still unclear if such an approach exists, or what it would look like.
"""
# TODO: update description with analysis from PR thread

from collections.abc import Set as AbstractSet


def func(x: int) -> str:
    # should not be mutable and should only contain ints
    result: AbstractSet[str] = set()
    other: AbstractSet[object] = result
    # At the time of writing, pyright seems to ignore the annotation on other in favor of its inferred type.
    # reveal_type reveals that it considers other a built-in set. As a result, pyright is unsound for this example, like mypy,
    # but for a different root cause. For a more elaborate example that showcases the same root cause for pyright, see
    # mutable_inplace_indirect.
    other |= {x}
    return next(iter(result))
