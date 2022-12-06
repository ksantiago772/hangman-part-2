def play(word):
 word_completion = "_" * len(word)
 guessed = False
 guessed_letters = []
 guessed_word = []
 num_lives = 6

 print("Hello, we are playing a game of hangman. Im thinking of a word and you have to guess it.")
 print(word_completion)




 while guessed and num_lives > 0:
    guess = input("What letter would you like to guess?").lower()
    if guess in guessed_letters:
        print("you already guessed the letter")
    if str(guess) not in word:
        print(guess, "is not in the word")
        num_lives -= 1 
        guessed_letters.append(guess)
   

    if guess in word:
        print("you got a letter")
        guessed_letters.append(guess)
       
    else:("not a valid guess")
    print(word_completion)
 return play