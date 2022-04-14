import os
import sys

from wordsearch import find_words, main, read_wordlist

def test_1():
    assert find_words([], [], "") == []


def test_2():
    assert find_words(["a"], [[], []], "") == []


def test_3():
    for d in "rludxyzw":
        assert find_words(["a"], [["a"]], d) == [("a", 1)]


def test_4():
    assert find_words(["ab"], [["a", "b"]], "r") == [("ab", 1)]
    for d in "ludxyzw":
        assert find_words(["ab"], [["a", "b"]], d) == []


def test_5():
    for d in "ryd":
        assert find_words(["ab"], [["a", "a"], ["a", "b"]], d) == [("ab", 1)]
    for d in "luxwz":
        assert find_words(["ab"], [["a", "b"]], "l") == []


def test_6():
    directions = ["d", "l", "r", "u", "w", "x", "y", "z", "udlrwxyz"]
    base_path = "C:\\Projects\\Oryan-Hassidim\\Ex\\Ex5\\Additional Files\\"
    original_argv = sys.argv[:]
    sys.argv.clear()
    sys.argv += ["","","","",""]
    for d in directions:
        sys.argv[1] = base_path + "word_list.txt"
        sys.argv[2] = base_path + "mat.txt"
        sys.argv[3] = "C:\\users\\oryan\\desktop\\output.txt"
        sys.argv[4] = d
        main()
        assert os.path.isfile("C:\\users\\oryan\\desktop\\output.txt")
        expected = read_wordlist(f"{base_path}outfile_{d}.txt")
        actual = read_wordlist("C:\\users\\oryan\\desktop\\output.txt")
        assert len(actual) == len(set(actual))
        assert set(expected) == set(actual)
    sys.argv.clear()
    sys.argv += original_argv



def test_7():
    assert find_words(["bob"], [["b", "o", "b"]], "lr") == [("bob", 2)]


def test_8():
    assert find_words(["bob"], [["b", "O", "b"]], "lr") == []


def test_9():
    expected = [("dog", 1), ("god", 1)]
    actual = find_words(["dog", "god"], [["d", "o", "g"]], "lr")
    assert len(actual) == len(set(actual))
    assert set(expected) == set(actual)


def test_10():
    expected = [("bob", 2)]
    actual = find_words(["bob"], [["b"], ["o"], ["b"], ["o"], ["b"]], "d")
    assert len(actual) == len(set(actual))
    assert set(expected) == set(actual)


def test_11():
    expected = [("bob", 4)]
    actual = find_words(["bob"], [["b"], ["o"], ["b"], ["o"], ["b"]], "ud")
    assert len(actual) == len(set(actual))
    assert set(expected) == set(actual)


def test_12():
    expected = [("bob", 2), ("cat", 1), ("bobcat", 1)]
    actual = find_words(
        ["bob", "cat", "bobcat"], [["b", "o", "b", "c", "a", "t"]], "lr"
    )
    assert len(actual) == len(set(actual))
    assert set(expected) == set(actual)


def test_13():
    mat = list(map(list, ["abcd",
                          "eabc"]))
    expected = [("aa",1), ("bb",1), ("cc",1), ("d", 1), ("e", 1)]
    actual = find_words(["aa", "bb", "cc", "dd", "ee", "d", "e"], mat, "y")
    assert len(actual) == len(set(actual))
    assert set(expected) == set(actual)
    actual = find_words(["aa", "bb", "cc", "dd", "ee", "d", "e"], mat, "x")
    assert len(actual) == len(set(actual))
    assert set(expected) == set(actual)
    