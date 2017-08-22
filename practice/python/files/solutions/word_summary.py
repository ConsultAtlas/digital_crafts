def wordSummary():
    word_histogram = dict()
    sentence = "When I was a young wart hog there were other wart hogs and I and friends and then there were lions."
    words = sentence.split()
    #print words
    for word in words:
        if word not in word_histogram:
            word_histogram[word] = 1
        else:
            word_histogram[word] += 1
    return word_histogram
    the_best = sorted(word_histogram.values())
    print(the_best)
print(wordSummary())

#print(letterSummary('banana'))

#import collections
#print(collections.Counter('banana'))
