from random import choice
wrongLetters=0
correctLetters=[]
guess=None
guessedWords=[]
with open("words.txt") as words:
    words=list(words.read().split())
hangman=[
    """
  +---+
  |   |
      |
      |
      |
      |
=========""", """
  +---+
  |   |
  O   |
      |
      |
      |
=========""", """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""", """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""", """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""", """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""", """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========="""]
word=choice(words)
print(hangman[0])
underscores=["_" for i in range(len(word))]
print("".join(underscores), word)
while not guess==word:
    guess = input("\033[mGuess a word ")
    if guess in guessedWords:
        print("\033[0;31;49mYou already guessed this word. \n")
    else:
        if guess.lower() in words:
            guessedWords.append(guess)
            if guess==word:
                exit("\033[0;32;49mYou got the word correct! \n")
            else:
                if bool(set(list(guess))&set(list(word))):
                    correctLetters+=list((set(list(guess))&set(list(word))))
                else:
                    print(hangman[wrongLetters+1])
                    wrongLetters+=1
        else:
            print("\033[0;31;49mInvalid Word. Please check your spelling. \n")
    if wrongLetters==6:
            exit("Game over")
    underscores = "".join([i if i in correctLetters else '_' for i in word])
    if "_" not in underscores:
        exit("\033[0;32;49mYou got the word correct! \n")
    print("\033[m" + "".join(underscores))
