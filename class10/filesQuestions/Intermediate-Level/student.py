with open('students.txt', 'r') as infile:
    lines = infile.readlines()
with open('report.txt', 'w') as outfile:
    for line in lines:
        name, marks = line.strip().split(',')
        marks = int(marks)
        status = 'Pass' if marks >= 50 else 'Fail'
        outfile.write(f"{name},{marks},{status}\n")

print("Pass/Fail status saved to 'report.txt'.")
