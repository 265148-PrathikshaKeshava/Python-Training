from collections import Counter
import string
from itertools import permutations
def getSpan(str1, ss):
    spans = []
    start = 0
    while start < len(str1):
        index = str1.find(ss, start)
        
        if index == -1:
            break

        spans.append((index, index + len(ss) - 1))
        start = index + 1    

    return start, spans

def reverseWords(s):
    word_split = s.split()
    reversed_sentence = reversed(word_split)
    return ' '.join(reversed_sentence)


def removePunc(s):
    return ''.join([char for char in s if char not in string.punctuation])

def countWords(s):
    word_split = s.split()
    return len(word_split)

def characterMaps(s):
    ch_m = Counter(s)  
    for k, v in ch_m.items():  
        print(f"The character '{k}' count is {v}")
    return ch_m

def makeTitle(s):
    print("The title: ", s.title())
    return s.title()

def normalizeSpace(s):
    return ' '.join(s.split())

def transform(s):
    rev = s[::-1]
    return rev.swapcase()

def permutation(s):
    return list(permutations(s))




if __name__ == '__main__':
    print(getSpan("Hello world world", 'wo'))
    print(reverseWords("Prathiksha"))
    print(removePunc("Prathiksha! Hello"))
    print(countWords("Prathiksha hello world"))
    print(characterMaps("prathiksha"))
    print(makeTitle("hello world"))
    print(normalizeSpace("hello  world   Prathiksha"))
    print(permutation("hello"))
