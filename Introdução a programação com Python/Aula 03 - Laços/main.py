
# a = int(input('Digite um numero: '))
#
# div = 0
# for x in range(1, a+1):
#     resto = a % x
#     print(a)
#     if resto == 0:
#         div += 1
#
# if div == 2:
#     print(f'numero {a} é primo')
# else:
#     print(f'não é primo {a}')

# a = int(input('Digite um numero: '))
# for i in range(a):
#     div = 0
#     for x in range(1, i+1):
#         resto = i % x
#         if resto == 0:
#             div += 1
#
#     if div == 2:
#         print(f'numero {i} é primo')
#         print(f'o numero{a} possui {i}')


nota = int(input('Entre com uma nota: '))
while nota > 10:
    nota = int(input('NOta insvalida. Entre com a nota correta: '))

