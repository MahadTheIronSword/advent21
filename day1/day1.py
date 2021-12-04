def is_element_last_in_list(list, element):
    return element == list[-1]

def get_increases(arr):
    increases = 0

    for i in range(len(arr)):
        current = arr[i]

        if not is_element_last_in_list(arr, current):
            next_val = arr[i + 1]

            if next_val > current:
                increases += 1
    
    return increases

def get_larger_sums(arr):
    increases = 0

    for i in range(2, len(arr) - 1):
        current_sum = arr[i - 2] + arr[i - 1] + arr[i]
        next_sum = arr[i - 1] + arr[i] + arr[i + 1]

        if next_sum > current_sum:
            increases += 1

    return increases


def eval_file(file):
    opened = open(file, 'r')

    arr = []

    for line in opened:
        stripped = line.strip()
        arr.append(int(stripped))

    return arr

        

if __name__ == '__main__':
    raw_input = eval_file('./inputs/inputs1.txt')
    total_increases = get_increases(raw_input)
    total_increased_sums = get_larger_sums(raw_input)
    print(total_increases, total_increased_sums)
