def calc(matrix, n):

    if n == 0:
        return 132

    index = 1
    result_matrix = matrix

    matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

    while index != n:
        k = 0

        for str in result_matrix:
            result_temp_mass = []

            for col in range(len(matrix[0])):
                digit = 0

                for index_t in range(len(str)):
                    digit += str[index_t] * matrix[col][index_t]

                result_temp_mass.append(digit)

            result_matrix[k] = result_temp_mass
            k += 1

        index += 1

    return result_matrix


A = [[1, 2], [0, 1]]
print(calc(A, 2 ))
