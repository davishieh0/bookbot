number_charaters = {}

def get_num_words(book):
  words = book.split()
  return len(words)

def get_num_charaters(text):
  for c in text:
    c = c.lower()
    try:
      number_charaters[c] +=1
    except KeyError:
      number_charaters[c] = 1
  return number_charaters  