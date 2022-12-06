with open('input.txt') as file:
    data = file.read().strip()


def detect_marker(num):
    num_minus_one = num-1
    for i in range(num_minus_one, len(data)):

        if len(set(data[i-num_minus_one:i+1])) == num:
            print(i+1, data[i-num_minus_one:i+1])
            break
    return i+1


detect_marker(4)
detect_marker(14)
