# Find the Greatest of the Two Numbers
# Given two integer inputs as number1 and number2, the objective is to find the largest among the two. Therefore we’ll write a code to Find the Greatest of the Two Numbers in Python Language.

# Example
# Input : 20 40
# Output : 40

def greatest_of_two(numb1, numb2):
    if numb1 == numb2:
        return "EQUAL!!"
    elif numb2 > numb1:
        return int(numb2)
    else:
        return int(numb1)
    
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

result = greatest_of_two(first_number, second_number)

print(f"The Greatest between {first_number} and {second_number} is {result}.")