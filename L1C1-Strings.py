# How to write any string in python:
# '  ' is avoided as apostrophe is also considered as quote, hence we use double quote.
print("Aditya's World")
my = "Hello World"

# we can also use triple quote to use multiline string
Multiline = """Those were the good days
when we used to play cricket """

# How to access any individuals char of string separately:
# (len()): determines the length of string i.e. from 0 to 10 total 11 char
print(len(my))

# it will print the char at nth index location
print(my[9])        # Element at 9th index is L
print(my[-1])       # [-1] to print the last char: D
# it will print a range of the char starting from index 0 to 3rd index
print(my[0:4])

# Method: is just a function that belongs to an object.
# String Methods : to convert UC to LC:
print(my.lower())  # OP is hello world
print(my.upper())  # OP is HELLO WORLD

# String Methods : to count no. of char (repetition) in string:
print(my.count("o"))  # OP is 2

# String Methods : to find index of any char in a string:
print(my.find("rld"))  # OP is 8

# String Methods : to replace some char by other char in string:
message = "Hello Everyone"
new_message = message.replace("Everyone", "Universe")
# instead of new_message, we could have written 'message' too, which will have a new assigned value with replaced char.
print(new_message)  # OP is Hello Universe

# String Methods : How to add multiple string & concatenate together
greeting = "Hi"
name = "Adams"
welcome_message = greeting + ', ' + name + '. Welcome to the Team!'
print(welcome_message)
# OP is: Hi, Adams. Welcome to the Team!


# The above method should be avoided to get rid of tracking operators and their places
# Instead of above, we should follow formatted strings:
welcome_message = "{}, {}. Welcome to the Team!".format(greeting, name)
print(welcome_message)
# OP is: Hi, Adams. Welcome to the Team!


# The above formatted string method can also be replaced by
# a very easy method called: f string:
welcome_message = f"{greeting}, {name}. Welcome to the Team!"
print(welcome_message)  # OP is: Hi, Adams. Welcome to the Team!
# To change case of string, you can also add method directly into the placeholder:
welcome_message = f"{greeting}, {name.upper()}. Welcome to the Team!"
print(welcome_message)  # OP is: Hi, ADAMS. Welcome to the Team!
# For more detailed knowledge on String Formatting, refer to todo: L1C2-String Formatting file.


# There are lots of different methods that we can use in our strings.
# Now, to know everything that we can do, there are a couple of things that we can do:
# First one is Dir function : If we pass any variable, it'll show all the methods and attributes
# that we have access to.
print(dir(name))  # OP: '__add__', '__class__', '__contains__', '__delattr__'.....& so on.
# But, it doesn't show what any of those actually do.
# So to show more info about these string methods, we can use HELP function &
# we need to run on the string class itself like:
print(help(str))
# It helps to remember what does any method exactly do.
# If we need to understand any method specifically, we can write it as:
print(help(str.lower))
# Output will be:
#   lower(self, /)
#           Return a copy of the string converted to lowercase.
