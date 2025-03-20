# Indexing Example
str="Python"
print(str[2])
print(str[-3])

list=['abc',2,5,'ef']
print(list[0])
print(list[-1])

# Last character of String
str="Python"
print(str[-1])

# List access third element
list=[1,2,3,4,5]
print(list[2])

# Slicing
numbers = [10, 20, 30, 40, 50, 60]
print(numbers[0:3])  # Output: [10, 20, 30]
print(numbers[-3:])  # Output: [40, 50, 60]
print(numbers[::2])  # Output: [10, 30, 50]

# Reverse String using Slicing
str="Python"
print(str[::-1])

# List Concatenation
l=[10,20,30]
l1=[2,3,5]
print(l+l1)

# List Repetition
l=[2,3,4]
print(l*3)

# Count Occurrence of Elements
l=[1,2,2,2,2,3,3]
print(l.count(2))
print(l.count(3)) 

# Check if string is palindrome
str=input()
a=str[::-1]
if(str==a):
 print("palindrome")
else:
 print("not palindrome")

# Implement a function that returns the length of the longest word in a sentence.
def length(str):
 word=str.split()
 return max(len(i)for i in word)

str=input()
print(length(str))

# Nested list indexing
l=[1,2,3,[4,5]]
print(l[3][0])

# How do you convert a list of characters into a string?
l=['a','b','c']
print(''.join(l))

# Remove duplicate in list
def remove(lst):
    ans=[]
    for i in lst:
        if i not in ans:
            ans.append(i)
    return ans
            
lst=[1,2,2,3,3,3,3,4,4]            
print(remove(lst))            

# Write a function that takes a list of tuples and sorts it by the second element of each tuple.
def sort(lst):
    return sorted(lst,key=lambda x:x[1])
    
tup=[(1,10),(3,5),(2,8)]
print(sort(tup))

# Implement a program to flatten a nested list of arbitrary depth.
def flatten(lst):
    ans=[]
    for i in lst:
        if isinstance(i,list):
            ans.extend(flatten(i))
        else:
            ans.append(i)
    return ans
    
lst=[1,[2,[3,4]]]
print(flatten(lst))

# Create a function that rotates a list to the right by k steps.
def rotate(lst,k):
    k=k%len(lst)
    return lst[-k:]+lst[:-k]
    
lst=[1,2,3,4,5]
k=2
print(rotate(lst,k))

# Given two strings, write a function that returns True if they are anagrams.
def ana(s1,s2):
    return sorted(s1)==sorted(s2)
    
s1=input()
s2=input()
print(ana(s1,s2))

# Create a function to split a list into chunks of a specified size.
def split(lst,size):
    ans=[]
    for i in range(0,len(lst),size):
        ans.append(lst[i:i+size])
    return ans
lst=[1,2,3,4,5,6,7,8,9]
size=3
print(split(lst,size))

# Implement a function that merges two sorted lists into one sorted list.
def sort(l1,l2):
    return sorted(l1+l2)
l1=[1,5,8]
l2=[2,4,6]
print(sort(l1,l2))