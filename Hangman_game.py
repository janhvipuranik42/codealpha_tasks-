import random
words = [ "apple", "banana","mango","grapes","orange" ]
word = random.choice(words)
guessed = ["_"] * len(word)
chances = 6

while chances >0 and "_" in guessed:
    print("Word:"," ".join(guessed))
    guess = input("Enter a letter: ")
    
    if guess in word:
        for i in range (len(word)):
            if word[i] == guess:
               guessed[i]= guess

    else:
        chances = chances - 1
        print("Wrong! Chances left: ",chances) 

if "_" not in guessed :
    print("You won! Word is: ", word)
else:
    print("You lost! Word was: ",word)