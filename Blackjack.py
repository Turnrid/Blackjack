# Tyler Jolly
# Assn 15
# CS 1400-001

from modules.deck import Deck
from time import sleep


def win(hands, numPlayers, bet, total):
    dealerScore = checkValue(hands, numPlayers)
    if dealerScore > 21:
        print("Dealer Busts")
        dealerScore = 0
    for i in range(numPlayers):
        if checkValue(hands, i) > 21:
            total[i] = total[i] - bet[i]
        elif checkValue(hands, i) > dealerScore:
            print("Player ", i + 1, "Wins!")
            total[i] = total[i] + bet[i]
        elif checkValue(hands, i) == dealerScore:
            print("Player", i + 1, "Ties with the Dealer")
        elif checkValue(hands, i) < dealerScore:
            print("Dealer beats Player ", i + 1)
            total[i] = total[i] - bet[i]


def dealer(hands, numPlayers, deck):
    print("Dealers Turn")
    sleep(1)
    print("Dealers hand is", hands[numPlayers], "\n")
    done = False
    while not done:
        if checkValue(hands, numPlayers) <= 17:
            count = 0
            print("\nThe dealer takes a card\n")
            hit(hands, numPlayers, deck)
            count += 1
            sleep(1)
            print(hands[numPlayers])
            sleep(1)
        elif checkValue(hands, numPlayers) <= 21:
            print("\nThe dealer holds\n")
            done = True
        elif checkValue(hands, numPlayers) > 21:
            print("\nThe dealer busts\n")
            done = True


def hit(hands, player, deck):
    hand = hands[player]
    hand.append(deck.draw())
    return hand


def checkValue(hands, player):
    totalValue = 0
    aceCount = 0
    for card in hands[player]:
        getValue = card.getCardValue()
        if getValue > 10:
            getValue = 10
        if getValue == 1:
            aceCount += 1
        totalValue += getValue
    for i in range(aceCount):
        if totalValue < 12:
            totalValue += 10
    return totalValue


if __name__ == '__main__':

    numPlayers = int(input("\n\tWelcome to Black Jack!!!\n\nHow many players are there? (1 - 5): "))
    print()
    moneys = [100] * numPlayers
    bet = [0] * numPlayers

    while True:
        con = False

        for i in range(numPlayers):
            if moneys[i] > 0:
                con = True
                bet[i] = int(input("Please enter your bet amount: (Minimum bet of $5) "))
                if bet[i] < 5:
                    bet[i] = 5

        if con == False:
            break

        hands = []
        for i in range(numPlayers + 1):
            hands.append([])

        deck = Deck()
        for j in range(2):
            for i in range(numPlayers + 1):
                if i == numPlayers or moneys[i] > 0:
                    hands[i].append(deck.draw())

        for i in range(numPlayers):
            if moneys[i] <= 0:
                continue
            done = False

            while not done:
                print()
                print("Player " + str(i + 1), "\nYour Hand: " + str(hands[i]) + "\n")
                print("Menu")
                print("\t1) Like to hit?")
                print("\t2) Like to hold?\n")
                choice = int(input("Choose an option: "))
                print()

                if choice == 1:
                    hit(hands, i, deck)
                    playerValue = checkValue(hands, i)
                    if playerValue > 21:
                        print("Player " + str(i + 1), "\nYour Hand: " + str(hands[i]))
                        print("You Bust\n")
                        done = True
                elif choice == 2:
                    done = True

        dealer(hands, numPlayers, deck)
        win(hands, numPlayers, bet, moneys)
        for i in range(numPlayers):
            print("Player ", i + 1, "has", moneys[i])
        again = input("Would you like to play again, y or n: ")
        if again == "n":
            moneys = [0] * numPlayers
    print("Thanks For Playing")
