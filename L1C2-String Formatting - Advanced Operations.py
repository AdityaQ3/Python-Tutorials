person = {'name': 'Jenn', 'age': 23}

# 1st formatting style (concatenation) strings:
# sentence = 'My name is ' + person['name'] + ' and I am ' + str(person['age']) + ' years old.'
# print(sentence)

# 2nd formatting style :
sentence = 'My name is {} and I am {} years old.'.format(person['name'], person['age'])
print(sentence)         # OP: My name is Jenn, and I am 23 years old.

# 3rd formatting style :
sentence = 'My name is {0} and I am {1} years old.'.format(person['name'], person['age'])
print(sentence)         # It has more importance when there's placeholder whose value needs to be repeated,
# like shown in example below:
tag = 'h1'
text = 'This is a headline'
sentence = '<{0}>{1}</{0}>'.format(tag, text)   # value at '0 & 1' will be replaced by 'tag and text' respectively.
print(sentence)         # OP: <h1>This is a headline</h1>

# unlike above examples where we were passing the dictionary to format and accessing the name and
# age of the dictionary within format, we can access the fields directly within the placeholders by:
sentence = 'My name is {0[name]} and I am {1[age]} years old.'.format(person, person)
print(sentence)
# The above formatting is taking it is 0th and 1's value from same dictionary i.e. person.
# Hence, it can also be simplified as:
sentence = 'My name is {0[name]} and I am {0[age]} years old.'.format(person)
print(sentence)
# By using above placeholder formatting you can access the value of a List also. For example:
L = ['MSD', 7]
sentence = 'My name is {0[0]} and {0[1]} is my lucky number'.format(L)
print(sentence)


# class Person():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# p1 = Person('Jack', '33')
#
# sentence = 'My name is {0.name} and I am {0.age} years old.'.format(p1)
# print(sentence)

# sentence = 'My name is {name} and I am {age} years old.'.format(name='Jenn', age='30')
# print(sentence)

# sentence = 'My name is {name} and I am {age} years old.'.format(**person)
# print(sentence)

# for i in range(1, 11):
#     sentence = 'The value is {}'.format(i)
#     print(sentence)


# pi = 3.14159265

# sentence = 'Pi is equal to {}'.format(pi)

# print(sentence)

sentence = '1 MB is equal to {} bytes'.format(1000 ** 2)
print(sentence)

import datetime

my_date = datetime.datetime(2016, 9, 24, 12, 30, 45)

# print(my_date)

# March 01, 2016

sentence = '{:%B %d, %Y}'.format(my_date)

print(sentence)

# March 01, 2016, fell on a Tuesday and was the 061 day of the year.

sentence = "{:%B %d, %Y} fell on a {0} and was the {0} day of the year".format(my_date)

print(sentence)
