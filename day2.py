def part1():
    strategy = {"A X": 1 + 3, "A Y": 2 + 6, "A Z": 3 + 0,
                "B X": 1 + 0, "B Y": 2 + 3, "B Z": 3 + 6,
                "C X": 1 + 6, "C Y": 2 + 0, "C Z": 3 + 3}
    return sum([strategy[line] for line in open("input2.txt").read().split("\n")])


def part2():
    # A=ROCK1 B=PAPER2 C=SCISSORS3
    # X=LOSE0 Y=DRAW3  Z=WIN6
    strategy = {"A X": 3 + 0, "A Y": 1 + 3, "A Z": 2 + 6,
                "B X": 1 + 0, "B Y": 2 + 3, "B Z": 3 + 6,
                "C X": 2 + 0, "C Y": 3 + 3, "C Z": 1 + 6}
    return sum([strategy[line] for line in open("input2.txt").read().split("\n")])


print(part1())
print(part2())

# A:ROCK B: PAPER C: SCISSORS Enemy
# X:ROCK Y: PAPER Z: SCISSORS Me
