from itertools import permutations
import nltk
nltk.download('words')

from functools import reduce
import math


# Task 1
words = set(nltk.corpus.words.words())

def permute_word(word):
    perms = []
    for length in range(1, len(word)+1):
        perms.extend([''.join(p) for p in permutations(word, length)])
    
    valid_words = [p for p in set(perms) if p in words]
    return valid_words

print(permute_word('sad'))


# Task 2
def wallis_product(n):
    L = [(2 * i) / (2 * i - 1) * (2 * i) / (2 * i + 1) for i in range(1, n+1)]
    return reduce(lambda x, y: x * y, L)

L = wallis_product(10000)
pi_approximation = 2 * L

print(pi_approximation, math.pi)


#Task 3

def change(amount, coins=[25, 10, 5, 1]):
    if amount == 0:
        return [[]]  
    
    result = set()
    for coin in coins:
        if coin <= amount:
            sub_results = change(amount - coin, coins)
            for sub_result in sub_results:
                result.add(tuple(sorted([coin] + sub_result)))
    
    return [list(comb) for comb in result]

print(change(40))