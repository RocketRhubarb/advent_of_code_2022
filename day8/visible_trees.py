import numpy as np

with open('input.txt') as file:
    data = file.read().strip()

data = [[*row] for row in data.split('\n')]
trees = np.array(data).astype('int64')

n_rows, n_cols = trees.shape

n_visible = 0

top_score = 0

# loop over all non-edge positions
for y_pos in range(1, n_cols-1):
    for x_pos in range(1, n_rows-1):

        # visible if it is the largest number in sequence to edge
        height = trees[x_pos, y_pos]

        height_up = trees[:x_pos, y_pos] - height
        height_down = trees[x_pos+1:, y_pos] - height
        height_left = trees[x_pos, :y_pos] - height
        height_right = trees[x_pos, y_pos+1:] - height

        visible = (
            max(height_left) < 0
            or 0 > max(height_right) < 0
            or max(height_up) < 0
            or max(height_down) < 0
        )

        if visible:
            n_visible += 1

        # compute scenic score

        def score(heights):
            len_to_higher = np.where(heights >= 0)
            if len(len_to_higher[0]) == 0:
                return len(heights)
            else:
                return (len_to_higher[0]+1)[0]

        scenic_score = 1
        scenic_score *= score(np.flip(height_up))
        scenic_score *= score(height_down)
        scenic_score *= score(np.flip(height_left))
        scenic_score *= score(height_right)
        if scenic_score > top_score:
            top_score = scenic_score

print(n_visible + n_rows * 2 + (n_cols - 2) * 2)

print(top_score)
