# read data

with open('input.txt') as file:
    data = file.read()

crates, procedures = data.split('\n\n')

# set up crates as stacks

lines = crates.split('\n')
stacks = [[] for _ in range(9)]

for line in lines[-2::-1]:
    chars = list(line)
    for idx, char in enumerate(chars[1::4]):
        if char != ' ':
            stacks[idx].append(char)


# go over procedure
for procedure in procedures.strip().split('\n'):
    _, move_num, _, move_from, _, move_to = procedure.split(' ')

    for char in stacks[int(move_from)-1][-int(move_num):]:
        stacks[int(move_to)-1].append(char)

    for _ in range(int(move_num)):
        stacks[int(move_from)-1].pop()

# find answer

print(''.join([stack[-1] for stack in stacks]))
