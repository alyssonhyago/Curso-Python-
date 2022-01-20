
# a = int(input(' Pirmiero valor: '))
# b = int(input(' Segundo valor: '))
# c = int(input(' Terceiro numero: '))
# if a > b and a > c:
#     print(f'o maior número é {a}')
# elif b > a and b > c:
#     print(f' o maior número é {b}')
# else:
#     print(f'o maior numero é {c}')
#
# print('Fim do programa!')

# a = int(input('Digite um valor: '))
# b = int(input('Digite um valor: '))
#
# resto_a = a % 2
# resto_b = b % 2
#
# if resto_a == 0 or resto_b == 0:
#     print(f' o numero digitado {a} é par')
# else:
#     print(f' o numero é {a} impar')


a = int(input('Primeira nota: '))
b = int(input('Segunda nota: '))
c = int(input('terceira nota: '))
d = int(input('quarta nota: '))
if a or b or c or d > 10:
    print('voce digitou valores maior que 10')
    input()
media = (a + b + c + d)/4

print(f'media: {media}')


