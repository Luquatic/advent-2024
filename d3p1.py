import re

with open('input.txt', 'r') as file:
    content = file.read()

def main():
    sum = 0
    pattern = r'mul\(\d{1,3},\d{1,3}\)'
    matches = re.findall(pattern, content)

    for match in matches:
        numbers = re.findall(r'\d{1,3}', match)
        sum += int(numbers[0]) * int(numbers[1])

    print(sum)

    

if __name__ == "__main__":
    main()
