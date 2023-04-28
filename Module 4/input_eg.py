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