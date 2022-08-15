
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

Exercício N°1:
- Uma possui várias turmas. Cada turma é composta por algumas crianças e
uma professora. Além disso, cada criança é definida por uma matricula com registros de pai e mãe.
Para que haja maior controle das turmas, foi proposto um sistema que possui as seguintes
funcionalidades:
* Criar uma turma específica com uma professora
* Cadastrar uma criança e inseri-la em uma turma
* Buscar uma turma e apresentar todas as pessoas que a compõem
* Buscar uma criança e apresentar suas informações de matricula
Implemente tal sistema!
- Observações importantes!
* O projeto deve ser salvo e armazenado em um repositório no GitHub
* Não há necessidade da utilização de um banco de dados para tal, entretanto caso seja optado pela
utilização, deixe os arquivos necessários (.sql) no projeto
* O projeto deve possuir interação em console
* A escolha de tecnologia é totalmente livre – Pode-se utilizar qualquer tipo de ferramenta
presente
na linguagem Python. Além disso, pode-se utilizar qualquer tipo de paradigma desejado
(Programação Funcional, POO, Programação assincrona, Programação Procedural…)
- Sobre a avaliação:
* Serão tomados como elementos avaliativos todos os processos de construção do sistema:
Organização de Diretórios, Formação dos Commits, Formação dos PRs (caso haja), Criação e
formatação de métodos e funções, utilização correta de pacotes importados, nomeação de
variáveis…
OBS: O projeto tem como objetivo servir como um estudo de caso para entender melhor os
modos de produção e perspectiva pessoal sobre construção e arquitetura de projetos. Portanto,
não há “construção errada” e basta implementar o sistema de acordo com convicções
pessoais. É desejavel a conclusão do projeto, entretanto, em casos de dificuldade, basta apenas
indicar a resolução
Prazo: 4 dias úteis → Finalização 26/07 23:00 (Terça-feira dia 26 de maio as 23 horas)
- Caso a finalização seja realizada antes do prazo estipulado, basta entrar em contato



            # ARQUIVO PROCESS_HANDLER
            # comece aqui 01
            # ROTA NÚMERO 01
            # aqui fica a primeira comunicação do usuário com o projeto
            # começa mostrando as opções para o usuário escolher a ação 
            # que ele pretende fazer

            # importar método de introdução do processo
            # criando a lṍgica de criar a turma
            # Segunda rota > registrando a turma do sistema


            # criando método com o type annotation None que significa que não sabemos o que ele ira nos retornar
            # se for verdadeira a ação do usuário a opção válida escolhida por ele se for o número 1, ele vai iniciar o processo de registro da classe/turma
            # se o número escolhido por ele for o 1, ele irá iniciar o registro da classe
            # caso a opção escolhida pelo usuário não seja nenhuma dessas ele irá imprimir



                # REGISTRY_CLASS_PROCESS
                # importando tela de visualização na view de registrar a classe
                # criando a primeira lógica controllers
                # o nome do arquivo 'registry_class_process' da views é igual a classe do 'RegistryClassViews' da mesma na views
                # o nome do arquivo 'registry_class_controller' é igual a classe do 'RegistryClassController'
                # armazenamos o método 'registry_class_page' que está dentro da classe 'RegistryClassViews' *na variável teacher
                # armazena a variável professora no método criado no 'controller' chamado 'registry' com o nome do arquivo chamado 'registry_class_controller'
                # criando uma estrutura condicional 
                # se a resposta fornecida pelo usuário não for vazia 'None', registra a nova escola 


        # ARQUIVO >> FIRST_VIEW
        # ROTA NÚMERO 03

        # primeiro método dentro da view a visualização da página com todas as opções
        # para imprimir a mensagem


        # ROTA: ARQUIVO NÚMERO 02 >>> INTRODUCTION_PROCESS

        # estamos importando dentro da pasta views o método de inicialização da página
        # está pasta views é onde estará armazenada a parte visual do relacionamento do usuário com o sistema direto 

        # criando uma função de inicia o processo o sistema
        # ele armazena a função e nos retornará o commando escolhido pelo usuário 
        # no caso deste sistema será o número 1