import numpy as np
from random import randint


class Matrix:
    def __init__(self, dim = 10, p_one = 0.4, p_two = 0.4, threshold = 0.3):

        self.dim = dim
        self.entries = dim * dim
        self.n_one = int(self.entries * p_one)
        self.n_two = int(self.entries * p_two)
        self.n_empy = self.entries -  (self.n_one + self.n_two)
        self.threshold = threshold
        self.matrix = np.zeros(shape=(dim, dim))

        self.populate()

    def populate(self):
        i = 0

        while i < self.n_one:
            x = randint(0, self.dim - 1)
            y = randint(0, self.dim - 1)
            if self.matrix[x][y] == 0:
                self.matrix[x][y] = 1
                i += 1

        i = 0
        count_two = 0
        while i < self.n_two:
            x = randint(0, self.dim - 1)
            y = randint(0, self.dim - 1)
            if self.matrix[x][y] == 0:
                self.matrix[x][y] = 2
                i += 1

    def assert_insatisfied(self):
        unsatisfied = []
        for x in range(self.dim - 1):
            for y in range(self.dim - 1):
                if self.matrix[x][y] != 0 and self.check_position(x, y):
                    unsatisfied.append((x, y))


    def check_position(self, x, y):
        if x == 0 and y == 0:
            # top left
            return

        elif x == 0 and y == self.dim - 1:
            #top right
            return

        elif x == self.dim - 1 and y == 0:
            # bottom left
            return

        elif x == self.dim - 1 and y == self.dim -1:
            # bottom right
            return

        elif x == 0:
            # ceiling
            return

        elif y == 0:
            # left wall
            return

        elif x == self.dim - 1:
            # floor
            return

        elif y == self.dim - 1:
            # right wall
            return

        else:
            # regular case
            same = 0
            diff = 0

    # number of different races not being used
    def check_neighborhood(self, neighborhood, pos) -> bool:
        my_race = self.matrix[pos[0]][pos[1]]
        same_race = 0
        diff_race = 0
        num_neighbors = 0

        if len(neighborhood) == 0:
            return True

        for neighbor in neighborhood:
            if self.matrix[neighbor[0]][neighbor[1]] == 0:
                continue
            elif self.matrix[neighbor[0]][neighbor[1]] == my_race:
                same_race += 1
                num_neighbors += 1
            else:
                diff_race += 1
                num_neighbors += 1

        ratio = same_race / num_neighbors

        return ratio > self.threshold

    def move_unsatisfied(self, unsat):
        for u in unsat:
            x = randint(0, self.dim - 1)
            y = randint(0, self.dim - 1)
            if self.matrix[x][y] == 0:
                self.matrix[x][y] = u[0][1]