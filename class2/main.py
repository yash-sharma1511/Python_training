# Error Classification
# Fixed for loop: Added missing colon
for i in range(5):
    print(i)

# Fixed division error: Avoid division by zero
x = 10 / 1 

# Corrected formula for area of a circle
def calculate_area(radius):
    return 3.14 * radius * radius  # πr² formula for area

# Debugging Complex Functions
def process_data(data):
    total = 0
    count = 0  # To keep track of valid numbers

    for item in data:
        try:
            total += int(item)
            count += 1
        except ValueError:
            print(f"Skipping invalid entry: {item}")  # Handling non-numeric values

    return total / count if count > 0 else 0  # Avoid ZeroDivisionError

print(process_data(['10', '20', 'abc', '30']))  # Fixed missing parenthesis

# Advanced Debugging Challenge
import random

def unreliable_function():
    number = random.choice([0, 1, 2])
    
    try:
        return 10 / number
    except ZeroDivisionError:
        return "Error: Division by zero"

for i in range(10):
    print(unreliable_function())

# Writing Debug-Friendly Code
def calculate_discount(price, discount):
    try:
        if isinstance(discount, str) and discount.endswith('%'):
            discount = float(discount.strip('%'))
        
        return price - (price * discount / 100)
    except (ValueError, TypeError):
        return "Invalid discount format"

print(calculate_discount(100, '10%'))  # Output: 90.0
print(calculate_discount(200, 'abc'))  # Output: Invalid discount format
