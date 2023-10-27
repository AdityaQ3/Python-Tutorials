# adi = int(input("enter the number you want to reverse-->>>"))
# my_list = [int(digit) for digit in str(adi)]
# print(my_list)
# my_list.sort(reverse=True)
# print(my_list)

num = int(input("Enter an integer: "))
# convert integer to string and split into characters
num_str = str(num)

num_list = list(num_str)

num_list.reverse()

num2 = ''.join(map(str, num_list))

num3 = int(num2)

print(num3)
print(type(num3))


# num = [1, 4, 6, 7, 5, 3, 2]
# sorted_num = sorted(num)
# reverse_sorted_num = sorted(sorted_num, reverse=True)
#
# print(num)
# print(sorted_num)
# print(reverse_sorted_num)
