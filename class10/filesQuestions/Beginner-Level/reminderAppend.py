new_task = "6. Backup important files"
with open('reminder.txt', 'a') as file:
    file.write(new_task + '\n')

print("New task added to 'reminder.txt'.")
