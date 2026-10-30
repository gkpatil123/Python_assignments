# 34. Create a list and find common elements between two lists.

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
print("List 1:", list1)
print("List 2:", list2)

common_elements = [item for item in list1 if item in list2]
print("Common elements:", common_elements)
