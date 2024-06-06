print('Hello World!')
print('====== Exercício de Fibonacci ======')

anterior = 0
atual = 1

while atual <= 100:
    print(atual)
    proximo = atual
    atual = anterior + atual
    anterior = proximo