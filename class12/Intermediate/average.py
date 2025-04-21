def average_marks(marks: list[float]) -> float:
    total=sum(marks)
    avg=total/len(marks)
    return avg
marks=[20,10,15,25,0]
print(average_marks(marks))        