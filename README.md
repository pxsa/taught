# Taught

This repo is dedicated to what I've taught to my students at school.

## Table of Contents

- [Common Data Structures](#common-data-structures-in-python)
  - [Dictionaries](#dictionaries-maps-and-hashtables)
  - [Key Takeaways](#key-takeaways)
- [Arrays](#array-data-structures)

## Common Data Structures in Python

Data structures are something that every Python learner and developer should learn about. Ofcourse they're the basis and fundamental things to know.

### Dictionaries, Maps and Hashtables

Python dictionaries or `dicts` for short are a central data structure. Simply it's just an array with key-value pairs. For example `Phone books`.

```python
phonebook = {
    'hasan': 1234,
    'akram': 3432,
    'siavash': 8765,
}

squares = {x: x*x for x in range(1, 4)}

print(phonebook['akram']) # 3432
print(squares) # {1: 1, 2: 4, 3: 9}
```

Python dicts have time complexity of O(1) for lookup, insert, update, ande delete operations in the average case.

### Key Takeaways

- Dictionaries are the central data structure in Python.
- The build-in dict type will bo good enough most of the time.
- Specialized implementations. like read-only or ordered dicts, are available in the Python standard library.

### Array Data Structures

Arrays are another important and fundamental data structure in all programming alnguages, and in most of the algorithms they are used.  `Arrays` are fixed-size that allow each element to bo located based on its index. in the contrast with `linked list`, arrays tend to store elements near each other in the memory. The time complexity for accessing elements in an array is about O(1). Python hase several array-like data structures which each have slightly different characteristics.

- list - **Mutable Dynamic Arrays**

  - don't mixed up this with `linkedlist`.
  - It takes up more space as it can store all diffrent types.
  - It's a `dynamic array` behind the scenes. It means you can add or remove elements and the list will automatically adjust the backing store by allocation or releasing memory.

    ```python
    arr = ["shamsi", "kimia", "khodayar"]
    print(arr[0]) # shamsi
    print(arr) # ["shamsi", "kimia", "khodayar"]
    
    # list is MUTABLE ;)
    arr[0] = "khodaYar"

    del arr[1]
    print(arr) # ["khodaYar", "khodayar"]
    ```

- tuple - **Immutable Containers**

  - Like python list but tuples are Immutable. It means elements can't be added or removed dynamically. all elements in a tuple must be defined at creation time.

- array.array - **Basic Typed Arrays**

  - Just like python list but they just can accept only one single type.

  ``` python
    import array
    
    arr = array.array('f', (1.0, 1.5, 2.0))
    
    print(arr[1])
    arr[1] = 17.0
    print(arr) # array('f', [1.0. 17.0. 2.0])

    del arr[1]
  ```

- str - **Immutable Arrays of Characters**
- bytes - **Immutable Arrays of Single Bytes**
- bytearray - **Mutable Arrays of Single Bytes**

## Python class 2024

Join the following telegram channel for further  information and homeworks. `@pxsaTaught`
