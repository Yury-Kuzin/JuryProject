# Jury Project
def fill_matrix_1(n, m):
    return [[i * j for j in range(m)] for i in range(n)]


def fill_matrix_2(n, m):
    return [[(i + j) % 2 for j in range(m)] for i in range(n)]
