print('Hello World!')
print('====== Exercício de lista de frutas ======')

lista_frutas = ['Banana', 'Maçã', 'Pera', 'Uva', 'Laranja']

fruta_verificada = input('Digite a fruta que gostaria de verificar: ')

if fruta_verificada in lista_frutas:
    print('A fruta ' + fruta_verificada + ' já está na lista!')
elif fruta_verificada == '999':
    print('Algoritmo encerrado!')
    exit()
else:
    lista_frutas.append(fruta_verificada)
    print('Fruta ' + fruta_verificada + ' estava fora da lista. Agora ela foi adicionada com sucesso!')
    print(lista_frutas)