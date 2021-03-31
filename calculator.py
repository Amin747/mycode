#!/usr/bin/env python3

# FUNCTIONS CHALLENGE

# Make a calculator that takes two integers and adds/subtracts/divides/multiplies them!

# Use FUNCTIONS to create a calculator! Your script must accept the following user input:

# a float/integer
# another float/integer
# an operator (add, subtract, divide, multiply)
# make sure that you can't divide by zero!
# Your script should return the answer!

# BONUS 1: Make the script human-error proof. Use IF/ELIF/ELSE and TRY/EXCEPT where necessary!

# BONUS 2: If the user types in a bad input, have them type it in again! Use a WHILE LOOP!
def add (a, b) : print (a+b)
def sub (a, b) : print (a-b)
def mul (a, b) : print (a*b)
def div (a, b) : print (a/b)

operations = ["+", "-", "/", "*"]

operation = str(input("Hi! Welcome to my calculator app! What operation do you want to run? Please choose one of +, -, *, or /\n"))

while operation not in operations :
    operation = str(input("Wrong input! Please choose one of +, -, *, or /\n"))

a = float(input("Nice! What is the first number in this operation?\n"))
b = float(input("Alright! and what is the second number in this operation?\n"))
while (b==0 or b==0.0) and operation == "/" :
    b = float(input("The denominator cannot be 0! Please try againand provide a valid second number\n"))
if operation=="+" : add(a,b)
elif operation=="-": sub(a,b)
elif operation=="*": mul(a,b)
elif operation=="/": div(a,b)
else : print("The operation is invalid, Please try again!")
