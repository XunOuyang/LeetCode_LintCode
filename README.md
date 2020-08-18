# LeetCode

Different types of problem

## Trie
## Dynamic Programming
#### 560, 974, 325
#### 
## DFS
## BFS
## Tree
## Linkedlist
## Two pointer
## Heap/Priority Queue
## Binary Search
## Backtrack
## Union_find
## Array
### continuous subarray

### Python 
#### collections.counter
The counter in python can be sorted, it can be sorted by either elements or frequency. 
```
for item in sorted(counter.items(), key=lambda item:item[1]):
  print(item)
```

#### nonlocal and global keyword
nonlocal will make the variable as the same of the variable with the same name but one layer outside.
global will make the variable as the same of the variable with the same name but the outermost one.

Without nonlocal:
```
x = 0
def outer():
    x = 1
    def inner():
        x = 2
        print("inner:", x)

    inner()
    print("outer:", x)

outer()
print("global:", x)

# inner: 2
# outer: 1
# global: 0
```
With nonlocal:
```
x = 0
def outer():
    x = 1
    def inner():
        nonlocal x
        x = 2
        print("inner:", x)

    inner()
    print("outer:", x)

outer()
print("global:", x)

# inner: 2
# outer: 2
# global: 0
```

With global:
```
x = 0
def outer():
    x = 1
    def inner():
        global x
        x = 2
        print("inner:", x)

    inner()
    print("outer:", x)

outer()
print("global:", x)

# inner: 2
# outer: 1
# global: 2
```

Reference: https://stackoverflow.com/questions/1261875/python-nonlocal-statement
