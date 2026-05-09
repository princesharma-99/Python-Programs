# arbitrary_arguments.py
def arbitrary_sum(*args, **kwargs):
    print('Positional args:', args)
    print('Keyword args:', kwargs)
    return sum(args) + sum(kwargs.values())

print(arbitrary_sum(1, 2, 3, bonus=5, tax=2))
