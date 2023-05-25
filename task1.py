number = int(input('Input number'))
result = ''

def hex16(number, result=None):
    while number >= 1:
        res = number % 16
        if res > 9:
            match:
                case 10:
                    res = str('a')
                case 11:
                    res = str('b')
                case 12:
                    res = str('c')
                case 13:
                    res = str('d')
                case 14:
                    res = str('e')
                case 15:
                    res = str('f')
        result += str(res)
        number = number // 16

    return result[::-1]

print(hex16(number, result), hex(number))
