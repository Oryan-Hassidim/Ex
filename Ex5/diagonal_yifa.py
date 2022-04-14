def diagonal1(matrix):
    """
    The function takes the upper left corner and turn each diagonal into a string,
    :param matrix:the matrix that we search for our words in it
    :return: a list of all the strings consist of the diagonals
    """
    corner_strings_xy = []
    for row in range(len(matrix) - 2, -1, -1):
        diag_str = matrix[row][0]
        for j in range(1, row + 1):
            diag_str += matrix[row - j][j]
            if (j + 1) == len(matrix[0]):
                break
        corner_strings_xy.append(diag_str)
    return corner_strings_xy


print(diagonal1(list(map(list, ["ab", "ab"]))))
print(diagonal1(list(map(list, ["abcdef"]*6))))

def diagonal3(corner_strings_xy, matrix):
    """
    The function takes the lower right corner and turn each diagonal into a string
    :param corner_strings_xy: the list of strings thht the function "diagonal2" returns
    :param matrix: the matrix we are searching in for the word
    :return: corner_string_xy with new strings, consist of the new diagonal strings
    """
    for col in range(len(matrix[0])):
        diag_str = matrix[-1][col]
        for char in range(1, len(matrix[0]) - col):
            next_char = matrix[-char - 1][col + char]
            diag_str += next_char
            if char + 1 == len(matrix):
                break
        corner_strings_xy.append(diag_str)
    return corner_strings_xy
    
    

print(diagonal3([], list(map(list, ["ab", "ab"]))))
print(diagonal3([], list(map(list, ["abc", "abc"]))))
print(diagonal3([], list(map(list, ["abcd", "abcd", "abcd"]))))
print(diagonal3([], list(map(list, ["abcdef"] * 9))))


def diagonal2and4(mat):
    flipped_mat = [row[::-1] for row in mat]
    return diagonal3(diagonal1(flipped_mat), flipped_mat)

matrix = [[1, 2, 3, 4, 5, 6],
          [1, 2, 3, 4, 5, 6],
          [1, 2, 3, 4, 5, 6],
          [1, 2, 3, 4, 5, 6],
          [1, 2, 3, 4, 5, 6],
          [1, 2, 3, 4, 5, 6],
          [1, 2, 3, 4, 5, 6],
          [1, 2, 3, 4, 5, 6],
          [1, 2, 3, 4, 5, 6]]
print(diagonal1(matrix))

