# Sequences and its type
  - Sequences are containers with items stored in a deterministic ordering. Each sequence data type comes with its unique capabilities.
  - Strings- the string is a sequence of Unicode characters written inside a single or double-quote.They are immutable.
  - Lists-Lists are a single storage unit to store multiple data items together. It’s a mutable data structure, therefore, once declared, it can still be altered [].
  - Tuples-Just like Lists, Tuples can store multiple data items of different data types. The only difference is that they are immutable and are stored inside the parenthesis ().
  - Byte Sequences-The bytes() function returns an immutable bytes sequence in between quotes, preceded by a ‘B’ or ‘b’.
  - Byte Arrays-Just like bytes sequence, bytes arrays also return a bytes object. The only difference is that they are mutable. 
  - Range()-It returns a sequence of integers in the specified range. By default, it starts the sequence from 0 (if not specified). 

# Difference between Strings,Lists and Tuples
  - Strings-A sequence of characters, Immutable, Supports Indexing and Slicing , Fast for text operations, Used for text processing.
  - Lists-An ordered mutable collection, Supports Indexing and Slicing, Slower due to mutability, Used for dynamic collections.
  - Tuples-An ordered immutable collection, Supports Indexing and Slicing, Faster due to immutability, Used for fixed collections.

# Indexing with Example
  - Indexing is a way to access elements in sequences like strings, lists, and tuples using their position.
  - Python uses zero-based indexing, meaning the first element is at index 0.
  - Negative indexing (-1, -2, etc.) allows access from the end.
  - Works on strings, lists, tuples, and other iterable objects.

# What is the result of `len([1, [2, 3], 4])` and why?
  - output- 3
  - The len() function counts top-level elements in the list.

# Slicing
  - Slicing is a technique to extract a portion of a sequence (string, list, or tuple) using the syntax:
  - sequence[start:stop:step]

# What will `my_tuple = (1, 2, 3); print(my_tuple[1:])` output?
  - Output-(2,3)

#  Explain the difference between `list.append()` and `list.extend()`
   - list.append()-Adds a single element to the end of list.
   - list.extend()-Adds each element of an iterable to the list individually. 
   - list=[1,2,3]; list.append([4,5]); output-[1,2,3,[4,5]]
   - list=[1,2,3]; list.extend([4,5]); output-[1,2,3,4,5]
# Write code to split the sentence: "Learn Python, step by step!" into words.
   - str="Learn Python, step by step!"
   - print(str.split())

# Join a list `['Python', 'is', 'fun']` into a single string.
   - l=['Python', 'is', 'fun']
   - print(' '.join(l))

# Given a list `numbers = [1, 2, 2, 3, 4, 2]`, find the index of the first `2`.
   - numbers = [1, 2, 2, 3, 4, 2]
   - print(numbers.index(2))
