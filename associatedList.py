def ask_for_pair (question):
    return input("Your " + question + "? ")

def main() :
    questions = ("Name", "Street", "Phone Number", "Zipcode State", "Email Address")
    usr_keyvals = {}
    
    for q in questions:
        usr_keyvals.update({q : ask_for_pair(q)})

    for pair in usr_keyvals:
        print(pair, usr_keyvals[pair])

if __name__ == "__main__":
    main()