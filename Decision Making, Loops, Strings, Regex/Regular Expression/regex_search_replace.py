# regex_search_replace.py
import re
text = input('Enter text: ')
pattern = input('Enter pattern to search: ')
replacement = input('Enter replacement text: ')
result = re.sub(pattern, replacement, text)
print('Result:', result)
