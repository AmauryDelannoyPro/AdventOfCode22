def evaluate_part1():
    seq = "".join(charlist)
    for i in range(len(charlist)):
        if seq.count(charlist[i]) > 1:
            return False
    return True

charlist = list()
if __name__ == '__main__':
    with open("input", "r") as input_list:
        score1, score2 = 0, 0
        for line in input_list.read().splitlines():
            # Do your job here !
            for idchar, char in enumerate(line):
                if len(charlist) < 4:
                    charlist.append(char)
                    continue
                if evaluate_part1():
                    score1 = idchar
                    break
                else:
                    charlist.pop(0)
                    charlist.append(char)

        print(f"Part 1 : {score1}")  # 1651
        print(f"Part 2 : {score2}")  #
