MATCHES = ['a', 'e', 'i', 'o', 'u', 'y', 'xr', 'yt']


def rule_1(text: str) -> str:
    # Primero convertimos el texto a minuscula
    # iteramos la lista de matches
    # verificamos que el input comience con un match
    # si es cierto le agregamos 'ay'
    # salimos del loop
    # devolvemos el texto modificado
    text: str = text.lower()
    for match in MATCHES:
        if text.startswith(match):
            if match == 'y':
                continue
            text = text + 'ay'
            break

    return text


def rule_2(text: str) -> str:

    output:str = rule_1(text)

    if output.endswith('ay'):
        return output
#rrry
#yrrr
    for index, letter in enumerate(output):
        if letter not in MATCHES or (index == 0 and letter == 'y'):
            output = output[1:] + letter
        else:
            break

    output += 'ay'

    return output

def rule_3(text: str) -> str:
    # Hacer la misma evaluacion que en la regla 2
    # square = uaresqay
    # square
    # quare + s
    # quares
    # uares + q
    # uaresq + ay

    # qweqwe + qu + ay
    # hacerle split
    # ver si el indice 0 == 'u'
    # si es 'u' mover u al indice -3
    # devolverlo
    output:str = rule_2(text)

    if output[0] == 'u' and output[-3] == 'q':
        output = output[1:-2] + 'uay'

    return output

def rule_4(text:str) -> str:
    output:str = rule_3(text)
    return output

def translate(text):
    words_in_text:list[str] = text.split()
    translated_words: list[str] = []
    output:str = ""
    for index in range( len(words_in_text) ):
        translated_words.append(rule_4(words_in_text[index]))

    output = " ".join(translated_words)
    return output