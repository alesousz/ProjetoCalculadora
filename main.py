
print('Bem-vindos a calculadora PICA DO PY!')
numero_1 = float(input("Digite o primeiro numero: "))
numero_2 = float(input("Digite o segundo numero: "))
operação = input("Digite a operação: ")

if(operação == "+"):
    resultado = numero_1 + numero_2
elif(operação == "-"):
    resultado = numero_1 - numero_2
elif(operação == "*"):
    resultado = numero_1 * numero_2
else:
    resultado = numero_1 / numero_2


print("O Resultado é: ", resultado)


