import string

def sao_anagramas(string1, string2):
    vector1=[0]*26
    vector2=[0]*26

    for character in string1.lower():
        if 'a' <= character <= 'z':
            vector1[ord(character)-97] += 1

    for character in string2.lower():
        if 'a' <= character <= 'z':
            vector2[ord(character)-97] += 1

    return vector1 == vector2

def cifra_de_cesar(texto, deslocamento):
    texto_codificado = ""

    for letra in texto:
        if letra.isupper():
            texto_codificado += chr((ord(letra) - 65 + deslocamento) % 26 + 65)
        elif letra.islower():
            texto_codificado += chr((ord(letra) - 97 + deslocamento) % 26 + 97)
        else:
            texto_codificado += letra

    return texto_codificado

def encontrar_maior_palavra(frase):
    palavras = frase.split()
    maior_palavra = ""
    maior_tamanho = 0

    for palavra in palavras:
        limpa = palavra.strip(string.punctuation)
        
        if any(ch.isdigit() for ch in limpa):
            continue
        
        if len(limpa) > maior_tamanho:
            maior_tamanho = len(limpa)
            maior_palavra = limpa

    return maior_palavra

frase = "O rato roeu a roupa do rei de Roma 1000000."
print(encontrar_maior_palavra(frase))