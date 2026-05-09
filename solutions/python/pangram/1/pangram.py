def is_pangram(sentence: str) -> bool:
    """
    I want to make a list of the letters in the sentence. I want to make sure that I only insert the
    alphabetical characters from the sentence. Then, I want to transform that list into a set()
    so that no duplicate values are inserted in the list and then compare if it's lenght is == to 26.
    """
    
    letters_in_sentence: list[str] = [ltr.lower() for ltr in sentence if ltr.isalpha()]
    return len(set(letters_in_sentence)) == 26