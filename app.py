class Pilha:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.lista = [None] * self.tamanho
        self.topo = -1

    def push(self, valor):
        if self.topo == self.tamanho - 1:
            print("Pilha cheia")
        else:
            self.topo += 1
            self.lista[self.topo] = valor

    def pop(self):
        if self.topo == -1:
            print("Pilha vazia")
            return None
        else:
            valor = self.lista[self.topo]
            self.topo -= 1
            return valor

class Fila:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.lista = [None] * self.tamanho
        self.inicio = 0
        self.fim = -1
        self.quantidade = 0

    def enqueue(self, valor):
        if self.fim == self.tamanho - 1:
            self.fim = -1
        self.fim += 1
        self.lista[self.fim] = valor
        self.quantidade += 1

    def dequeue(self):
        if self.quantidade == 0:
            print("Fila vazia")
            return None
        valor = self.lista[self.inicio]
        self.inicio += 1
        if self.inicio == self.tamanho:
            self.inicio = 0
        self.quantidade -= 1
        return valor

lista = [1, 2, 3, 4, 5]
pilha = Pilha(5)
fila = Fila(10)

for i in range(len(lista)):
    pilha.push(lista[i])

for i in range(len(lista)):
    fila.enqueue(pilha.pop())

lista = [6, 7, 8, 9, 10]

for i in range(len(lista)):
    pilha.push(lista[i])

for i in range(len(lista)):
    fila.enqueue(pilha.pop())

while fila.quantidade > 0:
    print(fila.dequeue(), end=" ")