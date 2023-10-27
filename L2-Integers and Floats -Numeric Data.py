# To comment a line of code, press Ctrl+/
# To move a line up or down, press Alt+Shift+Up or Alt+Shift

# Floats are decimal numbers.
# Integers are whole numbers.

num = 3
print(type(num))

# Arithmatic Operators: follows BOD-MOS rules!
# Addition: 3+2         OP: 5
# Subtraction: 3-2      OP: 1
# Multiplication: 3*2   OP: 6
# Division: 3/2         OP: 1.5 in python3; 1 in python2
# Floor Division: 3//2  OP: 1
# Exponent: 3**2        OP: 3*3=9
# Modulus: 3%2          OP: 1 (Remainder); Usage: To find Even/Odd numbers

# Syntax for Incrementing values:
num = 5
num = num+1             # OP: 6
# new method to increment the value:
num *= 3                # now value of num is 6
print(num)              # OP: 18

# Syntax for absolute values:
print(abs(-27))         # OP: 27

# Syntax for round off values to the nearest int value:
print(round(3.157))     # OP: 3
print(round(3.157, 1))  # OP: 3.2, It will round-off to first digit after decimal.


# Comparison Operators: will return booleans (true/false values)
# Equal:        3 == 2#
# Not Equal:    3 != 2
# Greater Than: 3 > 2
# Less Than:    3 < 2
# Greater or Equal: 3 >= 2
# Less or Equal: 3 <= 2
num1 = 5
num2 = 6
print(num1 == num2)        # OP: False
print(num1 != num2)        # OP: True
print(num1 > num2)         # OP: False
print(num1 < num2)         # OP: True
print(num1 >= num2)        # OP: False
print(num1 <= num2)        # OP: True


# Casting: when there's a variable which looks like a number, but actually is a string;
# to solve those problems, we can use 'casting' to change the data type and can use them
# as numbers and perform mathematical operators.
num3 = '100'
num4 = '150'
num3 = int(num3)        # It will change the datatype of string to integer
print(type(num3))       # OP: <class 'int'>
num4 = int(num4)
print(num3+num4)
