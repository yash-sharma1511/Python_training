def bmi(weight: float, height: float) -> float:
    if weight <= 0 or height <= 0:
        raise ValueError("Weight and height must be greater than zero.")
    return weight/(height**2)
weight = 70.0  
height = 1.75  
print(bmi(weight, height))