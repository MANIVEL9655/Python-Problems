
def palindrom(n):
    interger_to_string = str(n)
    reverse_Str= interger_to_string[::-1]
    print(reverse_Str)
    if interger_to_string==reverse_Str:
        print("The give number is palindrome")
    else:
        print("Not a Palindrome")
n=int(input("Enter the Number"))
palindrom(n)