

class Error(Exception):
    pass

class InputError(Error):

    def __init__(self, mensagem):
        self.mensagem = mensagem

while True:
    try:
        x = int(input('Entre com uma nota de 0 a 10: '))
        print(x)
        if x > 10:
            raise InputError('Nota não pode ser maior que 10')
        elif x < 0:
            raise InputError('NOta nao pode ser menor que zero')
        break
    except ValueError:
        print('Valor inválido. Deve-se digitar apenas números')

    except InputError as ex:
        print(ex)