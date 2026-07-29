def set_mat_to_zero(mat):

    row = len(mat)
    col = len(mat[0])

    MARK = -1

    for i in range(row):

        for j in range(col):

            if mat[i][j] == 0:

                for c in range(col):

                    if mat[i][c] != 0:

                        mat[i][c] = MARK

                for r in range(row):

                    if mat[r][j] != 0:

                        mat[r][j] = MARK

    for i in range(row):
        for j in range(col):
                if mat[i][j] == MARK:
                    mat[i][j] = 0


    return mat


def set_mat_to_zero_obt(mat):

    row = len(mat)
    col = len(mat[0])

    first_row = any(mat[0][j] == 0 for j in range(col))
    first_col = any(mat[i][0] == 0 for i in range(row))

     # mark the row col zero if any zero

    for i in range(1,row):
         for j in range(1,col):

             if mat[i][j] == 0:

                 mat[i][0] = 0
                 mat[0][j] = 0

    # fill the matrix with zero

    for i in range(1,row):
        for j in range(1,col):
            if mat[i][0] == 0 or mat[0][j] == 0:

                mat[i][j] = 0


    if first_row:
        for j in range(col):
            mat[0][j] = 0

    if first_col:
        for i in range(row):
            mat[i][0] = 0

    return mat

print(set_mat_to_zero([[1,1,1],[1,0,1],[1,1,1]]))
print(set_mat_to_zero_obt([[1,1,1],[1,0,1],[1,1,1]]))
