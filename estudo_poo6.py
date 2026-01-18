class Tabuada:
    def __init__(self, numero):
        self.numero = numero

    def adicao(self):
        print(f"\nTabuada de Adição do {self.numero}")
        for i in range(1, 11):
            print(f"{self.numero} + {i} = {self.numero + i}")

    def subtracao(self):
        print(f"\nTabuada de Subtração do {self.numero}")
        for i in range(1, 11):
            print(f"{self.numero} - {i} = {self.numero - i}")

    def multiplicacao(self):
        print(f"\nTabuada de Multiplicação do {self.numero}")
        for i in range(1, 11):
            print(f"{self.numero} x {i} = {self.numero * i}")

    def divisao(self):
        print(f"\nTabuada de Divisão do {self.numero}")
        for i in range(1, 11):
            # Evita divisão por zero
            if i != 0:
                print(f"{self.numero} ÷ {i} = {self.numero / i:.2f}")


# Programa principal
if __name__ == "__main__":
    valor = int(input("Digite um número para gerar a tabuada: "))
    tabuada = Tabuada(valor)

    tabuada.adicao()
    tabuada.subtracao()
    tabuada.multiplicacao()
    tabuada.divisao()
