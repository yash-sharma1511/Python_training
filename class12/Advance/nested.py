def nested_sum(data: list) -> int:
    total=0
    for item in data:
        if isinstance(item,list):
            total+=nested_sum(item)
        else:
            total+=item
    return total
data=[1,[2,3],[4,5],6]
print(nested_sum(data))            