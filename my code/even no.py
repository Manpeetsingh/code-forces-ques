# Program to print all even numbers between 1 and N inclusive

# Input: number N
N = int(input("Enter a number: "))

# Loop through numbers from 1 to N
for i in range(2, N+1, 2):  # start at 2, step by 2
    print(i)
