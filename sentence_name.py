#Sentences in (anonymous)functions
import random

def main() :
    #Input of the user
    usr_in = input("\nType thine name: ")
    
    #The sentences are kept in this array
    sentences = ["Greetings to you, ", "Marvelous programming there, ", "The Earth seems rather flat this morning, "]    
    
    #This statement generates an anonymous function
    sentence_function = lambda sentence, name : sentence + name + '.'
    
    for s in sentences :
        print(sentence_function(s, str(usr_in)))

    #If one wished to randomize it, it could be like this:
    #sentence_function = lambda sentence, name : sentence + name + '.'
    #print("\t~Randomized~\n\n" + sentence_function(str(sentences[random.randint(0,len(sentences) - 1)]), str(usr_in)))
    #print("\n")

    #The normal way of using functions:
    print("-- Normal way of doing this: --" )
    print("First sentence: " + sentence_1(usr_in))
    print("Second sentence: " + sentence_1(usr_in))
    print("Third sentence: " + sentence_1(usr_in))
    
#Below is the "boring" way of solving this problem;
def sentence_1(name):
    return "Greetings to you, " + name + '.'
def sentence_2(name):
    return "Marvelous programming there, " + name + '.'
def sentence_3(name): 
    return "The Earth seems rather flat this morning, " + name + '.'

if __name__ == "__main__":
    main()