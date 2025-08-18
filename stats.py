chars = {}


def getNumWords(book):
    words = book.split()
    return len(words)


def getCharsDict(text):

    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1

        else:
            chars[lowered] = 1

    return chars


def sortCharacterCounts(characterCounts):
    def sortOn(items):
        return items["num"]

    characterCountsList = []
    for char in characterCounts:
        characterCountsList.append({"char": char, "num": characterCounts[char]})

    characterCountsList.sort(reverse=True, key=sortOn)
    return characterCountsList
