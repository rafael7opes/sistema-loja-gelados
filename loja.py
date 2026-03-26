print('Sejam bem-vindos à loja de Gelados do Rafael Lopes!')
print('-'*50)
print('-'*20, 'CARDÁPIO', '-'*20) #Cardápio com sabores e preços
print('-'*50)
print('---|  Tamanho  |  Cupuaçu (CP)  |  Açaí  (AC) |---')
print('---|     P     |    R$ 9.00     |   R$ 11.00  |---')
print('---|     M     |    R$ 14.00    |   R$ 16.00  |---')
print('---|     G     |    R$ 18.00    |   R$ 20.00  |---')
print('-'*50)

total = 0 #Acumulador começa em 0

while True: #Loop para escolher quantos sabores o usuario desejar e seus tamanhos
    sabor = input('Entre com o sabor desejado (CP/AC): ').upper()
    if sabor != 'CP' and sabor != 'AC':
        print('Sabor inválido! Tente novamente.') #Se o sabor for errado, avisa e pede de novo!
        continue

    tamanho = input('Entre com o tamanho desejado (P/M/G): ').upper()
    if tamanho != 'P' and tamanho != 'M' and tamanho != 'G':
     print('Tamanho inválido! Tente novamente.') #Se o tamanho for errado, avisa e pede de novo!
     continue

    if sabor == 'CP': #Define o preço baseado no sabor e tamanho
       if tamanho == 'P':
          preco = 9
       elif tamanho == 'M':
          preco = 14
       elif tamanho == 'G':

        
          preco = 18

    elif sabor == 'AC':
       if tamanho == 'P':
          preco = 11
       elif tamanho == 'M':
          preco = 16
       elif tamanho == 'G':
          preco = 20

    total += preco

#Define o nome do sabor por extenso para imprimir na mensagem
    if sabor == 'CP':
        nome_sabor = 'Cupuaçu'
    else:
       nome_sabor = 'Açai'

#Exibe a mensagem com o pedido e o preço formatado com duas casas decimais
    print(f'Você pediu um {nome_sabor} no tamanho {tamanho}: R${preco:.2f}')       

    mais = input('Deseja pedir mais alguma coisa? (S/N): ').upper()
    while mais != 'S' and mais != 'N': #Enquanto não digitar S ou N, repete a pergunta!
        mais = input('Deseja pedir mais alguma coisa? (S/N): ').upper()
    if mais == 'N':
        break #Se digitar N, encerra o loop e mostra o valor final do pedido

print(f'Valor total do pedido: R${total:.2f}')      

