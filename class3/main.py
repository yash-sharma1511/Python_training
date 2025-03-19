# Investigate Circular Imports
# module_a.py
def func_a():
    return "Function A"

def call_func_b():
    import module_b  # Import only inside the function to avoid the loop
    return module_b.func_b()

print(call_func_b()) 

#module_b.py
import module_a  # This is okay because func_a is not called immediately

def func_b():
    return "Function B"

#.Dynamic Module Loading

import importlib

def dynamic_import():
    module_name = input("Enter module name: ")  # Example: math
    function_name = input("Enter function name: ")  # Example: sqrt
    argument = input("Enter argument: ")  # Example: 25

    try:
        # Import the module dynamically
        module = importlib.import_module(module_name)
        
        # Get the function from the module
        function = getattr(module, function_name)

        # Convert the argument to a number if possible
        if argument.replace(".", "", 1).isdigit():  
            argument = float(argument) if "." in argument else int(argument)

        # Call the function with the argument
        result = function(argument)
        print("Output:", result)

    except ModuleNotFoundError:
        print(f"Error: Module '{module_name}' not found.")
    except AttributeError:
        print(f"Error: Function '{function_name}' not found in module '{module_name}'.")
    except Exception as e:
        print(f"Error: {e}")

# Run the function
dynamic_import()

# Custom Module with Exception Handling
# calculator.py

def divide(a, b):
    try:
        return a / b  # Attempt to divide
    except ZeroDivisionError:
        return "Cannot divide by zero."  # Handles division by zero
    except Exception as e:
        return f"Error: {e}"  # Handles other errors (e.g., wrong input type)
    
    import calculator  # Import the custom module

# Test cases
print(calculator.divide(10, 2))   #  Output: 5.0
print(calculator.divide(10, 0))   #  Output: "Cannot divide by zero."
print(calculator.divide(10, "a")) #  Output: "Error: unsupported operand type(s) for /: 'int' and 'str'"

# Advanced Import Strategies

def execute_function(module_name, function_name, *args):
    module = importlib.import_module(module_name)
    if hasattr(module, function_name):
        function = getattr(module, function_name)
        return function(*args)
    else:
        return "Function not found."

print(execute_function("math", "sqrt", 16))  # 4.0

# Optimize Import Time

import time

start = time.time()  # Start time
import math
end = time.time()  # End time

print(f"Import time: {end - start:.6f} seconds")

# Module Creation and Distribution
# Inside my_package/, create math_operations.py:
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
#Inside my_package/__init__.py:
from .math_operations import add, subtract
#Inside setup.py:
from setuptools import setup, find_packages

setup(
    name="my_package",
    version="0.1",
    packages=find_packages(),
    description="A simple math operations package",
    author="Your Name",
    author_email="your.email@example.com",
    install_requires=[],
)
#install package locally command for installing 'pip install' .
import my_package

print(my_package.add(5, 3))        # Output: 8
print(my_package.subtract(10, 4))

# Investigate sys.path
# To check sys.path
import sys
print(sys.path)
# To add custom path
import sys

# Add a custom directory
sys.path.append('/custom/path/to/modules')

# Now you can import your module from that path
import mymodule  

print(mymodule.some_function()) 


# Mocking Modules for Testing

from unittest import mock
import math  # Import the actual module

# Mocking math.sqrt to always return 100
with mock.patch('math.sqrt', return_value=100):
    print(math.sqrt(25))  # Output: 100

# Outside the mock context, it works normally
print(math.sqrt(25))  # Output: 5.0

# Import Side Effects
# Create a Module (my_module.py)
print("This runs on import!")

def my_function():
    return "Hello from my_function!"
# import module in (main.py)
import my_module

print("Import is done!")
print(my_module.my_function())  


# mymodule.py
print("Module mymodule is being imported!")

def hello():
    return "Hello from mymodule!"
# main.py
import sys
import mymodule  # First import

print(sys.modules['mymodule'])  # Check if mymodule is in cache

import mymodule  # Second import (does not execute print again)
print("Re-imported mymodule!")