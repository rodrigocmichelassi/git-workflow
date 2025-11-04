def sao_anagramas(string1, string2):
    vector1=[0]*26
    vector2=[0]*26

    for ch in string1.lower():
        if 'a' <= ch <= 'z':
            vector1[ord(ch)-97] += 1

    for ch in string2.lower():
        if 'a' <= ch <= 'z':
            vector2[ord(ch)-97] += 1

    return vector1 == vector2

def cifra_de_cesar(texto, deslocamento):
    pass

def valida_cpf(cpf_string):
    pass