# 37. Create a list and check palindrome list.

my_list = [1, 2, 3, 2, 1]
print("List:", my_list)

if my_list == my_list[::-1]:
    print("The list is a palindrome.")
else:
    print("The list is not a palindrome.")
