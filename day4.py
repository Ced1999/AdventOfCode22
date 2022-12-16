def part1():
    count = 0
    with open("input4.txt") as file:
        data = file.read().splitlines()
    for pair in data:
        first = pair.split(",")
        startstop0 = first[0].split("-")
        startstop1 = first[1].split("-")
        range1 = set(range(int(startstop0[0]), int(startstop0[1]) + 1))
        range2 = set(range(int(startstop1[0]), int(startstop1[1]) + 1))
        if range1.issubset(range2) or range2.issubset(range1):
            count += 1

    return count


def part2():
    count = 0
    with open("input4.txt") as file:
        data = file.read().splitlines()
    for pair in data:
        first = pair.split(",")
        startstop0 = first[0].split("-")
        startstop1 = first[1].split("-")
        range1 = set(range(int(startstop0[0]), int(startstop0[1]) + 1))
        range2 = set(range(int(startstop1[0]), int(startstop1[1]) + 1))
        if range1 & range2 != set():
            count += 1
    return count


print(part1())
print(part2())
