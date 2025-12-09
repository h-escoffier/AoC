# Day9 - AoC 2025 


# I used the package Shapely for the part2


from itertools import combinations
from tqdm import tqdm
from shapely import Polygon
import geopandas as gpd
import matplotlib.pyplot as plt
import imageio.v2 as imageio
import os, shutil


def read_input(path): 
    with open(path) as f: 
        content = [line.split() for line in f.readlines()]
        new_content, final_content = [], []
        for elm in content: 
            new_content.append(elm[0].split(','))
        for elm in new_content: 
            x, y = int(elm[0]), int(elm[1])
            final_content.append((x,y))
    return final_content


# Part1 
def find_biggest_rectangle(content): 
    biggest_area = 0 
    for pts1, pts2 in combinations(content, 2):
        area = calcul_area(pts1, pts2)
        if area > biggest_area: 
            biggest_area = area
            best_points = (pts1, pts2)
    return biggest_area, best_points


def calcul_area(pts1, pts2): 
    x1, y1 = pts1
    x2, y2 = pts2
    # diag = np.sqrt((x1 - x2)**2 + (y1 - y2))
    diff_x = abs(x1 - x2) + 1
    diff_y = abs(y1 - y2) + 1 
    return diff_x*diff_y


def run_part1():
    content = read_input('2025/data/input_day9.txt')
    # content = read_input('2025/data/input_test.txt')
    b_area, best_points = find_biggest_rectangle(content)
    print(b_area, best_points)


# Part2
def identify_rectangle_inside(content): 
    polygon = Polygon(content)
    b_area = 0
    for pts1, pts2 in combinations(content, 2):
        pts3, pts4 = find_other_pts(pts1, pts2)
        test = Polygon([pts1, pts3, pts2, pts4])
        if test.covered_by(polygon): 
            area = calcul_area(pts1, pts2)
            if area > b_area: 
                b_area = area
                best_pts = (pts1, pts2)
    return b_area, best_pts
            

def find_other_pts(pts1, pts2): 
    x1, y1 = pts1
    x2, y2 = pts2
    pts3 = (x1, y2)
    pts4 = (x2, y1)
    return pts3, pts4


def run_part2(): 
    content = read_input('2025/data/input_day9.txt')
    # content = read_input('2025/data/input_test.txt')
    b_area, best_pts = identify_rectangle_inside(content)
    generate_gif(content)
    print(b_area, best_pts)


# Plot 
def generate_gif(content):
    polygon = Polygon(content)
    map_poly = gpd.GeoDataFrame(index=[0], geometry=[polygon])
    frames = []
    os.makedirs('frames', exist_ok=True)

    best_area = 0
    best_rect = None
    frame_id = 0
    counter = 0

    for pts1, pts2 in tqdm(combinations(content, 2)):
        is_best = False

        pts3, pts4 = find_other_pts(pts1, pts2)
        test = Polygon([pts1, pts3, pts2, pts4])

        ok = test.covered_by(polygon)
        area = calcul_area(pts1, pts2)

        counter += 1

        if ok and area > best_area:
            best_area = area
            best_rect = test     
            is_best = True       

        if counter % 500 == 0 or is_best:
            fig, ax = plt.subplots(figsize=(6, 6))
            fig.patch.set_facecolor('#222222')
            map_poly.boundary.plot(ax=ax, linewidth=1, color="#444444")
            map_poly.plot(ax=ax, color="#444444", alpha=1, edgecolor="#444444", linewidth=0.5)

            if best_rect:
                gpd.GeoSeries([best_rect]).boundary.plot(ax=ax, color="#E29D55", linewidth=0.5)
                gpd.GeoSeries([best_rect]).plot(ax=ax, color="#E29D55", alpha=1, edgecolor="#E29D55", linewidth=0.5)
            
            if ok:
                gpd.GeoSeries([test]).boundary.plot(ax=ax, color="#A8DB69", linewidth=0.5)
                gpd.GeoSeries([test]).plot(ax=ax, color="#A8DB69", alpha=0.5, edgecolor="#A8DB69", linewidth=0.5)
            else: 
                gpd.GeoSeries([test]).boundary.plot(ax=ax, color="#EBDD49", linewidth=0.5)
                gpd.GeoSeries([test]).plot(ax=ax, color="#EBDD49", alpha=0.9, edgecolor="#EBDD49", linewidth=0.5)

            ax.set_axis_off()

            fpath = f"frames/frame_{frame_id:04d}.png"
            plt.savefig(fpath, dpi=140)
            plt.close()
            frames.append(fpath)
            frame_id += 1

    with imageio.get_writer("2025/figures/gif_day9.gif", mode="I", fps=10, loop=0) as writer:
        for f in frames:
            writer.append_data(imageio.imread(f))

    shutil.rmtree("frames")


if __name__ == '__main__': 
    print('start')
    # run_part1()
    run_part2()
    print('end')
