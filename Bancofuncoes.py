

import sqlite3
conexao = sqlite3.connect('Banco_exercicio_Isa')
cursor = conexao.cursor()

def InserirUsuarios():
    nome = input('Digite seu nome: ')
    cidade = input('Mora em qual cidade: ')
    dados = [nome,cidade]
    banco = 'INSERT INTO usuarios (nome, cidade) VALUES (?,?)'
    cursor.execute(banco,dados)

def AlterarUsuarios():
    nome = input('Digite o nome que deseja substituir: ')
    id = input('Digite o identificador da pessoa a ser substituída: ')
    dados = [nome, id]
    banco = ('UPDATE usuarios SET nome = ? where id = ?')
    cursor.execute(banco,dados)

def DeletarUsuarios():
    nome = input('Digite o nome que deseja deletar: ')
    dados = [nome]
    banco = ('DELETE FROM usuarios where nome = ?')
    cursor.execute(banco,dados)

def ListaUsuarios():
    informacoes = cursor.execute('SELECT * FROM usuarios')
    for i in informacoes:
        print(i)
while True:
    print('~~'*30)
    print('ESCOLHA UMA OPÇÃO')
    opc = input('''1-> Inserir usuário:
2-> Alterar Usuário:
3-> Deletar usuário:
4-> Mostrar tabela de usuários:
5-> Sair\n''')
    if opc == '1':
        InserirUsuarios()
    elif opc == '2':
        AlterarUsuarios()
    elif opc == '3':
        DeletarUsuarios()
    elif opc == '4':
        ListaUsuarios()
    elif opc == '5':
        break


conexao.commit()
conexao.close
