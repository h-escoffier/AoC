# Day14 - AoC 2024 

# Note : I mix x and y at some point but it work !

import re 
import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import seaborn as sns
import os
import imageio.v2 as io
import random


def load_data(file): 
    data = []
    with open(file, "r") as f:
        content = f.readlines()
    pattern = r"p=(-?\d+),(-?\d+)\s+v=(-?\d+),(-?\d+)"
    for line in content:
        match = re.search(pattern, line)
        pos = (int(match.group(1)), int(match.group(2)))
        vel = (int(match.group(3)), int(match.group(4)))
        data.append([pos, vel])
    return data


# I will try to use numpy and work with a matrix instead of a list of lists
def create_grid(size_y, size_x):
    return np.full((size_y, size_x), 0)


def calcul_new_pos(robot, size_y, size_x):
    pos, vel = robot
    new_y = (pos[0] + vel[0]) % size_x
    new_x = (pos[1] + vel[1]) % size_y
    return (new_y, new_x)


def place_robot(bathroom, robot):
    pos, _ = robot
    bathroom[pos[1], pos[0]] += 1
    return bathroom


def count_robot_in_bathroom(bathroom):
    # Split in quadrant
    y_cut = bathroom.shape[0] // 2 
    x_cut = bathroom.shape[1] // 2
    # Quadrants
    q1 = bathroom[:y_cut, :x_cut]
    q2 = bathroom[:y_cut, x_cut + 1:]
    q3 = bathroom[y_cut + 1:, :x_cut]    
    q4 = bathroom[y_cut + 1:, x_cut + 1:]
    return q1.sum(), q2.sum(), q3.sum(), q4.sum()


def run_part1(): # 221579072 Too low 
    size_y = 103 # 7 
    size_x = 101 # 11
    data = load_data("data/day14_input.txt")
    updated_data = data
    for _ in tqdm(iterable=range(100), desc='Progress Report - 1'): 
        data = updated_data
        updated_data = []
        for robot in data: 
            new_pos = calcul_new_pos(robot, size_y, size_x)
            updated_data.append([new_pos, robot[1]])
    bathroom = create_grid(size_y, size_x)
    for robot in updated_data: 
        bathroom = place_robot(bathroom, robot)
    # print(bathroom)
    sumq1, sumq2, sumq3, sumq4 = count_robot_in_bathroom(bathroom)
    total = sumq1 * sumq2 * sumq3 * sumq4
    print(total)


def generate_random_colormap(matrix):
    unique_values = np.unique(matrix)
    colors = {}
    for val in unique_values:
        if val == 0:
            colors[val] = "white"  # Remove white color
        else:
            hue = random.random()  
            saturation = random.uniform(0.9, 1)  # Maximum saturation
            value = random.uniform(0.8, 1)  # High brightness 
            rgb = mcolors.hsv_to_rgb((hue, saturation, value))
            colors[val] = mcolors.to_hex(rgb)
    return colors


def plot_heatmap_from_matrix(matrix, title):
    plt.figure(figsize=(50, 50))
    colors = generate_random_colormap(matrix)
    cmap = mcolors.ListedColormap([colors[val] for val in sorted(colors.keys())])
    bounds = sorted(colors.keys())
    norm = mcolors.BoundaryNorm(bounds, cmap.N)
    sns.heatmap(
        matrix, cmap=cmap, cbar=False, square=True,
        linewidths=0.5, linecolor='black', xticklabels=False, yticklabels=False, norm=norm)
    plt.savefig('day14_plot/{}.png'.format(title))
    plt.close()


def create_animation(folder_path):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    images = []
    for file in tqdm(iterable=sorted(os.listdir(folder_path), key=alphanum_key), desc='Creating Gif'):
        file_path = os.path.join(folder_path, file)
        images.append(io.imread(file_path))
    frame_durations = [0.1] * (len(images) - 1) + [2]  # e.g., 0.1s per frame, 2s for the last frame
    io.mimsave('day14_gif.gif', images, duration=frame_durations, loop=0)


def run_part2():  # 7371 
    # size_y = 103 # 7 
    # size_x = 101 # 11
    # data = load_data("data/day14_input.txt")
    # counter = 0
    # good_value = 7371
    # updated_data = data
    # for i in tqdm(iterable=range(0, 7372), desc='Progress Report - 2'): 
    #     bathroom = create_grid(size_y, size_x)
    #     for robot in updated_data: 
    #         bathroom = place_robot(bathroom, robot)
    #     if counter == good_value: 
    #         # print(i)
    #         # print(counter)
    #         plot_heatmap_from_matrix(bathroom, i)
    #         good_value += 100
    #     counter += 1
    #     data = updated_data
    #     updated_data = []
    #     for robot in data: 
    #         new_pos = calcul_new_pos(robot, size_y, size_x)
    #         updated_data.append([new_pos, robot[1]])
    create_animation('day14_plot')


if __name__ == '__main__': 
    print('start')
    # position_test()
    # run_part1()
    run_part2()
    print('end')

