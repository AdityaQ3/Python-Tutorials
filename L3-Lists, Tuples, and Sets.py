# List, Tuples & Sets:

# List & Tuples allow us to work with sequential data
# Sets are un-ordered collection of values with no duplicates.


# Lists: has lots of functionality than any other data types in python------------------------------------------
# ------------------------ LIST---------------------------------------------------------------------------------


courses = ['History', 'Maths', 'Physics', 'Comp']  # To create a list we use [] and
# within the [], we put each value separated by ','.
print(courses)
print(len(courses))  # OP: 4

# To access each values individually, use[] after list & pass on the location of value, we want:
print(courses[0])  # OP: History
print(courses[3])  # OP: Comp
# Negative index can give the value of last index:
print(courses[-1])  # OP: Comp

# To access a range of values use [a:b] where 'a' is starting point which is inclusive and
# b is ending index which is not inclusive:
print(courses[0:2])  # OP: ['History', 'Maths']
# We can get same results if we use just [:b]-
print(courses[:2])  # OP: ['History', 'Maths'] - Starting from 0 index up to the 2nd index.
# Similarly, We can get all values of list starting form any index b (which is exclusive) to the end of the list
# by using [b:]-
print(courses[2:])  # OP: ['Physics', 'Comp']- Starting after 2nd index up to the last index.
# There's detailed video on 'slicing' attached in the description of the same video (Lect No. 04)


# List Methods: allows us to modify our lists:
# Add an item et the end of list:
courses1 = ['abc', 'def', 'ghi']
print(courses1)
courses1.append('jkl')
print(courses1)  # OP: ['abc', 'def', 'ghi', 'jkl']
# Add an item et the specific location of list:
courses1.insert(0, 'xyz')
print(courses1)  # OP: ['xyz', 'abc', 'def', 'ghi', 'jkl']

# Extent method: allows you to append all the elements of another list, tuple, or string to the end of the list.
courses2 = ['aaa', 'bbb']
courses1.extend(courses2)
print(courses1)  # OP: ['xyz', 'abc', 'def', 'ghi', 'jkl', 'aaa', 'bbb']

# similarly, you can extend an iterable list at a specific location of other list:
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8]
# Extend list2 at index 1 of list1
list1[1:1] = list2  # this syntax is used to insert the elements at the position 1 in list1
print(list1)  # Output: [1, 6, 7, 8, 2, 3, 4, 5]

# Remove an item/List from a list:
courses.remove('Maths')
print(courses)  # OP:['History', 'Physics', 'Comp'] which removed the iterable value from the list.

# Remove the last item from a list:
courses = ['History', 'Maths', 'Physics', 'Comp']
courses.pop()  # which will remove the last value from the list.
print(courses)  # OP:['History', 'Physics', 'Comp']
# One can also take out that last value out from the list & print it as:
courses = ['History', 'Maths', 'Physics', 'Comp']
popped = courses.pop()  # it will store the value of popped item into variable name 'propped'
print(popped)  # OP: Comp

# Sort any list by:
# Reverse method:
courses = ['History', 'Maths', 'Physics', 'Comp']
courses.reverse()
print(courses)  # OP: ['Comp', 'Physics', 'Maths', 'History']

# sort by alphabetically: it will sort alphabets in alphabetically order and numbers in ascending order:
courses = ['History', 'Maths', 'Physics', 'Physical Edu']
num = [1, 4, 6, 7, 5, 3, 2]
courses.sort()
num.sort()
print(courses)  # OP: ['History', 'Maths', 'Physical Edu', 'Physics']
print(num)  # OP: [1, 2, 3, 4, 5, 6, 7]

# sort by descending order: you can use sort method first and then reverse it after sorting or,
# we can just pass an argument into our sort methods like:
num = [1, 4, 6, 7, 5, 3, 2]
num.sort(reverse=True)
print(num)  # OP: [7, 6, 5, 4, 3, 2, 1]
# we don't need to alter the list, so can also get the sorted version of our list without alteration in original:
# Sorted Function: doesn't sort the list, inplace it return a sorted version of the original list-
courses = ['History', 'Maths', 'Physics', 'Physical Edu']
num = [1, 4, 6, 7, 5, 3, 2]
# to get the sorted list, we'll define a new variable and set it to return the sorted value:
sorted_courses = sorted(courses)
sorted_num = sorted(num)
print(sorted_courses)  # OP: ['History', 'Maths', 'Physical Edu', 'Physics']
print(sorted_num)  # OP: [1, 2, 3, 4, 5, 6, 7]

# Min, Max, Sum in any List:
num = [1, 4, 6, 7, 5, 3, 2]
print(min(num))   # OP: 1
print(max(num))      # OP: 7
print(sum(num))

# To find out the index of certain value/any element of the list:
courses = ['History', 'Maths', 'Physics', 'Comp']
print(courses.index('Comp'))  # OP: 3

# To check if the values are in there:
print('Maths' in courses)  # OP: True

# For loop through value of our list by using a for loop
courses = ['History', 'Maths', 'Physics', 'Comp']
for i in courses:
    print(i)  # OP: History\n Maths\n Physics\n Comp

# enumerate function shows the values along with their index in list, as:
for course in enumerate(courses):
    print(course)
    # OP:   (0, 'History')
    #       (1, 'Maths')
    #       (2, 'Physics')
    #       (3, 'Comp')

# if we assign two variables, index and course,
# The print statement includes both the index and the value separately,
# resulting in a clearer output.
courses = ['History', 'Maths', 'Physics', 'Comp']
for index, course in enumerate(courses):
    print(index, course)
    # OP: 0 History
    #     1 Maths
    #     2 Physics
    #     3 Comp


# you can also change the starting of indexing by giving the start value within the enumerate fn by :
courses = ['History', 'Maths', 'Physics', 'Comp']
for index, course in enumerate(courses, start=1):
    print(index, course)

# To convert the list items into a string where each element/item gets separated by a comma, we'll use 'join' fn:
courses = ['History', 'Maths', 'Physics', 'Comp']
str_courses = ', '.join(courses)
print(str_courses)
# to convert that string version of our list, we can use split fn to turn that back to original list
new_list = str_courses.split(', ')
print(new_list)


# Tuples: similar to List but it can't be modified as they are immutable -----------------------------------------
# ------------------------Tuples---------------------------------------------------------------------------------

# # Mutable fn of List:
# list_1 = ['History', 'Maths', 'Physics', 'Comp']
# list_2 = list_1
#
# list_1[0] = 'Art'
# print(list_1)       # OP: ['Art', 'Maths', 'Physics', 'Comp']
# print(list_2)        # OP: ['Art', 'Maths', 'Physics', 'Comp']
# # This feature of list, is called mutability.
#
# # Immutable fn of TupleS:
# tuple_1 = ('History', 'Maths', 'Physics', 'Comp')
# tuple_2 = tuple_1
#
# tuple_1[0] = 'Art'
# print(tuple_1)
# print(tuple_2)
# # OP: Traceback (most recent call last):
# #   File "C:\Users\aksingh3\PycharmProjects\Tutorial\L3-Lists, Tuples, and Sets.py", line 165, in <module>
# #     tuple_1[0] = 'Art'
# #     ~~~~~~~^^^
# # TypeError: 'tuple' object does not support item assignment


# Sets: are un-ordered collection of values with no duplicates.-----------------------------------------
# ------------------------Sets--------------------------------------------------------------------------------

CS_1 = {'History', 'Maths', 'Physics', 'Comp'}

print(CS_1)  # OP: {'Maths', 'Comp', 'Physics', 'History'} as it doesn't care about order and organized in random order.
# is is used to test that whether that value is present or not, or to find the duplicates values called Membership tests
# to check whether a specific element is contained in a sequence, such as strings, lists, tuples, or sets.

CS_1 = {'History', 'Maths', 'Physics', 'Comp', 'Maths'}
print(CS_1)   # OP: {'Maths', 'Comp', 'Physics', 'History'} as it filter the duplicate values

CS_1 = {'History', 'Maths', 'Physics', 'Comp'}
Art_1 = {'History', 'Maths', 'Art', 'Design'}

print(CS_1.intersection(Art_1))  # Common element from both sets : {'Maths', 'History'}
print(CS_1.union(Art_1))  # combined element of both sets: {'Art', 'Comp', 'Design', 'Physics', 'Maths', 'History'}
print(CS_1.difference(Art_1))   # what elements are different in CS1 than Art1 : {'Physics', 'Comp'}


# ------------------- Empty List/Tuple/Sets---------------------------------
# Empty Lists
empty_list = []
empty_list1 = list()

# Empty tuples
empty_tuple = ()
empty_tuple1 = tuple()

# Empty set
empty_set = {}  # this is not right as it creates an empty dictionary
empty_set1 = set()
