with open('5/input.txt', 'r') as inputfile:
    inputs = inputfile.readlines()[0]
inputs = [int(i) for i in inputs.split(",")]

# Part 1:

def part1(program, input_value):
    i = 0
    while i != len(program)-1:
        if program[i] % 100 == 99:
            break
        elif program[i] % 100 == 1:     # ADD
            op1 = program[i+1] if (program[i] % 1000 - program[i] % 100)/100 == 1  else program[program[i+1]]
            op2 = program[i+2] if (program[i] % 10000 - program[i] % 1000)/1000 == 1  else program[program[i+2]]
            program[program[i + 3]] = op1 + op2
            i = i + 4
        elif program[i] % 100 == 2:     # SUB
            op1 = program[i+1] if (program[i] % 1000 - program[i] % 100)/100 == 1  else program[program[i+1]]
            op2 = program[i+2] if (program[i] % 10000 - program[i] % 1000)/1000 == 1  else program[program[i+2]]
            program[program[i + 3]] = op1 * op2
            i = i + 4
        elif program[i] % 100 == 3:     # INPUT
            program[program[i + 1]] = input_value 
            i = i + 2
        elif program[i] % 100 == 4:     # OUTPUT
            op1 = program[i+1] if (program[i] % 1000 - program[i] % 100)/100 == 1  else program[program[i+1]]
            if op1 != 0:
                print("Debug Output: {}".format(op1))
            i = i + 2
    return

tmp_program = inputs.copy()
print("Part 1 solution:")
part1(tmp_program, 1)

# Part 2:

def part2(program, input_value):
    i = 0
    while i != len(program)-1:
        if program[i] % 100 == 99:
            return
        elif program[i] % 100 == 1:     # Add
            op1 = program[i+1] if (program[i] % 1000 - program[i] % 100)/100 == 1  else program[program[i+1]]
            op2 = program[i+2] if (program[i] % 10000 - program[i] % 1000)/1000 == 1  else program[program[i+2]]
            program[program[i + 3]] = op1 + op2
            i = i + 4
        elif program[i] % 100 == 2:     # Subtract
            op1 = program[i+1] if (program[i] % 1000 - program[i] % 100)/100 == 1  else program[program[i+1]]
            op2 = program[i+2] if (program[i] % 10000 - program[i] % 1000)/1000 == 1  else program[program[i+2]]
            program[program[i + 3]] = op1 * op2
            i = i + 4
        elif program[i] % 100 == 3:     # Input
            program[program[i + 1]] = input_value
            i = i + 2
        elif program[i] % 100 == 4:     # Output
            op1 = program[i+1] if (program[i] % 1000 - program[i] % 100)/100 == 1  else program[program[i+1]]
            return op1
        elif program[i] % 100 == 5:     # Jump if true
            op1 = program[i+1] if (program[i] % 1000 - program[i] % 100)/100 == 1  else program[program[i+1]]
            op2 = program[i+2] if (program[i] % 10000 - program[i] % 1000)/1000 == 1  else program[program[i+2]]
            if op1 != 0:
                i = op2
            else:
                i = i + 3
        elif program[i] % 100 == 6:     # Jump if false
            op1 = program[i+1] if (program[i] % 1000 - program[i] % 100)/100 == 1  else program[program[i+1]]
            op2 = program[i+2] if (program[i] % 10000 - program[i] % 1000)/1000 == 1  else program[program[i+2]]
            if op1 == 0:
                i = op2
            else:
                i = i + 3
        elif program[i] % 100 == 7:     # Less than
            op1 = program[i+1] if (program[i] % 1000 - program[i] % 100)/100 == 1  else program[program[i+1]]
            op2 = program[i+2] if (program[i] % 10000 - program[i] % 1000)/1000 == 1  else program[program[i+2]]
            if op1 < op2:
                program[program[i+3]] = 1
            else:
                program[program[i+3]] = 0
            i = i + 4
        elif program[i] % 100 == 8:     # Equals
            op1 = program[i+1] if (program[i] % 1000 - program[i] % 100)/100 == 1  else program[program[i+1]]
            op2 = program[i+2] if (program[i] % 10000 - program[i] % 1000)/1000 == 1  else program[program[i+2]]
            if op1 == op2:
                program[program[i+3]] = 1
            else:
                program[program[i+3]] = 0
            i = i + 4
    return

# Test cases:
assert part2([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99], 7) == 999
assert part2([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99], 8) == 1000
assert part2([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99], 9) == 1001

tmp_program = inputs.copy()
print("\nPart 2 solution: {}".format(part2(tmp_program, 5)))
