# Module 3: Literals, Variables and Operators 
## Operators
Operators are special symbols that does some operation on operands.
`a=b/c`
Here the '/' operator divides b by c and the '=' operator assigns the value to c.

## Numeric operator
- Addition:+
- Subtraction:-
- Float Division:/
- Absolute Division://
- Multiplication:*
- Exponential:**


### floating point accuracy
- Since floating point numbers are stored as binary due to which they aren't represented accurately.
- Eg:
```
>>> (0.1+0.2)==0.3
False
```
```
>>> 0.1+0.2
0.30000000000000004
```
- Decimal module can be used to set the precision level.

```
>>> (Decimal("0.1")+Decimal("0.2"))==Decimal("0.3")
True
```
## Unary and Bitwise Operators
### Unary Operator
- Positive(+):
```
>>> a=1
>>> +a
```
- Negative(-):
```
>>> a=1
>>> -a
-1
```
- Not(not):
```
>>> not True
False
```
### Bitwise Operator
- Bitwise AND(&)
```
>>> a=0b110
>>> b=0b001
>>> 
```
- Bitwise OR(|)
```
>>> a=0b110        
>>> b=0b001 
>>> bin(a|b)
'0b111'
```
- Bitwise XOR(^)
```
>>> a=0b110 
>>> b=0b001  
>>> bin(a^b)
'0b111'
```
- Bitwise NOT(~)
```
>>> a=0b000
>>> ~a  
-1
```
- Left Shift(<<)
```
>>> a=0b001
>>> bin(a<<1)
'0b10'
```
- Right Shift(>>)
```
>>> a=0b100   
>>> bin(a>>1)
'0b10'
```
## Boolean Operators
### Boolean Operator
- and: returns true if both operand is true `a and b`.
- or: return true if any operand is true `a or b`.
- not:retuns true if the operand is false `not <operand>`.
### Comparision Operator
- ==: returns true if value of both operands are same
- !=: returns true if value of both operands are not same
- <: returns true if value of operand in the left is less than the operand at right.
- >: returns true if operand at left is greater than operand at right.
- <=: returns true if operand at left is smaller or equals to operand at right.
- >=: returns true if operand at left is greater or equals to the operand at right.
## Comments
- Single line comments are written using # before comments
```#this is a comment```
- Multiline comment are written inside '''...'''.
```
'''
This
is
a 
comment
'''
```
## Strings and its operators
- Strings are a sequence of characters.
- Strings are by default stored as unicodes.
- Done in module 5

#### Using variables with string
```
>>> first="Adithya"
>>> last="Pokharel"
>>> f"{first} {last}"
'Adithya Pokharel'
>>> "{} {}".format(first,last)
'Adithya Pokharel'
```