def tokar(word: str):
    '''Check if a string is a palindrome
    Parameters: word
    Returns: string that tells if word is a palindrome
    Example:
    tokar("Dallassallad")'''
    stripped_word = word.replace('.', '').replace(' ', '').replace(',', '')
    if stripped_word.lower() == stripped_word[::-1].lower():
        return f'"{word}"" is a palindrome'
    else:
        return f'"{word}"" is not a palindrome'
