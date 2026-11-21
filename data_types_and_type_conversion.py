# Python Data Types and Type Conversion

# Task 1: Identifying Data Types
name = "Prem"
age = 19
percentage = 84.80
is_student = True

print("DATA TYPES")
print(type(name))
print(type(age))
print(type(percentage))
print(type(is_student))

print("*" * 30)

# Task 2: String to Integer Conversion
a = "100"
b = "50"

total = int(a) + int(b)

print("STRING TO INTEGER CONVERSION")
print("Sum:", total)

print("*" * 30)

# Task 3: String to Float Conversion
price = "99.50"
quantity = 2

price = float(price)
total_price = price * quantity

print("STRING TO FLOAT CONVERSION")
print("Total Price:", total_price)

print("*" * 30)

# Task 4: Integer and Float Conversion
x = 25
y = 10.5

print("BEFORE CONVERSION")
print("x:", x, type(x))
print("y:", y, type(y))

x = float(x)
y = int(y)

print("AFTER CONVERSION")
print("x:", x, type(x))
print("y:", y, type(y))