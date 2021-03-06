import timeit, time, os
from mpi4py import MPI
from sequential import sequential
from scalling import calculate, calc_amdal, plot_graph, calc_gustaf
import random

# a = [[15, -11, -12, 12], [-15, -2, 15, -15], [12, 14, -12, -6], [-1, -8, 16, -13]]
# b = [[0, 15, 14, 9], [-3, -7, -12, -4], [10, 10, -16, 15], [-13, -3, 9, 3]]
a = [
    [-14, 10, - 11, 2, 7 ,- 21],
    [30, 5, 33, - 34, 12, 35],
    [25, 4, 21, 26, - 26, - 6],
    [16, 36, -7, 0, 13, -11],
    [-17, 17, 3, -3, -34, -6],
    [2, -1, -10, 9, -14,14]
]
b = [
    [-9, 2, -16, 0, -32, -9],
    [-21, -6, 10, -12, 10, 18],
    [-9, 1, 9, 35, -21, 34],
    [2, 28, -5, 30, -1, -29],
    [-1, 20, -1, 27, -29, -1],
    [-6, -36, -25, -16, -7, -33]
]

# a = [[49, 10, 40, -58, -21, -36, 50, 9],
#      [-5, -59, -18, -13, 27, 58, -56, 59],
#      [-23, -34, 33, 5, -6, -20, -11, -42],
#      [57, 21, -49, -8, -10, 42, -55, -26],
#      [-3, 52, 53, -48, -6, 4, 3, -30],
#      [23, 60, 15, -39, 40, -9, -1, -7],
#      [48, 39, 42, -51, -32, -57, 16, -52],
#      [-35, -52, 1, -8, -28, -51, -56, -36]]

# b = [[-43, 64, -36, -6, 3, -8, 10, -52],
#      [-48, -2, 62, 63, 29, 44, 20, -47],
#      [29, -34, -31, -50, 17, -51, 1, 15],
#      [41, -40, -47, 24, -9, 59, -24, 64],
#      [18, 54, 51, -4, 36, -31, -1, 35],
#      [4, 28, -40, -50, -34, -11, 37, -7],
#      [57, -40, -55, 23, -45, 27, 9, -36],
#      [54, -1, 16, -11, -12, 4, 25, -30]]
n = 6
# a = [[random.randint(-(100), 100) for _ in range(n)] for _ in range(n)]
# b = [[random.randint(-(100), 100) for _ in range(n)] for _ in range(n)]

if __name__ == '__main__':
    # p = 2
    # sequential(a, b, n, p)
    p = 10
    os.system("mpiexec -n {0} python -m mpi4py parallel.py".format(p))
    # for i in range(30):
    #     sequential(a, b, n, p)
        # os.system("mpiexec -n {0} python -m mpi4py parallel.py".format(p))


    # speedUp = []
    # cpu = [4,16,25]
    # gustaf = calc_gustaf(cpu)
    # speedUp.append(calculate("resources/parallel4.txt", "resources/sequential_strong.txt"))
    # speedUp.append(calculate("resources/parallel_weak16.txt", "resources/sequential_weak16.txt"))
    # speedUp.append(calculate("resources/parallel_weak25.txt", "resources/sequential_weak25.txt"))
    # print(speedUp)
    # plot_graph(speedUp, gustaf, cpu, "Slabo")