# Day24 - AoC 2024 


from tqdm import tqdm


def load_data(path):
    values = {}
    operations = []

    with open(path, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue# skip empty lines

            if ':' in line and '->' not in line:
                var, val = line.split(':')
                values[var.strip()] = int(val.strip())

            elif '->' in line:
                left, output = line.split('->')
                output = output.strip()
                parts = left.strip().split()
                if len(parts) == 3:
                    input1, op, input2 = parts
                    operations.append((input1, op, input2, output))

    return values, operations


def function_and(input1, input2):
    if input1 == 1 and input2 == 1:
        return 1
    return 0


def function_or(input1, input2):
    if input1 == 0 and input2 == 0:
        return 0
    return 1


def function_xor(input1, input2):
    if input1 != input2:
        return 1
    return 0


def read_operations(operations, values, missing):
    at_least_one_missing = False
    i = 0
    for input1, op, input2, output in operations:
        if input1 not in values or input2 not in values:
            at_least_one_missing = True
            continue
        if input1 in values and input2 in values:
            if op == "AND":
                values[output] = function_and(values[input1], values[input2])
            elif op == "OR":
                values[output] = function_or(values[input1], values[input2])
            elif op == "XOR":
                values[output] = function_xor(values[input1], values[input2])
        i += 1
    if at_least_one_missing:
        missing = True
    elif not at_least_one_missing:
        missing = False
    return values, missing


def sort_values(values):
    sorted_values = sorted(values.items(), key=lambda item: item[0]) 
    return {k: v for k, v in sorted_values}


def keep_only_z_keys(values):
    return {k: v for k, v in values.items() if k.startswith('z')}


def export_values(values):
    value_bits = ''
    for _, value in reversed(list(values.items())):
        value_bits += str(value)
    return value_bits


def convert_bits_to_int(bits):
    return int(bits, 2)


def run_part1():
    # values, operations = load_data('data/input_test.txt')
    values, operations = load_data('data/day24_input.txt')
    missing = True
    while missing:
        values, missing = read_operations(operations, values, missing)
    z_values = sort_values(keep_only_z_keys(values))
    # print(z_values)
    value_int = convert_bits_to_int(export_values(z_values))
    print(value_int)


if __name__ == "__main__":
    print("start")
    run_part1()
    print("end")
