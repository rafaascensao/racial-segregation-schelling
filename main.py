from matrix import  Matrix

def main():
    m = Matrix()
    unsatisfied = m.assert_insatisfied()
    print("unsatisfied percentage = ", (len(unsatisfied) / m.entries) * 100)
    steps = 0
    while len(unsatisfied) > 0:
        m.move_unsatisfied(unsatisfied)
        unsatisfied = m.assert_insatisfied()
        print("unsatisfied percentage = ", (len(unsatisfied) / m.entries) * 100)
        steps += 1

    print("all satisfied.\n steps: ", steps)

if __name__ == '__main__':
    main()