def max_of_three(x,y,z):
    num_list = [x,y,z]
    max_num = 0
    
    for i in num_list:
        if i > max_num:
            max_num = i 
    return max_num
def max(x, y):
    if x > y:
        return x
    else:
        return y

def main():
    #print("Max value " + str(max(20,30)))
    print("Max val is " + str(max_of_three(3,6,8)))

if __name__ == "__main__":
    main()