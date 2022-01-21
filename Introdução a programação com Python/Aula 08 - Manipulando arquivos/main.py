# w -> sobrescreve, a -> adiciona
def escrever_arquivo(texto):
    arquivo = open('teste.txt', 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()

    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    aluno_nota = aluno_nota.split('\n')

    lista_media = []
    for x in aluno_nota:
        lista_nota = x.split(',')
        aluno = lista_nota[0]
        lista_nota.pop(0)
        media = lambda notas: sum([int(i) for i in notas])/4
        print(media(lista_nota))
        lista_media.append({aluno:media(lista_nota)})
    return lista_media


if __name__ == '__main__':
    media_notas('notas.txt')
    #escrever_arquivo('Segunda linha')
    aluno = '\nLuacas, 10, 9, 4, 7'
    atualizar_arquivo('notas.txt', aluno)
   # ler_arquivo('teste.txt')