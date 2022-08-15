import os
from typing import Dict
# aqui vamos colocar o que o usuário vai ver na tela

class RegistryChildViews:
    def registry_child_view(self) -> Dict:
        self.__clear()

        print('Criação de Cadastro da Criança \n\n')
        child = input('Determine o nome da criança: ')
        mother = input('Determine o nome da mãe: ')
        father = input('Determine o nome do pai: ')
        class_id = input('Determine o ID da Turma: ')
        
        return {
            "child": child,
            "mother": mother,
            "father": father,
            "class": class_id,
        }
    
    def registry_child_success(self, new_child: any) -> None:
        self.__clear()
        
        message = '''
            Criança cadastrada com sucesso!
            * Infos:
                Id da Matrícula: {}
                Nome da criança: {}
                Id da Turma: {}
        '''.format(new_child.id, new_child.name, new_child.school_class.id)
        print(message)
        
    def registry_child_fail(self, error: str) -> None:
        self.__clear()
        
        message = '''
            Ocorreu um erro ao cadastrar a criança(aluno)
        '''.format(error)
        print(message)
        
    def __clear(self):
        os.system('cls||clear')