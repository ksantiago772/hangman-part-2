import random
from word import word_list
num_lives = 6 
 def get_word():
  word = random.choice(word_list)
word_letters=(list)word
word_completion = "_" * len(word)
guessed_let = []