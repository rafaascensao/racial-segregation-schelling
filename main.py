from matrix import  Matrix
from scalefree import Scale_Free
import matplotlib.pyplot as plt

def run_matrix():
    m = Matrix()
    print(m.matrix)
    unsatisfied = m.assert_unsatisfied()
    unsat_evolution = []
    print("Unsatisfied percentage = ", (len(unsatisfied) / m.entries) * 100)
    steps = 0
    while len(unsatisfied) > 0:
        m.move_unsatisfied(unsatisfied)
        #print(m.matrix)
        unsatisfied = m.assert_unsatisfied()
        unsat_evolution.append(len(unsatisfied) / m.entries * 100)
        steps += 1


    print("all satisfied.\n steps: ", steps)

    step_list = [i for i in range(steps)]

    plt.imshow(m.matrix, interpolation='nearest')
    plt.show()

    plt.scatter(step_list, unsat_evolution)
    plt.show()

def run_graph():
    g = Scale_Free()
    unsatisfied = g.assert_unsatisfied()
    print("unsatisfied:", unsatisfied)
    steps = 0
    while len(unsatisfied) > 0:
        g.move_unsatisfied(unsatisfied)
        unsatisfied = g.assert_unsatisfied()
        print("Unsatisfied percentage = ", (len(unsatisfied) / g.size) * 100)
        steps += 1
        print("unsatisfied:", unsatisfied)
    print("all satisfied.\n steps: ", steps)


if __name__ == '__main__':
    run_matrix()
