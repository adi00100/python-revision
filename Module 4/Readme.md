# Module 4: Input/Output Operations 
## Typecasting
- Process of converting one datatype to another datatype if compatible. Eg: float to int,list to set,etc.
- Example of converting a list object to set object:
```
>>> a=[1,1,2,3,4,1,2]
>>> set(a)
{1, 2, 3, 4}
```
## Input function
- input() is used to take input from user. The input() function always returns the string datatype so it should be typecasted to the required datatype.
```
>>> age=int(input("Enter your age:"))
Enter your age:20
```
## Print function
- Print function is used to display output to display or file. It can tae one or more arguments of different types and display their values on console or file.
`print(object(s), sep=separator, end=end, file=file, flush=flush)`
Eg:
```
>>> print("Hello","World",sep=' ',end='!\n',file=sys.stdout,flush=False)
Hello World!
```

## User Input from within python and through command line
```
# input_eg.py
from sys import argv

def range(start,stop,offset):
    while start<stop:
        print(start,end=" ")
        start+=offset

if __name__=="__main__":
    if(len(argv)==1):
        start=int(input("Enter the start of a range:"))
        stop=int(input("Enter the stop of a range:"))
        offset=int(input("Enter the offset:"))
        range(start,stop,offset)
    else:
        start,stop,offset=int(argv[1]),int(argv[2]),int(argv[3])
        range(start,stop,offset)
```
## Taking input from program
```
PS C:\Users\adithya.pokharel\OneDrive - Cotiviti\Desktop\intern\Python Revision\Module 4> python input_eg.py
Enter the start of a range:1 
Enter the stop of a range:10
Enter the offset:1
1 2 3 4 5 6 7 8 9 
```
## Giving input from command line
```
PS C:\Users\adithya.pokharel\OneDrive - Cotiviti\Desktop\intern\Python Revision\Module 4> python input_eg.py 1 10 1
1 2 3 4 5 6 7 8 9 
```