# Python_Conditional_Statements.py
"""
Topic: Conditional Statements in Python
Author: 
"""

# ---------------------------
# What are Conditional Statements?
# ---------------------------
# Conditional statements are used to perform different actions based on different conditions.
# Python uses if, elif, and else keywords for decision making.

# ---------------------------
# Basic if Statement
# ---------------------------
age = 20
if age >= 18:
    print("You are eligible to vote.")

# ---------------------------
# if-else Statement
# ---------------------------
num = 5
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# ---------------------------
# if-elif-else Ladder
# ---------------------------
marks = 75
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: D or below")

# ---------------------------
# Nested if Statements
# ---------------------------
x = 10
y = 20
if x > 5:
    if y > 15:
        print("Both conditions are True")

# ---------------------------
# Using Logical Operators with Conditions
# ---------------------------
username = "admin"
password = "1234"
if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Login failed")


#---------------------------------------------------------------


# 1. Write a program to find the greatest among three numbers. 


x = int(input("x:-"))
y = int(input("y:-"))
z = int(input("z:-"))
if x>y and x>z:
     a = x,"is greatest one"
elif y>x and y>z:
     a = y,"is greatest one"
else:
     a = z,"is greatest one"
     
print(a)


#----------------------------------------------------------------------
# 2. Write a program to check whether a number is positive, negative, or zero using nested if. 


numm = int(input("number:-"))
if numm==0:
     a = numm, "is zero"
elif numm>0:
     a = numm, "is postive"
else:
     a = numm, "is negative"
print(a)

