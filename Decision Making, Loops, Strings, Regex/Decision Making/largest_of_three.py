# largest_of_three.py
a = float(input('Enter first number: '))
b = float(input('Enter second number: '))
c = float(input('Enter third number: '))
maximum = a
if b > maximum:
    maximum = b
if c > maximum:
    maximum = c
print(f'The largest number is {maximum}')
