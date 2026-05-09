with open('sample_output.txt', 'a', encoding='utf-8') as file:
    file.write('Appended line.')
with open('sample_output.txt', 'r', encoding='utf-8') as file:
    print(file.read())