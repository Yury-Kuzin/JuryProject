# Jury Project
def fill_matrix_1(n, m):
    # Comment 666
    return [[i * j for j in range(m)] for i in range(n)]


def fill_matrix_2(n, m):
    # Comment
    return [[(i + j) % 2 for j in range(m)] for i in range(n)]
