# string_formatting.py
name = input('Enter your name: ')
age = int(input('Enter your age: '))
print(f'Hello, {name}. Next year you will be {age + 1}.')
print('Hello, {}. You are {} years old.'.format(name, age))
