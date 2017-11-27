import networkx as nx
from random import choice

class Scale_Free:
    def __init__(self, size = 100, p_one = 0.4, p_two = 0.4, threshold = 1.0):

        self.size = size
        self.n_one = int(self.size * p_one)
        self.n_two = int(self.size * p_two)
        print("ONE ", self.n_one)
        print("TWO ", self.n_two)
        self.n_empty = self.size - (self.n_one + self.n_two)
        print("EMPTY: ", self.n_empty)
        self.threshold = threshold

        self.graph = nx.scale_free_graph(size)
        self.races = {node: 0 for node in self.graph.nodes()}
        self.populate()

    def populate(self):
        empty_positions = self.empty_nodes()

        for i in range(self.n_one):
            node = choice(empty_positions)
            self.races[node] = 1
            empty_positions.remove(node)

        for j in range(self.n_two):
            node = choice(empty_positions)
            self.races[node] = 2
            empty_positions.remove(node)

    def empty_nodes(self) -> list :
        empty = [node for node in self.races.keys() if self.races[node] == 0]
        return empty

    def assert_unsatisfied(self):
        unsatisfied = []
        for node in self.graph.nodes():
            if self.races[node] == 0:
                continue
            elif self.check_neighborhood(node):
                unsatisfied.append(node)
        return unsatisfied

    def check_neighborhood(self, node):
        neighbors = self.graph.neighbors(node)
        my_race = self.races[node]
        same_race = 0
        num_neighbors = 0
        for n in neighbors:
            if self.races[n] == 0:
                continue
            elif self.races[n] == my_race:
                same_race += 1
            num_neighbors += 1

        try:
            ratio = same_race / num_neighbors
        except ZeroDivisionError:
            return False
        print("Ratio: ", ratio)
        return ratio < self.threshold

    def move_unsatisfied(self, unsat):
        empty_positions = self.empty_nodes()

        for u in unsat:
            random_empty = choice(empty_positions)
            self.races[random_empty] = self.races[u]
            self.races[u] = 0
            empty_positions.remove(random_empty)

    def get_race_list(self, race):
        res = [node for node in self.races if self.races[node] == race]
        return res