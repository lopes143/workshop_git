def add(n1, n2):
    return n1 + n2


def calculadora_simples():
    print("------------------------------")
    
    numero1 = float(input("Primeiro número: "))
    operador = input("Operador: ")
    numero2 = float(input("Segundo número: "))

    if operador == '+':
        resultado = add(numero1, numero2)
    else:
        print("Operador inválido.")
        return

    print("Resultado: " + str(round(resultado)))

# Executa
while True:
    calculadora_simples()
    print("Hello World!")
