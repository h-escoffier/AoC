# Day17 - AoC 2024 


import re


def load_data(path):
    with open(path) as f:
        content = f.read()

    # Extract register values
    registers = {
        match.group(1): int(match.group(2))
        for match in re.finditer(r'Register (\w): (\d+)', content)
    }

    # Extract program values
    program_match = re.search(r'Program: ([\d,]+)', content)
    program = list(map(int, program_match.group(1).split(','))) if program_match else []

    return registers, program


def read_program(program, index):
    opcode = program[index]
    operands = program[index + 1]
    return opcode, operands


def select_opcode(opcode, lit_operand, combo_operand, register, index, all_out):
    if opcode == 0:
        # adv
        num = register.get('A', 0)
        den = 2**combo_operand 
        new_a = num // den
        register['A'] = new_a
        return register, index + 2, all_out
    elif opcode == 1:
        # bxl
        register['B'] = register.get('B', 0) ^ lit_operand
        return register, index + 2, all_out
    elif opcode == 2:
        # bst
        register['B'] = combo_operand % 8
        return register, index + 2, all_out
    elif opcode == 3:
        # jnz 
        if register['A'] == 0:
            return register, index + 2, all_out
        else:
            index = lit_operand
            return register, index, all_out
    elif opcode == 4:
        # bxc 
        register['B'] = register.get('B', 0) ^ register.get('C', 0)
        return register, index + 2, all_out
    elif opcode == 5:
        # out
        num = combo_operand
        out = num % 8
        all_out.append(out)
        return register, index + 2, all_out
    elif opcode == 6:
        # bdv
        num = register.get('A', 0)
        den = 2**combo_operand
        new_b = num // den
        register['B'] = new_b  
        return register, index + 2, all_out
    elif opcode == 7:
        # cdv
        num = register.get('A', 0)
        den = 2**combo_operand
        new_c = num // den
        register['C'] = new_c
        return register, index + 2, all_out


def select_operand_value(operand, register):
    if operand == 0: 
        operand_value = 0 
        return operand_value
    elif operand == 1:
        operand_value = 1 
        return operand_value
    elif operand == 2:
        operand_value = 2 
        return operand_value
    elif operand == 3:
        operand_value = 3 
        return operand_value
    elif operand == 4:
        operand_value = int(register.get('A', 0)) 
        return operand_value
    elif operand == 5:
        operand_value = int(register.get('B', 0))
        return operand_value
    elif operand == 6:
        operand_value = int(register.get('C', 0))
        return operand_value
    elif operand == 7:
        # print("Invalid operand (7)")
        return None


def run_part1():
    # register, program = load_data("data/input_test.txt")
    register, program = load_data("data/day17_input.txt")
    # print(register, program)
    index = 0 # Initial index for the program
    all_out = []
    while index < len(program):
        # print(program[index:index + 2])
        opcode, lit_operand = read_program(program, index)
        combo_operand = select_operand_value(lit_operand, register)
        register, index, all_out = select_opcode(opcode, lit_operand, combo_operand, register, index, all_out)
        # print(all_out)
    print(all_out)
    output = ','.join(map(str, all_out))
    print(output)


if __name__ == "__main__":
    print('start')
    run_part1()  
    print('end')