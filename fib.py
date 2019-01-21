def main():
    
    for val in fib(int(input("Give the ength of the Fibonacci sequence: "))):
        print(str(val))

def fib(len):
    x = 0
    y = 1
    i = 0

    while( i < len):    
        z = x + y
        x = y
        y = z
        yield z
        i+=1

if __name__ == "__main__":
    main()