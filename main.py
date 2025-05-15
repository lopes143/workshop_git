def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return float(n1/n2)

def bigger(n1, n2):
    if n1 > n2:
        return n1 
    if n1 < n2:
        return n2 
    if n1 == n2:
        return 0 

def calculadora_simples():
    print("------------------------------")
    
    numero1 = float(input("Primeiro número: "))
    operador = input("Operador: ")
    numero2 = float(input("Segundo número: "))

    if operador == '+':
        resultado = add(numero1, numero2)

    elif operador == '-':
        resultado = sub(numero1, numero2)

    elif operador == '*':
        resultado = mul(numero1, numero2)

    elif operador == '/':
        resultado = div(numero1, numero2)

    else:
        print("Operador inválido.")
        return

    print("Resultado: " + str(round(resultado)))

# Executa
while True:
    calculadora_simples()
    print("dlkjawdkjsadiajwdoijsaoidjwaoidjoisajdoiwjdoiajs8743983274983274")
