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
            

inp = input("message to encode: ").replace('j', 'i').upper()
if len(inp) % 2 == 1: inp += ' '

output_matrix = [matrix_find(SQUARE, let) for let in inp]
output_matrix = list(zip(*output_matrix)) #transpose matrix
output_matrix = output_matrix[0] + output_matrix[1] #flatten into array
output_matrix = zip(output_matrix[::2], output_matrix[1::2]) #make pairs straight across

print(''.join(SQUARE[y][x] for x, y in output_matrix))