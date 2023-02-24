# função para adição
def adicao(a, b):
    return a + b


# função para subtracao
def subtracao(a, b):
    return a - b


# função para multiplicacao
def multiplicacao(a, b):
    return a * b


# função para divisao
def divisao(a, b):
    return a / b

# Menu
print("Entra:\n"
      "\n1.Adicao"
      "\n2.Subtracao"
      "\n3.Multiplicacao"
      "\n4.Divisao\n")

escolha = input("Digite a escolha: ")

a = int(input("Insira o primeiro número: "))
b = int(input("Insira o segundo número: "))

if escolha == '1':
    print(adicao(a, b))

elif escolha == '2':
    print(subtracao(a, b))

elif escolha == '3':
    print(multiplicacao(a, b))

elif escolha == '4':
    print(divisao(a, b))

else:
    print("Escolha inválida")