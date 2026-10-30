# 19. Create a list of 10 numbers and remove duplicates.

numbers = [10, 20, 30, 20, 40, 10, 50, 60, 40, 70]
print("Original list:", numbers)

# Preserve order while removing duplicates
unique_numbers = list(dict.fromkeys(numbers))
print("List after removing duplicates:", unique_numbers)
