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
    pass

def valida_cpf(cpf_string):
    pass