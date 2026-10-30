# 33. Create a list and find the second largest number.

numbers = [12, 45, 2, 89, 34, 89, 67]
print("Numbers:", numbers)

unique_numbers = sorted(list(set(numbers)))
if len(unique_numbers) >= 2:
    second_largest = unique_numbers[-2]
    print("Second largest number:", second_largest)
else:
    print("Not enough unique numbers.")
