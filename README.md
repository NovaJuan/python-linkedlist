# python-linkedlist
Linked List created using python, and implemented in a friends list CLI.

> Author: Juan Romero (NovaJuan)

## Technologies used:
- Python 3.7.4
---
## Run the demo
1. Clone the repo
   ```
   $ git clone https://github.com/NovaJuan/python-linkedlist.git
   ```
2. Change directory to the repo folder
   ```
   $ cd python-linkedlist
   ```
3. Run the `main.py` file to run the Demo
   ```
   $ python main.py
   ```
---
## How to use the Linked list
To use it, you have to import the `LinkedList` class into the file you goint to use, then initialize with a class with all the properties and methods you want in each elemente of the list.

When adding an new element, you use keywords to each property, the method extract those keywords and create a instance of the class. THE KEYWORDS HAVE TO MATCH EACH PROPERTY OF THE CLASS.

### Instance Methods
* ``insert()``: Add a element to the list, can be in the beginning (index parameter not used) or in an specific index (index parameter used)
  ```
  linkedlist.insert(index,property1=value1,property2=value2...)
  ```
* ``append()``: Add a element to the end of the list.
  ```
  linkedlist.append(property1=value1,property2=value2...)
  ```
* ``remove()``: Remove a element on a specific index, and if index is not present remove the first element of the list.
  ```
  linkedlist.remove(index)
  ```
* ``foreach()``:Loop at each element and pass the data as a paramenter into the given function.
  ```
  linkedlist.foreach(func)
  ```
* ``pop()``: Remove the last element of the list.
  ```
  linkedlist.pop()
  ```


### Example
```
from linkedlist.py import LinkedList


class User:
    name = None
    age = None

    def __init__(self,name,age):
        self.name = name 
        self.age = age 


users = LinkedList(User)


users.append(name='John',age=21)
```