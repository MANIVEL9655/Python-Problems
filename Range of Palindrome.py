from Palindrom2 import pal
def find_palindromes(start, end):
    palindromes = []
    for num in range(start, end + 1):
        if pal(num):
            palindromes.append(num)
    return palindromes
# Example usage
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
print("Palindrome numbers:",find_palindromes(start, end))