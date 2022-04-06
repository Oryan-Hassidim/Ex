#############################################################
# FILE : wordsearch.py
# WRITER : Oryan Hassidim , oryan.hassidim , 319131579
# EXERCISE : intro2cs2 Ex5 2022
# DESCRIPTION: A simple program which reads wordlist and
#              characters matrix from files, and searches
#              the words in the matrix in given direction.
#              Prints the output to a file.
# STUDENTS I DISCUSSED THE EXERCISE WITH: --
# WEB PAGES I USED:
# NOTES: A lot of dictionaries for better performance.
#############################################################

# from multiprocessing import Pool
from itertools import chain
from sys import argv
from pathlib import Path
from os import remove


def normalize(line):
    """
    Normalizes a line of characters from file.
    :param line: a line of characters.
    :return: a line of characters.
    """
    return line.strip().replace("\n", "")


def read_wordlist(filename):
    """
    Reads a wordlist from a file and returns a list of words.
    :param filename: path for the file.
    :return: list of words.
    """
    wordlist = []
    with open(filename, "r", encoding="ascii") as file:
        for line in file:
            wordlist.append(line.strip())
    return wordlist


def read_matrix(filename):
    """
    Reads a matrix of charaters from file, seperated by commas.
    returns a list of lists.
    :param filename: path for the file.
    :return: list of lists.
    """
    matrix = []
    with open(filename, "r", encoding="ascii") as file:
        for line in file:
            matrix.append(normalize(line).split(","))
    return matrix


def index_words(word_list):
    """
    Takes as parameter a list of words.
    Returns a dictionary of the words as lists of characters, indexed by
    their *first letter* and then their *length*.
    :param word_list: list of words.
    :return: dict<first_char, dict<length, char_list> >.
    """
    index_dict = {}
    for word, times in word_list:
        first = word[0]
        group = index_dict.get(first)
        if group is None:
            index_dict[first] = {len(word): [(list(word), times)]}
        else:
            group[len(word)] = group.get(len(word), []) + [(list(word), times)]
    return index_dict


def calculate_diagonal_directions(matrix):
    """
    Takes a matrix as a parameter ang returns all diagonal from
    top-left to bottom-right.
    Like this:
    a b c d
    e a b c
    f e a b
    """
    chunk = list(chain(*matrix))
    height, width = len(matrix), len(matrix[0])
    lst1 = [
        chunk[column : width * min(width - column, height) : width + 1]
        for column in range(width)
    ]
    lst2 = [
        chunk[row * width : row * width + width * min(width, height - row) : width + 1]
        for row in range(1, height)
    ]
    return lst1 + lst2


def flip_matrix(matrix):
    """
    Flips the given matrix around Y-Axis.
    Like:
    a b c d      d c b a
    e f g h  =>  h g f e
    i j k l      l k j i
    """
    return [row[::-1] for row in matrix]


def transpose_matrix(matrix):
    """
    Transposes the given matrix.
    Like:
    a b c d      a e i
    e f g h  =>  b f j
    i j k l      c g k
                 d h l
    """
    return list(map(list, zip(*matrix)))


def r_y_x(matrix, r, y, x):
    """
    Takes as argument a matrix, and 3 booleans directions.
    Returns all lines in those directions.
    :param matrix: a matrix of characters.
    :param r: boolean value whether collect the stright lines from
    left to right.
    :param y: boolean value whether collect the diagonal of the matrix
    from top-left corner.
    :param x: boolean value whether collect the diagonal of the matrix
    from buttom-right corner.
    """
    result = []
    if r:
        result += matrix
    if y or x:
        diagonals = calculate_diagonal_directions(matrix)
        if y:
            result += diagonals
        if x:
            result += flip_matrix(diagonals)
    return result


def calculate_directions(matrix, directions):
    """
    Takes matrix and directions string.
    Returns list of all lines to check.
    :param matrix: matrix of characters.
    :param directions: directions string, encoded in "ryxlzwud" pattern.
    :return: list of characters lists.
    """
    result = []
    r, y, x, l, z, w, u, d = map(lambda x: x in directions, "ryxlzwud")

    if r or y or x:
        result += r_y_x(matrix, r, y, x)

    # for left reading we Y-Axis flip the matrix.
    if l or z or w:
        flipped = flip_matrix(matrix)
        result += r_y_x(flipped, l, z, w)

    # for up-down reading we transpose the matrix.
    if u or d:
        transposed = transpose_matrix(matrix)
        if d:
            result += transposed
        if u:
            result += flip_matrix(transposed)

    return result


def find_in_lists(indexed_words, direction_index, lists):
    """
    Finds all occurances of sub-lists in given list of lists.
    Collect them to the times array which attached to the sublist
    in the given index (for parrall proccessing).
    """
    for lst in lists:
        length = len(lst)
        for i, char in enumerate(lst):
            # all words which starts in the current letter.
            group = indexed_words.get(char)
            if group is None:
                continue
            for word_length, words in group.items():
                # check if there is enough space to the word
                if word_length > length - i:
                    continue
                for word, times in words:
                    # find the *first* correct word, if exists.
                    if word == lst[i : i + word_length]:
                        times[direction_index] += 1
                        break


def find_words(word_list, matrix, directions):
    """
    Takes as parameter list of words, matrix of characters
    and directions encoded by "udrlwxyz" letters.
    Returns list of tuples with the words founded and times.
    :param word_list: list of words.
    :param matrix: list of lists of characters.
    :param directions: string of directions.
    :return: list of tuples.
    """
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return []

    # for collecting faster the instances, we assign reference types (list)
    # attached to the words.
    # and, I mistakenly thought we should write to the file in the order we received...
    words = [(word, [0]) for word in word_list]
    # index the words by first character and length
    indexed = index_words(words)
    # collect the sub-lists we need to check for any direction
    lines = calculate_directions(matrix, directions)

    # check the words for every direction
    find_in_lists(indexed, 0, lines)

    # return tuples
    return [(word, times[0]) for word, times in words if times[0] > 0]


def write_output(results, file_name):
    """
    Writes output line by line to the file in the given path.
    Deletes the file if exists.
    """
    my_file = Path(file_name)
    if my_file.is_file():
        remove(file_name)

    with open(file_name, "a", encoding="ascii") as file:
        for word, times in results:
            file.write(word)
            file.write(",")
            file.write(str(times))
            file.write("\n")
        file.flush()
        file.close()


def chek_input():
    """Validates the input."""
    issues = []
    if len(argv) != 5:
        issues.append("args count to this program must be 4!")
    else:
        my_file = Path(argv[1])
        if not my_file.is_file():
            issues.append("the word_list file doesn't exists in the given path!")
        my_file = Path(argv[2])
        if not my_file.is_file():
            issues.append("the matrix file doesn't exists in the given path!")
        if len(set(argv[4]) - set("ryxlzwud")) > 0:
            issues.append(
                "valid directions are 'r', 'y', 'x', 'l', 'z', 'w', 'u' and 'd' only!"
            )
    if len(issues) > 0:
        print(*issues, sep = "\n")
        return False
    return True


def main():
    """
    Reads from command-line arguments the parameters of the program, run
    it and prints the output to the output file.
    """
    words = read_wordlist(argv[1])
    matrix = read_matrix(argv[2])
    output_file = argv[3]
    directions = argv[4]
    write_output(find_words(words, matrix, directions), output_file)


if __name__ == "__main__":
    if chek_input():
        main()
