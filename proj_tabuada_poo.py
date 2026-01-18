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
            if i != 0:
                print(f"{self.numero} ÷ {i} = {self.numero / i:.2f}")


# Esse trecho só roda se você executar tabuada.py diretamente
if __name__ == "__main__":
    print("Este arquivo define a classe Tabuada.")
    print("Execute main.py para usar o programa principal.")
