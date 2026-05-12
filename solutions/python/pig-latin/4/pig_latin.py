MATCHES = ['a', 'e', 'i', 'o', 'u', 'y', 'xr', 'yt']

def rule_1(text: str) -> str:
    text = text.lower()

    for match in MATCHES:
        if text.startswith(match):
            if match == 'y':
                continue
            text = text + 'ay'
            break
        
    return text


def rule_2(text: str) -> str:
    output = rule_1(text)
    
    if output.endswith('ay'):
        return output

    for index, letter in enumerate(output):
        if letter not in MATCHES or (index == 0 and letter == 'y'):
            output = output[1:] + letter
        else:
            break
        
    output += 'ay'

    return output


def rule_3(text: str) -> str:
    output = rule_2(text)

    if output.startswith('u') and output.endswith('qay'):
        output = output[1:-2] + 'uay'
    
    return output


def rule_4(text: str) -> str:
    output:str = rule_3(text)
    return output


def translate(text: str) -> str:
    words_in_text = text.split()
    
    translated_words: list[str] = [rule_4(word) for word in words_in_text]
    
    return " ".join(translated_words)