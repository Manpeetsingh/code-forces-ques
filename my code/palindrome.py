string = input("Enter a string: ")

# Remove spaces and convert to lowercase
cleaned = string.replace(" ", "").lower()

if cleaned == cleaned[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
