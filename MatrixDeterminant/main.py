def determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]

    else:
        eq = list()
        for ic, c in enumerate(matrix[0]):
            m = [[c for i, c in enumerate(r) if i != ic] for i, r in enumerate(matrix) if i != 0]
            eq.append(c * determinant(m))

        return sum([-v if (i % 2 == 1) else v for i, v in enumerate(eq)])
