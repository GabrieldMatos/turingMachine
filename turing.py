from estado import *

'''
Created on 19/01/2018

@author: Gabriel de Matos Oliveira Fernandes
'''
# Classe que implementa a máquina de Turing
# Parametro: alfabeto representa o alfabeto aceito para uma determinada máquina de Turing
# Parametro: estados representa os estados de uma máquina de Turing
# parametro: est_inicial representa o estado inicial da máquina
# Parametro: alfabeto_aux representa o alfabeto auxiliar usado na máquina
# Parametro: simb_inicio representa o simbolo que inicia a maquina
# Parametro: simb_branco representa o simbolo branco para essa maquina
# Atributo: fita representa a fita da maquina
# Atributo: estado_inicial representa o primeiro estado da maquina
# Atributo: cabeca representa a cabeca de leitura/escrita da maquina
# Atributo: estado_atual representa o estado atual da maquina  
class turing():
    def __init__(self,alfabeto,estados,est_inicial,alfabeto_aux,simb_inicio,simb_branco):
        self.alfabeto = alfabeto
        self.estados = estados
        self.estados.append(estado('?'))
        self.estado_inicial = est_inicial
        self.alfabeto_aux = alfabeto_aux
        self.simb_inicio = simb_inicio
        self.simb_branco = simb_branco
        self.fita = []
        self.cabeca = 0
        self.estado_atual = self.estado_inicial
    
    # Metodo que verifica se aceita ou não uma linguagem
    # Parametro: cadeia representa a cadeia de caracteres a ser computado
    # Parametro: passos representa os passos da maquina
    # retorno: retorma a fita depois de computada a cadeia
    def aceita(self,cadeia,passos=True):
        self.cabeca = 0
        self.fita = self.simb_inicio + cadeia + self.simb_branco
        self.estado_atual = self.estado_inicial
        
        if passos:
            print("---- Cadeia "+cadeia+" ----")
        
        while 0 <= self.cabeca < len(self.fita):
            saida = self.programa()
            if passos:
                print(saida)
            
        if passos:
            if self.get_estado(self.estado_atual).is_final:
                print("Cadeia '"+cadeia+"' aceita!")
            else:
                print("Cadeia '"+cadeia+"' rejeitada!")
                
            print("-----------------"+("-"*len(cadeia)))
        
        return self.fita[1:-1]
    
    # Metodo que executa a maquina de Turing 
    # Retorno: A transição para cada iteração da maquina
    def programa(self):
        saida = "programa("+self.estado_atual+","+self.fita[self.cabeca]+") = "
        transicao = self.get_estado(self.estado_atual).get_transicao(self.fita[self.cabeca])
    
        # Ve se simbolo esta em alfabeto
        if not self.checar_simbolo(self.alfabeto,self.fita[self.cabeca]):
            print(self.fita[self.cabeca]+" nao pertence ao alfabeto!")
            self.cabeca = len(self.fita)
        #
        
        if transicao is not None:
            # Se houver algo para escrever, escreve.
            if transicao[1] is not None:
                
                if not self.checar_simbolo(self.alfabeto_aux,transicao[1]):
                    print(self.fita[self.cabeca]+" nao pertence ao alfabeto!")
                    self.cabeca = len(self.fita)
                
                aux = list(self.fita)
                aux.pop(self.cabeca)
                aux.insert(self.cabeca,transicao[1])
                self.fita = ''.join(aux)
            #
            
            # Ve para qual lado mover a cabeca.
            if transicao[2]:
                self.cabeca += 1
            else:
                self.cabeca -= 1
            #
            
            # Procura e faz a transicao
            if transicao[3] is not None:
                self.estado_atual = transicao[3]
            else:
                self.estado_atual = '?'
            #
        else:
            self.cabeca = len(self.fita)
            self.estado_atual = '?'
            
        saida += self.estado_atual
        
        return saida
    
    # Metodo para encontrar um estado especifico
    # Parametro: nome representa o nome do estado
    # Retorno: o estado caso ele faça parte dos estados
    def get_estado(self,nome):
        for estado in self.estados:
            if estado.get_nome() is nome:
                return estado
                break
                
        return None
    
    # Metodo usado para checar se um simbolo faz parte do alfabeto
    # Parametro: alfabeto representa o alfabeto usado na maquina
    # Parametro: simbolo representa o simbolo a ser checado
    # Retorno: True caso exista o simbolo no alfabeto, False caso contrario   
    def checar_simbolo(self,alfabeto,simbolo):
        if simbolo is self.simb_inicio or self.simb_branco:
            return True
        
        for i in alfabeto:
            if i is simbolo:
                return True
            
        return False