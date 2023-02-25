"""
lambda expression
One of Pythons most useful (and for beginners, confusing) tools is the lambda expression. lambda expressions allow us to create "anonymous" functions. This basically means we can quickly make ad-hoc functions without needing to properly define a function using def.

Function objects returned by running lambda expressions work exactly the same as those created and assigned by defs. There is key difference that makes lambda useful in specialized roles:

lambda's body is a single expression, not a block of statements.

The lambda's body is similar to what we would put in a def body's return statement. We simply type the result as an expression instead of explicitly returning it. Because it is limited to an expression, a lambda is less general that a def. We can only squeeze design, to limit program nesting. lambda is designed for coding simple functions, and def handles the larger tasks.
Lets slowly break down a lambda expression by deconstructing a function:


Lets slowly break down a lambda expression by deconstructing a function:

def square(num):
    result = num**2
    return result
square(2)
4
We could simplify it:

def square(num):
    return num**2
square(2)
4
We could actually even write this all on one line.

def square(num): return num**2
square(2)
4
"""

square = lambda x : x**2
print(square(2))

print(list(map(lambda x: x**2, [1,2,3,4,5,6])))


print(list(filter(lambda x: x % 2 ==0, [1,2,3,4,5,56,6,7,7,8])))