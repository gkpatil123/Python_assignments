# 40. Create a list and demonstrate all list methods.

my_list = [10, 20, 30]
print("Initial list:", my_list)

# 1. append(x)
my_list.append(40)
print("1. append(40):", my_list)

# 2. extend(iterable)
my_list.extend([50, 60])
print("2. extend([50, 60]):", my_list)

# 3. insert(i, x)
my_list.insert(2, 25)
print("3. insert(2, 25):", my_list)

# 4. remove(x)
my_list.remove(25)
print("4. remove(25):", my_list)

# 5. pop([i])
popped_item = my_list.pop()
print(f"5. pop() -> removed {popped_item}:", my_list)

# 6. index(x)
idx = my_list.index(20)
print(f"6. index(20): {idx}")

# 7. count(x)
my_list.append(20)
cnt = my_list.count(20)
print(f"7. count(20) in {my_list}: {cnt}")

# 8. sort()
my_list.sort()
print("8. sort():", my_list)

# 9. reverse()
my_list.reverse()
print("9. reverse():", my_list)

# 10. copy()
copied = my_list.copy()
print("10. copy():", copied)

# 11. clear()
my_list.clear()
print("11. clear():", my_list)
