# name = 'Andrei Neagoie'
# age = 50 
# relationship_status = 'single'

# relationship_status = 'it\'s complicated'

# print(relationship_status)

# storage data type, take an input turn it into interger from a string(birth_year)
birth_year = input('what year were you born?')
print(type(birth_year))
age = 2019 - int(birth_year)

print(f'your age is: {age}')

# float is a numberical value, storage data type, take an input turn it into interger from a string(birth_year)
birth_year = input('what year were you born?')
print(type(birth_year))
age = 2019 - float(birth_year)

print(f'your age is: {age}')

# storage data type, take an input turn it into interger from a string(birth_year)
birth_year = input('what year were you born?')
print(type(birth_year))
age = 2019 - bool(birth_year)

print(f'your age is: {age}')

#bool turns into a true value 1 and false value 0