def get_max_calories():
    file = open("input1.txt")
    data = file.read().split("\n")
    count = 0
    max = 0
    for item in data:
        if item == "":
            if count > max:
                max = count
            count = 0
        else:
            count += int(item)
    return max


def get_max_calories_listcomp():
    return max([sum(map(int, item.split())) for item in open("input1.txt").read().strip().split("\n\n") if item is not ""])
def get_top_three_listcomp():
    return sum(sorted([sum(map(int, item.split())) for item in open("input1.txt").read().strip().split("\n\n") if item is not ""])[-3:])

def get_top_three():
    file = open("input1.txt")
    data = file.read().split("\n")
    elfs = []
    count = 0
    max = 0
    for item in data:
        if item == "":
            if count > max:
                max = count
            elfs.append(count)
            count = 0
        else:
            count += int(item)
    elfs.sort()
    return sum(elfs[-3:])


print(get_max_calories())
print(get_top_three())
print(get_max_calories_listcomp())
print(get_top_three_listcomp())