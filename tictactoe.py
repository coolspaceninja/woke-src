map=([0,0,0],[0,0,0],[0,0,0])

def check_diagonal():
    if map[0][0] == "x" and map[1][1] == "x" and map[2][2] == "x":
        return True
    if map[0][2] == "x" and map[1][1] == "x" and map[2][0] == "x":
        return True      
    return False

def check_col(ix):
    if  map[0][ix] == "x" and map[1][ix] == "x" and map[2][ix] == "x":
        return True
    return False

def check_row(minimap):
    for x in minimap:
        if x != "x":
            return False;
    return True

def check_win():
    for y in map:
        if check_row(y):
            return True

    col_count = int(len(map))-1
    while col_count >= 0:
        if check_col(col_count):
            return True
        col_count-=1
    if check_diagonal():
        return True
    return False

def main():

    print("Tic Tac Toe!\n")
    while(check_win() == False):
        
        for i in map:
            print(i)
        
        #Player input
        x = input("Type x-coordinate: ")
        y = input("Type y-coordinate: ")

        #Keep x in bounds
        if x > 3:
            x = 3
        elif x < 1:
            x = 1

        #Keep y in bounds
        if y > 3:
            y = 3
        elif y < 1:
            y = 1
        
        map[y-1][x-1] = "x"
    
    for i in map:
            print(i)
    print("Victory! Well played!")
    

if __name__ == "__main__":
    main()
