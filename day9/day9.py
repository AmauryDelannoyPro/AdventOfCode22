
# Classe Map
#   Width x Height
#   def addcol
#       width.insert(0)
#       or
#       width.append()
#   pareil pour addLine

# def moveT
#   isMoveNeeded ?
#       update map
def moveH(direction):

    pass

class World:
    map = ["s"]

    def add_col(self):
        self.map.append("")

    def display(self):
        for line in self.map:
            for col in line:
                print(col)


if __name__ == '__main__':
    with open("input", "r") as input_list:
        score1, score2 = 0, 0
        world = World()

        # 1er déplacement, H bouge mais pas T
        # Après le 1er tour, T est a la position de H au tour précedant
        # Nan, pas bon si H revient sur ses pas
        # Avant de bouger T a H-1, on vérifie la distance T<->H.
        # Si Distance > 1, on fait T = H-1

        # Calcul de map :
        # option 1 (pas top) : on calcul les diff R/L et U/D
        # option 2 : faire méthode add colonne (gauche ou droite) et pareil pour ligne

        for line in input_list.read().splitlines():
            direction, quantite = line.split(" ")
            # print(direction, quantite)
            for move in range(1, int(quantite)):
                # print(direction)
                moveH(direction)

        print(f"Part 1 : {score1}")  #
        print(f"Part 2 : {score2}")  #
