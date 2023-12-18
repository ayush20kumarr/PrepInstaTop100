# Find the Sum of The First N Natural Numbers in Python
# Given an integer input the objective is to write a code to Find the Sum of First N Natural Numbers in C++. To do so we simply keep adding the value of the iter variable using a for loop.

# Example
# Input : num = 8
# Output : 36

# Where first 8 number is 1, 2, 3, 4, 5, 6, 7, 8
# Sum of numbers = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 = 36

def sum_of_first_Natural_Numbers(n):
    if n <= 0:
        return "NATURAL NUMBERS!!"
    else:
        ans = n*(n+1)/2
        return int(ans)
    
number = int(input("Enter a number: "))

result = sum_of_first_Natural_Numbers(number)

print(f"The sum of first {number} numbers is {result}.")