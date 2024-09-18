# Recebe a entrada do usuário
numero_digitado = float(input("Digite um número: "))

# Verifica e exibe o resultado
if numero_digitado > 0:
    print("O número ",numero_digitado," é positivo.")
elif numero_digitado < 0:
    print("O número ",numero_digitado," é negativo.")
else:
    print("O número é igual a zero.")
