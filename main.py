# Jury Project
def fill_matrix_1(n, m):
    # Comment
    return [[i * j for j in range(m)] for i in range(n)]


def fill_matrix_2(n, m):
    return [[(i + j) % 2 for j in range(m)] for i in range(n)]


def fill_matrix_3(n, m):
    return [[min(j, i, m - j - 1, n - i - 1) for j in range(m)] for i in range(n)]


def print_matrix(matrix):
    for row in matrix:
        for n in row:
            print(f'{n:<4d}', end='')
        print()
