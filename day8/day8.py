def find_vertical_tree(actual_line, actual_col, sens):
    current_val = table[actual_line][actual_col]

def find_horizontal_tree(actual_line, actual_col, sens):
    current_val = table[actual_line][actual_col]


def find_visible_trees(actual_line, actual_col):
    score = 0

    score += find_vertical_tree(idline, idcol, 1)
    score += find_vertical_tree(idline, idcol, -1)
    score += find_horizontal_tree(idline, idcol, 1)
    score += find_horizontal_tree(idline, idcol, -1)
    return score


def calculate_edge_tree():
    # Pour les arbres en bordures, faire :
    # ligne + col - 2 pour les coins * 2 pour faire l'autre moitié
    # (nb_col + nb_lig -2) * 2
    return (len(table) + len(table[0]) - 2) *2

table = []
if __name__ == '__main__':
    with open("input", "r") as input_list:
        score1, score2 = 0, 0

        for i, line in enumerate(input_list.read().splitlines()):
            # Do your job here !
            table.append(list(int(l) for l in line))
            pass

        # On boucle en skipant le 1er et dernier arbre des lignes / col
        for idline, line in enumerate(table[:-1]):
            for idcol, col in enumerate(line[:-1]):
                if idline == 0 or idcol == 0:
                    continue
                score1 += find_visible_trees(idline, idcol)
        score1 += calculate_edge_tree()

        print(f"Part 1 : {score1}")  #
        print(f"Part 2 : {score2}")  #
