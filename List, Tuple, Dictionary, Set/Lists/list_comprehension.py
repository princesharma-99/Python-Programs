# list_comprehension.py
squares = [x * x for x in range(1, 11)]
print('Squares:', squares)
evens = [x for x in range(1, 21) if x % 2 == 0]
print('Even numbers:', evens)
