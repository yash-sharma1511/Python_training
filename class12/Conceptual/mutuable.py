def modify(lst):
    lst.append(4)
    lst[0] = 10
    print("Inside", lst)
ori = [1, 2, 3]
modify(ori)
print("Outside", ori)
# When you pass a mutable object, like a list, to a function in Python, the function can modify the object itself because both the caller and the function refer to the same object in memory. This is different from passing an immutable object, where a new object would be created inside the function.
# Inside the function: We modify the original list by appending a new element (4) and changing the first element (1 becomes 10).
# Outside the function: Since lists are mutable, the changes made inside the function are reflected in the original list outside the function.