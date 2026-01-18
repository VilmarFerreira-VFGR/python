'''
Programação Orientada a Objetos (POO) em Python é um paradigma que organiza 
o código em torno de classes e objetos, permitindo representar entidades do 
mundo real com atributos (dados) e métodos (comportamentos). Isso facilita 
a reutilização, manutenção e expansão do código.

Classe         → É como um molde ou modelo. Define atributos e métodos.
Objeto         → É uma instância da classe, ou seja, algo criado a partir do molde.
Atributos      → São as características do objeto (ex: nome, idade).
Métodos        → São as ações que o objeto pode realizar (ex: falar, andar).
Encapsulamento → Protege os dados internos do objeto.
Herança        → Permite que uma classe herde atributos e métodos de outra.
Polimorfismo   → Permite que métodos tenham comportamentos diferentes 
'''

# Definição de classe
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome   # Atributo
        self.idade = idade # Atributo

    def falar(self):       # Método
        print(f'Olá, meu nome é {self.nome} e tenho {self.idade}.')

# Criando objetos
p1 = Pessoa('Ana', 25)
p2 = Pessoa('Carlos', 30)
p3 = Pessoa('Paulo', 40)

# Usando métodos
p1.falar()
p2.falar()
p3.falar()