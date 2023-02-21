def get_letter_dict():
    for i in range(1, len(line_with_size_regularized), size_slot_character):
        if line_with_size_regularized[i].isalpha():
            letter_dict[idline].append(line_with_size_regularized[i])
        else:
            letter_dict[idline].append(" ")
    return letter_dict


letter_dict = []
size_slot_character = 4

if __name__ == '__main__':

    with open("input", "r") as input_list:
        score1, score2 = 0, 0

        input_data = input_list.read().splitlines()
        # Search Empty line between stacks and moves
        split_line = input_data.index("")

        # l'un ou autre nb_col, a voir si besoin
        # nb_col = input_data[split_line-1][-1:]
        nb_col = len(input_data[split_line-1].replace(" ", ""))

        for idline, line in enumerate(input_data):
            line_with_size_regularized = line
            while len(line_with_size_regularized) < nb_col*size_slot_character:
                line_with_size_regularized += " "

            letter_dict.append([])
            if idline >= split_line-1 and line.__contains__("move"):
                move_info = line.split(" ")
                print(f"{move_info}")
            letter_dict = get_letter_dict()

        print(letter_dict)
        print(f"Part 1 : {score1}")  #
        print(f"Part 2 : {score2}")  #
