def compute_sum(first_term, last_term):
    total_sum = 0
    for number in range(first_term, last_term + 1):
        total_sum += number
    return total_sum

def main():
    first_term = int(input("Enter first term number: "))
    last_term = int(input("Enter last term number: "))
    total = compute_sum(first_term, last_term)
    print(f"The sum of the numbers from {first_term} to {last_term} is {total}")

if __name__ == "__main__":
    main()