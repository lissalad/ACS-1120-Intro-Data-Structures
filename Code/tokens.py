
def tokenize(source):
  punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~…‘“”'''
  words = []
  text = open(source).read().split() # text -> list of words

  for w in text:
    w = w.lower() # de-capitalize
    for letter in w: # go through letters in word
      if letter in punc: 
        w = w.replace(letter, "") # remove character if it's in punctuation list
    words.append(w)

  return words