lista_numeros = []

for i in range(5):
    num = int(input("Digite um número inteiro: "))
    lista_numeros.append(num)

soma = 0

for num in lista_numeros:
    soma += num

print("A lista de números digitados é:", lista_numeros)
print("A soma dos valores da lista é:", soma)
