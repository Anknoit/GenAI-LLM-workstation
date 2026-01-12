# Python Basics
Q1. How does Python handles memory management?
Memory = big warehouse

Objects (int, list, dict, string, etc.) = boxes stored in warehouse

Python = warehouse manager (you don’t manage it manually)

* variables dont store value they store references(address)
- Reference Counting
    - counts no. of variables pointing to an object(value)
    - if rc = 0, pthon removes the object from memory
- Generational Garbage Collection
    - Cyclical scan of rc pointing to each other only hence rc never gets 0, removes it in periodic scan

- Stack and Heap
    - stack stores variables pointing/referencing to objects
    - heap stores objects
    ```python
     a = [1,2,3]
     b = a
     ```
     ```css
    STACK                 HEAP
    -----                 ----
    a ───────┐
              ├────▶ [1, 2, 3]
    b ───────┘
    ```

- Memory Pooling/Interning
    - Reuse memory for small objects(because tracking validation for pooling or interning is memory intensive).
     WHY? because creating and destroying memory again and again is lame
    - use same memory for objects that are small and of similar value, only done for immutable objects (tuple)

Q2. What is the difference between shallow and deep copy?
- Shallow copy: creates a new object and copies the references of the original object to the new object.
- Deep copy: creates a new object and copies the values of the original object to the new object.

Q3. What is GIL? 
- GIL (Global Interpreter Lock) is a mutex that protects access to Python objects, preventing multiple native threads from executing Python bytecodes at once.
- Especially in cases like Refernce counting, Generational Garbage Collection, etc. 
- ```python
    a =  [1,2,3]
    a.append(4)
    ```
    - If there are multiple threads appending and deleting from the list, GIL ensures that only one thread can execute at a time.
    