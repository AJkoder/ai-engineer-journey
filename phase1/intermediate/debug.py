numbers = [10, 20, 30, 40, 50]
target = 50

found_index = -1

for i in range(len(numbers)):

    if numbers[i] == target:
        found_index = i
        break

if found_index != -1:
    print("Target found at index:", found_index)
else:
    print("Target not found!")