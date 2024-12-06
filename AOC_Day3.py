import re

with open("input.txt", "r") as file:
    data = file.read()

#Define regex patterns
mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)" 
do_pattern = r"do\(\)"                       
dont_pattern = r"don't\(\)"                 

#processesing data to look for regex patterns
def process_memory(data):
    total_sum = 0
    include = True  #Start with mul instructions enabled by default

    # Iterate through memory character by character
    index = 0
    while index < len(data):
        # Check for do() 
        if re.match(do_pattern, data[index:]):
            include = True
            index += len("do()")
            continue

        # Check for don't()
        elif re.match(dont_pattern, data[index:]):
            include = False
            index += len("don't()")
            continue

        # Check for mul(x, y)
        mul_match = re.match(mul_pattern, data[index:])
        if mul_match:
            x, y = map(int, mul_match.groups())
            product = x * y
            if include:
                total_sum += product
            index += len(mul_match.group(0))  # Advance past the matched mul(x, y)
            continue

        # If no instruction matches, advance to the next character
        index += 1

    return total_sum

result = process_memory(data)
print(f"total sum of prods: {result}")