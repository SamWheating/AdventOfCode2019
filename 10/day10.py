from math import gcd, atan2, pi
import sys

with open('10/input.txt') as ifp:
    inputs = ifp.readlines()
inputs = [[a for a in list(line) if a != '\n'] for line in inputs]
# address points as inputs[x][y]

# Test inputs

test_input_1 = [['.','#','.','.','#'],
                ['.','.','.','.','.'],
                ['#','#','#','#','#'],
                ['.','.','.','.','#'],
                ['.','.','.','#','#']]

test_input_2 = [['.','.','.','.','.','.','#','.','#','.'],
                ['#','.','.','#','.','#','.','.','.','.'],
                ['.','.','#','#','#','#','#','#','#','.'],
                ['.','#','.','#','.','#','#','#','.','.'],
                ['.','#','.','.','#','.','.','.','.','.'],
                ['.','.','#','.','.','.','.','#','.','#'],
                ['#','.','.','#','.','.','.','.','#','.'],
                ['.','#','#','.','#','.','.','#','#','#'],
                ['#','#','.','.','.','#','.','.','#','.'],
                ['.','#','.','.','.','.','#','#','#','#']]

with open('10/test_input3.txt') as ifp:
    test_input_3 = ifp.readlines()
    test_input_3 = [[a for a in list(line) if a != '\n'] for line in test_input_3]

# Part 1

def count_visible(base, coords):
    """ Given a base coordinate and the coordinate of all meteors,
    counts the number of meteors visible from the base. """
    coords = [coord for coord in coords if coord != base]
    relative_coords = []
    for coord in coords:
        relative_coords.append(((coord[0] - base[0]),(coord[1] - base[1])))
    reduced = set()
    for coord in relative_coords:
        reduced.add((coord[0]/gcd(coord[0], coord[1]), (coord[1]/gcd(coord[0], coord[1]))))
    return len(reduced)

def part1(inputs):
    """ Given the raw map data, finds the meteor from which the most others can be seen. """
    coords = []
    width = len(inputs[0])
    height = len(inputs)
    for x in range(width):
        for y in range(height):
            if inputs[y][x] == '#':
                coords.append((x,y))
    counts = []
    for coord in coords:
        counts.append(count_visible(coord, coords))
    return(max(counts))

# test cases:

assert part1(test_input_1) == 8
assert part1(test_input_2) == 33
assert part1(test_input_3) == 210

print("Part 1 Solution: {}".format(part1(inputs)))

# Part 2:

def get_base_coords(inputs):
    coords = []
    width = len(inputs[0])
    height = len(inputs)
    for x in range(width):
        for y in range(height):
            if inputs[y][x] == '#':
                coords.append((x,y))
    counts = {}
    for coord in coords:
        counts[count_visible(coord, coords)] = coord
    return counts[max(counts.keys())]


def find_closest(base, coords):
    if len(coords) == 1:
        return coords[0]
    lowest_dist = 100000000
    for coord in coords:
        dist = (base[0] - coord[0])**2 + (base[1] - coord[1])**2
        if dist < lowest_dist:
            lowest_dist = dist
            best = coord
    return best

    
def part2(inputs):
    # Create a dict of {angle(rad) : [all meteors in that line]
    base = get_base_coords(inputs)
    coords = []
    width = len(inputs[0])
    height = len(inputs)
    for x in range(width):
        for y in range(height):
            if inputs[y][x] == '#':
                coords.append((x,y))
    coords = [coord for coord in coords if coord != base]
    relative_coords = {}
    angles = {}
    for coord in coords:
        # Computes angle, up is pi/2, left is -pi/2 right is 0.
        angle = atan2((base[1] - coord[1]),(coord[0] - base[0]))
        if angle in angles:
            angles[angle].append(coord)
        else:
            angles[angle] = [coord]

    laser_angle = pi/2 + 0.001  # Start facing straight up (just a hair left)
    destroyed = 0
    while(destroyed < 200):
        sorted_angles = [angle for angle in angles if angle < laser_angle]
        if len(sorted_angles) == 0:
            laser_angle = pi + 0.001
            continue
        sorted_angles.sort(reverse=True)
        laser_angle = sorted_angles[0]
        target = find_closest(base, angles[laser_angle])
        # print("{}: {}".format(destroyed+1,target))
        angles[laser_angle].remove(target)
        if angles[laser_angle] == []:
            del angles[laser_angle]
        destroyed += 1
        
    return target[0] * 100 + target[1]

assert part2(test_input_3) == 802

print("Part 2 Solution: {}".format(part2(inputs)))
