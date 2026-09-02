# AoC 2015 - Day23


def readInput(path): 
    with open(path) as f: 
        content = [line.rstrip().split(" ") for line in f.readlines()]
    return content


def processInst(name, value, registers, idx): 
    if name == "hlf": 
        registers[value[0]] = int(registers[value[0]] / 2)
        return registers, idx + 1
    
    if name == "tpl": 
        registers[value[0]] = int(registers[value[0]] * 3)
        return registers, idx + 1
    
    if name == "inc": 
        registers[value[0]] = registers[value[0]] + 1
        return registers, idx + 1
    
    if name == "jmp": 
        return registers, idx + int(value[0])
    
    if name == "jie": 
        reg, val = value
        if reg == 'a,': 
            reg = 'a'
        if reg == 'b,':
            reg = 'b'
        if registers[reg] % 2 == 0:
            return registers, idx + int(val)
        else: 
            return registers, idx + 1
        
    if name == "jio": 
            reg, val = value
            if reg == 'a,': 
                reg = 'a'
            if reg == 'b,':
                reg = 'b'
            # if registers[reg] % 2 == 1: jkhdsjkfhjkze rve fgjkfhg
            if registers[reg] == 1:  
                # print(val)
                return registers, idx + int(val)
            else: 
                return registers, idx + 1

    print('error')


def runPart1(path):
    registers = {
        "a": 0,
        "b": 0
    }
    content = readInput(path)
    idx = 0
    while idx <= len(content) - 1: 
        name = content[idx][0]
        value = content[idx][1:]
        registers, idx = processInst(name, value, registers, idx)
    print(registers)


def runPart2(path): 
    registers = {
            "a": 1,
            "b": 0
        }
    content = readInput(path)
    idx = 0
    while idx <= len(content) - 1: 
        name = content[idx][0]
        value = content[idx][1:]
        registers, idx = processInst(name, value, registers, idx)
    print(registers)
    

if __name__ == '__main__': 
    print('start')
    input_path = "2015/data/input_day23.txt"
    # input_path = "2015/data/input_test.txt"
    runPart1(input_path)
    runPart2(input_path)
    print('end')
