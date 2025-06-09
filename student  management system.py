import json
import os

STUDENTS_FILE = "students.json"

def load_students():
    if not os.path.exists(STUDENTS_FILE):
        return []
    with open(STUDENTS_FILE, "r") as file:
        return json.load(file)

def save_students(students):
    with open(STUDENTS_FILE, "w") as file:
        json.dump(students, file, indent=4)

def add_student():
    students = load_students()
    student = {
        "id": input("Enter student ID: "),
        "name": input("Enter student name: "),
        "age": input("Enter student age: "),
        "grade": input("Enter student grade: ")
    }
    students.append(student)
    save_students(students)
    print("Student added successfully!\n")

def view_students():
    students = load_students()
    if not students:
        print("No students found.\n")
        return
    for student in students:
        print(f"ID: {student['id']}, Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")
    print()

def search_student():
    students = load_students()
    search_id = input("Enter student ID to search: ")
    for student in students:
        if student['id'] == search_id:
            print(f"Found: {student}")
            return
    print("Student not found.\n")

def update_student():
    students = load_students()
    update_id = input("Enter student ID to update: ")
    for student in students:
        if student['id'] == update_id:
            student['name'] = input("Enter new name: ")
            student['age'] = input("Enter new age: ")
            student['grade'] = input("Enter new grade: ")
            save_students(students)
            print("Student updated successfully.\n")
            return
    print("Student not found.\n")

def delete_student():
    students = load_students()
    delete_id = input("Enter student ID to delete: ")
    updated_students = [s for s in students if s['id'] != delete_id]
    if len(updated_students) == len(students):
        print("Student not found.\n")
    else:
        save_students(updated_students)
        print("Student deleted successfully.\n")

def main():
    while True:
        print("\n=== Student Management System ===")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
