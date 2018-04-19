'''
Created on 19/01/2018

@author: Gabriel de Matos Oliveira Fernandes
'''


# Classe que representa cada estado de uma maquina de Turing
# Parametro: nome representa o nome do estado a fazer parte do conjunto de estados da maquina
# Parametro: trancicoes representa as transicoes de cada estado
# Parametro: is_final representa se se um estado é final ou não
class estado():
    def __init__(self,nome,transicoes=[],is_final=False):
        self.nome = nome
        self.transicoes = transicoes
        self.is_final = is_final
        
    def __str__(self):
        return self.nome
    # Metodo usado para resgatar uma transicao de um determinado estado
    # Parametro: simbolo representa o simbolo a sem lido em uma transicao
    # retorno: caso a transicao seja valida retorna a transicao, caso contrario retorna None
    def get_transicao(self,simbolo):
        for transicao in self.transicoes:
            if transicao[0] is simbolo:
                    return transicao
                
        return None
    # Metodo usado para resgatar o nome de um estado
    # Retorno: o nome do estado   
    def get_nome(self):
        return self.nome
            