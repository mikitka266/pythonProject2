import fractions

number1: str = input('input number1 ')
number2 = input('input number2 ')


def summ(numb2, numb1):
    numb1.split('/')
    numb2.split('/')
    a=int(numb1[0])
    b=int(numb1[1])
    c=int(numb2[0])
    d=int(numb2[1])
    number3 = (a*d + b*c)/(c*d)
    return number3


def mult(numb2, numb1):
    numb1.split('/')
    numb2.split('/')
    a = int(numb1[0])
    b = int(numb1[1])
    c = int(numb2[0])
    d = int(numb2[1])
    number4 = (a * b) / (c * d)
    return number4


print(summ(number2, number1))

