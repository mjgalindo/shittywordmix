import sys

def subtractBag(targetBag, sourceBag):
    targetBag = targetBag.copy()
    for letter, count in sourceBag.items():
        targetBag[letter] -= count
        if targetBag[letter] == 0:
            del targetBag[letter]
    return targetBag

def checkMatch(bag1, bag2):
    for letter, count in bag2.items():
        if letter not in bag1 or bag1[letter] < count:
            return False
    return True

def createBag(word):
    parts = {}
    for letter in word:
        if letter not in parts:
            parts[letter] = 0
        parts[letter] += 1
    return parts

words = []
with open("palabras.txt", 'r') as f:
    for word in f.readlines():
        word = word.replace('\n', '').lower()
        if len(word) < 3:
            continue
        words.append((word, createBag(word)))

targetWord = ''.join(sys.argv[1:]).lower()
query = createBag(targetWord)

removed = 0
originalLength = len(words)
for i, word in enumerate(words):
    if not checkMatch(query, word[1]):
        del words[i]
        removed+=1
print("Removed ", removed, " out of ", originalLength)


matches = []

for i, word in enumerate(words):
    if checkMatch(query, word[1]):
        subQuery = subtractBag(query, word[1])
        for j, word2 in enumerate(words[i+1:]):
            if checkMatch(subQuery, word2[1]):
                if (len(word[0]) + len(word2[0]) == len(targetWord)):
                    matches.append((word[0], word2[0]))

for match in matches:
    print(*match)
