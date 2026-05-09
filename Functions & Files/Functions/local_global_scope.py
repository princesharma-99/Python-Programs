# local_global_scope.py
count = 0

def increment():
    global count
    count += 1
    return count

print('Initial count:', count)
print('After increment:', increment())
