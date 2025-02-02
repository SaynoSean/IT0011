def analyze_string(input_string):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    num_vowels = 0
    num_consonants = 0
    num_spaces = 0
    num_others = 0

    for char in input_string:
        if char in vowels:
            num_vowels += 1
        elif char in consonants:
            num_consonants += 1
        elif char == ' ':
            num_spaces += 1
        else:
            num_others += 1

    print("Vowels:", num_vowels)
    print("Consonants:", num_consonants)
    print("Spaces:", num_spaces)
    print("Other characters:", num_others)

input_string = input("Enter a string: ")
analyze_string(input_string)