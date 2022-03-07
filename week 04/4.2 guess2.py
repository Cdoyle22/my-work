# Modify program in guess1 so that the program tells the user if there guess is too high or too low. 
# Author: Ciara Doyle


numberToGuess = 30

guess = int(input("Guess the number:"))
while guess !=numberToGuess:
    if guess < numberToGuess:
        print ("too low")
    else:
        print ("too high")
    guess = (int(input("Please guess again:")))

print ("Well done! Yes the number was ", numberToGuess)
