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


print(part1())
