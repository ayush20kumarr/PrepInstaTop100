# Find the Sum of N Natural Numbers in Python
# Given an integer input number, the objective is to sum all the numbers that lay from 1 to the integer input number and print the sum. In order to do so we usually use iteration to sum all the numbers until the input variable number.

# Example
# Input : number = 5
# Output : 15
# Explanation : 1 + 2 + 3 + 4 + 5 = 15

def sum_of_Natural_Numbers(n):
    sum = 0
    for x in range(0, n+1):
        sum = sum + x
    return int(sum)

    
number = int(input("Enter a number: "))

result = sum_of_Natural_Numbers(number)

print(f"The sum of first {number} numbers is {result}.")