import math

def num_permutations(word):
    return math.factorial(len(word))

def num_permutations(word):
    if word == "":
        return 1
    count = 0
    for c in word:
        count += num_permutations(word.replace(c, ""))
    return count

def num_different_permutations(word):
    if word == "":
        return 1
    count = 0
    options = set()
    for c in word:
        new_word = word.replace(c, "", 1)
        if new_word not in options:
            count += num_different_permutations(new_word)
            options.add(new_word)
    return count

def num_filtered_permutations(word, first = ""):
    if word == "":
        return 1
    count = 0
    options = set()
    for c in word:
        new_word = word.replace(c, "", 1)
        if new_word not in options and c != first:
            count += num_filtered_permutations(new_word, c)
            options.add(new_word)
    return count

