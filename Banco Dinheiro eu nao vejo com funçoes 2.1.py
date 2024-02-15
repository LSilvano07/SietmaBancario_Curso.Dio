def depositar(valor, saldo, extrato, /):

    if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'
            print('Depósito realizado com sucesso')
        
    else: 
            print('Operação falhou! O valor informado é inválido.')
    
    return saldo, extrato

def sacar(valor, saldo, extrato):
     
     if valor > limite: 
                print('Valor de saque ultrapassa o limite, tente novamente!')

     elif valor > saldo:
                print('Saldo insuficiente!')

     elif valor <= saldo:
                extrato += f'Saque: R$ {valor:.2f}\n'
                print('Saque realizado com sucesso!')
                saldo = saldo - valor

     return saldo, extrato

def mostrar_extrato (extrato):
        print('\n=============== EXTRATO ===============')
        if not extrato:
              print('Não foram realizadas movimentações.')
              
        else:
            print(extrato)
            print(f'\nSaldo: R$ {saldo:.2f}')
            print('===================d====================')
        
        return extrato

def criar_usuario(usuarios, contas, AGENCIA):
    cadastro_user = dict()
     

    cpf = input('Informe o seu CPF (Ex: 48900098907): ')
    
    for usuario in usuarios:
        if cpf == usuario.get('CPF'):
            print('CPF já foi cadastrado.')
            return usuarios
        
    proxima_conta = len(contas) + 1 
    contas.append(proxima_conta)     
    cadastro_user['Nome'] = input('Informe o nome completo: ')
    cadastro_user['CPF']  = cpf
    cadastro_user['Conta'] = proxima_conta
    cadastro_user['Agencia'] = AGENCIA 
    cadastro_user['Data de Nascimento'] = input('Informe a data de nascimento (dd-mm-aaaa): ')
    cadastro_user['Endereço'] = input('Informe seu endereço (logradouro, número - bairro - cidade/estado): ')
    usuarios.append(cadastro_user)
    
    
    return usuarios, contas, AGENCIA

def listar_contas(usuarios):
    cpf = input('Informe seu CPF: ')
    
    for usuario in usuarios:
        if cpf == usuario.get('CPF'):
            print(f"Nome: {usuario['Nome']}, CPF: {usuario['CPF']}, Conta: {usuario['Conta']}, Agência: {usuario['Agencia']}, Data de Nascimento: {usuario['Data de Nascimento']}, Endereço: {usuario['Endereço']}")
            return
    print("Usuário não encontrado.")

     



LIMITE_SAQUES = 3
AGENCIA = '0001'

saldo = 0 
limite = 500
extrato = ''
numero_saques = 0 
usuarios = []   
contas = []


while True:
    
    menu = input('''Bem vindo ao Banco Dinheiro eu nao vejo!
Escolha a opção desejada para continuar:
[d] Depositar
[s] Sacar
[e] Extrato
[nc] Nova conta
[lc] Listar Contas
[q] Sair: ''')

    if menu == 'd':
          valor = float(input('Informe o valor de deposito: '))

          saldo, extrato = depositar(valor, saldo, extrato)
    
    elif menu == 's':
        if LIMITE_SAQUES > 0:

            LIMITE_SAQUES -= 1

            valor = float(input('Informe o valor de saque:'))
            saldo, extrato = sacar(valor, saldo, extrato)

        else:
            print('Limite de saques atingido!')

    elif menu == 'e':
         mostrar_extrato(extrato)
    
    elif menu == 'nc':
         criar_usuario(usuarios, contas, AGENCIA)
         

    elif menu == 'lc':
        listar_contas(usuarios)

    elif menu == 'q':
          break    

    else:
          print('operação invalida')

  