if __name__ == '__main__':
    a = int(input("Enter value a: "))
    b = int(input("Enter value b: "))
    
    def intDiv(a,b):
        division = a//b
        return division
    mydiv=intDiv(a,b)
    print(mydiv)

def floatDiv(a,b):
    flotdiv = a/b
    return flotdiv
mydiv1 = floatDiv(a,b)
print(mydiv1)

    