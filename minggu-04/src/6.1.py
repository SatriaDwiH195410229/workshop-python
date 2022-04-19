# There is a variant of the import statement that imports names from a module directly into the importing module’s symbol table. For example:
>>> from fibo import fib, fib2
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

# There is even a variant to import all names that a module defines:
>>> from fibo import *
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

# If the module name is followed by as, then the name following as is bound directly to the imported module.
>>> import fibo as fib
>>> fib.fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

It can also be used when utilising from with similar effects:
>>> from fibo import fib as fibonacci
>>> fibonacci(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377