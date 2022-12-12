def play(word):
 word_completion = "_ " * len(word)
 guessed = False
 guessed_letters = []
 approved_letters = []
 guessed_word = []
 num_lives = 6
 # tries = 0
 print("Hello, we are playing a game of hangman. Im thinking of a word and you have to guess it.")
 print(word_completion)

   


 while not guessed and num_lives > 0 :
    guess = input("What letter would you like to guess?").lower()
    
    if guess in guessed_letters:
        print("You already guessed the letter, try again")
    if str(guess) not in word:
        print(guess, "is not in the word")
        num_lives -= 1 
        guessed_letters.append(guess)
   

    if guess in word:
        print("you got a letter")
        approved_letters.append(guess)
        if approved_letters ==  word:
          print("You Win!")
          we_stole_this = [letter if letter in approved_letters else '-' for letter in word]
      print('current word:', ' '.join(we_stole_this))
           break
    if guess not in  word:
      guessed_letters.append(guess)
    
       
    
      
      
    else:("not a valid guess")
    print(word_completion)


 


