class _No:
    def __init__(self, valor):
        self.valor = valor 
        self.proximo = None 
        self.anterior = None

class Lista_Simples:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0
    
    def __str__(self):
        value_list= '['
        if self.inicio is not None:
            perc = self.inicio
            value_list += str(perc.valor)
            while perc.proximo is not None:
                perc = perc.proximo
                value_list += ', '
                value_list += str(perc.valor)
        value_list += ']'
        return value_list
    
    def vazia(self): # Verificar se a lista está vazia
        if self.inicio is None:
            return True
        return False
    
    def tamanho(self): # Tamanho da Lista
        return self.tamanho

    def adicionar(self, valor): #Adicionar elemento ao final da lista
        no = _No(valor) 
        if self.vazia(): 
            self.inicio = self.fim = no
            self.tamanho += 1
        else:
            self.fim.proximo = no
            no.anterior = self.fim
            no.proximo= None
            self.fim = no
            self. tamanho += 1
    
    def adicionar_inicio(self, valor): #Adicionar elemento no inicio da lista
        no = _No(valor)
        if self.vazia(): #Verificar se a lista está vazia
            self.inicio=self.fim = no #Se estiver vazia irá criar como o primeiro elemento
        else:
            no.proximo=self.inicio #Se houver elemento na lista criará como ultimo elemento da lista
            self.inicio.anterior = no
            no.anterior = None
            self.inicio = no
        self.tamanho += 1
            
    def inserir(self, index, valor): #Inserir elemento no index desejado com o valor
        meio = int(self.tamanho / 2)
        if index> self.tamanho:
            raise IndexError ("Posição inválida")
        elif index == self.tamanho:
            self.adicionar(valor)
        elif index == 0:
            self.adicionar_inicio(valor)
        else:
            if index <= meio: #Verificar se é index procurado é menor que a metade da lista
                no = _No(valor)
                perc = self.inicio
                cont = 0
                while cont < index - 1:
                    perc = perc.proximo
                    cont += 1
                no.proximo = perc.proximo
                perc.proximo.anterior = no
                perc.proximo = no
                no.anterior = perc
            else: #Acessar a outra metade da lista
                no = _No(valor) 
                perc = self.fim
                cont = self.tamanho
                while cont > index:
                    perc = perc.anterior
                    cont -= 1
                no.proximo = perc.proximo
                perc.proximo.anterior = no
                perc.proximo = no
                no.anterior = perc
            self.tamanho += 1
 
    def remover_inicio_lista(self): #Remover o inicio da lista
        if self.vazia():
            raise TypeError('Lista está vazia')
        elif self.tamanho == 1:
            self.inicio = None
            self.fim = None
        else:
            self.inicio = self.inicio.proximo
            self.inicio = None
            self.tamanho -= 1
    
    def remover_fim_lista(self): #Remover o ultimo elemento da lista
        if self.vazia():
            raise TypeError('Liesta está vazia')
        elif self.tamanho == 1:
            self.inicio = None
            self.fim = None
        else:
            self.fim = self.fim.anterior
            self.fim.proximo = None
            self.tamanho -=1
    
    def remover_index(self, index): #Remover Index desejado da lista
        if self.vazia():
            raise TypeError('Lista está vazia.')
        elif index == 0:
            self.remover_inicio_lista() #Remover Inicio (index)
        elif index == self.tamanho -1:
            self.remover_fim_lista() #Remover Fim (index)
        else:
            perc = self.procurar_index(index-1) #Irá procurar o index (-1)
            perc.proximo = perc.proximo.proximo #Perc vai pegar uma casa a mais para ligar-se a lista.
        self.tamanho-=1
        return True
    
    def remover_item(self, valor): #Remover Item (Valor) da lista
        if self.tamanho == 0:
            TypeError('Lista está Vazia.')
        perc = self.inicio
        if perc.valor == valor: #Se for o início
            self.inicio = self.inicio.proximo #O inicio vai começar da segunda casa
            self.tamanho -= 1
            return
        while perc.proximo: #enquanto houver um próximo ele continua
            if perc.proximo.valor == valor:
                aux = perc.proximo #Aux será o apontador para o item da exclusão
                perc.proximo = aux.proximo #Liga o antecessor do Aux com o próximo do Aux
                self.tamanho -= 1
            perc = perc.proximo
            return
        raise ValueError('Não existe esse valor na lista.')
    
    def editar_item(self, index, valor): #Substituir valor de um item com um index desejado
        perc = self.procurar_index(index)
        perc.valor = valor

    def procurar_index(self, index): #Procurar um index e retornar valor
        if index > self.tamanho or self.tamanho == 0: #Verificar se tem algo na lista
            raise IndexError('Não existe elementos na lista')
        elif index == 0:
            return self.inicio
        else:
            perc = self.inicio
            for i in range(index):
                perc = perc.proximo #Quando o valor do index for encontrado, ele irá retornar com os dados
            return perc

    
    def procurar_valor(self,index): #Irá percorrer a lista até o index selecionado e irá retornar o valor.
        if index > self.tamanho or self.tamanho == 0: #Verificar se tem algo na lista
            raise IndexError('Não existe elementos na lista')
        else:
            perc = self.inicio
            for i in range(index):
                perc = perc.proximo #Quando o valor do index for encontrado, ele irá retornar com os dados
            return f' O valor do index é ',perc.valor
                    
    def valor_repetido(self, valor): #OK
        cont = 0
        perc = self.inicio
        while perc:
            if perc.valor == valor:
                cont +=1
            perc = perc.proximo
        return f'O valor {valor} aparece {cont} vezes na lista.'
    
    def ordenamento_sort(self):
        for i in range(self.tamanho-1): #Fazer com todos os elementos da Lista
            inicio=self.inicio #Apontador 'Inicio' apontado para Inicio
            flag=inicio.proximo #Apotandor 'Flag' para próxima casa do Inicio
            aux=None #Apontador Auxiliador
            while flag: #
                if inicio.valor>flag.valor: #Enquando apontador inicio for maior que apontador flag
                    if aux == None:
                       aux = inicio.proximo
                       flag = flag.proximo
                       aux.proximo = inicio
                       inicio.proximo = flag
                       self.inicio = aux
                    else:   #Se o apontador auxiliador for menor que o apontador Inicio
                        temp = flag #( Temp > Auxiliadora de Apontador)
                        flag = flag.proximo
                        aux.proximo = inicio.proximo
                        aux=temp
                        temp.proximo = inicio
                        inicio.proximo = flag
                else:   #Regravamento da Lista
                    aux=inicio
                    inicio=flag
                    flag=flag.proximo
            i=i+1 #'Finalizador' do Processo    

lista = Lista_Simples()
lista.adicionar(1)
lista.adicionar(2)
print(lista)
lista.inserir(0,3)
print(lista)
lista.remover_index(1)
lista.adicionar(4)
print(lista)
print({lista.tamanho},' <-- Tamanho da Lista')
print(lista.valor_repetido(1))
print(lista)
lista.remover_item(1)
lista.editar_item(0,2)
lista.editar_item(1,2)
lista.adicionar(5)
print(lista)
lista.editar_item(0,1)
print(lista)
lista.adicionar(3)
lista.ordenamento_sort()
print(lista,' <-- Lista Ordenada')
print(lista.procurar_valor(3))
#OK