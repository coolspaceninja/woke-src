#Functions and sentences
def main():
    usr_in = input("\nType thine name: ")

    #First i will use lambdas to solve the problem
    
    #The sentences are kept in this array
    sentences = ["Greetings to you, ", "Marvelous programming there, ", "The Earth seems rather flat this morning, "]    
    print("\n ~ This is the lambda-way ~ ")
    
    #For each sentence, a new function will be created and called within this forLoop:
    for s in sentences :

        #The line below generates a new function based upon the current string in this forloop
        sentence_func = lambda name : s + name + '.'
        
        #Here the function is called, and its output is printed
        print(sentence_func(usr_in))

    #Here is the normal way of doing this (in case the above method is to weird for this course)
    print("\n~ Here is the orthodox way of solving the task ~")
    sentence_1(usr_in)
    sentence_2(usr_in)
    sentence_3(usr_in)

if __name__ == "__main__":
    main()

#Below are each function
def sentence_1(name):
    return "Greetings to you, " + name + '.'
def sentence_2(name):
    return "Marvelous programming there, " + name + '.'
def sentence_3(name): 
    return "The Earth seems rather flat this morning, " + name + '.'