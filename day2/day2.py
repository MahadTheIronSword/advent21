def eval_file(file):
    opened = open(file, 'r')

    arr = []

    for line in opened:
        stripped = line.strip()
        arr.append(stripped)

    return arr


def read_commands(commands, with_aim):
    current_position = {
        'horizontal': 0,
        'depth': 0,
        'aim': 0
    }

    for command in commands:
        split = command.split()
        
        action, value = split[0], int(split[1])

        if action == 'forward':
            current_position['horizontal'] += value
            
            if with_aim:
                current_position['depth'] += (current_position['aim'] * value)
        elif action == 'down':
            if not with_aim:
                current_position['depth'] += value
            else:
                current_position['aim'] += value
        elif action == 'up':
            if not with_aim:
                current_position['depth'] -= value
            else:
                current_position['aim'] -= value

    return current_position['horizontal'] * current_position['depth']


if __name__ == '__main__':
    raw_input = eval_file('./inputs/inputs2.txt')
    total = read_commands(raw_input, False)
    total_with_aim = read_commands(raw_input, True)

    print(total, total_with_aim)
