def sao_anagramas(string1, string2):
    pass

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

def valida_cpf(cpf_string):
    pass