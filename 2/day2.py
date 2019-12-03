with open('2/input.txt', 'r') as inputfile:
    inputs = inputfile.readlines()[0]
inputs = [int(i) for i in inputs.split(",")]

# Part 1:

def part1(program):
    i = 0
    while i != len(program)-1:
        if program[i] == 99:
            return program
        elif program[i] == 1:
            program[program[i + 3]] = program[program[i+1]] + program[program[i+2]]
        elif program[i] == 2:
            program[program[i + 3]] = program[program[i+1]] * program[program[i+2]]
        i = i + 4
    return program

# test case:
assert part1([1,9,10,3,2,3,11,0,99,30,40,50]) == [3500,9,10,70,2,3,11,0,99,30,40,50]

tmp_program = inputs.copy()
tmp_program[1] = 12
tmp_program[2] = 2

print("Solution #1: {}".format(part1(tmp_program)[0]))

# Part 2:

def part2(program):
    for noun in range(100):
        for verb in range(100):
            tmp_program = inputs.copy()
            tmp_program[1] = noun
            tmp_program[2] = verb
            if part1(tmp_program)[0] == 19690720:
                return (100 * noun) + verb

# no test case ):

print("Solution #2: {}".format(part2(inputs)))
