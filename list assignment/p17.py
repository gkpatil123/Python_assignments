# 17. Create a list of mixed data types and display them.

mixed_list = [101, "Python", 3.14, True, [1, 2], {"language": "Python"}]
print("Mixed data types list:", mixed_list)

for item in mixed_list:
    print(f"Element: {item!r:<25} Type: {type(item).__name__}")
