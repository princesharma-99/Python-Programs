# string_functions.py
text = input('Enter a sentence: ')
print('Uppercase:', text.upper())
print('Lowercase:', text.lower())
print('Number of words:', len(text.split()))
print('Replaced string:', text.replace('a', '@'))
