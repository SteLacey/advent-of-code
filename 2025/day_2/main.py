import re

day_1_regex = r'^(\d+)\1$'
day_2_regex = r'^(\d+)\1+$'

def parse_input():
    with open('input.txt', 'r') as file:
        line = file.read()
        return line.split(',')


def find_invalid_ids(file: list, regex: str):
    total = 0
    for ids in file:
        split = ids.split('-')
        start = int(split[0])
        end = int(split[1])
        for i in range(start, end + 1):
            if re.match(regex, str(i)) is not None:
                total += i
    print(total)


if __name__ == '__main__':
    find_invalid_ids(parse_input(), day_1_regex)
    find_invalid_ids(parse_input(), day_2_regex)