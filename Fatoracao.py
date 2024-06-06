print('Hello World!')
print('====== Exercício de números fatorial ======')

numero_fatorial = int(input("Digite o número: "))

resultado = 1
contagem = 1

while contagem <= numero_fatorial:
    resultado = resultado * contagem
    contagem = contagem + 1

print(resultado)
