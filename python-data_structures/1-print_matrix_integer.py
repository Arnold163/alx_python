def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return
    for row in matrix:
        for i, num in enumerate(row):
            if i <len(row) - 1:
                print("{:d} " .format(num), end="")
            else:
                print("{:d}" .format(num))

    if row !=matrix[-1]:
        print(end=" ")           

if __name__ == "__main__":
    matrix = [[]]

    print_matrix_integer()

