# --------------For Loops: -----------------------------------------------------
# --------------For Loops: -----------------------------------------------------

nums = [1, 2, 3, 4, 5]
for num in nums:
    print(num)
# OP : 1\2\3\4\5

print("\n")

# To break the loop for any particular value in list, we can use break fn:
nums = [6, 7, 8, 9, 0]
for num in nums:
    if num == 8:
        print('bug found')
        break
    print(num)
# OP: 6/ 7/ Bug Found

print("\n")

# Just to find particular value and print/highlight/replace that, while completing the loop:
nums = [16, 17, 18, 19]
for num in nums:
    if num == 18:
        print('bug found')
        continue
    print(num)

print("\n")

# Nested loop : a new loop within the exiting loop:
nums = [6, 7, 8, 9]
for num in nums:
    for letter in 'adi':
        print(num, letter)

print("\n")


# for looping in a range, we can use range fn as follows:
for i in range(10):
    print(i)    # OP: Nums Starting from 0 to 9
print("\n")

for i in range(12, 18):
    print(i)    # OP: Nums Starting from 12 to 17
print("\n")


# --------------While Loops: -----------------------------------------------------
# --------------While Loops: -----------------------------------------------------
