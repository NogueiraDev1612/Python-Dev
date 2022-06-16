print ('Este programa simula uma operação bancária, espero que goste.')
print ()
print ()
print ()
emConta = int(input('Coloque a quantidade de débito que deseja ter em conta. \n' ))

decisao = input('O que deseja fazer? Marque uma opção de 1 a 3. \n 1 Sacar \n 2 Consultar Saldo \n 3 Transferir \n ')  
print(decisao)
if  decisao == '1':
    print('Você tem em conta: ', emConta)
    sacar = int(input('Digite a o quanto deseja: '))
    if sacar > emConta:
            print('Você não tem o suficiente! Digite uma quantidade que você tenha!')
    else:
            print('Sacando valor desejado: ', sacar)
            emConta = emConta - sacar
            print('Valor disponível: ', emConta)
if  decisao == '2':
    print(emConta)
    decisao1 = input('Deseja continuar? \n 1 - SIM \n 2 - NÃO')
    if decisao1 ==  '1':
        print('Aperte F5, pois não sei como reinicia kkkk')
    else: print('FIM.')

if decisao == '3':
    trans = int(input('Quanto deseja tranferir? '))
    if trans > emConta:
        print('Você não tem o suficiente! Digite uma quantidade que vocÊ tenha!')
    else:
        print('Você tem:', emConta)
        print('Tranferindo: ', trans)
        emConta = emConta - trans
        print('Restou apenas', emConta)
