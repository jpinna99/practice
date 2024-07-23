import random

money = 100
num = random.randint(1, 10)

# Write game of chance functions
coin_flip_call = input("Guess Heads or Tails: ")
coin_flip_call = coin_flip_call.title()


def heads_or_tails(coin_flip_call, bet):
    print(f"You guessed {coin_flip_call}.")
    result = random.randint(1, 2)
    if result == 1:
        result = "Heads"
    else:
        result = "Tails"
    if coin_flip_call == result:
        print("The result of the coin flip is " + result + ". Congratulations! You have won " + str(bet) + "!")
        return bet
    else:
        print("The result of the coin flip is " + result + ". Tough luck! You have lost " + str(bet) + "!")
        return -bet


cho_guess = input("Guess Even or Odd: ")
cho_guess = cho_guess.title()


def cho_han(cho_guess, bet):
    num1 = random.randint(1, 6)
    num2 = random.randint(1, 6)
    result = num1 + num2
    print(f"You guessed {cho_guess}.")
    if result % 2 == 0 and cho_guess == "Even":
        print("The sum of the two dice is " + str(result) + " and is even. Congratulations! You have won " + str(
            bet) + ".")
        return bet
    elif result % 2 != 0 and cho_guess == "Odd":
        print("The sum of the two dice is " + str(result) + " and is odd. Congratulations! You have won " + str(
            bet) + ".")
        return bet
    elif result % 2 == 0 and cho_guess == "Odd":
        print("The sum of the two dice is " + str(result) + " and is even. Tough luck! You have lost " + str(bet) + ".")
        return -bet
    elif result % 2 != 0 and cho_guess == "Even":
        print("The sum of the two dice is " + str(result) + " and is odd. Tough luck! You have lost " + str(bet) + ".")
        return -bet
    else:
        print("Not a valid guess")


def pick_a_card(bet):
    pack_of_cards = []
    counter_1 = 0
    while counter_1 < 4:
        for i in range(1, 14):
            pack_of_cards.append(i)
        counter_1 += 1
    pack_of_cards.sort()
    for i in range(len(pack_of_cards)):
        if pack_of_cards[i] == 1:
            pack_of_cards[i] = "Ace"
        if pack_of_cards[i] == 11:
            pack_of_cards[i] = "Jack"
        if pack_of_cards[i] == 12:
            pack_of_cards[i] = "Queen"
        if pack_of_cards[i] == 13:
            pack_of_cards[i] = "King"

    player1_pick = random.randint(1, 13)
    if player1_pick == 1:
        player1_pick = "Ace"
    if player1_pick == 11:
        player1_pick = "Jack"
    if player1_pick == 12:
        player1_pick = "Queen"
    if player1_pick == 13:
        player1_pick = "King"

    pack_of_cards.remove(player1_pick)
    random_index = random.randint(1, 51)
    player2_pick = pack_of_cards[random_index - 1]

    print(f"You have drawn {str(player1_pick)}.")
    print(f"The other player has drawn {str(player2_pick)}.")

    if player1_pick == player2_pick:
        print("It's a tie!")
        return 0
    elif player1_pick == "Ace" and player2_pick != "Ace":
        print("You win " + str(bet) + "!")
        return bet
    elif player2_pick == "Ace" and player1_pick != "Ace":
        print("You lose " + str(bet) + "!")
        return -bet
    elif player1_pick == "King" and player2_pick != "Ace":
        print("You win " + str(bet) + "!")
        return bet
    elif player1_pick == "Queen" and (player2_pick != "King" and player2_pick != "Ace"):
        print("You win " + str(bet) + "!")
        return bet
    elif player1_pick == "Jack" and (player2_pick != "King" and player2_pick != "Ace" and player2_pick != "Queen"):
        print("You win " + str(bet) + "!")
        return bet
    elif player2_pick == "King" and player1_pick != "Ace":
        print("You lose " + str(bet) + "!")
        return -bet
    elif player2_pick == "Queen" and (player1_pick != "King" and player2_pick != "Ace"):
        print("You lose " + str(bet) + "!")
        return -bet
    elif player2_pick == "Jack" and (player1_pick != "King" and player1_pick != "Ace" and player1_pick != "Queen"):
        print("You lose " + str(bet) + "!")
        return -bet
    elif player1_pick > player2_pick:
        print("You win " + str(bet) + "!")
        return bet
    else:
        print("You lose " + str(bet) + "!")
        return -bet


# Call games of chance functions
money += heads_or_tails(coin_flip_call, 5)
print(""" """)
money += cho_han(cho_guess, 10)
print(""" """)
money += pick_a_card(15)
print(""" """)
print(f"You have {money} remaining.")
