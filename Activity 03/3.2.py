def get_input(prompt):
    return input(prompt)

def process_name(first, last):
    full_name = f"{first} {last}"
    return full_name, full_name.upper(), full_name.lower(), len(full_name)

def display_output(full_name, upper, lower, length):
    print("-" * 78)
    print(f"Full Name: {full_name}")
    print(f"Full Name (Upper Case): {upper}")
    print(f"Full Name (Lower Case): {lower}")
    print(f"Length of Full Name: {length}")
    print("-" * 78)

first_name = get_input("Enter your first name: ")
last_name = get_input("Enter your last name: ")

full_name, upper_case, lower_case, name_length = process_name(first_name, last_name)

display_output(full_name, upper_case, lower_case, name_length)
