# AoC 2015 - Day4 

import hashlib 


def encode(input): 
    res = hashlib.md5(input.encode())
    return res.hexdigest()


def run_part(input, part): 
    research = True
    nb = 0 
    while research:
        test_string = input + str(nb)
        md5_hash = encode(test_string)
        if part == 1: 
            start_hash = "00000"
        else: # part2
            start_hash = "000000"
        if md5_hash.startswith(start_hash): 
            print(nb)
            research = False
        nb += 1          


if __name__ == '__main__': 
    print('start')
    run_part('yzbqklnj', 1)
    run_part('yzbqklnj', 2)
    print('end')