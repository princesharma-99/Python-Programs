# positional_keyword_arguments.py
def describe_person(name, age, country='USA'):
    return f'{name} is {age} years old and lives in {country}.'

print(describe_person('John', 30))
print(describe_person(name='Lina', age=26, country='Canada'))
