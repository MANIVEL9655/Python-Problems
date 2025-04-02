print("The given data");print("The normal data")
def is_palindrome(n):
    original = n
    reverse = 0

    while n > 0:
        digit = n % 10  # Get the last digit
        reverse = reverse * 10 + digit  # Build the reversed number
        n //= 10  # Remove the last digit

    return original == reverse

# Example Usage:
num = int(input("Enter a number: "))
if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")
