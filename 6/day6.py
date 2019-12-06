with open('6/input.txt', 'r') as inputfile:
    inputs = inputfile.readlines()
    inputs = [row.replace('\n', '').split(')') for row in inputs]

test_input = [['COM', 'B'],
                ['B','C'],
                ['C','D'],
                ['D','E'],
                ['E','F'],
                ['B','G'],
                ['G','H'],
                ['D','I'],
                ['E','J'],
                ['J','K'],
                ['K','L']]

# Part 1:

def get_indirects(orbits, planet):
    """recursively finds all orbits + indirect orbits"""
    if planet == "COM":
        return []
    else: 
        planets_below = get_indirects(orbits, orbits[planet])
        planets_below.append(orbits[planet])
        return planets_below

def part1(inputs):
    orbits = {}       #  {moon: earth}
    indirects = {}
    # amass all direct orbits
    for orbit in inputs:
        if orbit[1] not in orbits:
            orbits[orbit[1]] = orbit[0]
    unique_planets = list(set(orbits.keys()))
    for planet in unique_planets:
        indirects[planet] = get_indirects(orbits, planet)
    return sum([len(indirects[planet]) for planet in unique_planets])

assert part1(test_input) == 42

print("Part 1 Solution: {}".format(part1(inputs)))

# Part 2:

def part2(inputs):
    orbits = {}       #  {moon: earth}
    indirects = {}
    # amass all direct orbits
    for orbit in inputs:
        if orbit[1] not in orbits:
            orbits[orbit[1]] = orbit[0]
    unique_planets = list(set(orbits.keys()))
    # amass all indirect orbits as a path to COM
    for planet in unique_planets:
        indirects[planet] = get_indirects(orbits, planet)
    minimum_distance = 100000000    # big!    
    for planet in unique_planets:   # Consider every planet as a possible turnaround point 
        if planet not in indirects['YOU']:
            continue
        if planet not in indirects['SAN']:
            continue
        distance_down = len(indirects['YOU']) - indirects['YOU'].index(planet)
        distance_up = len(indirects['SAN']) - indirects['SAN'].index(planet)
        distance = distance_up + distance_down
        if distance < minimum_distance:
            minimum_distance = distance
    return minimum_distance - 2     # have to remove the initial orbit on each end of the trip

test_input2 = [['COM', 'B'],
                ['B','C'],
                ['C','D'],
                ['D','E'],
                ['E','F'],
                ['B','G'],
                ['G','H'],
                ['D','I'],
                ['E','J'],
                ['J','K'],
                ['K','L'],
                ['K','YOU'],
                ['I','SAN']]

assert part2(test_input2) == 4

print("Part 2 solution: {}".format(part2(inputs)))
