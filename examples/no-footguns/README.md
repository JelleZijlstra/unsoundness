The "no-footguns" category hosts examples of unsoundness that do not require
the use of `Any`,`# type: ignore`, `@overload`, `typing.cast` or any other tools
that are loopholes in the type system by design.
This is arguably the most dangerous category, because you can crank your type checking
settings up to 11, forbid all the dangerous footguns and still miss bugs that type
checkers "ought to have found" in an ideal world.