# contador_letras = lambda lista: [len(x) for x in lista]
#
# lista_animais = ['cachorro', 'gato']
#
# print(contador_letras(lista_animais))
#
#
# soma = lambda a, b: a + b
#
# print(soma(5, 10))

calculadora = {
    'soma': lambda a , b: a + b,
    'subtração': lambda a, b : a - b,
    'multiplica': lambda a, b : a * b,
    'dividi': lambda a, b : a / b,
}


soma = calculadora['soma']
print(soma(10,5))

