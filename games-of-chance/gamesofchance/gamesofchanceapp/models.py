from django.db import models

# Create your models here.

# --- Coin Toss Function ---

# 001 - Import the random module and create a variable called money that starts with 100.
import random

totalMoney = 100

def greeting():
    global name
    name = input("Please Enter a Username: ")
    print("\n")
    print("Hello {}".format(name))
    print("Lets play a game of Heads or tails!")
    print("\n")
    return name

# Get value for wager1 and guess variables

def wager1_value():
    global wager1
    print("You have {}".format(totalMoney))
    print("\n")
    bet1 = input("Please enter your wager: ")
    wager1 = int(bet1)
    return wager1

def guess_value():
    global guess
    print("\n")
    guess = input("Please enter your guess (Heads or Tails): ")
    return guess

# 002 - Create a function that simulates flipping a coin and calling either "Heads" or "Tails".
def coin_flip(guess, wager1):
    # 'coinside' generates a side of the coin that wins.
    coinSide = random.randint(1,2)
    global totalMoney
    # First conditional statement allows for a winning argument of 'Heads'. 1 is a match to 'Heads.
    if guess == "Heads" and coinSide == 1:
        # 'totalMoney' equals the starting money plus the bet.
        totalMoney = totalMoney + (wager1 * 2)
        # print out the bet as an integer.
        yourBet = int(wager1)
        print("\n")
        yourBetString = "Your bet is {}".format(yourBet)
        print(yourBetString)
        # print out string iterpolated with totalMoney
        headsWins = "Heads, you won! You now have {}".format(totalMoney)
        print(headsWins)
        return totalMoney

    # elif statement allows for a winning argument of 'Tails'. 2 is a match to 'Tails.
    elif guess == "Tails" and coinSide == 2:
        # 'totalMoney' equals the starting money plus the bet.
        totalMoney = totalMoney + wager1
        # print out the bet as an integer.
        yourBet = int(wager1)
        print("\n")
        yourBetString = "Your bet is {}".format(yourBet)
        print(yourBetString)
        # print out string iterpolated with totalMoney
        tailsWins = "Tails, you won! You now have {}".format(totalMoney)
        print(tailsWins)
        return totalMoney

    # else statement prints if you loose. E.g if logical comparison operators do not match.
    else:
        # 'totalMoney' equals the starting money subtracted by the bet as the user lost.
        totalMoney = totalMoney - wager1
        # print out the bet as an integer (subtracted).
        yourBet = int(wager1)
        print("\n")
        yourBetString = "Your bet is {}".format(yourBet)
        print(yourBetString)
        # print out string iterpolated with totalMoney
        lost = "You lost! You now have {}".format(totalMoney)
        print(lost)
        return totalMoney

# Call coin_flip function
greeting()
wager1_value()
guess_value()
coin_flip(guess, wager1)

def play_coin_flip_again():
    playCoinFlipAgain = input("Would you like to play again! Y/N: ")
    if playCoinFlipAgain == "Y":
        wager1_value()
        guess_value()
        coin_flip(guess, wager1)
        play_coin_flip_again()
    else:
        print("\n")
        print("{}, lets play a game of Cho-Han!".format(name))
        print("\n")

play_coin_flip_again()





# --- Cho-Han Function ---



# 003 - Create a function that simulates rolling two dice and adding the results together. The player predicts whether the sum of those dice is odd or even and wins if their prediction is correct.
# Get values for wager and oddOrEven variables

def wager2_value():
    global wager2
    print("You have {}".format(totalMoney))
    bet2 = input("Please enter your wager: ")
    wager2 = int(bet2)
    return wager2

def odd_or_even_value():
    global oddOrEven
    oddOrEven = input("Please enter odd or even: ")
    return oddOrEven

def cho_han(oddOrEven, wager2, totalMoney):

    # 'dice1' & 'dice2' each generates a number between 1 -6.
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    # Print out the values of the dice thrown
    roll = input("Press 'Enter' to roll both dice!")
    print(roll)
    print("\n")
    print("Dice 1 = {}".format(dice1))
    print("Dice 2 = {}".format(dice2))
    print("\n")

    # Get the modulo of the sum of the two values added together
    sumOfTwoDice = (dice1 + dice2) % 2

    # Write a conditional statement that uses logical operators to find out if the left over modulo value in 'sumOfTwoDice' is odd or even and prints if the user has guessed correctly. This in turn adds or subtracts the totalMoney value. 
    if sumOfTwoDice == 0 and oddOrEven == "even":
        # Add the 'totalMoney' to the winnings
        totalMoney = totalMoney + (wager2 * 2)
        print("Even!")
        print("You have won {}! you now have {}".format(name, totalMoney))
        return totalMoney
    # Create an elif statement that prints if the 'sumOfTwoDice' is odd.
    elif sumOfTwoDice != 0 and oddOrEven == "odd":
         # Add the 'totalMoney' to the winnings
        totalMoney = totalMoney + (wager2 * 2)
        print("Odd!")
        print("You have won {}! you now have {}".format(name, totalMoney))
        return totalMoney
    else:
        totalMoney = totalMoney - wager2
        print("Sorry {}, you lost! you now have {}".format(name, totalMoney))
        return totalMoney

wager2_value()
odd_or_even_value()
cho_han(oddOrEven, wager2, totalMoney)

def play_cho_han_again():
    playChoHanAgain = input("Would you like to play again! Y/N: ")
    if playChoHanAgain == "Y":
        wager2_value()
        odd_or_even_value()
        cho_han(oddOrEven, wager2, totalMoney)
        play_cho_han_again()
    else:
        print("\n")
        print("{}, lets play a game of Highest card wins!".format(name))
        print("\n")


play_cho_han_again()


# --- Cho-Han Function ---

# Get values for wager and guess variables

# print("\n")
# print("{}, lets play a game of highest card wins".format(name))
# print("\n")
# bet3 = input("Please enter your wager: ")
# wager3 = int(bet2)
# userCard = input("Please pick a card! Please type in the following format - king: diamonds")
# computerCard = random.randint(0, 53)

# 004 - Create a function that simulates two players picking a card randomly from a deck of cards. The higher number wins.

# def highest_card(wager3, name, userCard, computerCard):
