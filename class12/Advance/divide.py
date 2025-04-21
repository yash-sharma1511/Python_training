def safe_divide(x: float, y: float) -> float:
    try:
        return x / y
    except ZeroDivisionError:
        return 'divide zero error'
print(safe_divide(10,0))  
print(safe_divide(10,2))  
