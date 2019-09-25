### Problem:

You've created a button with a command but you want to pass an argument to that command.

### Solution:

Use Lambda

### Discussion

Python supports an interesting syntax that lets you define one-line mini-functions on the fly.
Borrowed from Lisp, these so-called lambda functions can be used anywhere a function is required.

```python
# Let's make a function that doubles the input x.
>>> def f(x):
...     return x*2
...
>>> f(3)
6


# Now let's make a lambda function that does the same thing and then assign it to the variable g.
>>> g = lambda x: x*2
>>> g(3)
6
```

The lambda function `g = lambda x: x*2` accomplishes the same thing as the function f().

Note the abbreviated syntax here: there are no parenthesis around the argument list, and the return keyword is missing)
as it is implied since the entire function can only be one expression. Also the function has no name but it can be
called through the variable it is assigned to.

