# Find the Sum of the Numbers in a Given Range
# Given two integer inputs as the range [ low , high ], the objective is to find the sum of the numbers that lay in the intervals given by the integer inputs. Therefore we’ll write a code to Find the Sum of the Numbers in a Given Range in Python Language.

# Example
# Input : 2 5
# Output : 14

def rangeSum(num1, num2):
    sum = 0
    for x in range(num1, num2+1):
        sum += x
    return int(sum)

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

result = rangeSum(first_number, second_number)

print(f"The Sum of the Numbers in a Given Range i.e from {first_number} and {second_number} is {result}.")