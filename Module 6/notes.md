# Module 6: Python Flow Control
## If else and elif
```
>>> def check(a):
...     if(a>100):
...             print("Greater than 100")
...     elif(a==100):
...             print("Equals 100")
...     else:
...             print("Less than 100")
...
>>> check(200)
Greater than 100
>>> check(100)
Equals 100
>>> check(0)
Less than 100
```
## pass:placeholder for function,conditinal statement,class,loop,etc.
```
>>> def test():
...     pass
...
>>> class C:
...     pass
...
>>> for i in range(10):
...     pass
...
```

## range:returns a generator that can produce a sequence of numbers.
`range(start,stop,step)`
```
>>> a=range(0,10)
>>> a
range(0, 10)
>>> for i in a:
...     print(i)
...
0
1
2
3
4
5
6
7
8
9
>>>
```
## while and for loop and else
```
>>> a=0
>>> while(a<10):
...     a+=1
...     print(a)
... else:
...     print("1-10 has been displayed successfully")
...
1
2
3
4
5
6
7
8
9
10
1-10 has been displayed successfully
>>>
```
```
>>> for i in range(10):
...     print(i)
... else:
...     print("1-10 has ben displayed successfylly")
...
0
1
2
3
4
5
6
7
8
9
1-10 has ben displayed successfylly
```

## Nesting Loops and Conditionals
```
>>> for i in range(10):
...     for j in range(10):
...             pass
...     else:
...             print("Inner loop completed {} times".format(i))
...
Inner loop completed 0 times
Inner loop completed 1 times
Inner loop completed 2 times
Inner loop completed 3 times
Inner loop completed 4 times
Inner loop completed 5 times
Inner loop completed 6 times
Inner loop completed 7 times
Inner loop completed 8 times
Inner loop completed 9 times
```
## Break and continue
```
>>> for i in range(10):
...     print(i)
...     if(i==5):
...             break
...     else:
...             continue
...
0
1
2
3
4
5
```
## List comprehension
```
>>> [i for i in range(10)]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```