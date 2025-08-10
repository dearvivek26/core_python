
"""
Topic: DataType  and variables
Author: 

"""

# -----------------------------------------------------------------------
# What is a Variable?
# ------------------
# It is a short name of any values .
# Variable like a container where we can store values.
#---------------------------------------------------

#Limitation of vaariable -
#            ● Variable should start with alphabet.    A1= ✅ |  1A= ❌
#            ● Variable is case senstive.
#            ● Variable can't conatain any special charactor.
#            ● Variable can alphanumeric.
#            ● Variable can contain _ underscore.
#---------------------------------------------------------------------------

# Syntax: variable_name = value
name = "Piryanka Jha"      # string
age = 23                  # integer
height = 5.5            # float
is_student = True       # boolean

# ---------------------------
# Displaying Variable Types
# ---------------------------
print(type(name))       # <class 'str'>
print(type(age))        # <class 'int'>
print(type(height))     # <class 'float'>
print(type(is_student)) # <class 'bool'>

# ---------------------------
# Multiple Variable Assignment
# ---------------------------
a, b, c = 2, 6.5, "hello"
print(a, b, c)

# Assigning the same value to multiple variables:
a = b = c = 23 
print(a, b, c)

# ---------------------------
# Data Types in Python
# ---------------------------
# 1. Text Type      : str

# 2. Numeric Types  :1.int
#                        2.float
#                             3.complex 

# 3. Sequence Types :1.list
#                         2.tuple
#                             3.range

# 4. Mapping Type   : dict
# 5. Set Types      : set
# 6. Boolean Type   : bool
# 7. Binary Types   : bytes
# 8. None Type      : none
# ---------------------------
# Type Casting
# ---------------------------
s = "13"
num = int(s)  # convert string to integer
print(num + 5)    # Output: 15