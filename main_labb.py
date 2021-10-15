import random
from betting import betting


def winnings(total_bet, guesses):
    return total_bet * guesses


def game(correct_answer):

    counter = 10 # Counter that goes to 10 and then quits, if right answer: resets
    new_bet = 0
    bet = eval(input("How much would you like to bet?:\n"))  # The amount the user wants to bet
    while counter >= 0:
        try:
            guess = eval(input("Please enter a guess:\n"))
            new_bet += bet
            if counter == 0:
                print("Sorry your guesses ran out. . .")
                break
            elif guess == 'quit()':
                break
            elif guess == correct_answer:
                print("""
                Congratulations! You guessed right!
                
                """)
                winnings(new_bet, counter)
                break
            elif guess < 0 or guess > 40:
                print("Please try guessing a whole number between '1' and '40'")
            elif guess < correct_answer:
                print("Sorry, too low. . .")
                print(f"You have {counter} guesses left. . .")
                counter -= 1
            elif guess > correct_answer:
                print("Sorry, too high. . .")
                print(f"You have {counter} guesses left. . .")
                counter -= 1
        except NameError:
            print("Please try guessing a whole number between '1' and '40'")
        except TypeError:
            print("Please try guessing a whole number between '1' and '40'")
        except KeyboardInterrupt:
            print("Please try guessing a whole number between '1' and '40'")
        except SyntaxError:
            print("Please try guessing a whole number between '1' and '40'")


random_number = random.randint(1, 40)  # Correct answer
deposition = eval(input("How much do you want to deposit?:\n"))  # Amount of money the user inputs
print("""
                            Time to guess!
           Your job is to guess a number between '1' and '40'
             For each wrong guess, your deposit will shrink 
             If you guess right before you are out of money,
          the total amount that you bet so far will be multiplied
                 by the amount of guesses you have left.  
            """)
print(f"Your balance is: {deposition}")
game(random_number)
#new_input = str(input("Would you like to play again?\n\t [Y], [N]"))
#if new_input.upper() == 'Y':
#    game(random_number)
#else:
print("Thank you for playing! Come back soon!")
