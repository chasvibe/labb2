import platform
import psutil
import math


def GetPCInfo():
    Result = "\nName: "
    Result += platform.node()
    Result += "\nOS: "
    Result += platform.platform()
    Result += "\nCPU: "
    Result += platform.processor()
    Result += "\nArchitecture: "
    Result += platform.machine()
    Result += "\nMemory: "
    Result += str(math.ceil(psutil.virtual_memory().total/(1024.**3))) + "GB"
    Result += "\nMemory Usage: "
    Result += str(psutil.virtual_memory().percent) + "%"
    Result += "\nPython Version: "
    Result += platform.python_version()
    return Result
print(GetPCInfo())


def primes():

    print("""
    A prime number is a natural number with exactly 2 factors
    wich means that it can only be diveded by 1 and itself,
    and it's not evenly divisible by any other whole number.

    Here you can search for how many prime numbers there are 
    within a span and which numbers within that span that
    are prime. Search between a defined starting number
    and a defined ending number by your choice.
    """)

    i = int(input("Enter the start number: "))
    end_nr = int(input("Enter the end number: "))
    counter = 0

    while(i < end_nr):
        if i == 0 : i += 2
        elif i == 1 : i += 1
        j = 2
        while(j <= (i/j)):
            if not(i%j): break
            j += 1
        if (j > i / j):
            counter += 1
            print(i, "is prime. ")
        i += 1
    return f"\nTotal number of primes {counter}\n"


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


def multiplication(a,b):
    return a*b



