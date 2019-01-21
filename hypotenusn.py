import math

def hypotenuse_c(a,b):
    return (a * a) + (b * b)

def main ():
    
    a = input("A: ")
    b = input("B: ")

    c = hypotenuse_c(a,b)
    c = math.sqrt(c)
    
    print("Length of hypotenuse is: " + str(int(c)))
    print("\n\nAngles: \n- - - - - - - - - - - - - -")
    
    angel_z = math.degrees(math.acos((b**2 + c**2 - a**2) / (2*b*c)))
    angel_y = math.degrees(math.acos((c**2 + a**2 - b**2) / (2*c*a)))
    angel_x = math.degrees(math.acos((a**2 + b**2 - c**2) / (2*a*b)))

    print("Angle z: "+str(angel_z))
    print("Angle y: "+str(angel_y))
    print("Angle x: "+str(angel_x))


if __name__ == "__main__":
    main()