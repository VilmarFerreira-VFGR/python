from proj_tabuada_poo import Tabuada

def main():
    valor = int(input("Digite um número para gerar a tabuada: "))
    tabuada = Tabuada(valor)

    tabuada.adicao()
    tabuada.subtracao()
    tabuada.multiplicacao()
    tabuada.divisao()

if __name__ == "__main__":
    main()
