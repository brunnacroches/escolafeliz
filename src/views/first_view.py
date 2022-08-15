def introduction_page():
    message = '''
        Sistema de Cadastro Escolar
        
        * Cadastrar Turma - 1
        * Cadastrar Criança - 2
        * Buscar Turma - 3
        * Buscar Criança - 4
        * Sair - 5
    '''
    print(message)
    command = input('Comando: ')
    
    return command 
