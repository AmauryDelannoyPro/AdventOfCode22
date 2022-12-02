def part1():
    score = 0
    if entry[1] == 'X' and entry[0] == 'C':
        score += 6
    elif entry[1] == 'X' and entry[0] == 'A':
        score += 3
    elif entry[1] == 'Y' and entry[0] == 'A':
        score += 6
    elif entry[1] == 'Y' and entry[0] == 'B':
        score += 3
    elif entry[1] == 'Z' and entry[0] == 'B':
        score += 6
    elif entry[1] == 'Z' and entry[0] == 'C':
        score += 3
    return score


def win():
    return 6


def draw():
    return 3


def lose():
    return 0


if __name__ == '__main__':
    with open("input", "r") as input_list:
        # A = Rock, B = Paper, C = Scissors
        # Part 1
        # X = Rock, Y = Paper, Z = Scissors
        # Part 2
        # X = Lose, Y = Draw, Z = Win
        my_shape = {'X': 1, 'Y': 2, 'Z': 3}
        score_part1 = 0
        score_part2 = 0
        for line in input_list.read().splitlines():
            # Do your job here !
            entry = line.split(" ")
            print(entry)

            # Add my selected score shape
            score_part1 += my_shape[entry[1]]
            score_part1 += part1()

            match entry[0]:
                case 'A':
                    match entry[1]:
                        case 'X':
                            score_part2 += lose()
                            score_part2 += my_shape['Z']
                        case 'Y':
                            score_part2 += draw()
                            score_part2 += my_shape['X']
                        case 'Z':
                            score_part2 += win()
                            score_part2 += my_shape['Y']
                case 'B':
                    match entry[1]:
                        case 'X':
                            score_part2 += lose()
                            score_part2 += my_shape['X']
                        case 'Y':
                            score_part2 += draw()
                            score_part2 += my_shape['Y']
                        case 'Z':
                            score_part2 += win()
                            score_part2 += my_shape['Z']
                case 'C':
                    match entry[1]:
                        case 'X':
                            score_part2 += lose()
                            score_part2 += my_shape['Y']
                        case 'Y':
                            score_part2 += draw()
                            score_part2 += my_shape['Z']
                        case 'Z':
                            score_part2 += win()
                            score_part2 += my_shape['X']

        print(f"My score part 1 is {score_part1}")
        print(f"My score part 2 is {score_part2}")
