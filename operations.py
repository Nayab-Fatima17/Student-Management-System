from file_handler import save_students


def add_student(students):
    name = input("Enter name: ").strip()

    # Generate unique ID
    if len(students) == 0:
        new_id = 1
    else:
        new_id = max(s["id"] for s in students) + 1

    # Validate age
    while True:
        try:
            age = int(input("Enter age: "))
            if age <= 0:
                print("Age must be positive")
                continue
            break
        except:
            print("Invalid age! Enter a number.")

    # Validate marks
    while True:
        try:
            marks = float(input("Enter marks: "))
            if marks < 0 or marks > 100:
                print("Marks must be between 0 and 100")
                continue
            break
        except:
            print("Invalid marks! Enter a number.")

    student = {
        "id": new_id,
        "name": name,
        "age": age,
        "marks": marks
    }

    students.append(student)
    print(f"Student added successfully with ID: {new_id}")

    save_students(students)

def view_students(students):
    if len(students) == 0:
        print("No students found")
        return

    print("\n====== STUDENT MANAGEMENT SYSTEM ======")
    print("\n--- Student List ---")
    print("ID   Name        Age   Marks   Grade")
    print("--------------------------------------")

    for s in students:
        grade = get_grade(s["marks"])
        print(f"{s['id']:<4} {s['name']:<12} {s['age']:<5} {s['marks']:<7} {grade}")

def search_student(students):
    try:
        student_id = int(input("Enter student ID to search: "))
    except:
        print("Invalid ID!")
        return

    for s in students:
        if s["id"] == student_id:
            print("Found:", s)
            return

    print("Student not found")

def delete_student(students):
    try:
        student_id = int(input("Enter student ID to delete: "))
    except:
        print("Invalid ID!")
        return

    for s in students:
        if s["id"] == student_id:
            students.remove(s)
            print(f"Student '{s['name']}' (ID: {s['id']}) deleted successfully")
            save_students(students)
            return

    print("Student not found")

def get_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    else:
        return "D"
    
def update_student(students):
    try:
        student_id = int(input("Enter student ID to update: "))
    except:
        print("Invalid ID!")
        return

    for s in students:
        if s["id"] == student_id:
            print("Current data:", s)

            new_name = input("Enter new name (leave blank to keep same): ").strip()

            # Update age
            while True:
                age_input = input("Enter new age (leave blank to keep same): ")
                if age_input == "":
                    break
                try:
                    new_age = int(age_input)
                    if new_age <= 0:
                        print("Age must be positive")
                        continue
                    s["age"] = new_age
                    break
                except:
                    print("Invalid age!")

            # Update marks
            while True:
                marks_input = input("Enter new marks (leave blank to keep same): ")
                if marks_input == "":
                    break
                try:
                    new_marks = float(marks_input)
                    if new_marks < 0 or new_marks > 100:
                        print("Marks must be between 0 and 100")
                        continue
                    s["marks"] = new_marks
                    break
                except:
                    print("Invalid marks!")

            if new_name != "":
                s["name"] = new_name

            print("\nUpdated Student Details:")
            grade = get_grade(s["marks"])
            print(f"ID: {s['id']} | Name: {s['name']} | Age: {s['age']} | Marks: {s['marks']} | Grade: {grade}")

            save_students(students)
            return

    print("Student not found")

def show_top_students(students: list[dict]):
    if len(students) == 0:
        print("No students found")
        return

    # Sort by marks (highest first)
    sorted_students = sorted(students, key=lambda x: x["marks"], reverse=True)

    print("\n--- Top Students ---")

    for i, s in enumerate(sorted_students[:3], start=1):
      grade = get_grade(s["marks"])
      print(f"{i}. ID: {s['id']} | Name: {s['name']} | Age: {s['age']} | Marks: {s['marks']} | Grade: {grade}")
