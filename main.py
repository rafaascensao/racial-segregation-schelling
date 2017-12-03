from matrix import  Matrix
from scalefree import Scale_Free
import matplotlib.pyplot as plt
import networkx as nx
import argparse

def run_matrix(threshold, ones, twos, dimension):
    m = Matrix(dimension, ones, twos, threshold)
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

    plt.plot(unsat_evolution)
    plt.show()

    plt.plot(segregation)
    plt.show()

def run_graph(threshold, ones, twos, dimension):
    g = Scale_Free(dimension*dimension, ones, twos, threshold)
    unsatisfied = g.assert_unsatisfied()
    #print("unsatisfied:", unsatisfied)
    steps = 0
    unsat_evolution = list()
    segregation = list()
    segregation.append((g.calculate_segregation() - 0.5)*2)
    while len(unsatisfied) > 0:
        g.move_unsatisfied(unsatisfied)
        unsatisfied = g.assert_unsatisfied()
        print("Unsatisfied percentage = ", (len(unsatisfied) / g.size) * 100)
        steps += 1
        unsat_evolution.append((len(unsatisfied) / g.size) * 100)
        segregation.append((g.calculate_segregation() - 0.5) * 2)

    print("all satisfied.\n steps: ", steps)
    plot_graph(g)
    plt.plot(unsat_evolution)
    plt.show()

    plt.plot(segregation)
    plt.show()


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

def verify_arguments(threshold, ones, twos):
    value = True
    print(ones)
    if threshold < 0 or threshold > 1:
        print('ERROR: Threshold must be between 0 and 1')
        value = False

    if ones < 0 or ones > 1:
        print('ERROR: Race one must be between 0 and 1')
        value = False

    if twos < 0 or twos > 1:
        print('ERROR: Race two must be between 0 and 1')
        value = False

    if ones+twos >= 1:
        print('ERROR: Race one + two must be under 1')
        value = False

    return value

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Computer simulation of the Schelling model')
    parser.add_argument("-tp","--type", help='Type of the representation of the model (either matrix or scalefree)', default='matrix')
    parser.add_argument('-thold', '--threshold', type=float, help='Threshold desired', default=0.3)
    parser.add_argument('-o','--ones', type=float, help='Percentage of agents belonging to race one', default=0.4)
    parser.add_argument('-t','--twos', type=float, help='Percentage of agents belonging to race two', default=0.4)
    parser.add_argument('-d', '--dimension', type=int, help='Percentage of agents belonging to race two', default=50)
    args = parser.parse_args()
    if not verify_arguments(args.threshold, args.ones, args.twos):
        print('Arguments given are not approriate')
    elif args.type == 'matrix':
        run_matrix(args.threshold, args.ones, args.twos, args.dimension)
    elif args.type == 'scalefree':
        run_graph(args.threshold, args.ones, args.twos, args.dimension)
    else:
        print('ERROR: Type must be either matrix or scalefree')

