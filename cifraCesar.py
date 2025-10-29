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

res = cifra_de_cesar("O rato roeu a roupa do rei de roma", 3)
print(res)