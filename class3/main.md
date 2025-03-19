# Investigate Circular Imports
  - A circular import happens when two Python files depend on each other, causing an infinite loop where Python doesn’t know which file to load first.
  - Use Function-Level Import (Lazy Importing)
  - Instead of importing the module at the top, we import it inside a function where it is actually needed.

# Dynamic Module Loading
  - Dynamic module loading means importing a module at runtime instead of writing a fixed import statement in the code. It allows a program to load and use modules flexibly based on user input, configuration files, or specific conditions.

# Custom Module with Exception Handling
  - Defines a function divide(a, b).
  - If b = 0, it catches the ZeroDivisionError and returns "Cannot divide by zero."
  - If any other error occurs (e.g., invalid inputs like text instead of numbers), it catches the general exception and returns "Error: <error_message>".

# Advanced Import Strategies
  - Advanced import strategies help in dynamically loading modules, handling missing functions, and improving code organization.

# Module Creation and Distribution
  - Create a package folder and module files (math_operations.py)
  - Add __init__.py to make it a package
  -	Write setup.py for installation
  - Install locally using pip install .
  - Import and test the package

# Investigate sys.path
  - sys.path.append()-Temporary, valid for current session.
  - Modify PYTHONPATH	Permanent solution for custom imports(Add the path to PYTHONPATH in your system’s environment variables.)
  - Check sys.path	Debug import issues

# Mocking Modules for Testing
  - Mocking is a technique used in testing to replace real dependencies with fake ones. This helps isolate the function being tested and control its behavior.

# Import Side Effects
  - Import side effects occur when a module automatically executes code as soon as it is imported, rather than just defining functions, classes, or variables. This can be useful for setting up configurations, logging, or initializing resources but can also cause unexpected behavior.
  # Logging & Configuration
    - import logging
    - print("Setting up logging...")
    - logging.basicConfig(level=logging.DEBUG)
  # Database Connections or Setup
    - import sqlite3
    - print("Connecting to database...")
    - conn = sqlite3.connect("my_database.db")
  # To prevent a module from executing code during import
    - def greet():
    - return "Hello from my_module!"
    - if __name__ == "__main__":
    - print("This runs only when executed directly!")

# Investigate Python’s Import Caching
  - When you import a module in Python, it is cached in sys.modules to avoid redundant imports and improve   performance. This means that subsequent imports of the same module do not reload it—Python just reuses the cached version.
# How to reload module
   - import importlib
   - import mymodule
   - importlib.reload(mymodule)  
# Inspect all loaded modules
   - import sys
   - print(sys.modules.keys()) 

