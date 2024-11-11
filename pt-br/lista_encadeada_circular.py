# Documentação link: https://www.geeksforgeeks.org/circular-linked-list/

class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


    def inserir_lista_vazia(self):



if __name__ == "__main__":
    # Inicializando e alocando memória para os nós
    primeiro = No(2)
    segundo = No(3)
    ultimo = No(4)

    # Conectando os nós
    primeiro.next = segundo
    segundo.next = ultimo
    ultimo.next = primeiro
