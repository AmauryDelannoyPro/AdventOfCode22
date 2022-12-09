
def find_visible_trees_by_subpart(id_line, id_col, line, start_col, end_col):
    current_val = table[id_line][id_col]
    current_max = max(line[start_col:end_col])

    if current_val > current_max :
        visible_trees_dict[(id_line, id_col)] = current_val


def find_visible_trees(idline, idcol):
    current_line = table[idline]
    current_col = concat_col_val(idcol)
    # Horizontal
    find_visible_trees_by_subpart(idline, idcol, current_line, 0, idcol)
    find_visible_trees_by_subpart(idline, idcol, current_line, idcol + 1, len(current_line))
    # Vertical
    find_visible_trees_by_subpart(idline, idcol, current_col, 0, idline)
    find_visible_trees_by_subpart(idline, idcol, current_col, idline + 1, len(current_col))


def concat_col_val(id_col):
    return list(v[id_col] for v in table)


def add_edge_tree():
    global visible_trees_dict
    for idline, line in enumerate(table):
        for idcol, col in enumerate(line):
            if idline == 0 or idcol == 0 \
                or idline == len(table)-1 or idcol == len(line)-1:
                visible_trees_dict[(idline, idcol)] = table[idline][idcol]


table = []
visible_trees_dict = {}
if __name__ == '__main__':
    with open("input", "r") as input_list:
        score1, score2 = 0, 0

        for i, line in enumerate(input_list.read().splitlines()):
            # Do your job here !
            table.append(list(int(l) for l in line))
            pass

        add_edge_tree()
        # On boucle en skipant le 1er et dernier arbre des lignes / col
        for idline, line in enumerate(table[:-1]):
            for idcol, col in enumerate(line[:-1]):
                if idline == 0 or idcol == 0:
                    continue
                find_visible_trees(idline, idcol)
        score1 = len(visible_trees_dict)
        print(f"Part 1 : {score1}")  # 1538
        print(f"Part 2 : {score2}")  #
