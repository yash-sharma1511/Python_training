def return_example(x):
    return x * 2

def print_example(x):
    print(x * 2)

result = return_example(5)
print(result)  
print_example(5)                   
print(print_example(5))  

# return gives a value back to the caller so it can be used later.
# print just displays the value on the screen — it does not return anything.
# return_example(5) → returns 10 → can be stored in result
# print_example(5) → prints 10, but returns None