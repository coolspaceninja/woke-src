def to_km(n):
    return float(float(n) * 1000)

def to_m(n):
    return float(n / 1000)

def main():
    
    usr_in =input("M or KM? ")
    if usr_in == "M":
        usr_val = input("Type the number: ")
        print(to_m(float(usr_val)))

    elif usr_in == "KM":
        usr_val = input("Type the number: ")
        print(to_km(float(usr_val)))KM
        
    else:
        print("Unclear input")


if __name__ == "__main__":
    main()