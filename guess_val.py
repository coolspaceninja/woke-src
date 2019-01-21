import random

def main():
    secret = random.randint(1,99)
    #print("Secret: " + str(secret))

    while(True):
        usr_in = input("Guess a value between 0 and 100 (meaning 1-99 are valid values): ")

        if usr_in == secret:
            print("Congratulations, " + str(usr_in) + " was correct!")
            break
        else:
            print("Sorry, try again")

if __name__ == "__main__":
    main()