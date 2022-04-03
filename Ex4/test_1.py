import unittest
import hangman

class Test_test_1(unittest.TestCase):
    def test_A(self):
        self.assertEqual(hangman.update_word_pattern("abc","___", "a"), "a__") 
    def test_B(self):
        self.assertEqual(hangman.filter_words_list(["abc","abb"], "_b_",[]), ["abc"])

if __name__ == '__main__':
    unittest.main()
