import re

# inputs
lb = 231832
ub = 767346

# Part 1:

def validate_code_part1(code):
    code = str(code)
    if re.search(r"(\d)\1{1}", code) is None:
        return False
    digits = [int(c) for c in code]
    for i in range(len(digits)-1):
        if digits[i+1] < digits[i]:
            return False
    return True

assert validate_code_part1(111111)
assert not validate_code_part1(223450)
assert not validate_code_part1(123456)

count = 0
for i in range(lb, ub+1):
    if validate_code_part1(i):
        count += 1

print("Part 1 Solution: {}".format(count))

# Part 2:

def validate_code_part2(code):
    code = str(code)
    digits = [int(c) for c in code]
    for i in range(len(digits)-1):
        if digits[i+1] < digits[i]:
            return False
    # Check for the presence of exactly 2 identical adjacent digits
    # This is super hacky but I'm short on time + regex skills
    double_criteria = False
    for i in range(10):
        regex_string = "(?<![{0}])([{0}][{0}])(?![{0}]+)".format(i)
        if re.search(regex_string, code) is not None:
            double_criteria = True
    if not double_criteria:
        return False
    return True

assert validate_code_part2(112233)
assert not validate_code_part2(123444)
assert validate_code_part2(112222)

count = 0
for i in range(lb, ub+1):
    if validate_code_part2(i):
        count += 1

print("Part 2 Solution: {}".format(count))