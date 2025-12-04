# Day4 - AoC 2025 

#h1 = 1764830537 - 07:35
#h2 = 1764830142 - 07:42

#c1 = 1764829474 - 07:24
#c2 = 1764830098 - 07:34


import imageio
from PIL import Image, ImageDraw, ImageFont


def read_input(path): 
    with open(path, "r") as file:
        lines = file.readlines()
    content = []
    for line in lines:
        line = line.strip()
        content.append(list(line))
    return content


# Part1 
def parse_roll(content): 
    accesible = 0 
    for i in range(len(content)): 
        row = content[i]
        for j in range(len(row)): 
            elm = row[j]
            if elm == '@': 
                nb_adj = count_adj(i,j, len(content), len(row), content)
                if nb_adj < 4: 
                    accesible += 1 
    return accesible


def count_adj(i, j, max_i, max_j, content): 
    counter = 0 
    if i - 1 >= 0 and j - 1 >= 0: 
        if content[i - 1][j - 1] == '@': 
            counter += 1 
    if j - 1 >= 0: 
        if content[i][j - 1] == '@': 
            counter += 1 
    if i + 1 < max_i and j - 1 >= 0: 
        if content[i + 1][j - 1] == '@': 
            counter += 1 
    if i - 1 >= 0: 
        if content[i - 1][j] == '@': 
            counter += 1
    if i + 1 < max_i:
        if content[i + 1][j] == '@': 
            counter += 1
    if i - 1 >= 0 and j + 1 < max_j: 
        if content[i - 1][j + 1] == '@': 
            counter += 1 
    if j + 1 < max_j: 
        if content[i][j + 1] == '@': 
            counter += 1 
    if i + 1 < max_i and j + 1 < max_j:
        if content[i + 1][j + 1] == '@': 
            counter += 1 
    return counter


def run_part1(): 
    content = read_input('2025/data/input_day4.txt')
    # content = read_input('2025/data/input_test.txt')
    nb_accesible = parse_roll(content)
    print(nb_accesible)


# Part2 
def advanced_parse_roll(content, update_content): 
    accesible = 0 
    for i in range(len(content)): 
        row = content[i]
        for j in range(len(row)): 
            elm = row[j]
            if elm == '@': 
                nb_adj = count_adj(i,j, len(content), len(row), content)
                if nb_adj < 4: 
                    accesible += 1 
                    update_content[i][j] = '.'
    return accesible, update_content


def run_part2(): 
    content = read_input('2025/data/input_day4.txt')
    # content = read_input('2025/data/input_test.txt')
    total_accesible = 0 
    # Init while loop
    accesible = 1
    update_content = content
    while accesible != 0:
        accesible, update_content = advanced_parse_roll(content, update_content)
        content = update_content
        total_accesible += accesible
    print(total_accesible)


# Vizualisation 
def matrix_to_image(matrix, fontsize=20):
    rows = len(matrix)
    cols = len(matrix[0])
    
    img = Image.new("RGB", (cols * fontsize, rows * fontsize), color=(5, 5, 5))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("JetBrainsMono-Regular.ttf", fontsize)
    
    for i in range(rows):
        for j in range(cols):
            char = matrix[i][j]
            if char == 'x': 
                color = (255, 230, 40)
            else: 
                color = (80, 255, 80) 

            bbox = draw.textbbox((0, 0), char, font=font)
            w = bbox[2] - bbox[0]
            h = bbox[3] - bbox[1]
            x = j * fontsize + (fontsize - w) / 2
            y = i * fontsize + (fontsize - h) / 2

            draw.text((x, y), char, font=font, fill=color)
    
    return img


def image_parse_roll(content, update_content): 
    accesible = 0 
    for i in range(len(content)): 
        row = content[i]
        for j in range(len(row)): 
            elm = row[j]
            if elm == '@': 
                nb_adj = count_adj(i,j, len(content), len(row), content)
                if nb_adj < 4: 
                    accesible += 1 
                    update_content[i][j] = 'x'
    return accesible, update_content


def update_matrix(content): 
    new_content = content
    for i in range(len(content)): 
        row = content[i]
        for j in range(len(row)): 
            if row[j] == 'x': 
                new_content[i][j] = '.'
    return new_content 


def create_gif(): # 1m36 
    content = read_input('2025/data/input_day4.txt')
    # content = read_input('2025/data/input_test.txt')
    total_accesible = 0 
    # Init animation 
    frames = []
    # Init while loop
    accesible = 1
    update_content = content
    while accesible != 0:
        img = matrix_to_image(content, 20)
        frames.append(img)
        content = update_matrix(content)
        accesible, update_content = image_parse_roll(content, update_content)
        content = update_content
        total_accesible += accesible
    
    frames[0].save("git_day4.gif",
                   save_all=True,
                   append_images=frames[1:],
                   duration=200,
                   loop=0)


if __name__ == '__main__': 
    print('start')
    run_part2()
    create_gif()
    print('end')
