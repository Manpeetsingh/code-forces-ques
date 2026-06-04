words = input("Enter the words seprated by space")
print()

# print the words in alphebatical order
cleaned = string.replace(" ", "").lower()

if cleaned == cleaned[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
