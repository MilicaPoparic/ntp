import timeit, time
from mpi4py import MPI
import math, copy
import numpy as np
from util import add_and_multiply, step_one, write_to_file, write

# treba mi lista velicine p da cuva parove a i b i c mozda

blocks = []


def multiply_and_shift(data):
    blocks.append([data[0], data[1], data[2]])
    return blocks


def sequential(a, b, n, p):
    step, dim1, s1 = 0, 0, 0
    p_sqrt = int(math.sqrt(p - 1))
    p_sqrt_2 = p_sqrt ** 2
    range_per_row = int((p - 1) / p_sqrt)
    block_dim = int(n / p_sqrt)
    dim2 = block_dim
    s2 = range_per_row
    rows = {}
    c = [[0 for i in range(n)] for j in range(n)]
    dest = 0
    write("sequential.txt", "matrices a, b", a, b)
    start_time = time.time()
    a, b = step_one(a, b, n)
    for i in range(n):
        a_block, b_block, data = [], [], []
        for j in range(dim1, dim2):
            a_block.append(a[j][step:step + block_dim])
            b_block.append(b[j][step:step + block_dim])
        if len(a_block[block_dim - 1]) == block_dim:
            # print(a_block, "A BLOKCINA")
            c_block = [[0 for i in range(block_dim)] for j in range(block_dim)]
            data = [a_block, b_block, c_block]
            dest += 1
            if dest == p:
                dest = 1
            blocks = multiply_and_shift(data)
        step = step + block_dim
        if (i + 1) % block_dim == 0:
            step = 0
            dim1 += block_dim
            dim2 += block_dim


    c_blocks = [[[0 for k in range(block_dim)] for j in range(block_dim)] for i in range(p-1)]

    for m in range(n):
        blocks_shifted = copy.deepcopy(blocks)
        for i in range(p - 1):
            process = i + 1
            add_and_multiply(blocks[i][0], blocks[i][1], blocks[i][2], block_dim)
            write_to_file('sequential.txt', m + process, blocks[i][0], blocks[i][1], blocks[i][2])
            for s in range(block_dim):
                for k in range(block_dim):
                    c_blocks[i][s][k] += blocks[i][2][s][k]
            left_shift_dest = process - 1 + p_sqrt if (process - 1) % p_sqrt == 0 else process - 1
            left_shift_source = process + 1 - p_sqrt if process % p_sqrt == 0 else process + 1

            new_col = [i[0] for i in blocks[left_shift_dest - 1][0]]

            for j in range(block_dim):
                blocks_shifted[i][0][j] = blocks[i][0][j][1:] + [new_col[j]]

            up_shift_dest = process - p_sqrt if process - p_sqrt > 0 else process + range_per_row * (range_per_row - 1)
            up_shift_source = process - range_per_row * (range_per_row - 1) if (
                                                                                   process + p_sqrt) > p_sqrt_2 else process + p_sqrt
            new_row = (blocks[up_shift_dest - 1][1][0])
            blocks_shifted[i][1] = blocks[i][1][1:] + [new_row]

        blocks = blocks_shifted

    for l in range(range_per_row):
        rows[l] = []
        for m in range(s1, s2):
            rows[l].append(c_blocks[m])
        s1 += range_per_row
        s2 += range_per_row

    end_time = time.time()
    print(np.bmat([rows[i] for i in rows.keys()]))
    print("Process finished in ", end_time - start_time)
    write("sequential.txt", "result: ", np.bmat([rows[i] for i in rows.keys()]), '-------------------------')
