Python 2.7.3 (default, Jun 22 2015, 19:43:34) 
[GCC 4.6.3] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> vars ()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, '__package__': None}
>>> __builtins__.input.__doc__
'input([prompt]) -> value\n\nEquivalent to eval(raw_input(prompt)).'
>>> print __builtins__.input.__doc__
input([prompt]) -> value

Equivalent to eval(raw_input(prompt)).
>>> from math import sin
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__doc__': None, '__name__': '__main__', '__package__': None, 'sin': <built-in function sin>}
>>> print sin.__doc__
sin(x)

Return the sine of x (measured in radians).
>>> import math
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__doc__': None, '__name__': '__main__', '__package__': None, 'sin': <built-in function sin>, 'math': <module 'math' (built-in)>}
>>> math.exp
<built-in function exp>
>>> print math.exp.__doc__
exp(x)

Return e raised to the power of x.
>>> import math as matematika
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, 'matematika': <module 'math' (built-in)>, '__doc__': None, '__name__': '__main__', '__package__': None, 'sin': <built-in function sin>, 'math': <module 'math' (built-in)>}
>>> matematika.log.__doc__
'log(x[, base])\n\nReturn the logarithm of x to the given base.\nIf the base not specified, returns the natural logarithm (base e) of x.'
>>> log(10,10)

Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    log(10,10)
NameError: name 'log' is not defined
>>> math.log(10,10)
1.0
>>> matematika log(10,10)
SyntaxError: invalid syntax
>>> matematika.log(10,10)
1.0
>>> from math import sin as sinuss
>>> sinuss(5)
-0.9589242746631385
>>> ================================ RESTART ================================
>>> 
>>> ================================ RESTART ================================
>>> 
>>> 
