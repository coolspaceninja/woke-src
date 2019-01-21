def main():
    names = ["Johannes", "Samuel", "Mathew", "Joseph", "Thomas", "Nazareth", "Athene"]
    namescpy = list(names)
    newnamelist = []
    
    for s in names:
        best = s
        toRemove = 0
        for temp_s in namescpy:
            if get_index(temp_s[0]) < get_index(best[0]):
                toRemove = 1
                best = temp_s

        if toRemove == 1:
            namescpy.remove(best)
            newnamelist.append(best + " "+ str(get_index(best[0])))
            toRemove = 0
        elif (s + " " + str(get_index(s[0]))) not in newnamelist:
            print(s)
            newnamelist.append(s + " " + str(get_index(best[0])))
    
    print(newnamelist)

def get_index(toIndex):
    alphastr=("abcdefghijklmnopqrstuvxyz").upper()
    return alphastr.index(toIndex)

if __name__ == "__main__":
    main()