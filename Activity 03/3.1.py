print("-" * 78)

def get_input(prompt):
    return input(prompt)

def process_name(first, last):
    return first + " " + last, first[:3]

def display_output(full_name, sliced_name, age):
    print("-" * 78)
    print(f"\nFull Name: {full_name}")
    print(f"Sliced Name: {sliced_name}")
    print(f"Greeting Message: Hello, {sliced_name}! Welcome. You are {age} years old.")
    print("-" * 78)

first_name = get_input("Enter your first name: ")
last_name = get_input("Enter your last name: ")
age = get_input("Enter your age: ")

full_name, sliced_name = process_name(first_name, last_name)

display_output(full_name, sliced_name, age)
