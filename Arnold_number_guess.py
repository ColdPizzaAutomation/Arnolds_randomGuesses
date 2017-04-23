import random

guessMade = 0
number = random.randint(1,20)

print("I am going to ask you a bunch of questions, and I want to have them answered immediately.\n")

myName = input("\nWhat is your name?")
myTitle = input("\nWhat is it that you do?")
myName = myName.capitalize()
myTitle = myTitle.capitalize()


print(myName, "\nI'm a cybernetic organism. Living tissue over a metal endoskeleton." "\nMy CPU has picked at random a number between 1 and 20. \nYou are a(an)", myTitle, "— you have 5 chances to guess the correct number.")

while guessMade < 5:
    guess = input("\nTake a guess: ")
    guess = int(guess)
    guessMade +=1
    
    if guess == number:
        print("\nNumber", number, "was correct.  Now, run! go!  get to the choppa.")
        
    elif guessMade == 5: 
        print("\n", number, "was the number. Program and user terminated.")
         
    
 

    
              
    
