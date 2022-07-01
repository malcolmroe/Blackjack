import random

from numpy import not_equal
Account_Value = 100
print("Your Starting Account Balance is 100.")
while Account_Value > 0:
    deck1 = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8,
             9, 9, 9, 9, 10, 10, 10, 10, "J", "J", "J", "J", "Q", "Q", "Q", "Q", "K", "K", "K", "K", "A", "A", "A", "A"]
    deck2 = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8,
             9, 9, 9, 9, 10, 10, 10, 10, "J", "J", "J", "J", "Q", "Q", "Q", "Q", "K", "K", "K", "K", "A", "A", "A", "A"]
    deck3 = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8,
             9, 9, 9, 9, 10, 10, 10, 10, "J", "J", "J", "J", "Q", "Q", "Q", "Q", "K", "K", "K", "K", "A", "A", "A", "A"]
    deck4 = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8,
             9, 9, 9, 9, 10, 10, 10, 10, "J", "J", "J", "J", "Q", "Q", "Q", "Q", "K", "K", "K", "K", "A", "A", "A", "A"]
    random.shuffle(deck1)
    random.shuffle(deck2)
    random.shuffle(deck3)
    random.shuffle(deck4)
    deck = deck1 + deck2 + deck3 + deck4
    print(" ")
    Wager = input("Enter Your Wager: ")
    a = Wager.isnumeric()
    while a == False:
        print("Please Enter a Number.")
        Wager = input("Enter Your Wager: ")
        a = Wager.isnumeric()
    while int(Wager) > Account_Value:
        print("Wager larger than Account Value. Please enter another amount.")
        Wager = input("Enter Your Wager: ")
    print(" ")
    print("...........Dealing Cards...........")
    print(" ")

    Account_Value = Account_Value - int(Wager)

    player_hand = []
    dealer_hand = []
    player_hand_total = 0
    dealer_hand_total = 0
    Blackjack = False

    player_card1 = deck[0]
    player_hand.append(player_card1)
    del deck[0]
    if player_hand[0] == "J":
        player_hand_total = 10
    elif player_hand[0] == "Q":
        player_hand_total = 10
    elif player_hand[0] == "K":
        player_hand_total = 10
    elif player_hand[0] == "A":
        player_hand_total = 11
    else:
        player_hand_total = player_hand[0]

    dealer_card1 = deck[0]
    dealer_hand.append(dealer_card1)
    del deck[0]
    if dealer_hand[0] == "J":
        dealer_hand_total = 10
    elif dealer_hand[0] == "Q":
        dealer_hand_total = 10
    elif dealer_hand[0] == "K":
        dealer_hand_total = 10
    elif dealer_hand[0] == "A":
        dealer_hand_total = 11
    else:
        dealer_hand_total = dealer_hand[0]

    player_card2 = deck[0]
    player_hand.append(player_card2)
    del deck[0]
    if player_hand[1] == "J":
        player_hand_total = player_hand_total + 10
    elif player_hand[1] == "Q":
        player_hand_total = player_hand_total + 10
    elif player_hand[1] == "K":
        player_hand_total = player_hand_total + 10
    elif player_hand[1] == "A":
        player_hand_total = player_hand_total + 11
    else:
        player_hand_total = player_hand_total + player_hand[1]

    dealer_card2 = deck[0]
    dealer_hand.append(dealer_card2)
    del deck[0]
    if dealer_hand[1] == "J":
        dealer_hand_total = dealer_hand_total + 10
    elif dealer_hand[1] == "Q":
        dealer_hand_total = dealer_hand_total + 10
    elif dealer_hand[1] == "K":
        dealer_hand_total = dealer_hand_total + 10
    elif dealer_hand[1] == "A":
        dealer_hand_total = dealer_hand_total + 11
    else:
        dealer_hand_total = dealer_hand_total + dealer_hand[1]

    print("----------------------------------------")
    print("Dealer Hand: Unknown,", dealer_hand[1])
    print("Total: Unknown")
    print("----------------------------------------")
    print("Your Hand: ", player_hand)
    print("Total: ", player_hand_total)
    print("----------------------------------------")
    while Blackjack == False:
        player_below_21 = True
        dealer_below_21 = True
        if player_hand_total == 21:
            Blackjack == True
            if dealer_hand_total == 21:
                print("Push")
                Account_Value = Account_Value + int(Wager)
                print("You're Account Balance is: ", Account_Value)
                print("----------------------------------------")
            print("BLACKJACK!")
            player_below_21 = False
            Account_Value = Account_Value + int(Wager)*3
            print("Dealer: ", dealer_hand, dealer_hand_total)
            print("Your Hand: ", player_hand, player_hand_total)
            print("----------------------------------------")
            print("You Win!")
            print("You're Account Balance is: ", Account_Value)
            print("----------------------------------------")
            break
        print("Would You Like to: ")
        print(" - Hit (Enter 'H')")
        print(" - Stay (Enter 'S')")
        status = input("     >  ")
        print("----------------------------------------")
        while status.upper() == "H":
            if player_hand_total > 21:
                player_below_21 = False
            while player_below_21:
                if status.upper() == "H":
                    player_card3 = deck[0]
                    player_hand.append(deck[0])
                    del deck[0]
                    if player_hand[-1] == "J":
                        player_hand_total = player_hand_total + 10
                    elif player_hand[-1] == "Q":
                        player_hand_total = player_hand_total + 10
                    elif player_hand[-1] == "K":
                        player_hand_total = player_hand_total + 10
                    elif player_hand[-1] == "A":
                        player_hand_total = player_hand_total + 11
                    else:
                        player_hand_total = player_hand_total + player_hand[-1]
                if player_hand_total > 21:
                    player_below_21 = False
                    status = "S"
                    print("Busted!")
                    print("Dealer: ", dealer_hand, dealer_hand_total)
                    print("Your Hand: ", player_hand, player_hand_total)
                    print("----------------------------------------")
                    print("Dealer Wins.")
                    print("You're Account Balance is: ", Account_Value)
                    print("----------------------------------------")
                if status.upper() == "S":
                    break
                print(player_hand, player_hand_total)
                print("----------------------------------------")
                print("Would You Like to: ")
                print(" - Hit (Enter 'H')")
                print(" - Stay (Enter 'S')")
                status = input("     >  ")
                print("----------------------------------------")
                print(player_hand, player_hand_total)

        if player_below_21 == True:
            if status == "S":
                while dealer_hand_total < 17:
                    dealer_hand.append(deck[0])
                    del deck[0]
                    if dealer_hand[-1] == "J":
                        dealer_hand_total = dealer_hand_total + 10
                    elif dealer_hand[-1] == "Q":
                        dealer_hand_total = dealer_hand_total + 10
                    elif dealer_hand[-1] == "K":
                        dealer_hand_total = dealer_hand_total + 10
                    elif dealer_hand[-1] == "A":
                        dealer_hand_total = dealer_hand_total + 11
                    else:
                        dealer_hand_total = dealer_hand_total + dealer_hand[-1]
                    if dealer_hand_total > 21:
                        dealer_below_21 = False
                print(" ")

        if player_below_21:
            if player_hand_total > dealer_hand_total:
                Account_Value = Account_Value + int(Wager)*2
                print("Dealer: ", dealer_hand, dealer_hand_total)
                print("Your Hand: ", player_hand, player_hand_total)
                print("----------------------------------------")
                print("You Win!")
                print("You're Account Balance is: ", Account_Value)
                print("----------------------------------------")

        if dealer_below_21 == False:
            if dealer_hand_total == 21:
                if player_hand_total == 21:
                    print("Push")
                    Account_Value = Account_Value + int(Wager)
                    print("You're Account Balance is: ", Account_Value)
                    print("----------------------------------------")
                print("Dealer: ", dealer_hand, dealer_hand_total)
                print("Your Hand: ", player_hand, player_hand_total)
                print("----------------------------------------")
                print("Dealer Wins.")
                print("You're Account Balance is: ", Account_Value)
                print("----------------------------------------")
            elif dealer_hand_total > player_hand_total:
                print("Dealer: ", dealer_hand, dealer_hand_total)
                print("Your Hand: ", player_hand, player_hand_total)
                Account_Value = Account_Value + int(Wager)*2
                print("----------------------------------------")
                print("Dealer Busts, You Win!")
                print("You're Account Balance is: ", Account_Value)
                print("----------------------------------------")
        if player_below_21:
            if dealer_below_21:
                if dealer_hand_total > player_hand_total:
                    print("Dealer: ", dealer_hand, dealer_hand_total)
                    print("Your Hand: ", player_hand, player_hand_total)
                    print("----------------------------------------")
                    print("Dealer Wins.")
                    print("You're Account Balance is: ", Account_Value)
                    print("----------------------------------------")

        if dealer_hand_total == player_hand_total:
            print("Dealer: ", dealer_hand, dealer_hand_total)
            print("Your Hand: ", player_hand, player_hand_total)
            print("----------------------------------------")
            print("Push")
            Account_Value = Account_Value + int(Wager)
            print("You're Account Balance is: ", Account_Value)
            print("----------------------------------------")
        break

    if Account_Value > 0:
        print(" ")
        print("Next Hand: ")
        print("----------------------------------------")
    if Account_Value <= 0:
        print("Bank Account Empty :(. Better Luck Next Time!")
