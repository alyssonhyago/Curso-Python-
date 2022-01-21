class Calculadora:

    def soma (self, valor_a, valor_b):
        return valor_a + valor_b

    def subtracao (self, valor_a, valor_b):
        return valor_a - valor_b

    def multiplica (self, valor_a, valor_b):
        return valor_a * valor_b

    def divisao (self, valor_a, valor_b):
        return valor_a / valor_b


calculadora = Calculadora()  # instanciando a classe
print(calculadora.soma(10,2))
print(calculadora.subtracao(5,3))
print(calculadora.multiplica(4,3))
print(calculadora.divisao(50,4))