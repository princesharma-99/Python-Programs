# break_continue_pass.py
for number in range(1, 11):
    if number == 5:
        print('Skipping 5 with continue')
        continue
    if number == 8:
        print('Stopping at 8 with break')
        break
    if number == 3:
        pass
    print('Number:', number)
