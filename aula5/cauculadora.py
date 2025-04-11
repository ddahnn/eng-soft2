def somar( a, b ):
    return a + b

def subtrair( a, b ):
    return a - b

def multi( a, b ):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("Não é possivel  dividir por zero.")
    return a / b

'''print(somar(20,9))
print(subtrair(20,49))
print(multi(4,9))
print(dividir(5,50))
print(dividir(50,5))
print(dividir(20,4))


 '''