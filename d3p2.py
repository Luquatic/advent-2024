import re

with open('input.txt', 'r') as file:
    content = file.read()

def main():
    sum = 0
    pattern = r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)'
    matches = re.findall(pattern, content)
    enabled = True
    new_matches = []

    for index, match in enumerate(matches):
        if match == 'don\'t()':
            enabled = False
        elif match == 'do()':
            enabled = True
            
        
        if enabled and match != 'do()' and match != 'don\'t()':
            new_matches.append(matches[index])

    for match in new_matches:
        numbers = re.findall(r'\d{1,3}', match)
        sum += int(numbers[0]) * int(numbers[1])

    print(sum)

    

if __name__ == "__main__":
    main()
