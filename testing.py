"""
character = 20
age = 10
had = 5

if character == age:
    print("you are greater than you think")

elif character > age:
    print("you are less than you think")
elif age >= had:
    print("you are more of you")
else:
    print("you are not that interesting you know! ")

numbersList = [1, 1]
numbersSet = {1, 1}
lettersSet = {"A", "A", "B", "C", "C"}

print(numbersList)
print(numbersSet)
print(lettersSet)


lettersA = {"A", "B", "C", "D"}
lettersB = {"A", "D", "E", "F"}
union = lettersA | lettersB
intersection = lettersA & lettersB
difference = lettersA - lettersB

print(f"Union = {union}")
print(f"intersection ={intersection}")
print(f"difference = {difference}")
"""

import calculator

#from calculator import add
#from calculator import subtract
#from calculator import divide
#from calculator import multiply

print(calculator.add(2,2))
print(calculator.subtract(2,2))
print(calculator.divide(2,4))
print(calculator.multiply(2,2))