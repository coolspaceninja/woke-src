def fahr (n):
    return (n - 32) * 5/9
def cel (n):
    return (n * 9/5) + 32

def main():
    usr_in = input("What type of conversion do you wish to apply? C or F? ")
    
    if usr_in == 'C':
        print("Celsius: " + fahr(float(input("Type your fahrenheit value: "))) + "C")

    if usr_in == 'F':
        print("Fahrenheit: " + cel(float(input("Type your celsius value: "))) + "F")
        
    else:
        print("Error: malformed input")

if __name__ == "__main__":
    main()