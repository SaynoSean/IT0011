import os

students = []

def validate_student_id(student_id):
    return isinstance(student_id, int) and 100000 <= student_id <= 999999

def validate_student_name(name):
    return isinstance(name, tuple) and len(name) == 2 and all(isinstance(part, str) for part in name)

def validate_grade(grade):
    return isinstance(grade, (int, float)) and 0 <= grade <= 100

def calculate_final_grade(class_standing, major_exam):
    return 0.6 * class_standing + 0.4 * major_exam

def open_file():
    global students
    filename = input("Enter the filename to open: ")
    if not os.path.exists(filename):
        print("File does not exist.")
        return
    with open(filename, 'r') as file:
        students = []
        for line in file:
            student_id, first_name, last_name, class_standing, major_exam = line.strip().split(',')
            student_id = int(student_id)
            class_standing = float(class_standing)
            major_exam = float(major_exam)
            students.append((student_id, (first_name, last_name), class_standing, major_exam))
    print(f"Records loaded from {filename}.")

def save_file():
    filename = input("Enter the filename to save: ")
    with open(filename, 'w') as file:
        for student in students:
            student_id, name, class_standing, major_exam = student
            first_name, last_name = name
            file.write(f"{student_id},{first_name},{last_name},{class_standing},{major_exam}\n")
    print(f"Records saved to {filename}.")

def save_as_file():
    filename = input("Enter the new filename to save: ")
    with open(filename, 'w') as file:
        for student in students:
            student_id, name, class_standing, major_exam = student
            first_name, last_name = name
            file.write(f"{student_id},{first_name},{last_name},{class_standing},{major_exam}\n")
    print(f"Records saved to {filename}.")

def show_all_records():
    if not students:
        print("No records found.")
        return
    for student in students:
        student_id, name, class_standing, major_exam = student
        first_name, last_name = name
        final_grade = calculate_final_grade(class_standing, major_exam)
        print(f"ID: {student_id}, Name: {first_name} {last_name}, Class Standing: {class_standing}, Major Exam: {major_exam}, Final Grade: {final_grade:.2f}")

def order_by_last_name():
    if not students:
        print("No records found.")
        return
    sorted_students = sorted(students, key=lambda x: x[1][1])
    for student in sorted_students:
        student_id, name, class_standing, major_exam = student
        first_name, last_name = name
        final_grade = calculate_final_grade(class_standing, major_exam)
        print(f"ID: {student_id}, Name: {first_name} {last_name}, Class Standing: {class_standing}, Major Exam: {major_exam}, Final Grade: {final_grade:.2f}")

def order_by_grade():
    if not students:
        print("No records found.")
        return
    sorted_students = sorted(students, key=lambda x: calculate_final_grade(x[2], x[3]), reverse=True)
    for student in sorted_students:
        student_id, name, class_standing, major_exam = student
        first_name, last_name = name
        final_grade = calculate_final_grade(class_standing, major_exam)
        print(f"ID: {student_id}, Name: {first_name} {last_name}, Class Standing: {class_standing}, Major Exam: {major_exam}, Final Grade: {final_grade:.2f}")

def show_student_record():
    student_id = int(input("Enter the student ID: "))
    for student in students:
        if student[0] == student_id:
            student_id, name, class_standing, major_exam = student
            first_name, last_name = name
            final_grade = calculate_final_grade(class_standing, major_exam)
            print(f"ID: {student_id}, Name: {first_name} {last_name}, Class Standing: {class_standing}, Major Exam: {major_exam}, Final Grade: {final_grade:.2f}")
            return
    print("Student record not found.")

def add_record():
    student_id = int(input("Enter student ID (6 digits): "))
    if not validate_student_id(student_id):
        print("Invalid student ID.")
        return
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    if not validate_student_name((first_name, last_name)):
        print("Invalid student name.")
        return
    class_standing = float(input("Enter class standing grade: "))
    major_exam = float(input("Enter major exam grade: "))
    if not validate_grade(class_standing) or not validate_grade(major_exam):
        print("Invalid grade.")
        return
    students.append((student_id, (first_name, last_name), class_standing, major_exam))
    print("Record added successfully.")

def edit_record():
    student_id = int(input("Enter the student ID to edit: "))
    for i, student in enumerate(students):
        if student[0] == student_id:
            print("Current record:")
            student_id, name, class_standing, major_exam = student
            first_name, last_name = name
            print(f"ID: {student_id}, Name: {first_name} {last_name}, Class Standing: {class_standing}, Major Exam: {major_exam}")
            new_first_name = input("Enter new first name (leave blank to keep current): ")
            new_last_name = input("Enter new last name (leave blank to keep current): ")
            new_class_standing = input("Enter new class standing grade (leave blank to keep current): ")
            new_major_exam = input("Enter new major exam grade (leave blank to keep current): ")
            if new_first_name:
                first_name = new_first_name
            if new_last_name:
                last_name = new_last_name
            if new_class_standing:
                class_standing = float(new_class_standing)
            if new_major_exam:
                major_exam = float(new_major_exam)
            students[i] = (student_id, (first_name, last_name), class_standing, major_exam)
            print("Record updated successfully.")
            return
    print("Student record not found.")

def delete_record():
    student_id = int(input("Enter the student ID to delete: "))
    for i, student in enumerate(students):
        if student[0] == student_id:
            students.pop(i)
            print("Record deleted successfully.")
            return
    print("Student record not found.")

# Main menu
def main_menu():
    while True:
        print("\n--- Student Record Management System ---")
        print("1. Open File")
        print("2. Save File")
        print("3. Save As File")
        print("4. Show All Students Record")
        print("5. Order by Last Name")
        print("6. Order by Grade")
        print("7. Show Student Record")
        print("8. Add Record")
        print("9. Edit Record")
        print("10. Delete Record")
        print("11. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            open_file()
        elif choice == '2':
            save_file()
        elif choice == '3':
            save_as_file()
        elif choice == '4':
            show_all_records()
        elif choice == '5':
            order_by_last_name()
        elif choice == '6':
            order_by_grade()
        elif choice == '7':
            show_student_record()
        elif choice == '8':
            add_record()
        elif choice == '9':
            edit_record()
        elif choice == '10':
            delete_record()
        elif choice == '11':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main_menu()