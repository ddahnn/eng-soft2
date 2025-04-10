from datetime import datetime

data_nasc = input("Digite sua data de nascimento (DD/MM/AAAA): ")
data_nasc = datetime.strptime(data_nasc, "%d/%m/%Y")

dia_hoje = datetime.today()

# Calculando a idade
idade = dia_hoje.year - data_nasc.year

# Verificando se já fez aniversário este ano
if (dia_hoje.month, dia_hoje.day) < (data_nasc.month, data_nasc.day):
    idade -= 1

print(f"Sua idade é: {idade} anos")


if idade >= 18:
    print("Voce é maior de idade Se fudeu!")



    ''' Job git lab funciona em paralelo
    stage ele funciona por fila
    '''