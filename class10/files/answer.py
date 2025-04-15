import csv

def add_student():
    name = input("Enter name: ")
    age = input("Enter age: ")
    grade = input("Enter grade: ")

    with open('student.csv', 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['Name', 'Age', 'Grade'])
        if file.tell() == 0:  
            writer.writeheader()
        writer.writerow({'Name': name, 'Age': age, 'Grade': grade})

def view_students():
    try:
        with open('student.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("No records found.")

def main():
    while True:
        print("\n1. Add Student\n2. View Students\n3. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()