
with open('input.txt') as file:
    calorie_list = file.readlines()

# parse new line characters
calorie_list = [cal.strip('\n') for cal in calorie_list]

# group between spaces

grouped_calories = [0,]
idx = 0

for cal in calorie_list:
    if cal != '':
        grouped_calories[idx] += int(cal)
    else:
        idx += 1
        grouped_calories.append(0)

# find largest
print('Largest calorie per Elf', max(grouped_calories))

# find sum of three largest calories

accumulator = 0
for _ in range(3):
    largest = max(grouped_calories)
    grouped_calories.remove(largest)
    accumulator += largest

print(accumulator)
