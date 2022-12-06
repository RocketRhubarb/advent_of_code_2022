with open('input.txt') as file:
    data = file.read().strip().splitlines()

fully_overlap = 0
overlap = 0

for pair in data:
    pair = pair.split(',')
    left, right = [list(map(int, pair[0].split('-'))),
                   list(map(int, pair[1].split('-')))]

    left_lower, left_higher = left
    right_lower, right_higher = right

    left_range = set(range(left_lower, left_higher+1))
    right_range = set(range(right_lower, right_higher+1))

    intersection = left_range.intersection(right_range)

    if (intersection == left_range) or (intersection == right_range):
        fully_overlap += 1

    if (intersection != set()):
        overlap += 1

print(f'{fully_overlap} fully overlap')
print(f'{overlap} overlap')
