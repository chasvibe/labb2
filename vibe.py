import random


# Takes users bet and multiplies it with the amount of guesses the user has left
def winnings(user_bet, guesses):
    return user_bet * guesses


# Takes the deposition minus bet, and returns what's left
def bet(user_deposition, user_bet):
    return user_deposition - user_bet


print("""
                            Time to guess!
           Your job is to guess a number between '1' and '40'
             For each wrong guess, your deposit will shrink 
             If you guess right before you are out of money,
          the total amount that you bet so far will be multiplied
                 by the amount of guesses you have left.  
            """)
counter = 10  # Counter that goes to 10 and then quits, if right answer: resets
loop_counter = 0
while True:
    try:
        deposition = eval(input("\t\t    How much do you want to deposit?:\n\t\t\t\t  "))  # Amount of money the user inputs
        if deposition < 100:
            print("\t\t    Please enter a value over 100. . .\n ")
        else:
            break
    except NameError:
        print("\t\t    Please enter a value over 100. . .\n ")
    except TypeError:
        print("\t\t    Please enter a value over 100. . .\n ")
    except KeyboardInterrupt:
        print("\t\t    Please enter a value over 100. . .\n ")
    except SyntaxError:
        print("\t\t    Please enter a value over 100. . .\n ")


print(f"\t\t\t¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤")
print(f"\t\t\t  Your balance is: {deposition}")
print(f"\t\t\t¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤")


while deposition > 0:
    try:
        random_number = random.randint(1, 40)  # Correct answer
        while True:
            user_bet = eval(input("\t\t     How much would you like to bet?:\n\t\t\t\t  "))  # The amount the user wants to bet
            if user_bet > deposition:
                print("\t\t   You cannot bet more than you own. . .")
            else:
                break
        new_user_deposition = bet(deposition, user_bet)
        while counter >= 0:
            try:
                guess = eval(input("\t\t\t  Please enter a guess:\n\t\t\t\t  "))
                if counter == 0:
                    print("\t\t      Sorry your guesses ran out. . .")
                    new_user_deposition -= user_bet
                    deposition = new_user_deposition
                    break
                elif guess == 'quit()':
                    break
                elif guess == random_number:
                    print("""
                   ¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤
                   Congratulations! You guessed right!
                   ¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤
                    """)
                    new_user_deposition += winnings(user_bet, counter)
                    counter = 10
                    deposition = new_user_deposition
                    print(f"\t\t\t¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤")
                    print(f"\t\t\t  Your balance is: {new_user_deposition}")
                    print(f"\t\t\t¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤")
                    break
                elif guess < 0 or guess > 40:
                    print("\tPlease try guessing a whole number between '1' and '40'")
                elif guess < random_number:
                    print("\t\t\t    Sorry, too low. . .")
                    print(f"\t\t\tYou have {counter} guesses left. . .")
                    counter -= 1
                elif guess > random_number:
                    print("\t\t\t    Sorry, too high. . .")
                    print(f"\t\t\tYou have {counter} guesses left. . .")
                    counter -= 1
            #except NameError:
            #    print("\tPlease try guessing a whole number between '1' and '40'")
            except TypeError:
                print("\tPlease try guessing a whole number between '1' and '40'")
            except KeyboardInterrupt:
                print("\tPlease try guessing a whole number between '1' and '40'")
            except SyntaxError:
                print("\tPlease try guessing a whole number between '1' and '40'")
    #except NameError:
    #    print("\tPlease try guessing a whole number between '1' and '40'")
    except TypeError:
        print("\tPlease try guessing a whole number between '1' and '40'")
    except KeyboardInterrupt:
        print("\tPlease try guessing a whole number between '1' and '40'")
    except SyntaxError:
        print("\tPlease try guessing a whole number between '1' and '40'")


print("\t\t  Thank you for playing! Come back soon!")