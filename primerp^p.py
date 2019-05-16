import sympy 
import sys

def checkP():
    number = int(sys.argv[1])
    while (True):
        if (sympy.isprime(number)):
            y = number ** number
            x = y + 2
            print("Now checking: ",number)
            if (sympy.isprime(x)):
                print("=================================================\nThis is it!")
                print("Input prime number: ",number,">>>>> Output prime number: ",x)
                print(" ||-->> ", number," ^ ",number," + 2 = ", x)
                break
            else:
                number = number + 1
        else:
            number = number + 1

checkP()
