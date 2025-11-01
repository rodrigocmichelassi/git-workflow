import string

def sao_anagramas(string1, string2):
    pass

def cifra_de_cesar(texto, deslocamento):
    pass

def encontrar_maior_palavra(frase):
    palavras = frase.split()
    maior_palavra = ""
    maior_tamanho = 0

    for palavra in palavras:
        limpa = palavra.strip(string.punctuation)
        if len(limpa) > maior_tamanho:
            maior_tamanho = len(limpa)
            maior_palavra = limpa

    return maior_palavra