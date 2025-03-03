def get_student_info():
    last_name = input("Enter last name: ")
    first_name = input("Enter first name: ")
    age = input("Enter age: ")
    contact_number = input("Enter contact number: ")
    course = input("Enter course: ")
    return last_name, first_name, age, contact_number, course

def format_student_info(last_name, first_name, age, contact_number, course):
    return (
        f"Last Name: {last_name}\n"
        f"First Name: {first_name}\n"
        f"Age: {age}\n"
        f"Contact Number: {contact_number}\n"
        f"Course: {course}\n"
    )

def save_to_file(filename, data):
    with open(filename, 'a') as file:
        file.write(data)
    print(f"Student information has been saved to '{filename}'.")

filename = 'students.txt'
student_data = get_student_info()
formatted_info = format_student_info(*student_data)
save_to_file(filename, formatted_info)