from dictogram import Dictogram
from tokens import tokenize
class Markov(dict):

  def __init__(self, histogram, word_list):
    for word in histogram:
      following = []
      for i in range(len(word_list)):
        if word == word_list[i] and i + 1 < len(word_list):
          following.append(word_list[i+1])
      self.update({word: Dictogram(following)})
        
    # self.update({word:new Dictogram(new_words)})

  def sentence(self, histogram, length):
    start = histogram.sample()
    sentence = start
    addition = self[start].sample()
    for i in range(length):
      sentence += " " + addition
      addition = self[addition].sample()
    return sentence

if __name__ == '__main__':
  words = tokenize('./tmdb_horror.txt')
  histogram = Dictogram(words)

  markov = Markov(histogram, words)
  print(markov.sentence(histogram, 30))