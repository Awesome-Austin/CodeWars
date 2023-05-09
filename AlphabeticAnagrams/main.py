from string import ascii_uppercase as letters
from itertools import permutations


def listPosition(word):
    """Return the anagram list position of the word"""
    #     w = word[0]
    #     i = letters.find(w)

    #     # unique = {c: 0 for c in sorted(word) if letters.find(c) <= i}
    #     unique = {c: 0 for c in sorted(word) if letters.find(c) < i}
    print(word)
#     for c in unique.keys():
#         unique[c] = [c + ''.join(l) for l in set(permutations((word[:word.index(c)] + word[word.index(c) + 1:])))]

#     # c = sorted(unique.pop(word[0]))

#     # return sum([len(v) for k, v in unique.items()]) + c.index(word) + 1
#     return sum([len(v) for k, v in unique.items()])