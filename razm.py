a = int(input("Input your first number: "))
b = int(input("Input your seconde number: "))


def upphojtill(a,b):
    theAnswer = 1
    for i in range(b):
        theAnswer = theAnswer * a
        i = i +1
    return theAnswer

print(upphojtill(a,b))