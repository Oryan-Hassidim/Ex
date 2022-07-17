class WordIter():
    def __init__(self, word):
        self.__word = word
        self.__char = 0
    def __iter__(self):
        self.__char = 0
        return self
    def __next__(self):
        while True:
            if len(self.__word) == self.__char:
                raise StopIteration()
            char = self.__word[self.__char]
            self.__char += 1
            if char != ' ':
                return char

def get_iter1(word):
    return WordIter(word)

def get_iter2(word):
    for c in word:
        if c != ' ':
            yield c




def bunch_together(iterable, n):
    res = []
    iterable = iter(iterable)
    while True:
        try:
            res.append(next(iterable))
        except StopIteration:
            return
        for i in range(n-1):
            res.append(next(iterable, None))
        yield tuple(res)
        res.clear()


        
def iter_list_from(lst,ind):
    for i, x in enumerate(lst):
        if i >= ind:
            yield x

