# Check Whether a Number is Even or Odd in Python
# Given an integer input num, the objective is to write a code to Check Whether a Number is Even or Odd in Python. To do so we check if the number is divisible by 2 or not, it’s Even if it’s divisible otherwise Odd.

# Example 
# Input : num = 3
# Output : Odd 

def checkEvenOdd(numb):
    if numb % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
number = int(input("Enter a number: "))

result = checkEvenOdd(number)

print(f"The number {number} is {result}.")