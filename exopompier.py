import numpy as np
from random import randint
from time import sleep
import os

# print(np.linalg.norm(np.array([-2,4]), ord=1))


# 1ere Etape : un pompier - un feu. Le pompier se dirige vers le feu en avancant d'une case à chaque tour

# 2e Etape : un pompier - plusieurs feux. Une fois sur le feu,
# le pompier reste 5 tours pour l'éteindre et passe au feu suivant

# 3e Etape : plusieurs - plusieurs feux

class Pompier:
    """
    attributs:
        - position : np.array([int, int])
        - occupe : int
    methodes:
        - se_deplacer_vers(coord) : déplace le pompier d'une case vers coord
    """

    def __init__(self, position, board):
        self.position = np.array(position)
        self.board = board
        self.occupe = 0

    def se_deplacer_vers(self, dest):
        if dest[0] < self.position[0]:
            self.position[0] -= 1
        elif dest[0] > self.position[0]:
            self.position[0] += 1
        elif dest[1] < self.position[1]:
            self.position[1] -= 1
        elif dest[1] > self.position[1]:
            self.position[1] += 1
        else:
            self.occupe = 5

    def eteindre(self):
        self.occupe -= 1
        if self.occupe == 0:
            self.board.eteindre(tuple(self.position))


class Board:
    """
    attributs:
        - liste_pompiers
        - liste_feux : [(int:int)] (ex : [(2,3), (4,7)])
    methodes:
        - run() : effectue un tour
        - display() : affiche l'état des pompiers et des feux
    """

    def __init__(self):
        self.liste_pompiers = [Pompier([2, 3], self), Pompier([7, 8], self)]
        self.liste_feux = [(randint(0, 9), randint(0, 9)) for i in range(10)]
        self.size = (10, 10)

    def eteindre(self, position):
        self.liste_feux = [f for f in self.liste_feux if f != position]

    def _est_pompier(self, i, j):
        for p in self.liste_pompiers:
            if (np.array([i, j]) == p.position).all():
                return True
        return False

    def _est_feu(self, i, j):
        for f in self.liste_feux:
            if (i, j) == f:
                return True
        return False

    def _display_position(self, i, j):
        if self._est_pompier(i, j):
            return "X"
        elif self._est_feu(i, j):
            return "O"
        else:
            return " "

    def display(self):
        print("Display")
        for i in range(self.size[1]):
            print([self._display_position(i, j) for j in range(self.size[0])])

    def feu_le_plus_proche(self, position):
        feu_proche = self.liste_feux[0]
        distance = np.linalg.norm(position-np.array(feu_proche), ord=1)
        for feu in self.liste_feux:
            curr_distance = np.linalg.norm(position-np.array(feu), ord=1)
            if curr_distance < distance:
                distance = curr_distance
                feu_proche = feu
        return feu_proche

    def run(self):
        for p in self.liste_pompiers:
            if len(b.liste_feux) > 0:
                feu = self.feu_le_plus_proche(p.position)
                if p.occupe == 0:
                    p.se_deplacer_vers(feu)
                else:
                    p.eteindre()


b = Board()
while len(b.liste_feux) > 0:
    os.system("cls")
    b.display()
    b.run()
    sleep(1)
