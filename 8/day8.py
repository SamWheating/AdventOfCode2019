with open('8/input.txt', 'r') as inputfile:
    inputs = inputfile.readlines()[0]
inputs = [int(digit) for digit in inputs]

WIDTH = 25
HEIGHT = 6

def part1(inputs):
    layers = [inputs[i*150:(i+1)*150] for i in range(int(len(inputs)/(WIDTH*HEIGHT)))]
    least_zeros = 100000
    for layer in layers:
        if layer.count(0) < least_zeros:
            least_zeros = layer.count(0)
            liq = layer
    return liq.count(1) * liq.count(2)

print("Part 1 Solution: {}".format(part1(inputs)))

def form_pixels(inputs):
    pixels = [[[] for i in range(HEIGHT)] for i in range(WIDTH)]
    row = 0
    col = 0
    for bit in inputs:
        pixels[col][row].append(bit)
        col += 1
        if col == WIDTH:
            col = 0
            row += 1
        if row == HEIGHT:
            row = 0
    return pixels

def get_colour(pixel):
    for i in range(len(pixel)):
        if pixel[i] == 1:
            return '█'
        if pixel[i] == 0:
            return ' '
    raise Exception("Fully transparent pixel?") 

def print_pixels(pixels):
    for row in range(HEIGHT):
        disp = ""
        for col in range(WIDTH):
            disp += get_colour(pixels[col][row])
        print(disp)

def part2(inputs):
    pixels = form_pixels(inputs)
    print_pixels(pixels)

print("Part 2 Solution:")
part2(inputs)
