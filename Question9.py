# Check Whether a Number is a Prime or Not in Python
# Given an integer input the objective is to write a program to Check Whether a Number is a Prime or Not in Python Language.

# Example
# Input : 11
# Output : 11 is a Prime

# Brute Force
# def Prime_or_Not(num):
#     if num == 0 or num == 1:
#         return "Not prime"
#     elif num == 2:
#         return "Prime"
#     for x in range(2, num):
#         if (num % 2) == 0:
#             return "Not a Prime"
#         else:
#             return "Prime"
    
# number = int(input("Enter a number: "))

# result = Prime_or_Not(number)

# print(f'{number} is {result}.')

# Optimized

num = int(input("Enter a number: "))
flag = 0
if num<2:
  flag = 1
else:
  for i in range(2,int((num/2)+1)):
    if num%i==0:
      flag = 1
      break

if flag == 1:
  print('Not Prime')
else:
  print("Prime")