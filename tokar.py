def tokar(word: str):
    '''Check if a string is a palindrome
    Parameters: word
    Returns: string that tells if word is a palindrome
    Example:
    tokar("Dallassallad")'''
    stripped_word = word.replace('.', '').replace(' ', '')
    if stripped_word.lower() == stripped_word[::-1].lower():
        return f'{stripped_word} is a palindrome'
    else:
        return f'{stripped_word} is not a palindrome'
