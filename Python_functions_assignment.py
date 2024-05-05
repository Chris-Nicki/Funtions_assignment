# # Python Functions Assignment
print()
print("1. The Calculator App")
print()
# # 1. The Calculator App
# """ Objective: The aim of this assignment is to build a basic calculator that can perform addition,
#    subtraction, multiplication, and division.
# """ 
# # Task 1: Create functions for each arithmetic operation


print("""Hello, I am a calculator. 
Give me two numbers and an operator and I will reward you with the correct answer!""")
def addition(a, b):
     return a + b    
def subtraction(a, b):
     return a - b
def multiplication( a, b):
     return a * b
def division(a, b):
     if b == 0:
          print("Error!")
     else:
          return a / b
while True:
     num1 = float(input("Enter first number: "))
     operator = input("Enter operator (+, -, *, /): ")
     num2 = float(input("Enter second number: "))

     if operator == "+":
           result = addition(num1, num2)
     elif operator == "-":
          result = subtraction(num1, num2)
     elif operator == "*":
           result = multiplication(num1, num2)
     elif operator == "/":
          result = division(num1, num2)
     else:
          print("Give me a valid operator")
          continue
     
     print(f"The answer is {result}")
     break





print()
print("2. Shopping List Maker")
print()
"""Objective:
The aim of this assignment is to create a program that helps users make a shopping list.

Task 1: Write a function that lets the user add items to a list.
Task 2: Include a feature to remove items from the list.
Task 3: Add a function that prints out the entire list in a formatted way.
"""
print("Hi the fridge is looking empty, lets make a shopping list!")
list = [] 
def add_to_list(list): 
        item = input("What should we add to the list? ")
        if item not in list:
            list.append(item)
        else:
            print(f"{item} is already on list, we don't need more than one!")
def remove_from_list(item):
        item = input("What do we need to remove from the list? ")
        if item in list:
            list.remove(item)
        else:
            print("Item is not on your list, may be we should add it? ")
def view_list(item):
     print(f"Here is your list {list}")
def Shopping_list(list):
     while True:
          response = input("What would you like to do; add item,remove it, view list? ").lower()
          if response == "add item": 
               add_to_list(list)

          elif response =="remove item":
               remove_from_list(list)
    
          elif response == "view list":
               view_list(list)
              
Shopping_list(list)




      



    

          
 