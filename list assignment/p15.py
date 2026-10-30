# 15. Create a list and check membership using in keyword.

fruits = ["apple", "banana", "mango", "orange"]
print("List:", fruits)

target = "mango"
if target in fruits:
    print(f"'{target}' is present in the list.")
else:
    print(f"'{target}' is not present in the list.")
