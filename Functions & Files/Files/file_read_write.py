# file_read_write.py
with open('sample_output.txt', 'w', encoding='utf-8') as file:
    file.write('Hello from file_read_write!')
with open('sample_output.txt', 'r', encoding='utf-8') as file:
    print(file.read())
