# Warning: Modifying the computer_benefit may cause huge and lengthy output
import random

def main():
    
    #Global bounds for the game
    x = 1
    y = 99
    
    usr_secret = input("Think of a number between " + str(x)+"and" + str(y)+ ". The computer shall try to guess it: ")

    #Checking that users value are valid, adjusting them if not
    if usr_secret > y:
        usr_secret = y
    elif usr_secret < x:
        usr_secret = x

    while(True):
        
        #Difficulty settings:
        computer_guess = random.randint(x,y)
        
        #The benefit setting controls the steps the computer can go higher/lower 
        #based on last guess
        computers_benefit = 16

        if computer_guess == usr_secret:
            print("Computer: Success, it was " + str(usr_secret) + "! I read you like an open book, human!")
            break

        else:
            
            if computer_guess > usr_secret:
                print("Computer: I shall aim lower")

                #This loop hastens computers guessing ability by putting the ceiling of 
                # its guesses closer to the answer, 
                # but it does not make its random ceiling go out of bounds
                while(y > usr_secret and computers_benefit > 0):
                    y-=1
                    computers_benefit-=1
                
            else:
                print("Computer: I shall aim higher")

                #This loop hastens computers guessing ability by putting the lower bound of 
                # its guesses closer to the answer, 
                # but it does not make its random lower bound go out of bounds
                while(x < usr_secret and computers_benefit > 0):
                    x+=1
                    computers_benefit-=1

if __name__ == "__main__":
    main()