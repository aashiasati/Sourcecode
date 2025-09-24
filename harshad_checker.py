# Python Program: Harshad Number Checker & List Generator

def is_harshad(num):
    """Check if a number is a Harshad number"""
    digit_sum = sum(int(d) for d in str(num))
    return num % digit_sum == 0

def list_harshad_numbers(start, end):
    """Return list of Harshad numbers in a given range"""
    return [n for n in range(start, end + 1) if is_harshad(n)]

# ----------- Example Usage -----------
if name == "main":
    # Input from user
    n = int(input("Enter a number to check: "))
    if is_harshad(n):
        print(f"{n} is a Harshad number ✅")
    else:
        print(f"{n} is NOT a Harshad number ❌")

    # List Harshad numbers from 1 to 100
    print("\nHarshad numbers from 1 to 100:")
    print(list_harshad_numbers(1, 100))
