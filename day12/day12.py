from collections import deque
from pprint import pprint


def get_possible_move(lin, col, nb_row, nb_col):
    moves = []
    cur_val = map_tab[lin][col]
    # UP
    if lin > 0 :
        if abs(cur_val - map_tab[lin - 1][col]) <= 1 :
            moves.append((lin - 1, col))
    # DOWN
    if lin < nb_row - 1 :
        if abs(cur_val - map_tab[lin + 1][col]) <= 1 :
            moves.append((lin + 1, col))
    # LEFT
    if col > 0 :
        if abs(cur_val - map_tab[lin][col - 1]) <= 1 :
            moves.append((lin, col - 1))
    # RIGHT
    if col < nb_col - 1 :
        if abs(cur_val - map_tab[lin][col + 1]) <= 1 :
            moves.append((lin, col + 1))
    # print(f"Move pour [{lin}][{col}] = {moves}")
    return moves


def find_start_end():
    global start, end
    for i, cur_line in enumerate(map_tab):
        for j, cur_val in enumerate(cur_line):
            if map_tab[i][j] == ord('S'):
                map_tab[i][j] = ord('a')
                start = (i,j)
            elif map_tab[i][j] == ord('E'):
                map_tab[i][j] = ord('z')+1
                end = (i,j)


def create_graph():
    for i, cur_line in enumerate(map_tab):
        for j, cur_val in enumerate(cur_line):
            graph.update({(i,j): get_possible_move(i, j, len(map_tab), len(cur_line))})



def bfs(depart, goal, graphe):
    queue = deque([depart])
    visited_node = {depart:None}

    tour = 0
    while queue:
        node = queue.popleft()
        if node == depart:
            display[node[0]][node[1]] = "S"
        else:
            display[node[0]][node[1]] = "."
        if node == goal:
            print(f"GOAL {node}")
            break
        next_nodes = graphe[node]
        for next_node in next_nodes:
            if next_node not in visited_node:
                queue.append(next_node)
                visited_node[next_node] = node
                # print(f"Ajout {node} pour {next_node}")
        tour += 1
    return visited_node


map_tab = []
graph = {}
start = (0,0)
end = (0,0)
display = []

def affiche():
    for i, vali in enumerate(display):
        print("", end="")
        for j, valj in enumerate(vali):
            if valj in (".", "S"):
                print(valj, end="")
            else:
                print(chr(map_tab[i][j]), end="")
        print()


if __name__ == '__main__':
    with open("input", "r") as input_list:
        score1, score2 = 0, 0
        for line in input_list.read().splitlines():
            map_tab.append(list(ord(l) for l in line))
            display.append(list("X" for l in line))

        find_start_end()
        create_graph()
        visited = bfs(start, end, graph)
        # pprint(graph)
        # affiche()
        cur_node = end
        while cur_node != start:
            print(f'---> {cur_node[0]+1},{cur_node[1]+1} ', end='')
            cur_node = visited[cur_node]
            score1 += 1
        print()

        print(f"Part 1 : {score1}")  #
        print(f"Part 2 : {score2}")  #
