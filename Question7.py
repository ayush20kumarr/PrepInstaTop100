# Find the Greatest of the Three Numbers
# Given three integer inputs the objective is to find the largest among them. Therefore we write a code to Find the Greatest of the Three Numbers in Python.

# Example
# Input : 20 30 10
# Output : 30

def greatest_of_two(numb1, numb2, numb3):
    if numb1 >= numb2 and numb1 >= numb3:
        return int(numb1)
    elif numb2 >= numb1 and numb2 >= numb3:
        return int(numb2)
    else:
        return int(numb3)
    
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
third_number = int(input("Enter the third number: "))

result = greatest_of_two(first_number, second_number, third_number)

print(f"The Greatest among {first_number}, {second_number} and {third_number} is {result}.")
