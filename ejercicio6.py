def print_int_matrix(matrix):
    for row in matrix:
        print("\t".join(map(str, row)))
    print()


def main():
    order = int(input("Ingrese el orden de la matriz: "))

    matrix = [[0] * order for _ in range(order)]

    max_limit = (order * order + order) // 2
    counter = 1

    for row in range(0, order, 2):
        for column in range(row + 1):
            matrix[row][column] = counter
            counter += 1

        row += 1

        if counter < max_limit:
            for column in range(row, -1, -1):
                matrix[row][column] = counter
                counter += 1

    print_int_matrix(matrix)


if __name__ == "__main__":
    main()
