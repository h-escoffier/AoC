# Day9 - AoC 2025 


# I used the package Shapely for the part2


from itertools import combinations
from shapely import Polygon


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
    print(b_area, best_pts)
    

if __name__ == '__main__': 
    print('start')
    run_part1()
    run_part2()
    print('end')
