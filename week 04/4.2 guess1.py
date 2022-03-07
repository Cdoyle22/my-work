# A program that prompts the user to guess a number, the program should keep prompting the user to guess the number until the user gets the right one
# Author: Ciara Doyle

numberToGuess = 30

guess = int(input("Guess the number:"))
while guess !=numberToGuess:
    print ("Wrong")
    guess = (int(input("Please guess again:")))

print ("Well done! Yes the number was ", numberToGuess)



