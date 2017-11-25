import numpy as np
from random import randint, choice




class Matrix:
    def __init__(self, dim = 150, p_one = 0.44, p_two = 0.44, threshold = 0.7):

        self.dim = dim
        self.entries = dim * dim
        self.n_one = int(self.entries * p_one)
        self.n_two = int(self.entries * p_two)
        self.n_empy = self.entries - (self.n_one + self.n_two)
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

    def assert_unsatisfied(self):
        unsatisfied = []
        for x in range(self.dim):
            for y in range(self.dim):
                if self.matrix[x][y] != 0:
                    if self.check_position(x, y):
                        unsatisfied.append((x, y))
        #print("Unsastisfied: ", unsatisfied)
        return unsatisfied

    def check_position(self, x, y):
        neighbors = list()
        to_remove = list()
        neighbors.append((x, y - 1))
        neighbors.append((x, y + 1))
        neighbors.append((x - 1, y))
        neighbors.append((x + 1, y))
        neighbors.append((x - 1, y - 1))
        neighbors.append((x - 1, y + 1))
        neighbors.append((x + 1, y - 1))
        neighbors.append((x + 1, y + 1))
        position = (x, y)
        for t in neighbors:
            if t[0] < 0 or t[0] > self.dim-1:
                to_remove.append(t)
            elif t[1] < 0 or t[1] > self.dim-1:
                to_remove.append(t)

        for r in to_remove:
            neighbors.remove(r)

        return self.check_neighborhood(neighbors, position)

    # number of different races not being used
    def check_neighborhood(self, neighborhood, pos) -> bool:
        my_race = self.matrix[pos[0]][pos[1]]
        #print("NEIGHBORHOOD: ", neighborhood)
        same_race = 0
        num_neighbors = 0

        for neighbor in neighborhood:
            if self.matrix[neighbor[0]][neighbor[1]] == 0:
                continue
            elif self.matrix[neighbor[0]][neighbor[1]] == my_race:
                same_race += 1
            num_neighbors += 1
        try:
            ratio = same_race / num_neighbors
        except ZeroDivisionError:
            return True

        #print("Ratio :", ratio)
        return ratio < self.threshold

    def move_unsatisfied(self, unsat):

        empty_positions = self.empty_positions()

        for u in unsat:
            random_empty = choice(empty_positions)
            self.matrix[random_empty[0]][random_empty[1]] = self.matrix[u[0]][u[1]]
            self.matrix[u[0]][u[1]] = 0
            empty_positions.remove(random_empty)
            empty_positions.append((u[0], u[1]))

    def empty_positions(self) -> list:
        empty = list()
        for i in range(self.dim):
            for j in range(self.dim):
                if self.matrix[i][j] == 0:
                    empty.append((i, j))
        return empty