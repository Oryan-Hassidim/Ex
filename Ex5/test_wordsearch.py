import unittest
from wordsearch import normalize, index_words, calculate_directions


class Test_normalize(unittest.TestCase):
    def test_1(self):
        self.assertEqual(normalize(" lskr\n"), "lskr")


class Test_index_words(unittest.TestCase):
    def test_1(self):
        self.assertEqual(index_words([]), {})

    def test_2(self):
        self.assertEqual(
            index_words([("abcd", [0])]), {"a": {4: [(["a", "b", "c", "d"], [0])]}}
        )

    def test_3(self):
        self.assertEqual(
            index_words([("abcd", [0]), ("yjgto", [0])]),
            {
                "a": {4: [(["a", "b", "c", "d"], [0])]},
                "y": {5: [(["y", "j", "g", "t", "o"], [0])]},
            },
        )


class Test_calculate_directions(unittest.TestCase):
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

    def test_1(self):
        self.assertEqual(
            calculate_directions(self.matrix, "r"),
            [[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]],
        )

    def test_2(self):
        self.assertEqual(
            calculate_directions(self.matrix, "l"),
            [[[4, 3, 2, 1], [8, 7, 6, 5], [12, 11, 10, 9]]],
        )

    def rev(lst):
        lst.reverse()

    def test_3(self):
        self.assertEqual(calculate_directions(self.matrix, "d")[0][0], [1, 5, 9])
        self.assertEqual(calculate_directions(self.matrix, "u")[0][0], [9, 5, 1])

    def test_4(self):
        self.assertEqual(len(calculate_directions(self.matrix, "y")[0]), 6)


if __name__ == "__main__":
    unittest.main()
