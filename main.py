from file_handler import load_students
from operations import add_student, view_students, search_student, delete_student
from operations import update_student, show_top_students

students = load_students()
print("\nWelcome to Student Management System 🚀")
def menu():
    while True:
        print("\n1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Update Student")
        print("6. Show Top Students")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student(students)

        elif choice == "2":
            view_students(students)

        elif choice == "3":
            search_student(students)

        elif choice == "4":
            delete_student(students)

        elif choice == "5":
            update_student(students)

        elif choice == "6":
            show_top_students(students)

        elif choice == "7":
            print("\nSaving data and exiting... 👋")
            break 

        else:
            print("Invalid choice")

if __name__ == "__main__":
    menu()