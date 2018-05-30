import json
import time


corpus = [['extracting', 'opinions'],
['soo', 'min', 'kim', 'and'],
['abstract'],
['this', 'paper', 'presents', 'method', 'for', 'identifying', 'an'], 
['this', 'section', 'reviews', 'previous', 'works', 'in'], 
['subjectivity', 'detection', 'is'], 
['work', 'is', 'similar', 'to', 'ours', 'but', 'different']] * 1000000

# corpus = [['extracting', 'opinions'],
# ['soo', 'min', 'kim', 'and'],
# ['abstract'],
# ['this', 'paper', 'presents', 'method', 'for', 'identifying', 'an'], 
# ['this', 'section', 'reviews', 'previous', 'works', 'in'], 
# ['subjectivity', 'detection', 'is'], 
# ['work', 'is', 'similar', 'to', 'ours', 'but', 'different']] * 1000000

t1 = time.time()
new_corpus = list( map(lambda words: list(filter(lambda word: len(word)> 2, words)), corpus))
t2 = time.time()

# Pretty printing list of lists of words of length > 2
# print(json.dumps(new_corpus, indent=2))
print(t1, t2, t2-t1)

print('\nCORPUS2: NEW\n')
t1 = time.time()
new_corpus2 = [[ subelt for subelt in elt if len(subelt) >2 ] for elt in corpus]
t2 = time.time()
# print(new_corpus2)
print(t1, t2, t2-t1)

t1 = time.time()
new_corpus3 = [filter(lambda word: len(word) > 2, elt) for elt in corpus]
t2 = time.time()
print(t1, t2, t2-t1)

# print(new_corpus3)