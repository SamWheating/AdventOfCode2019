import itertools
import time

with open('7/input.txt', 'r') as inputfile:
    inputs = inputfile.readlines()[0]
inputs = [int(i) for i in inputs.split(",")]

class IntCodeProgramHalt(Exception):
    pass

class IntProgComputer():

    def __init__(self, instructions, phase_setting):
        self.state = instructions.copy()
        self.input_values = [phase_setting]
        self.has_run = False
        self.ip = 0             # instruction pointer to keep between runs

    def queue_input(self, value):
        """ Adds input to the computers FIFO queue of inputs"""
        self.input_values.insert(0, value)

    def intcode_runprog(self):
        # will run from current ip to next output
        i = self.ip
        program = self.state
        while i != len(program)-1:
            if program[i] % 100 == 99:
                raise IntCodeProgramHalt("Halting Program Execution.")
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
                program[program[i + 1]] = self.input_values.pop()
                i = i + 2
            elif program[i] % 100 == 4:     # Output
                op1 = program[i+1] if (program[i] % 1000 - program[i] % 100)/100 == 1  else program[program[i+1]]
                i = i + 2
                self.ip = i
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
            else:
                print("HALTING")
        return

def chain_amps(program, settings):
    """Run the program on 5 intcode computers, providing the given series of inputs
    The program expects 2 settings in order [input_signal, phase_setting]"""
    computers = []
    for setting in settings:
        computers.append(IntProgComputer(program, setting))

    computers[0].queue_input(0)
    computers[1].queue_input(computers[0].intcode_runprog())
    computers[2].queue_input(computers[1].intcode_runprog())
    computers[3].queue_input(computers[2].intcode_runprog())
    computers[4].queue_input(computers[3].intcode_runprog())
    return computers[4].intcode_runprog()

test_prog1 = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
test_settings1 = [4,3,2,1,0]
assert chain_amps(test_prog1, test_settings1) == 43210

def part1(program):
    max_output = 0
    for settings in itertools.permutations([0,1,2,3,4]):
        output = chain_amps(program, settings)
        if output > max_output:
            max_output = output
    return max_output

assert part1(test_prog1) == 43210

print("Part 1 Solution: {}".format(part1(inputs)))

# Part 2

def chain_amps_feedback(program, settings):
    """
    Run 5 amplifiers in series with the provided initial settings
    An output of one amplifier is passed to the input of the next one.
    Amp 5 input is fed back to Amp 1.
    Instruction pointers and program states are preserved.
    """
    computers = []
    for setting in settings:
        computers.append(IntProgComputer(program, setting))

    feedback_line = 0
    while True:
        try:
            computers[0].queue_input(feedback_line)
            computers[1].queue_input(computers[0].intcode_runprog())
            computers[2].queue_input(computers[1].intcode_runprog())
            computers[3].queue_input(computers[2].intcode_runprog())
            computers[4].queue_input(computers[3].intcode_runprog())
            feedback_line = computers[4].intcode_runprog()
        except IntCodeProgramHalt:
            return feedback_line

test_prog2 = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
test_settings2 = [9,8,7,6,5]
test_prog3 = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]
test_settings3 = [9,7,8,5,6]

assert chain_amps_feedback(test_prog2, test_settings2) == 139629729
assert chain_amps_feedback(test_prog3, test_settings3) == 18216

def part2():
    max_output = 0
    for settings in itertools.permutations([5,6,7,8,9]):
        output = chain_amps_feedback(inputs, settings)
        if output > max_output:
            max_output = output
    return max_output

print("Part 2 Solution: {}".format(part2()))
