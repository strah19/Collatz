import matplotlib.pyplot as plt
import sys

def collatz(v: int):
    return ((3 * v) + 1)

def log_group_collatz(max_collatz: int):
    log = open('collatz.txt', 'w')
    log.write('|------------------collatz conjecture------------------|')

    start_val = value = 1
    while start_val < max_collatz:
        log.write(str.format('\n{0} - ', value))

        while value != 1:
            if value % 2 == 0:
                value /= 2
            else:
                value = collatz(value)
            log.write(str.format(' {0} ', value))
        start_val += 1
        value = start_val

def graph_collatz(value: int):
    x = [0]
    y = [0]
    while value != 1:
        if value % 2 == 0:
            value /= 2
        else:
            value = collatz(value)
        x.append(x[len(x) - 1] + 1)
        y.append(value)

    plt.plot(x, y)

    plt.xlabel('Step')
    plt.ylabel('Value')
    plt.title('Collatz Conjecture')
    plt.show()

def graph_group_collatz(max: int, lowrange: int = 0, highrange: int = 0):
    if lowrange == 0 and highrange == 0:
        current = 1
    else:
        current = lowrange
        max = highrange
    while current < max:
        x = [0]
        y = [0]
        value = current
        while value != 1:
            if value % 2 == 0:
                value /= 2
            else:
                value = collatz(value)
            x.append(x[len(x) - 1] + 1)
            y.append(value)

        plt.plot(x, y)
        current += 1
    plt.xlabel('Step')
    plt.ylabel('Value')
    plt.title('Collatz Conjecture')
    plt.show()
log_group_collatz(100000)