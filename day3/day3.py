def get_letter_value(char):
    # lower case letter
    if ord(char) > 90:
        return ord(char) - 96
    else:
        return ord(char) - 38


def get_score_common_part(common_part):
    score = 0
    for letter in common_part:
        score += get_letter_value(letter)
    return score


def part1():
    common_part = set()
    mid_string = int(len(line) / 2)
    bag1, bag2 = line[:mid_string], line[mid_string:]
    # alternative way : common = list(set(bag1).intersection(set(bag2)))
    for letter in bag1:
        if letter in bag2:
            common_part.add(letter)
    return get_score_common_part(common_part)


def part2():
    # Alternative way
    # for i in range(0, len(input_list.read().splitlines()), 3):
    #     a, b, c = [set(items) for items in input_data[i:i + 3]]
    #     common = list(a & b & c)

    global elf_number
    score = 0
    elf_number += 1
    if elf_number % 3 == 0:
        for letter in elf_packages[0]:
            if letter in elf_packages[1] and \
                    letter in elf_packages[2]:
                common_part.add(letter)
        score += get_score_common_part(common_part)
        elf_packages.clear()
        common_part.clear()
        elf_number = 0
    return score


if __name__ == '__main__':
    with open("input", "r") as input_list:
        score = 0
        score2 = 0
        elf_number = 0
        elf_packages = dict()
        common_part = set()
        for line in input_list.read().splitlines():
            elf_packages[elf_number] = line
            score += part1()
            score2 += part2()

        print(f"My part result {score}")    # 8202
        print(f"My part2 result {score2}")  # 2864


