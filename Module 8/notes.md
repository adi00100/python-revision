#Module 8: File Handling, Exception Handling
##Context Managers
- Context managers are the objects that are used to manage resources for its proper allocation and releasing.
- Any object that has `__enter__` and `__exit__` method implemented can be used as context manager. 
- `__enter__` has the block of code that acquires the resources.
- `__exit__` has the block of code that releases the resources.
```
class File:
    def __init__(self,file_name,mode):
        self.file_name=file_name
        self.mode=mode
    
    def __enter__(self):
            self.file=open(self.file_name,self.mode)
            return self.file

    def __exit__(self,exc_type,exc_value,traceback):
            self.file.close()

with File("temp","w") as f:
      f.write("Hello world")
```
- If any error occurs within the with block then the error is passed to the `__exit__`  function which does the error handling.

##Reading and writing to Files
- Writing to file using write and writelines.
```
>>> ascii_lowercase
'abcdefghijklmnopqrstuvwxyz'
>>> a=[i+"\n" for i in ascii_lowercase]
>>> with open("temp","w") as file:
...     file.write("Writing from lists")
...     file.writelines(a)
```
- Reading from a file
```
>>> with open("temp","r") as file:
...     print(file.read())
...
Writing from listsa
b
c
d
e
f
g
h
i
j
k
l
m
n
o
p
q
r
s
t
u
v
w
x
y
z

>>>
```
##Python Exception
- Exception is a signal indicating that some error or unexpected behaviour has occured.
###Built in exception types
- Exception: Base class for all exception. New exception may be created by inheriting this class.
- FileNotFoundError
- ImportError
- IndexError: Raised when idex is not in range.
- ValueError: Raised when the function recieves an argument of the right tyoe but of inappropriate value.
-ZeroDivisionError
##Defining custom excption
```
class FactorialError(Exception):
    pass

def fac(a):
    if(a<0):
        raise FactorialError("Factorial of negative numbers are undefined.")
    elif(a==0):
        return 1
    else:
         return a*fac(a-1)

print(fac(-1))

$ python exception.py 
    print(fac(-1))
  File "C:\Users\adithya.pokharel\OneDrive - Cotiviti\Desktop\python\Python\Module 8\exception.py", line 6, in fac
    raise FactorialError("Factorial of negative numbers are undefined.")
__main__.FactorialError: Factorial of negative numbers are undefined.
```

##Exception Handling
- It is a mechanism that allows to handle any unexpected behaviour or errors.
```
try:
    #code that can raise error
except ExceptionType:
    #code to handle exception
finally:
    #code that gets executed if the exception is raised or not.
```


```
class FactorialError(Exception):
    pass

def fac(a):
    if(a<0):
        raise FactorialError("Factorial of negative numbers are undefined.")
    elif(a==0):
        return 1
    else:
         return a*fac(a-1)

try:
    fac(-1)
except FactorialError:
    print("Calculaiting factorial of negative number is not possible")
finally:
    print("Calculation of factorial completed.")

COTIVITI+adithya.pokharel@DESKTOP-U7S5KDH MINGW64 ~/OneDrive - Cotiviti/Desktop/python/Python/Module 8 (master)
$ python exception.py 
Calculaiting factorial of negative number is not possible
Calculation of factorial completed.
```