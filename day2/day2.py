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


if __name__ == '__main__':
    with open("input", "r") as input_list:
        # A = Rock, B = Paper, C = Scissors
        # Part 1
        # X = Rock, Y = Paper, Z = Scissors
        # Part 2
        # X = Lose, Y = Draw, Z = Win
        my_shape = {'X': 1, 'Y': 2, 'Z': 3}
        my_lose_shape = {'A': 'Z', 'B': 'X', 'C': 'Y'}
        my_draw_shape = {'A': 'X', 'B': 'Y', 'C': 'Z'}
        my_win_shape = {'A': 'Y', 'B': 'Z', 'C': 'X'}
        my_point = {'X': 0, 'Y': 3, 'Z': 6}
        score_part1 = 0
        score_part2 = 0
        for line in input_list.read().splitlines():
            # Do your job here !
            entry = line.split(" ")

            # Add my selected score shape
            score_part1 += my_shape[entry[1]]
            score_part1 += part1()

            # Add my win / draw / lose point
            score_part2 += my_point[entry[1]]
            score_part2 += my_shape[my_win_shape[entry[0]]]

        print(f"My score part 1 is {score_part1}") # 12772
        print(f"My score part 2 is {score_part2}") # 11618
