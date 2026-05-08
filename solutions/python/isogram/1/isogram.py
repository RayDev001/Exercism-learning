def is_isogram(string: str) -> bool:
    list_of_used_letters: list[str] = []
    
    for index, letter in enumerate(string):
        if letter.lower() not in list_of_used_letters:
            list_of_used_letters.append(string[index].lower())
        elif letter == " " or letter == "-":
            list_of_used_letters.append(string[index])
        else:
            return False
            
    return True