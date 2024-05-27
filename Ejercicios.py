


def numCovid(num):
    digitos = convertirLista(num)

    return combinaciones(digitos)

def convertirLista(num, digitos=[]):
    if num == 0:
        return digitos
    else:
        digito = num % 10
        return convertirLista(num//10, [digito] + digitos)

def combinaciones(digitos, i=0, combinacion=[]):
    
    if len(combinacion) == 3:
        return suma19(combinacion)
    
    if i >= len(digitos):
        return False
    
    if combinaciones(digitos, i + 1, combinacion + [digitos[i]]):
        return True
    
    if combinaciones(digitos, i + 1, combinacion):
        return True

    return False

def suma19(combinacion, suma=0):
    if combinacion == []:
        return suma == 19
    else:
        actual = combinacion[0]
        return suma19(combinacion[1:], suma+actual)
