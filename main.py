from matrix import  Matrix
import matplotlib.pyplot as plt

def main():
    m = Matrix()
    print(m.matrix)
    unsatisfied = m.assert_unsatisfied()

    print("Unsatisfied percentage = ", (len(unsatisfied) / m.entries) * 100)
    steps = 0
    while len(unsatisfied) > 0:
        m.move_unsatisfied(unsatisfied)
        #print(m.matrix)
        unsatisfied = m.assert_unsatisfied()
        print("Unsatisfied percentage = ", (len(unsatisfied) / m.entries) * 100)
        steps += 1

    print("all satisfied.\n steps: ", steps)
    plt.imshow(m.matrix, interpolation='nearest')
    plt.show()

if __name__ == '__main__':
    main()