def sort_by_salary(data):
    department_dict = {}
    for department, employee, salary in data:
        if department not in department_dict:
            department_dict[department] = []
        department_dict[department].append((employee, salary))
    for department in department_dict:
        department_dict[department].sort(key=lambda x: x[1], reverse=True)

    return department_dict
data = [
    ('HR', 'Alice', 50000),
    ('HR', 'Bob', 60000),
    ('Tech', 'Charlie', 120000),
    ('Tech', 'Dave', 110000),
    ('Tech', 'Eve', 115000)
]
result = sort_by_salary(data)
print(result)
