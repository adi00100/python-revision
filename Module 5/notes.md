#Module 5: Data types 
- Classification of data based on the type of values it holds. Eg.: float,int,str,etc.
##Strings
- Sequence of characters.
- Built in data type.
`msg="Hello World"`
##string function and methods
- len():returns length of string.
```
>>> a="Hello World"
>>> len(a)
11
```
- lower():Convert all characters to lowercase
```
>>> a.lower()
'hello world'
```
- upper():Convert all characters to uppercase.
```
>>> a.upper()
'HELLO WORLD'
```
- strip():remove whitespace from left and right. lstrip() and rstrip() can be used to remove whitespacefrom left and right respectively.
```
>>> a="   Hello  "
>>> a.strip()
'Hello'
>>> a.rstrip()
'   Hello'
>>> a.lstrip()
'Hello  '
```
##string methods
- replace(): Replaces all occurances of a substring with another substring.
```
>>> a="Hello"
>>> a.replace("ll","")
'Heo'
```

##string slicing
String slicing allows one to extract a portion of string by specifying the starting and ending indices.
`string[start:end:step]`

```
>>> a[0::2]
'Hlo'
```

##Introduction to List
- Collection data type that allows to store an ordered sequence of elements of different data types.
###Functions
- len():returns the number o elements in the sequence.
```
>>> a=[1,2,3]
>>> len(a)
3
```
- max():Returns the maximum item from list.
```
>>> max(a)
3
```
- sorted():Returns a new sorted list.
```
>>> a=[2,4,51,3,51]
>>> sorted(a)
[2, 3, 4, 51, 51]
```
###Methods
- append():Adds an item to the list.
```
>>> a=[1,2,3]
>>> a.append(4)
>>> a
[1, 2, 3, 4]
```

- extend():Adds an items of another list to the existing list.
```
>>> a=[1,2,3]
>>> a.extend([5,6,7])
>>> a
[1, 2, 3, 5,6,7]
```

- insert(): inserts an item to the speciic position.
```
>>> a
[1, 2, 3, 4, 2]
>>> a.insert(2,100)
>>> a
[1, 2, 100, 3, 4, 2]
```
- remove():Removes the first occurance of item from a list.
```
>>> a
[1, 2, 100, 3, 4, 2]
>>> a.remove(2)
>>> a
[1, 100, 3, 4, 2]
```
- pop():Remmoves and returns the item in the specified index.If no index is speciied then returns the last item. 
```
>>> a
[1, 100, 3, 4, 2]
>>> a.pop(1)
100
>>> a
[1, 3, 4, 2]
```
- index():returns the position of the first occurance of the given item.
```
>>> a
[1, 3, 4, 2]
>>> a.index(3)
1
```
- count():Returns the number of occurance of an item in the list.
```
>>> a=[1,1,1,]
>>> a.count(1)
3
```

- sort(): Sorts the list as specified.
```
>>> a=[2,1,4,6,2]
>>> a.sort()
>>> a
[1, 2, 2, 4, 6]
```
- reverse(): Reverses the order of items in a list.
```
>>> a
[1, 2, 2, 4, 6]
>>> a.reverse()
>>> a
[6, 4, 2, 2, 1]
```
##Nested List
- List that have another list as an item.

```
>>> [1,2,3,[1,2,3]]
[1, 2, 3, [1, 2, 3]]
```

##Intro to tuples and dictionaries
###Tuples
- Tuples ar immutable collection of elements i.e they cannot be modified once created.
- elements can be accessed as `<tuple_nam>[<index>]`
```
>>> (1,2,3)
(1, 2, 3)
```
###Dictionary
- Dictionaries are unordered collection of key-value pairs where each key is unique and and associated with a value.
```
>>> {"apple":2,"mango":4}
{'apple': 2, 'mango': 4}
```
##Dictionary Methods
- clear(): Removes all items from the dictionary.

- copy(): Returns a shallow copy.
```
>>> b=a.copy()
>>> b
{'apple': 2, 'mango': 3, 'cherry': 4}
```
- fromkeys(): Returns a new dictionary with keys from the iterable and values set to the default values.

- get():Returns the value for given key.
```
>>> a
{'apple': 2, 'mango': 3, 'cherry': 4}
>>> a.get('apple')
2
```
- items():Returns a view object that has the list of key-value pairs.
```
>>> a.items()
dict_items([('apple', 2), ('mango', 3), ('cherry', 4)])
```
- keys(): Retutns a view object that has the list of keys.
```
>>> a.keys()
dict_keys(['apple', 'mango', 'cherry'])
```
- pop():Removes and returns the value of the given key.
```
>>> a.pop("apple")
2
>>> a
{'mango': 3, 'cherry': 4}
```
- popitem(): Removes and returns the last inserted key-value pair from the dictionary.
```
>>> a
{'mango': 3, 'cherry': 4}
>>> a.popitem()
('cherry', 4)
```
- setdefault(): Returns the value for the given key if it exists in the dictionary ,otherwise sets the key to the default value and returns the value.
```
>>> a={'a':1,'b':2,'c':3}
>>> a.setdefault('c')
3
>>> a.setdefault('d')
>>> a
{'a': 1, 'b': 2, 'c': 3, 'd': None}
```
- update(): Updates the dictionary with key-value pairs from another dictionary or iterable.
```
>>> a
{'a': 1, 'b': 2, 'c': 3, 'd': None}
>>> b={'e':4,'f':5}
>>> a.update(b)
>>> a
{'a': 1, 'b': 2, 'c': 3, 'd': None, 'e': 4, 'f': 5}
```
- values(): Returns a view object that contains the value of the dictionary.
```
>>> a.values()
dict_values([1, 2, 3, None, 4, 5])
```
##Sets
Sets are collection of an unordered and unindexed datatype that has no duplicate elements.
```
>>> a={1,2,3,257,257}
>>> a
{1, 2, 3, 257}
```
###Methods of set
- add(): Adds an item to the set.
```
>>> a
{1, 2, 3, 4}
>>> a.add(10)
>>> a
{1, 2, 3, 4, 10}
```
- clear(): Removes all elements from the set.
```
>>> a
{1, 2, 3, 4, 10}
>>> a.clear()
>>> a
```
- copy(): Returns a copy of the set.
```
>>> int={1,2,3,4}
>>> int.copy()
{1, 2, 3, 4}
```
- difference(): Removes all items of a given set from existing set and returns the set.
```
>>> a={1,2,3,4}
>>> a.difference({2,3})
{1, 4}
```
- difference_update(): Removes all items from the given set and  
updates the existing set with the new set.
```
>>> a
{1, 2, 3}
>>> a.difference_update({2})
>>> a
{1, 3}
```
- discard(): Removes an item from the set.
```
>>> a={1,2,3,4}
>>> a.discard(2)
>>> a
{1, 3, 4}
```
- intersection():Returns the set of all elemens that are common in both.
```
>>> a.intersection({2,3,4,5})
{2, 3, 4}
>>> a={1,2,3,4}
>>> a.intersection({2,3,4,5})
{2, 3, 4}
```
- intersection_update(): Updates the set with the intersection of two sets.
```
>>> a
{1, 2, 3, 4}
>>> a.intersection_update({2,3,4,5})
>>> a
{2, 3, 4}
```
- union():Returns a set object that has elements of both set.
```
>>> a={1,2,3,4,5}
>>> a.union({8,9,10})
{1, 2, 3, 4, 5, 8, 9, 10}
```
- update():Updates the existing set with the elements of given set.
```
>>> a={1,2,3,4,5}
>>> a.update([6,7,8,9])
>>> a
{1, 2, 3, 4, 5, 6, 7, 8, 9}
```