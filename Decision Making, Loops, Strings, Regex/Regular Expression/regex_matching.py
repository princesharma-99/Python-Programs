# regex_matching.py
import re
pattern = input('Enter regex pattern: ')
text = input('Enter text to match: ')
if re.fullmatch(pattern, text):
    print('Full match found')
else:
    print('No full match')
