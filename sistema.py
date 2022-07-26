
# escola possui várias turmas
# cada turma é composta por algumas crianças e uma professora
# cada criança é definida por uma matrícula com registros de pai e mãe


# SISTEMA
# funcionalidades:
# criar turma específica com uma professora
# cadastrar uma criança e inseri-la em uma turma
# buscar turma e apresentar todas as pessoas que a compõem
# buscar uma criança e apresentar suas informações de matrícula

# Resolução:
# Quais são as tarefas bem definidas no projeto?
# 1 - Criar turma específica com uma professora
# 2 - Cadastar aluno
# 3 - Listar alunos cadastrados
# 4 - Buscar/Procurar criança e apresentar suas informações

# Criando uma função para cada ~

# subir no github

alunos = "João", "Caio" , "Rosana" , "Gigi"
professora = "Tia Helena", "Tia Catia" , "Tia Zizi"

turma = alunos + professora

# Exibir sistema
def exibir_sistema():
    print(''' Escolha uma opção: 
        1. Cadastrar aluno
        2. Listar alunos cadastrados
        3. Procurar dados do aluno      
    ''')

# Cadastrando o aluno
def cadastrar_aluno(alunos):
    identificador = input("Id ?")
    nome = input("Nome ?")
    idade = input(input("Idade ?"))
    alunos.append((identificador, nome, idade))
    
# foi cirado uma tupla com os dados - append

# Listando os alunos
def listar_alunos(alunos):
    for aluno in alunos:
        indetificador, nome, idade = aluno
        print(f'Nome:{nome}, idade:{idade}, id:{identificador}')

# Buscando um aluno
def buscar_aluno(alunos):
    aluno_buscado = input('Id? ')
    for pessoa in pessoas:
        identificador, nome, idade = pessoa
        if identificador == identificador_indesejado:
            print(f'Nome: {nome}, idade: {idade}, id: {identificador}')
            break 
    else:
        print(f'Aluno com id {aluno_buscado} não encontrado')

# Juntando tudo :
def main():
    pessoas = []
    
    while True:
        exibir_sistema()
        opçao = int(input('Opção? '))
        if opcao == 1:
            cadastar(alunos)
        elif opcao == 2:
            listar(alunos)
        elif opcao == 3:
            buscar(alunos)
        else:
            print('Opção inválida')