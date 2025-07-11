# unsoundness

The aim of this repository is to collect examples of unsoundness in the
Python type system: code that produces a runtime error that the type system
should catch, but that is accepted by type checkers.

What is soundness, anyway? In general, type systems are defined to be sound
if they can prevent type errors from happening at runtime. But in Python,
TypeErrors can happen for many reasons, not all of which the type system can
prevent. Conversely, some other categories of errors, such as NameError and
AttributeError, should usually be flagged by a type checker. It's not obvious to
me how "soundness" would be defined for the Python type system.

This repo sets a more concrete goal: write a function that can be used to fool
a type checker into turning a value of one type into another. Concretely, we
collect pieces of code with the following properties:

* There is a `def func(x: int) -> str:`
* At runtime, the function returns any integer argument unchanged
* Type checkers accept the code without errors

I'm interested in any examples, from the most boring ones (such as using
`# type: ignore`) to tricky uses of type narrowing.

## Why?

People sometimes mention that the Python type system is not sound. I'd like
to make that statement more concrete by documenting ways in which it is not
sound. This serves an educational purpose; it can also help inform future
additions to the type system.

## Rules

I want to collect soundness issues in the type system itself, not just bugs
in type checkers. At the same time, while there is
[a spec for the Python type system](https://typing.python.org/en/latest/),
it is not always very precise, and end users use individual type checkers, not the spec
directly. Therefore, examples collected in this repo generally should either
follow from the spec, or work under multiple type checkers, or both.
The repo's CI validates that examples in the `examples/` repo are accepted
by both mypy and pyright.

Some unsound behaviors apply only to one type checker. If the unsoundness is the result of a
deliberate choice by that type checker (not just a bug), it can be added to the `nonexamples`
directory. Files in this directory should define a dictionary of the form
`ACCEPTED_BY = {"mypy": True, "pyright": False}` to indicate which type checkers accept the code
(that is, have unsound behavior).

If this doesn't work well in practice, let's talk about it!

## Categories

To organize the collection, we'll put the examples into some rough categories,
corresponding to subdirectories within the `examples/` directory:

* `Any`: use of `Any` (including implicit `Any` on unannotated code)
* `directives`: use of type checker directives that bypass type checking, such as `# type: ignore`
* `TypeGuard`: use of `TypeGuard`
* `TypeIs`: use of `TypeIs`
* `narrowing`: use of other type narrowing constructs
* `protocol`: related to protocols
* `overload`: related to overloads
* `typeddict`: related to `TypedDict`
* `stdlib`: related to type definitions for the standard library (defined in typeshed)
* `override`: unsafe overrides in subclasses that are not caught by the type system
* `tuple`: related to special-cased tuple types
* `runtime`: runtime manipulation of objects that the type system does not recognize
* `generic`: use of generic classes and functions
* `descriptors`: use of descriptors
* `ctx-managers`: related to context managers
* `metaclasses`: related to metaclasses

More categories can be added as needed.

## Contributing

Contributions to this repo are welcome! We run a CI script that validates examples
fulfill the repo's criteria. You can it locally too with `uv run --locked scripts/validate.py`.
