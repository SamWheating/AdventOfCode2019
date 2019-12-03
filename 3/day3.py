import math

with open('3/input.txt', 'r') as inputfile:
    inputs = inputfile.readlines()
    input1 = inputs[0].split(',')
    input2 = inputs[1].split(',')

# Part 1

DIRECTIONS = {
              'U': (0,1),
              'D': (0, -1),
              'L': (-1, 0),
              'R': (1, 0)
            }

def trace_wire_set(wire):
    """ Returns a set of all coordinates covered by a wire, relative to center at 0,0 """
    coords = set()
    position = (0,0)
    for instruction in wire:
        direction = DIRECTIONS[instruction[0]]
        for i in range(int(instruction[1:])):
            position = (position[0] + direction[0], position[1] + direction[1])
            coords.add(position)
    return coords

assert trace_wire_set(['U2', 'L1', 'D2']) == {(0,1), (0,2), (-1, 2), (-1,1), (-1, 0)}

def part1(wire1, wire2):
    coords1 = trace_wire_set(wire1)
    coords2 = trace_wire_set(wire2)
    intersections = [i for i in coords1 if i in coords2]
    return min([math.fabs(i[0]) + math.fabs(i[1]) for i in intersections])

assert part1(['R8','U5','L5','D3'], ['U7','R6','D4','L4']) == 6
assert part1(['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51'],['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']) == 135
assert part1(['R75','D30','R83','U83','L12','D49','R71','U7','L72'],['U62','R66','U55','R34','D71','R55','D58','R83']) == 159

print("Part 1 solution: {}".format(part1(input1, input2)))

# part 2:

def trace_wire_list(wire):
    """ Returns a list of all coordinates covered by a wire, relative to center at 0,0 """
    coords = [(0,0)]
    position = (0,0)
    for instruction in wire:
        direction = DIRECTIONS[instruction[0]]
        for i in range(int(instruction[1:])):
            position = (position[0] + direction[0], position[1] + direction[1])
            coords.append(position)
    return coords

def get_intersections(wire1, wire2):
    """ Takes two wires and returns all the intersections between them """
    coords1 = trace_wire_set(wire1)
    coords2 = trace_wire_set(wire2)
    return [i for i in coords1 if i in coords2]

def part2(input1, input2):
    intersections = get_intersections(input1, input2)
    wire1 = trace_wire_list(input1)
    wire2 = trace_wire_list(input2)
    combined_distances = {}
    for intersection in intersections:
        combined_distances[intersection] = wire1.index(intersection) + wire2.index(intersection)
    return min(combined_distances.values())

assert part2(['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51'],['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']) == 410
assert part2(['R75','D30','R83','U83','L12','D49','R71','U7','L72'],['U62','R66','U55','R34','D71','R55','D58','R83']) == 610

print("Part 2 solution: {}".format(part2(input1, input2)))

