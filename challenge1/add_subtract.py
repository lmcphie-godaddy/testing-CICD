#ADD FUNCTION
def add(a:int, b:int):
    print("\na is " + str(a) + " and b is " + str(b))
    print("a + b =", a + b, "\n")
    return (a + b)

#SUBTRACT FUNCTION
def subtract(a:int, b:int):
    print("\na is " + str(a) + " and b is " + str(b))
    print("a - b =", a - b, "\n")
    return (a - b)

if __name__ == '__main__':
    x = 3
    y = 6
    
    add(x,y)
    subtract(x,y)
    # print("a + b =", add(x,y), "\n")
    # print("a - b =", subtract(x,y), "\n")