# Escopo

# Type annotation

# Definindo função dentro de um argumento

# Métodos Privados

# Métodos Públicos

# Argumentos Privados

# Chamar os atributos de forma privada





# ________________________________________________________________#

            ####            ISSUE 01           #####
            ####            CLASSSE FACHADA    #####
                ### SITE SOBRE MAIS DO ASSUNTO
                ## SITE 1:
                ## SITE 2:
    
# Delimitando o uso ou a chamada de uma biblioteca externa
# Delimitar a chamada -> a partir do método def around 
# Definindo o padrão de uso com a Classe Fachada (link para ter
# mais detalhes sobre essa chamada)
# A idéia é delimitar a chamada das bibliotecas externas criando uma
# classe com regras específicas de como vai ser chamada no decorrer
# do projeto
import numpy as np
from scipy import optimize

class CalculationManager:
    def __init__(self) -> None:
        self.__np = np
        self.__optimize = optimize
    
    def truncate(self, valule: float, decimal_places: int) -> float:
        exponencial = 10**decimal_places
        exponencial_value = self.__np.longfloat(value * exponencial)
        dividend = self.__np.trunc(exponencial_value)
        
        response = dividend/exponencial
        return float(response)
    
    def newton_optimization(self, function: callable, x0_value: int, disp: bool):
        return self.__optimize.newton(function, x0_value, disp=disp)
    
    def around(self, input_data: float, decimal_places: int) -> float:
        return self.__np.arount(input_data, decimal_places)
    
    def longfloat(self, input_data: float) -> float:
        return self.__np.longfloat(input_data)


# ________________________________________________________________#
            ####            ISSUE 02           #####
            ####            ARGUMENTOS PRIVADOS    #####
                ### SITE SOBRE MAIS DO ASSUNTO
                ## SITE 1:
                ## SITE 2:

 ###       ORGANIZANDO A CHAMADA DA LIB EXTERNA
 # No mesmo exemplo podemos deixar mais organizada a chamada das funções e métodos 
 # da libs deixando em evidencia, o benefício desta boa prática e deixar mais
 # claro e organizado e visível para que os outros programadores rapidamente possam 
 # acahar o uso delas:
        ## chamando: __np
        ## self.__np
        ## self.__optimize
    ## USO:
        ## exponencial_value = self.__np

import numpy as np
from scipy import optimize

class CalculationManager:
    def __init__(self) -> None:
        self.__np = np
        self.__optimize = optimize
    
    def truncate(self, valule: float, decimal_places: int) -> float:
        exponencial = 10**decimal_places
        exponencial_value = self.__np.longfloat(value * exponencial)
        dividend = self.__np.trunc(exponencial_value)


# ________________________________________________________________#

            ####            ISSUE 03           #####
            ####           ESCOPOS -> MÉTODOS PRIVADOS  #####
                ### SITE SOBRE MAIS DO ASSUNTO
                ## SITE 1:
                ## SITE 2:

    # Nessa issue, uma outra sugestão de boas práticas é reforçar a importancia
    # do uso dos escopos no código 
        # Primeiramente vou explanar um pouco sobre a importancia do uso dos
        # métodos privados
        # Comparando um método, ou uma classe como uma tarafa grande, carregada de instruções
        # dentro dela também colocamos várias "sub-tarefas", pequenas tarefas dentro dela
        # Ao mesmo tempo que é considerado boas práticas a reutilização destas, um dos primeiros problemas
        # que podem acontecer a multiplicidade de funções dentro dela, inviabilizando a sua reutilização
        # Mas como então reutilizar uma função ou método e excluir as outras dentro dela?
        # A solução seria utilizar os métodos privados ---> 
        # Com os métodos privados eles se tornam exclusivos deste método e quando são reutilizadas
        # os métodos privados são usados exclusivamente dentro deste método

from typing import Dict
from src.models.school_repository import school_enrollment

class FindChildController:

    def find(self, child_name: str):
        try:
            child_registry = self.__search_child_registry(child_name)
            registry = self.__format_registry_info(child_registry)
            return { "success": True, "registry": registry }
        except Exception as exception:
            return { "success": False, "error": str(exception) }

    def __search_child_registry(self, child_name: str) -> any:
        child_registry = school_enrollment.get_child(child_name)
        if child_registry is None: raise Exception('Criança não encontrada!')

        return child_registry

    def __format_registry_info(self, child_registry: any):
        return {
            "id": child_registry.id,
            "name": child_registry.name,
            "mother": child_registry.mother,
            "father": child_registry.father,
            "class_id": child_registry.school_class.id,
            "class_teacher": child_registry.school_class.teacher,
        }


# ________________________________________________________________#

            ####            ISSUE 04           #####
            ####           TYPE ANOTATION  #####
                ### SITE SOBRE MAIS DO ASSUNTO
                ## SITE 1:
                ## SITE 2:
    ##  São usadas para indicar os tipos de dados de variáveis ​​e entradas/saídas de funções e métodos .

    def registry_child(self, child: any) -> None:
        self.children.append(child)
    
    def get_class(self, class_id: str) -> any:
        for registry in self.classes:
            if registry.id == class_id:
                return registry
            