counter = 0

def checkSafety(input):
    global counter
    input = input.strip().split("\n")

    for i in input:
        numbers = list(map(int, i.split()))
        is_safe = True
        increasing = None

        for j in range(1, len(numbers)):
            diff = numbers[j] - numbers[j - 1]

            if abs(diff) < 1 or abs(diff) > 3:
                is_safe = False
                dampener(numbers)
                break

            if increasing is None:
                increasing = diff > 0
            elif (increasing and diff < 0) or (not increasing and diff > 0):
                is_safe = False
                dampener(numbers)
                break

        if is_safe:
            counter += 1

def dampener(list):
    global counter
    index = 0

    while index < len(list):
        new_list = list.copy()
        new_list.pop(index)
        is_safe = True
        increasing = None

        for i in range(1, len(new_list)):
            diff = new_list[i] - new_list[i - 1]

            if abs(diff) < 1 or abs(diff) > 3:
                is_safe = False
                index += 1
                break

            if increasing is None:
                increasing = diff > 0
            elif (increasing and diff < 0) or (not increasing and diff > 0):
                is_safe = False
                index += 1
                break

        if is_safe:
            counter += 1
            return
        
# Read the input file and call the function
with open("input.txt", "r") as f:
    content = f.read()

checkSafety(content)
print(counter)
