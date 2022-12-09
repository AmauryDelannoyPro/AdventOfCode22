def evaluate_part1(mylist):
    seq = "".join(mylist)
    for i in range(len(mylist)):
        if seq.count(mylist[i]) > 1:
            return False
    return True


def part1(current_line):
    charlist1 = list()
    PART1_LENGHT = 4
    for idchar, char in enumerate(current_line):
        if len(charlist1) < PART1_LENGHT:
            charlist1.append(char)
            continue
        if evaluate_part1(charlist1):
            print(f"Part 1 : {idchar}")  # 1651
            break
        else:
            charlist1.pop(0)
            charlist1.append(char)



def part2(current_line):
    charlist2 = list()
    PART2_LENGHT = 14
    for idchar, char in enumerate(current_line):
        if len(charlist2) < PART2_LENGHT:
            charlist2.append(char)
            continue
        if evaluate_part1(charlist2):
            print(f"Part 2 : {idchar}")  # 3837
            break
        else:
            charlist2.pop(0)
            charlist2.append(char)


if __name__ == '__main__':
    with open("input", "r") as input_list:
        for line in input_list.read().splitlines():
            # Do your job here !
            part1(line)
            part2(line)

