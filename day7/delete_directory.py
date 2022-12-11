
class File:
    def __init__(self, size, name, parent):
        self.name = name
        self.size = int(size)
        self.parent = parent
        parent.update_size(self.size)


class Dir:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = []
        self.size = 0

    def add_dir(self, dir, curr_dir):
        self.children.append(Dir(dir, curr_dir))

    def add_file(self, size, name):
        self.children.append(File(size, name, self))

    def update_size(self, size):
        self.size += size
        if self.parent:
            self.parent.update_size(size)


root_dir = Dir('/', None)
curr_dir = None


def change_dir(rel_path):
    global curr_dir
    if rel_path == '/':
        curr_dir = root_dir
    elif rel_path == '..':
        curr_dir = curr_dir.parent
    else:
        for child in curr_dir.children:
            if child.name == rel_path:
                curr_dir = child


def find_dirs(directory, min_cutoff, max_cutoff, res_list):
    if directory.size >= min_cutoff and directory.size <= max_cutoff:
        res_list.append(directory)

    for path in directory.children:
        if isinstance(path, Dir):
            res_list = find_dirs(path, min_cutoff, max_cutoff, res_list)
    return res_list


with open('input.txt') as file:
    data = file.read().strip()


for line in data.split('\n'):
    if line.startswith('$ cd'):
        change_dir(line.split()[-1])
    elif line.startswith('$ ls'):
        continue
    else:
        if line.startswith('dir'):
            curr_dir.add_dir(line.split()[1], curr_dir)
        else:
            curr_dir.add_file(*line.split())


# find all directories with a size smaller than 100000

print(sum([dir.size for dir in find_dirs(root_dir, 0, 100000, [])]))

# find smallest directory

disk_space = 70000000
needed_space = 30000000

free_space = disk_space - root_dir.size
space_to_be_freed = needed_space - free_space

print(min([dir.size for dir in find_dirs(
    root_dir, space_to_be_freed, needed_space, [])]))
