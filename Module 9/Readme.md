# Module 9: Modules and Packages
## Modules
- Any .py file can be a module which can have variables or functions defined.
- A module can also be a related code that makes the logic easy to understand,
- A module is used in some program by importing the module using import keywoed.
- To import specific function or variables one can use `from <module_name> and <func/var>`
- In this folder math.py is a module.

## Variants of modules
- Built in modules:math,venv,random,etc.
- Third party modules:numpy,pandas,requests,django
- User-defined modules:Created by user. 
## \_\_name__
- Built-in special variable used to indicate if the module is imported by another module or being excuted as main variable.
- If it is imported then `__name__="<Name_Of_importing_Moduke>"`
- If it is being executed as main program then `__name__='main'`


## Packages in Python
- Collection of modules in a folder with \_\_init.py__ file.
- Eg of package_eg folder in "Module 9"
```
>>> import package_eg
>>> dir(package_eg)
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'math']       
>>> import package_eg.math
>>> dir(package_eg.math)
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'add', 'mul', 'sqrt', 'sub']
>>>
```