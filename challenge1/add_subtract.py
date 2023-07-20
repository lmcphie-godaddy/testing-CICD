#ADD FUNCTION
def add(a:int, b:int):
    print("a is " + str(a) + ", b is " + str(b))
    return (a + b)

#SUBTRACT FUNCTION
def subtract(a:int, b:int):
    print("a is " + str(a) + ", b is " + str(b))
    return (a - b)

if __name__ == '__main__':
    print("a + b =", add(3,6), "\n")
    print("a - b =", subtract(3,6), "\n")