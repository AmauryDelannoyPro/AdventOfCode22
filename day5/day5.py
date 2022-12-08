if __name__ == '__main__':

    
    with open("input", "r") as input_list:
        score1, score2 = 0, 0
        letter_dict = []
        input_data = input_list.read().splitlines()
        # Search Empty line between stacks and moves
        split_line = input_data.index("")
        nb_col = len(input_data[split_line-1].replace(" ", ""))

        for idline, line in enumerate(input_data):
            letter_dict.append([])
            # On est sur la ligne avec les num de colonnes, on arrete pour l'instant
            if idline >= split_line-1:
                break
            for i in range(0, nb_col):
                letter_dict[idline].append(" ")
            print(letter_dict[idline])

        print(f"Part 1 : {score1}")  #
        print(f"Part 2 : {score1}")  #
