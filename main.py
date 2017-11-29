from matrix import  Matrix
from scalefree import Scale_Free
import matplotlib.pyplot as plt
import networkx as nx

def run_matrix():
    m = Matrix()
    segregation = list()
    print(m.matrix)
    unsatisfied = m.assert_unsatisfied()
    unsat_evolution = []
    print("Unsatisfied percentage = ", (len(unsatisfied) / m.entries) * 100)
    segregation.append((m.calculate_segregation() - 0.5)*2)
    steps = 0
    while len(unsatisfied) > 0:
        m.move_unsatisfied(unsatisfied)
        #print(m.matrix)
        unsatisfied = m.assert_unsatisfied()
        print("Unsatisfied percentage = ", (len(unsatisfied) / m.entries) * 100)
        segregation.append((m.calculate_segregation() - 0.5)*2)
        unsat_evolution.append(len(unsatisfied) / m.entries * 100)
        steps += 1


    print("all satisfied.\n steps: ", steps)
    #plt.imshow(m.matrix, interpolation='nearest')
    #plt.show()
    #steps = list(range(len(segregation)))

    plt.imshow(m.matrix, interpolation='nearest')
    plt.show()

    plot_steps_unsat(steps, unsat_evolution)

    plt.plot(segregation)
    plt.show()

def run_graph():
    g = Scale_Free()
    unsatisfied = g.assert_unsatisfied()
    #print("unsatisfied:", unsatisfied)
    steps = 0
    unsat_evotulion = []

    while len(unsatisfied) > 0:
        g.move_unsatisfied(unsatisfied)
        unsatisfied = g.assert_unsatisfied()
        print("Unsatisfied percentage = ", (len(unsatisfied) / g.size) * 100)
        steps += 1
        unsat_evotulion.append((len(unsatisfied) / g.size) * 100)

    print("all satisfied.\n steps: ", steps)
    plot_graph(g)
    plot_steps_unsat(steps, unsat_evotulion)


def plot_graph(g):
    race_one = g.get_race_list(1)
    print(len(race_one))
    race_two = g.get_race_list(2)
    print(len(race_two))
    empty = g.empty_nodes()
    print(len(empty))
    pos = nx.spring_layout(g.graph)
    nx.draw_networkx_nodes(g.graph, pos, nodelist=race_one, node_color='b', node_size=100, alpha=0.8)
    nx.draw_networkx_nodes(g.graph, pos, nodelist=race_two, node_color='g', node_size=100, alpha=0.8)
    nx.draw_networkx_nodes(g.graph, pos, nodelist=empty, node_color='r', node_size=100, alpha=0.8)

    nx.draw_networkx_edges(g.graph, pos, width=1.0, alpha=0.5)
    plt.show()

def plot_steps_unsat(steps, unsat_evolution):
    step_list = [i for i in range(steps)]

    plt.scatter(step_list, unsat_evolution)
    plt.show()


if __name__ == '__main__':
    run_matrix()
    run_graph()
