# Day12 - AoC 2025


from shapely import Polygon, MultiPolygon
import shapely.geometry as geom
import pyvista as pv 
import numpy as np
import pandas as pd 
import geopandas as gpd
import matplotlib.pyplot as plt


def read_input(path):
    with open(path) as f: 
        content = [line.strip() for line in f.readlines()]
    all_shape, regions = [], []
    shape = []
    for line in content: 
        if line == '': 
            shape.pop(0)
            all_shape.append(shape)
            shape = []
        else: 
            shape.append(line)
    for line in reversed(content): 
        if line == '': 
            break 
        regions.append(line)
    return all_shape, regions


# Part1 
def extract_info_region(regions): 
    formatted_regions = []
    for region in regions: 
        size_raw = region.split(':')[0]
        x, y = size_raw.split('x')
        size = (int(x), int(y))
        content = region.split(':')[1]
        content_raw = content.split(' ')
        content_raw.pop(0)
        formatted_content = [int(l) for l in content_raw]
        formatted_regions.append([size, formatted_content])
    return formatted_regions


def create_3d_object(pts, plot=False): 
    pts_array = np.array(pts, dtype=float)
    pts3 = np.c_[pts_array, np.zeros(len(pts_array))]

    n = len(pts3)
    faces = np.hstack([[n], np.arange(n)])
    poly = pv.PolyData(pts3, faces)
    object_3d = poly.triangulate()
    if plot: 
        object_3d.plot(color="skyblue", show_edges=True)
    return object_3d


# def create_shape_object(): 
    
#     # shapes = []
#     # for i in range(len(shapes)): 
#     #     for j in range(len(shapes[i])):
#     #         if shapes[i][j] == '#':
#     #             edges_square = [(i, j), (i+1, j), (i, j+1), (i+1, j+1)]
    
#     object_0 = create_3d_object([(0,0), (0,3), (3,3), (3,2), (2,2), (2,0)])
#     object_1 = create_3d_object([(0,1), (0,3), (3,3), (3,2), (2,2), (2,1), (3,1), (3,0), (1,0), (1,1)])
#     object_2 = create_3d_object([(0,0), (0,2), (1,2), (1,3), (3,3), (3,1), (2,1), (2,0)])
#     object_3 = create_3d_object([(0,0), (0,3), (2,3), (2,2), (3,2), (3,1), (2,1), (2,0)])
#     object_4 = create_3d_object([(0,0), (0,3), (3,3), (3,2), (1,2), (1,1), (3,1), (3,0)]) 
#     object_5 = create_3d_object([(0,0), (0,1), (1,1), (1,2), (0,2), (0,3), (3,3), (3,2), (2,2), (2,1), (3,1), (3,0)])

#     return [object_0, object_1, object_2, object_3, object_4, object_5]


def create_shape_object(): 
    object_0 = create_3d_object([(0,0), (0,3), (2,3), (2,2), (3,2), (3,0), (2,0), (2,1), (1,1), (1,0)])
    poly_0 = Polygon([(0,0), (0,3), (2,3), (2,2), (3,2), (3,0), (2,0), (2,1), (1,1), (1,0)])

    object_1 = create_3d_object([(0,1), (0,3), (3,3), (3,0), (2,0), (2,1)])
    poly_1 = Polygon([(0,1), (0,3), (3,3), (3,0), (2,0), (2,1)])

    object_2 = create_3d_object([(0,0), (0,1), (2,1), (2,2), (0,2), (0,3), (3,3), (3,0)])
    ploy_2 = Polygon([(0,0), (0,1), (2,1), (2,2), (0,2), (0,3), (3,3), (3,0)])

    object_3 = create_3d_object([(0,0), (0,3), (1,3), (1,2), (2,2), (2,1), (3,1), (3,0)])
    ploy_3 = Polygon([(0,0), (0,3), (1,3), (1,2), (2,2), (2,1), (3,1), (3,0)])

    object_4 = create_3d_object([(0,0), (0,3), (1,3), (1,2), (2,2), (2,3), (3,3), (3,0), (2,0), (2,1), (1,1), (1,0)]) 
    ploy_4 = Polygon([(0,0), (0,3), (1,3), (1,2), (2,2), (2,3), (3,3), (3,0), (2,0), (2,1), (1,1), (1,0)]) 

    object_5 = create_3d_object([(0,1), (0,3), (1,3), (1,2), (2,2), (2,1), (3,1), (3,0), (1,0), (1,1)])
    ploy_5 = Polygon([(0,1), (0,3), (1,3), (1,2), (2,2), (2,1), (3,1), (3,0), (1,0), (1,1)])

    return [poly_0, poly_1, ploy_2, ploy_3, ploy_4, ploy_5]

    
def is_enought_place(region, shapes): 
    x, y = region[0]
    # box = create_3d_object([(0,0), (x,0), (x,y), (0,y)])
    box = Polygon([(0,0), (x,0), (x,y), (0,y)])
    total_area = 0 
    for i in range(len(region[1])):
        total_area += shapes[i].area * region[1][i]
    if total_area > box.area: 
        return False
    return True

      
def run_part1():
    content = read_input('2025/data/input_day12.txt')
    # content = read_input('2025/data/input_test.txt')
    _, regions = content
    regions = extract_info_region(regions)
    shapes = create_shape_object()
    nb_valid = 0 
    for region in regions: 
        # is_enought_place(region, shapes)
        if is_enought_place(region, shapes): 
            nb_valid += 1 
    print(nb_valid)

            


# Part2
def run_part2():
    pass


if __name__ == "__main__":
    print('start')
    run_part1()
    run_part2()
    print('end')    