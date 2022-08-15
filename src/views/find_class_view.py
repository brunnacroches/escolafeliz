import os 

class FindSchoolClassViews:
    def find_class_view(self) -> str:
        self.__clear()
        
        print('Busca de Registro de Turma \n\n')
        class_id = input('Determine o id da turma para busca: ')
        
        return class_id
    
    def find_class_success(self, clas_registry: any) -> None:
        self.__clear()
        
        message = '''
            Turma {} - Professora {}
            * Infos:
        '''.format(
            class_registry["class_id"],
            class_registry["class_teacher"]
        )
        
        for registry in class_registry["registries"]:
            message += ''' \n
                Id da Matrícula: {}
                Nome da criança: {}
                Mãe da criança:  {}
                Pai da criança:  {}
            '''.format(
                registry["id"],
                registry["name"],
                registry["mother"],
                registry["father"]
            )
        
        print(message)
        
    def find_class_fail(self, error: str) -> None:
        self.__clear()
        
        message = '''
            Ocorreu um erro buscar Turma.
            {}
        '''.format(error)
        print(message)

    def __clear(self):
        os.system('cls||clear')
