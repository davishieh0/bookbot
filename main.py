from stats import getNumWords, getCharsDict, sortCharacterCounts
import sys
import logging


def getBookText(pathToFile):

    with open(pathToFile) as f:
        fileContents = f.read()
        return fileContents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    bookText = getBookText(sys.argv[1])
    numWords = getNumWords(bookText)

    print(f"{numWords} words found in the document")
    letterCounts = getCharsDict(bookText)
    letterCountsSorted = sortCharacterCounts(letterCounts)

    print(
        f"""
============ BOOKBOT ============
Analyzing book found at {sys.argv[1]}...
----------- Word Count ----------
Found {numWords} total words
--------- Character Count -------"""
    )

    for letter in letterCountsSorted:
        if letter["char"].isalpha():
            print(f"{letter['char']}: {letter['num']}")

    print("============= END ===============")


if __name__ == "__main__":
    try:
        main()
    except FileNotFoundError:
        print(f"Error: File '{sys.argv[1]}' not found.")
        sys.exit(1)
    except PermissionError:
        print(f"Error: Permission denied to read file '{sys.argv[1]}'.")
        sys.exit(1)
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        print("An unexpected error occurred. Check the logs.")
        sys.exit(1)
