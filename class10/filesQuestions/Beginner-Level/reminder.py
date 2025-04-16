tasks = [
    "1. Complete Python assignment",
    "2. Attend team meeting at 4 PM",
    "3. Review project documentation",
    "4. Go for a 30-minute walk",
    "5. Read a chapter from the book"
]
with open('reminder.txt', 'w') as file:
    for task in tasks:
        file.write(task + '\n')

print("Tasks written to 'reminder.txt' successfully!")
