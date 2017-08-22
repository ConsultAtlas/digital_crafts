def letterSummary(word):
    letter_histogram = dict()
    for letter in word:
        if letter not in letter_histogram:
            letter_histogram[letter] = 1
        else:
            letter_histogram[letter] += 1
    return letter_histogram


print(letterSummary('banana'))

#import collections
#print(collections.Counter('banana'))
