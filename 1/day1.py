import math

# Part 1:

modules = []
with open('1/input.txt', 'r') as inputfile:
    modules = inputfile.readlines()

def fuel(mass):
    return math.floor(mass/3) - 2

modules = [float(mass.replace('\n', '')) for mass in modules]
solution = sum([fuel(mass) for mass in modules])

assert fuel(100756) == 33583

print("Part 1 Solution: {}".format(solution))

# Part 2:

def calculate_fuel(mass):
    current = fuel(mass)
    total = current
    while(True):
        new = fuel(current)
        if new > 0:
            current = new
            total = total + new
        else:
            break
    return total

assert calculate_fuel(100756) == 50346

solution = sum([calculate_fuel(mass) for mass in modules])
print("Part 2 Solution: {}".format(solution))
