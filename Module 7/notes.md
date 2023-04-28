#Module 7: Introduction to Functions
##Creating Functions
- functions are created using `def` keyword.
```
>>> def hello(name):
...     print("Hello "+ name)
...
>>> hello("Adithya")
Hello Adithya
```
##Parameters and Arguments
- Parameters defines what a function takes as input.
- Arguments are the actual values/input passed to the function.
##Recursion
```
>>> def fact(a:int):
...     if(a<0):
...             print("Factorial of number <0 isn't possible")
...     elif(a==0):
...             return 1
...     else:
...             return a*fact(a-1)
...
>>> fact(5)
120
>>> fact(-1)
Factorial of number <0 isn't possible
>>> fact(0)
1
```
##Anonymous Function, lambdas
```
>>> a=lambda x:[i*i for i in x]
>>> a(range(10))
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```
- Sorting the letters are based on the UTF-8 encoding so "A" and "a" are not ordered serially.
```
>>> a=["A","B","b","a","c"]
>>> sorted(a)
['A', 'B', 'a', 'b', 'c']
```
- Sorting the same list by providing a key parameter with lambda function as argument. The lambda function takes the first character and returns a lower case.
```
>>> a=["A","B","b","a","c"]
>>> sorted(a,key=lambda x:x[0].lower())
['A', 'a', 'B', 'b', 'c']
```

```
>>> a=[1,2,3,4,5]
>>> sq=lambda x:[i**2 for i in x]
>>> sq(a)
[1, 4, 9, 16, 25]
```
##Python Scopes

##Global
- Any variable defined or declared outside in the global namespace.
- A variable can be defined global by using the global keyword inside a function but it must be invoked.
```
>>> g1="global variable withot global keyword"
>>> def test():
...     global g2
...     g2="global variable with global keyword in test()"
...
>>> globals()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'a': (1, 2, 3, [4, 5, 6, 10, 100]), 'g1': 'global variable withot global keyword', 'test': <function test at 0x00000174963CF040>}
>>> test()
>>> globals()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'a': (1, 2, 3, [4, 5, 6, 10, 100]), 'g1': 'global variable withot global keyword', 'test': <function test at 0x00000174963CF040>, 'g2': 'global variable with global keyword in test()'}
>>>
```
##Local
- Local variables are can be accessed and modified only within the functions they are defined.
```
>>> def test():
...     l_var="This can be accessed and modified only within test()"
...     print(l_var)
...
>>> test()
This can be accessed and modified only within test()
>>> print(l_var)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'l_var' is not defined
```
##nonlocal keywod
- In nested function if inner function wants to modify a variable that belongs to the outer scope then nonlocal can be used.
```
>>> def outer():
...     a="This is defined in outer scope"
...     def inner():
...             nonlocal a
...             a="This is defined in inner scope"
...             print(a)
...     inner()
...     print(a)
...
>>> outer()
This is defined in inner scope
This is defined in inner scope
```
##Shadowing (Hiding Names)
- Shadowing occurs when the local variabe has the same name as global variable. The variable in the global namespace gets hidden within the function.
