import random
from words import w_list 
from playing import play

list = w_list()
# print(list)
      


# print("Hello, we are playing a game of hangman. Im thinking of a word and you have to guess it.")

word = random.choice(list)
play(word)   
word_letters = word.split 
print(word_letters)

 

  