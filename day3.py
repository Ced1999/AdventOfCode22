def part1():
    data = open("input3.txt").read().splitlines()
    priorities = []
    for backpack in data:
        first = backpack[:len(backpack) // 2]
        second = backpack[len(backpack) // 2:]
        intersect = "".join(set(first) & set(second))
        for item in intersect:
            if item.islower():
                priorities.append(ord(item) - 96)
            if item.isupper():
                priorities.append(ord(item) - 38)
    return sum(priorities)


def part2():
    data = open("input3.txt").read().splitlines()
    sum = 0
    for index in range(0, len(data), 3):
        first = set(data[index])
        second = set(data[index + 1])
        third = set(data[index + 2])
        item = "".join(first & second & third)
        if item.islower():
            sum += ord(item) - 96
        if item.isupper():
            sum += ord(item) - 38

    return sum


print(part1())
print(part2())
