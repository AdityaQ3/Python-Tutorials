# Dictionary : Key-Value Pair
student = {'name': 'John', 'age': 25, 'courses': ['Maths', 'Comp']}

print(student)              # OP: {'name': 'John', 'age': 25, 'courses': ['Maths', 'Comp']}
print(student['courses'])   # OP: ['Maths', 'Comp']

# calling any key which don't exist, will return error, but sometimes we don't want to face errors and want to see any
# message instead. so for these cases:
# print(student['phone no.'])    # OP : KeyError: 'phone no.'

print(student.get('age'))           # OP: 25
print(student.get('phone no.'))     # OP: None

# if we want specific message instead of "NONE" if any key doesn't exist:
print(student.get('phone', 'Searched Item Not Found'))  # OP : Searched Item Not Found


# --- New Entry/Edit/Update Values in Dictionary:
# to add any new key or pair:
student['phone'] = '55-555-5555'
student['name'] = 'Jane'
print(student)  # OP: {'name': 'Jane', 'age': 25, 'courses': ['Maths', 'Comp'], 'phone': '55-555-5555'}

# Now, to update multiple key value pair, we can use the update fn:
student.update({'name': 'Aditya', 'age': 30, 'Address': 'Gorakhpur'})
print(student)
# OP: {'name': 'Aditya', 'age': 30, 'courses': ['Maths', 'Comp'], 'phone': '55-555-5555', 'Address': 'Gorakhpur'}

# Now, to delete any key value pair, we can use the del method :
del student['Address']
print(student)      # OP: {'name': 'Aditya', 'age': 30, 'courses': ['Maths', 'Comp'], 'phone': '55-555-5555'}

# To remove any key value pair, and store that removed key value into another variable we can use the pop fn:
phone = student.pop('phone')
print(student)      # Op: {'name': 'Aditya', 'age': 30, 'courses': ['Maths', 'Comp']}
print(phone)        # Op: 55-555-5555

# To know how many key-value pair are there in dictionary we can use 'len' fn:
print(len(student))     # OP: 3  ({'name': 'Aditya', 'age': 30, 'courses': ['Maths', 'Comp']})

# TO see all the available keys, use .keys() and to see values, use .values() method:
print(student.keys())       # OP: dict_keys(['name', 'age', 'courses'])
print(student.values())      # OP: dict_values(['Aditya', 30, ['Maths', 'Comp']])
print(student.items())      # OP: dict_items([('name', 'Aditya'), ('age', 30), ('courses', ['Maths', 'Comp'])])

# ** To loop through in any dictionary, if we'll use 'for key in student:' it will just look into the keys only,
# hence, we need to use 'items' method instead of using only 'key' or 'values' just like above-

for key, values in student.items():
    print(key, values)
# OP: name Aditya
    # age 30
    # courses ['Maths', 'Comp']
