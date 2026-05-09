# tell_seek.py
with open('sample_output.txt', 'r', encoding='utf-8') as file:
    print('Start position:', file.tell())
    text = file.read(10)
    print('Read text:', text)
    print('Position after read:', file.tell())
    file.seek(0)
    print('Position after seek:', file.tell())
