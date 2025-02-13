def is_palindrome(number):
    """Check if a given number is a palindrome."""
    num_str = str(number)
    return num_str == num_str[::-1]

def process_numbers_from_file(file_path):
    """Read a file, compute the sum of numbers in each line, and check if the sum is a palindrome."""
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        for index, line in enumerate(lines, start=1):
            try:
                numbers = list(map(int, line.strip().split(',')))
                total_sum = sum(numbers)
                status = "Palindrome" if is_palindrome(total_sum) else "Not a palindrome"
                print(f"Line {index}: {line.strip()} (sum {total_sum}) - {status}")
            except ValueError:
                print(f"Line {index}: Error - Invalid number format.")

    except FileNotFoundError:
        print(f"Error: Unable to locate '{file_path}'.")

process_numbers_from_file("numbers.txt")
