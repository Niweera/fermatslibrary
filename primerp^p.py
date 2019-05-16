import sympy 

def checkP():
    number = 4
    while (True):
        if (sympy.isprime(number)):
            print(number)
            y = number ** number
            x = y + 2
            if (sympy.isprime(x)):
                print("this is it! x: ",x," number: ",number)
                break
            else:
                number = number + 1
        else:
            number = number + 1

checkP()
