
def concat_col_val(id_col):
    """
    Create a list with each value in one column
    :param id_col: id column to concat
    :return: List with all value in one column
    """
    return list(v[id_col] for v in table)


def add_edge_tree():
    global visible_trees_dict
    for idline, line in enumerate(table):
        for idcol, col in enumerate(line):
            if idline == 0 or idcol == 0 \
                or idline == len(table)-1 or idcol == len(line)-1:
                visible_trees_dict[(idline, idcol)] = table[idline][idcol]


def find_visible_trees_by_subpart(id_line, id_col, part, start, end):
    """
    Browse in one direction, looking if current value is bigger
    :param id_line:
    :param id_col:
    :param part: current entire line or col
    :param start: where to start split :part
    :param end: where to stop split :part
    """
    current_val = table[id_line][id_col]
    current_max = max(part[start:end])

    if current_val > current_max :
        visible_trees_dict[(id_line, id_col)] = current_val


def find_scenic_score_by_subpart(id_line, id_col, part, start, end, reverse):
    current_val = table[id_line][id_col]
    new_scenic = next_biggest_tree(current_val, part, start, end, reverse)
    if scenic_table[id_line][id_col] == 0:
        scenic_table[id_line][id_col] = new_scenic
    else:
        scenic_table[id_line][id_col] *= new_scenic

def next_biggest_tree(current_val, part, start, end, reverse):
    view = 0
    if not reverse:
        for val in part[start:end]:
            view += 1
            if current_val <= val:
                break
    else:
        for val in reversed(part[start:end]):
            view += 1
            if current_val <= val:
                break

    return view


def find_visible_trees(idline, idcol):
    current_line = table[idline]
    current_col = concat_col_val(idcol)
    # Horizontal
    find_visible_trees_by_subpart(idline, idcol, current_line, 0, idcol)
    find_visible_trees_by_subpart(idline, idcol, current_line, idcol + 1, len(current_line))
    # Vertical
    find_visible_trees_by_subpart(idline, idcol, current_col, 0, idline)
    find_visible_trees_by_subpart(idline, idcol, current_col, idline + 1, len(current_col))

    # SCENIC SCORE
    # Horizontal
    find_scenic_score_by_subpart(idline, idcol, current_line, 0, idcol, True)
    find_scenic_score_by_subpart(idline, idcol, current_line, idcol + 1, len(current_line), False)
    # Vertical
    find_scenic_score_by_subpart(idline, idcol, current_col, 0, idline, True)
    find_scenic_score_by_subpart(idline, idcol, current_col, idline + 1, len(current_col), False)


table = []
visible_trees_dict = {}
scenic_table = []
if __name__ == '__main__':
    with open("input", "r") as input_list:
        score1, score2 = 0, 0

        for i, line in enumerate(input_list.read().splitlines()):
            # Do your job here !
            table.append(list(int(l) for l in line))
            scenic_table.append([0 for c in range(len(line))])

        add_edge_tree()
        # On boucle en skipant le 1er et dernier arbre des lignes / col
        for idline, line in enumerate(table[:-1]):
            for idcol, col in enumerate(line[:-1]):
                if idline == 0 or idcol == 0:
                    continue
                find_visible_trees(idline, idcol)

        score1 = len(visible_trees_dict)
        score2 = max(max(x) for x in scenic_table)
        print(f"Part 1 : {score1}")  # 1538
        print(f"Part 2 : {score2}")  # 496125
