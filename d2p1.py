def checkSafety(input):
    input = input.strip().split("\n")
    counter = 0

    for i in input:
        numbers = list(map(int, i.split()))
        is_safe = True
        increasing = None

        for j in range(1, len(numbers)):
            diff = numbers[j] - numbers[j - 1]

            if abs(diff) < 1 or abs(diff) > 3:
                is_safe = False
                break

            if increasing is None:
                increasing = diff > 0
            elif (increasing and diff < 0) or (not increasing and diff > 0):
                is_safe = False
                break

        if is_safe:
            counter += 1

    print("Counter:", counter)  # Print the counter value

# Read the input file and call the function
with open("input.txt", "r") as f:
    content = f.read()

checkSafety(content)
