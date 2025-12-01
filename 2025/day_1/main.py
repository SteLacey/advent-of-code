import math


def part_1(f: list[str]):
    start = 50
    zeros = 0
    for r in f:
        start = rot_dial_p1(r, start)
        if start == 0:
            zeros += 1
    print(f"Part 1: {zeros}")

def part_2(f: list[str]): # This is rubbish and there's definitely a better way than hardcoding edge cases lol
    start = 50
    clicks = 0
    for r in f:
        print(f"Start: {start}, Rot: {r.strip()}", end=", ")
        new = rot_dial_p2(r, start)
        if new < 1 or new > 99:
            calc = 1 if new == 0 else abs(math.floor(new / 100))
            if new < 0 and start == 0: # This is a disaster
                calc -= 1
            if new < 0 and new % 100 == 0: # So is this
                calc += 1
            print(f"New: {new}, Inc: {calc}")
            clicks += calc
        else:
            print(f"New: {new}")
        start = new % 100
    print(f"Part 2: {clicks}")


def rot_dial_p1(rot: str, start: int) -> int:
    delta = parse_rot(rot)
    return (start + delta) % 100


def rot_dial_p2(rot: str, start: int) -> int:
    delta = parse_rot(rot)
    return start + delta

def parse_rot(rot: str) -> int:
    amount = int(rot[1:])
    return -1 * amount if rot[0] == 'L' else amount

def read_file() -> list[str]:
    with open('input.txt') as f:
        return f.readlines()


if __name__ == '__main__':
    file = read_file()
    part_1(file)
    part_2(file)

