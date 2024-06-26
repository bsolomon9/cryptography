SQUARE = [
    "BGWKZ ",
    "QPNDS1",
    "IOAXE2",
    "FCLUM3",
    "THYVR4",
    "567890"
]


def matrix_find(matrix, val):
    for y in range(len(matrix)):
        for x in range(len(matrix)):
            if matrix[y][x] == val:
                return [x, y]


inp = input("input to decode:")


output_matrix = []
for let in inp:
    coords = matrix_find(SQUARE, let)
    output_matrix.extend(coords)


output_matrix = zip(output_matrix[:len(output_matrix)//2], output_matrix[len(output_matrix)//2:])
print(''.join(SQUARE[y][x] for x, y in output_matrix))

