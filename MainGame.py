
import importlib
import random
import PlayerBalance
import PlayerHand
import PlayerOptions
import DealerHand
import CalculatingPSUM
import CalculatingDSUM
import sys
import DealerAlgorithm

# Introduction Start
print("Welcome to Blackjack!")
cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
if PlayerBalance.player_name.strip().lower() in "":
    player_name = input("What's your name? ")
    player_name_file = open("PlayerBalance.py", "w")
    player_name_file.write(
        'balance = ' + '"' + PlayerBalance.balance + '"' + '\n'
        'player_name = ' + '"' + player_name + '"'
    )
    player_name_file.close()
    importlib.reload(PlayerBalance)
    print("Here are the rules, " + player_name + ':')
    print(
        'You draw 2 cards,and the dealer also 2 but one of his is hidden!' + '\n'
        'If you get an Ace and a 10 value card,you get a Blackjack!'
        'If the dealer doesnt have one,you get 150% of your bet!' + '\n'
        'The Goal of the game is to get as close to 21 without going over 21!'
        'You can Hit for a card,Stand to pass the turn,'
        'Split to split your hand and Double Down to double the bet!' + '\n'
        'Your starting player balance is 100!' + '\n'
        'Good luck! You can play around to learn more rules/tips/tricks!'
    )
elif PlayerBalance.player_name.strip().lower() not in "":
    player_name = PlayerBalance.player_name
    print("Yo " + PlayerBalance.player_name + '!')
    print("Your current balance is " + PlayerBalance.balance + '!')
    po2 = input("Wanna visit the Shop? ")
    if po2.strip().lower() in 'yes':
        print("Welcome to the Shop,look around if you want!")
        print("Drugs: 10000 money")
        print("Food: 1000")
        print("Water: 500")
        po3 = input("Do you want to buy something? ")
        if po3.lower().strip() in 'yes':
            po4 = input('What do you want to buy? ')
            if po4.lower().strip() in 'drugs' and float(PlayerBalance.balance) >= 10000:
                print("Drugs bought! You feel kindaAaAaaaaaaaaaaaaAAaAa WIierwdddd!")
                DealerAlgorithm.minusplayerbalancenormal(10000)
                importlib.reload(PlayerBalance)
            elif po4.lower().strip() in 'food' and float(PlayerBalance.balance) >= 1000:
                print("Food bought! You feel full and find the hope to continue gambling!")
                DealerAlgorithm.minusplayerbalancenormal(1000)
                importlib.reload(PlayerBalance)
            elif po4.lower().strip() in 'water' and float(PlayerBalance.balance) >= 500:
                print("Water bought! It's extremely fresh...worth it!")
                DealerAlgorithm.minusplayerbalancenormal(500)
                importlib.reload(PlayerBalance)
        elif po3.lower().strip() in 'no':
            print("Ok!")
        else:
            print("Are you on drugs? Get outta here with your crazy speech!")
    elif po2.strip().lower() in "no":
        print('Ok!')
    else:
        print("Are you on drugs? What are you saying!!")
        sys.exit()
bet = input("How much money do you want to bet, " + player_name + "? ")
if float(bet) > float(PlayerBalance.balance):
    print("You can't bet that amount because you don't have that much!")
else:
    print("Blackjack round started!")
    player_draw_file = open('PlayerHand.py', 'w')
    # Drawing the first 2 cards for the player -START
    player_draw_file.write(
        '\n' + 'main_hand = ["' + random.choice(cards) + '", ' + '"' + random.choice(cards) + '", '
        + '"", ' + '"", ' + '""' + ']'
    )
    player_draw_file.close()
    importlib.reload(PlayerHand)
    # -END
    # Showing the cards to the player
    print("You got " + PlayerHand.main_hand[0] + ' and ' + PlayerHand.main_hand[1] + '!')
    CalculatingPSUM.calculationpsum1(player_name)
    print(player_name + ' has a sum of ' + str(CalculatingPSUM.calculationpsum1(player_name)) + '!')
    dealer_draw_file = open("DealerHand.py", "w")
    # Drawing the first 2 cards for the dealer,only showing one -START
    dealer_draw_file.write(
        '\n' + 'main_hand = ["' + random.choice(cards) + '", ' + '"' + random.choice(cards) + '", '
        + '"", ' + '"", ' + '""' + ']'
    )
    dealer_draw_file.close()
    importlib.reload(DealerHand)
    print("The Dealer got " + DealerHand.main_hand[0] + ',' + 'the other one is hidden!')
    if DealerHand.main_hand[0] in "Queen, King, Jack" and DealerHand.main_hand[1] in "Ace" and\
            CalculatingPSUM.calculationpsum1(player_name) == 21:
        print(player_name + ' got a Blackjack! The Dealer revealed his card,it was ' + DealerHand.main_hand[1] + '!')
        print('The Dealer also got a Blackjack! ' + player_name + ' loses! ')
        DealerAlgorithm.minusplayerbalancenormal(bet)
        sys.exit()
    elif DealerHand.main_hand[1] in "Queen, King, Jack" and DealerHand.main_hand[0] in "Ace" and\
            CalculatingPSUM.calculationpsum1(player_name) == 21:
        print(player_name + ' got a Blackjack! The Dealer revealed his card,it was ' + DealerHand.main_hand[1] + '!')
        print('The Dealer also got a Blackjack! ' + player_name + ' loses! ')
        DealerAlgorithm.minusplayerbalancenormal(bet)
        sys.exit()
    elif DealerHand.main_hand[0] in "10" and DealerHand.main_hand[1] in "Ace" and CalculatingPSUM.calculationpsum1(player_name) == 21:
        print(player_name + ' got a Blackjack! The Dealer revealed his card,it was ' + DealerHand.main_hand[1] + '!')
        print('The Dealer also got a Blackjack! ' + player_name + ' loses! ')
        DealerAlgorithm.minusplayerbalancenormal(bet)
        sys.exit()
    elif DealerHand.main_hand[1] in "10" and DealerHand.main_hand[0] in "Ace" and CalculatingPSUM.calculationpsum1(player_name) == 21:
        print(player_name + ' got a Blackjack! The Dealer revealed his card,it was ' + DealerHand.main_hand[1] + '!')
        print('The Dealer also got a Blackjack! ' + player_name + ' loses! ')
        DealerAlgorithm.minusplayerbalancenormal(bet)
        sys.exit()
    elif CalculatingPSUM.calculationpsum1(player_name) == 21 and CalculatingDSUM.calculationdsum1() != 21:
        print(player_name + ' got a Blackjack! The Dealer revealed his card,it was ' + DealerHand.main_hand[1] + '!')
        print("The Dealer doesn't have a Blackjack,so " + player_name + " wins!")
        DealerAlgorithm.addplayerbalanceblackjack(bet)
        sys.exit()
    player_option = input("What will you do, " + player_name + "? ")
    # Start of Player's actual turn,with choices
    if player_option.lower().strip() in "hit":
        PlayerOptions.hit(player_name)
        if CalculatingPSUM.calculationsum2(player_name) >= 22:
            print(player_name + ' busts! The Dealer wins!')
            DealerAlgorithm.minusplayerbalancenormal(bet)
            sys.exit()
        elif CalculatingPSUM.calculationsum2(player_name) == 21:
            print(player_name + ' has a sum of 21!')
        elif CalculatingPSUM.calculationsum2(player_name) <= 20:
            print(player_name + ' has a sum of ' + str(CalculatingPSUM.calculationsum2(player_name)))
            player_option = input("What will you do, " + player_name + "? ")
            if player_option.lower().strip() in "hit":
                PlayerOptions.hit(player_name)
                if CalculatingPSUM.calculationsum3(player_name) >= 22:
                    print(player_name + ' busts! The Dealer wins!')
                    DealerAlgorithm.minusplayerbalancenormal(bet)
                    sys.exit()
                elif CalculatingPSUM.calculationsum3(player_name) == 21:
                    print(player_name + ' has a sum of 21!')
                elif CalculatingPSUM.calculationsum3(player_name) < 21:
                    print(player_name + ' has a sum of ' + str(CalculatingPSUM.calculationsum3(player_name)))
                    player_option = input("What will you do, " + player_name + "? ")
                    if player_option.lower().strip() in "hit":
                        PlayerOptions.hit(player_name)
                        if CalculatingPSUM.calculationsum4(player_name) >= 22:
                            print(player_name + ' busts! The Dealer wins!')
                            DealerAlgorithm.minusplayerbalancenormal(bet)
                            sys.exit()
                        elif CalculatingPSUM.calculationsum4(player_name) == 21:
                            print(player_name + ' has a sum of 21!')
                        elif CalculatingPSUM.calculationsum4(player_name) <= 20:
                            print(player_name + ' has a sum of ' + str(CalculatingPSUM.calculationsum4(player_name)))
                            print('--------------------------------------------------------------------------')
                            sys.exit()
                    elif player_option.lower().strip() in 'stand':
                        PlayerOptions.stand(player_name)
            elif player_option.lower().strip() in 'stand':
                PlayerOptions.stand(player_name)
    elif player_option.lower().strip() in 'split' and PlayerHand.main_hand[0] == PlayerHand.main_hand[1]:
        PlayerOptions.split(player_name)
        print("The Dealer revealed his card, it was " + DealerHand.main_hand[1] + '!')
        DealerAlgorithm.dealeralg(player_name, bet)
        print("Round over! Let's see who won!")
        importlib.reload(PlayerHand)
        importlib.reload(DealerHand)
        if CalculatingPSUM.calculationpsum1s(player_name) > CalculatingDSUM.calculationdsum4():
            importlib.reload(PlayerHand)
            importlib.reload(DealerHand)
            print(
                "Player's sum for the first hand is " + str(CalculatingPSUM.calculationpsum1s(player_name)) + "!" + '\n' +
                "The Dealer's sum is " + str(CalculatingDSUM.calculationdsum4()) + "!" + '\n'
                + player_name + " has won!"
            )
            DealerAlgorithm.addplayerbalancenormal(bet)
        elif CalculatingPSUM.calculationsum4(player_name) == CalculatingDSUM.calculationdsum4():
            importlib.reload(PlayerHand)
            importlib.reload(DealerHand)
            print(
                "Since Player's first hand's sum and The Dealer's sum are equal(" + str(
                    CalculatingPSUM.calculationpsum1s(player_name)) + "), it's a tie!"
            )
        elif CalculatingPSUM.calculationpsum1s(player_name) < CalculatingDSUM.calculationdsum4():
            importlib.reload(PlayerHand)
            importlib.reload(DealerHand)
            print(
                "Player's sum for the first hand is " + str(CalculatingPSUM.calculationpsum1s(player_name)) + "!" + '\n' +
                "The Dealer's sum is " + str(CalculatingDSUM.calculationdsum4()) + "!" + '\n'
                + "The Dealer has won!"
            )
            DealerAlgorithm.minusplayerbalancenormal(bet)
        elif CalculatingPSUM.calculationpsum1s(player_name) > CalculatingDSUM.calculationdsum3():
            importlib.reload(PlayerHand)
            importlib.reload(DealerHand)
            print(
                "Player's sum for the first hand is " + str(CalculatingPSUM.calculationpsum1s(player_name)) + "!" + '\n' +
                "The Dealer's sum is " + str(CalculatingDSUM.calculationdsum3()) + "!" + '\n'
                + player_name + " has won!"
            )
            DealerAlgorithm.addplayerbalancenormal(bet)
        elif CalculatingPSUM.calculationpsum1s(player_name) == CalculatingDSUM.calculationdsum3():
            importlib.reload(PlayerHand)
            importlib.reload(DealerHand)
            print(
                "Since Player's first hand's sum and The Dealer's sum are equal(" + str(
                    CalculatingPSUM.calculationpsum1s(player_name)) + "), it's a tie!"
            )
        elif CalculatingPSUM.calculationpsum1s(player_name) < CalculatingDSUM.calculationdsum3():
            importlib.reload(PlayerHand)
            importlib.reload(DealerHand)
            print(
                "Player's sum for the first hand is " + str(CalculatingPSUM.calculationpsum1s(player_name)) + "!" + '\n' +
                "The Dealer's sum is " + str(CalculatingDSUM.calculationdsum3()) + "!" + '\n'
                + "The Dealer has won!"
            )
            DealerAlgorithm.minusplayerbalancenormal(bet)
        elif CalculatingPSUM.calculationpsum1s(player_name) > CalculatingDSUM.calculationdsum2():
            importlib.reload(PlayerHand)
            importlib.reload(DealerHand)
            print(
                "Player's sum for the first hand is " + str(CalculatingPSUM.calculationpsum1s(player_name)) + "!" + '\n' +
                "The Dealer's sum is " + str(CalculatingDSUM.calculationdsum2()) + "!" + '\n'
                + player_name + " has won!"
            )
            DealerAlgorithm.addplayerbalancenormal(bet)
        elif CalculatingPSUM.calculationpsum1s(player_name) == CalculatingDSUM.calculationdsum2():
            importlib.reload(PlayerHand)
            importlib.reload(DealerHand)
            print(
                "Since Player's first hand's sum and The Dealer's sum are equal(" + str(
                    CalculatingPSUM.calculationpsum1s(player_name)) + "), it's a tie!"
            )
        elif CalculatingPSUM.calculationpsum1s(player_name) < CalculatingDSUM.calculationdsum2():
            importlib.reload(PlayerHand)
            importlib.reload(DealerHand)
            print(
                "Player's sum for the first hand is " + str(CalculatingPSUM.calculationpsum1s(player_name)) + "!" + '\n' +
                "The Dealer's sum is " + str(CalculatingDSUM.calculationdsum2()) + "!" + '\n'
                + "The Dealer has won!"
            )
            DealerAlgorithm.minusplayerbalancenormal(bet)
        if CalculatingPSUM.calculationsum4(player_name) > CalculatingDSUM.calculationdsum4():
            importlib.reload(PlayerHand)
            importlib.reload(DealerHand)
            print(
                "Player's sum for the second hand is  " + str(CalculatingPSUM.calculationsum4(player_name)) + "!" + '\n' +
                "The Dealer's sum is " + str(CalculatingDSUM.calculationdsum4()) + "!" + '\n'
                + player_name + " has won!"
            )
            DealerAlgorithm.addplayerbalancenormal(bet)
            sys.exit()
        elif CalculatingPSUM.calculationsum4(player_name) == CalculatingDSUM.calculationdsum4():
            importlib.reload(PlayerHand)
            importlib.reload(DealerHand)
            print(
                "Since Player's second hand's sum and The Dealer's sum are equal(" + str(
                    CalculatingPSUM.calculationsum4(player_name)) + "), it's a tie!"
            )
            sys.exit()
        elif CalculatingPSUM.calculationsum4(player_name) < CalculatingDSUM.calculationdsum4():
            importlib.reload(PlayerHand)
            importlib.reload(DealerHand)
            print(
                "Player's sum for the second hand is " + str(CalculatingPSUM.calculationsum4(player_name)) + "!" + '\n' +
                "The Dealer's sum is " + str(CalculatingDSUM.calculationdsum4()) + "!" + '\n'
                + "The Dealer has won!"
            )
            DealerAlgorithm.minusplayerbalancenormal(bet)
            sys.exit()
        elif CalculatingPSUM.calculationsum3(player_name) > CalculatingDSUM.calculationdsum3():
            importlib.reload(PlayerHand)
            importlib.reload(DealerHand)
            print(
                "Player's sum for the second hand is " + str(CalculatingPSUM.calculationsum3(player_name)) + "!" + '\n' +
                "The Dealer's sum is " + str(CalculatingDSUM.calculationdsum3()) + "!" + '\n'
                + player_name + " has won!"
            )
            DealerAlgorithm.addplayerbalancenormal(bet)
            sys.exit()
        elif CalculatingPSUM.calculationsum3(player_name) == CalculatingDSUM.calculationdsum3():
            importlib.reload(PlayerHand)
            importlib.reload(DealerHand)
            print(
                "Since Player's second hand's sum and The Dealer's sum are equal(" + str(
                    CalculatingPSUM.calculationsum3(player_name)) + "), it's a tie!"
            )
            sys.exit()
        elif CalculatingPSUM.calculationsum3(player_name) < CalculatingDSUM.calculationdsum3():
            importlib.reload(PlayerHand)
            importlib.reload(DealerHand)
            print(
                "Player's sum for the second hand is " + str(CalculatingPSUM.calculationsum3(player_name)) + "!" + '\n' +
                "The Dealer's sum is " + str(CalculatingDSUM.calculationdsum3()) + "!" + '\n'
                + "The Dealer has won!"
            )
            DealerAlgorithm.minusplayerbalancenormal(bet)
            sys.exit()
        elif CalculatingPSUM.calculationsum2(player_name) > CalculatingDSUM.calculationdsum2():
            importlib.reload(PlayerHand)
            importlib.reload(DealerHand)
            print(
                "Player's sum for the second hand is " + str(CalculatingPSUM.calculationsum2(player_name)) + "!" + '\n' +
                "The Dealer's sum is " + str(CalculatingDSUM.calculationdsum2()) + "!" + '\n'
                + player_name + " has won!"
            )
            DealerAlgorithm.addplayerbalancenormal(bet)
            sys.exit()
        elif CalculatingPSUM.calculationsum2(player_name) == CalculatingDSUM.calculationdsum2():
            importlib.reload(PlayerHand)
            importlib.reload(DealerHand)
            print(
                "Since Player's second hand's sum and The Dealer's sum are equal(" + str(
                    CalculatingPSUM.calculationsum2(player_name)) + "), it's a tie!"
            )
            sys.exit()
        elif CalculatingPSUM.calculationsum2(player_name) < CalculatingDSUM.calculationdsum2():
            importlib.reload(PlayerHand)
            importlib.reload(DealerHand)
            print(
                "Player's sum for the second hand is " + str(CalculatingPSUM.calculationsum2(player_name)) + "!" + '\n' +
                "The Dealer's sum is " + str(CalculatingDSUM.calculationdsum2()) + "!" + '\n'
                + "The Dealer has won!"
            )
            DealerAlgorithm.minusplayerbalancenormal(bet)
            sys.exit()
    elif player_option.lower().strip() in 'stand':
        PlayerOptions.stand(player_name)
    elif player_option.lower().strip() in 'doubledown':
        PlayerOptions.doubledown(player_name, bet)
        sys.exit()
    else:
        sys.exit()
    # End of player's turn,with choices
    # Start of final battle
    print("The Dealer revealed his card, it was " + DealerHand.main_hand[1] + '!')
    DealerAlgorithm.dealeralg(player_name, bet)
    print("Round over! Let's see who won!")
    importlib.reload(PlayerHand)
    importlib.reload(DealerHand)
    if CalculatingPSUM.calculationsum4(player_name) > CalculatingDSUM.calculationdsum4():
        importlib.reload(PlayerHand)
        importlib.reload(DealerHand)
        print(
            "Player's sum " + str(CalculatingPSUM.calculationsum4(player_name)) + "!" + '\n' +
            "The Dealer's sum is " + str(CalculatingDSUM.calculationdsum4()) + "!" + '\n'
            + player_name + " has won!"
        )
        DealerAlgorithm.addplayerbalancenormal(bet)
    elif CalculatingPSUM.calculationsum4(player_name) == CalculatingDSUM.calculationdsum4():
        importlib.reload(PlayerHand)
        importlib.reload(DealerHand)
        print(
            "Since Player's sum and The Dealer's sum are equal(" + str(
                CalculatingPSUM.calculationsum4(player_name)) + "), it's a tie!"
        )
    elif CalculatingPSUM.calculationsum4(player_name) < CalculatingDSUM.calculationdsum4():
        importlib.reload(PlayerHand)
        importlib.reload(DealerHand)
        print(
            "Player's sum is " + str(CalculatingPSUM.calculationsum4(player_name)) + "!" + '\n' +
            "The Dealer's sum is " + str(CalculatingDSUM.calculationdsum4()) + "!" + '\n'
            + "The Dealer has won!"
        )
        DealerAlgorithm.minusplayerbalancenormal(bet)
    elif CalculatingPSUM.calculationsum3(player_name) > CalculatingDSUM.calculationdsum3():
        importlib.reload(PlayerHand)
        importlib.reload(DealerHand)
        print(
            "Player's sum is " + str(CalculatingPSUM.calculationsum3(player_name)) + "!" + '\n' +
            "The Dealer's sum is " + str(CalculatingDSUM.calculationdsum3()) + "!" + '\n'
            + player_name + " has won!"
        )
        DealerAlgorithm.addplayerbalancenormal(bet)
    elif CalculatingPSUM.calculationsum3(player_name) == CalculatingDSUM.calculationdsum3():
        importlib.reload(PlayerHand)
        importlib.reload(DealerHand)
        print(
            "Since Player's sum and The Dealer's sum are equal(" + str(
                CalculatingPSUM.calculationsum3(player_name)) + "), it's a tie!"
        )
    elif CalculatingPSUM.calculationsum3(player_name) < CalculatingDSUM.calculationdsum3():
        importlib.reload(PlayerHand)
        importlib.reload(DealerHand)
        print(
            "Player's sum is " + str(CalculatingPSUM.calculationsum3(player_name)) + "!" + '\n' +
            "The Dealer's sum is " + str(CalculatingDSUM.calculationdsum3()) + "!" + '\n'
            + "The Dealer has won!"
        )
        DealerAlgorithm.minusplayerbalancenormal(bet)
    elif CalculatingPSUM.calculationsum2(player_name) > CalculatingDSUM.calculationdsum2():
        importlib.reload(PlayerHand)
        importlib.reload(DealerHand)
        print(
            "Player's sum is " + str(CalculatingPSUM.calculationsum2(player_name)) + "!" + '\n' +
            "The Dealer's sum is " + str(CalculatingDSUM.calculationdsum2()) + "!" + '\n'
            + player_name + " has won!"
        )
        DealerAlgorithm.addplayerbalancenormal(bet)
    elif CalculatingPSUM.calculationsum2(player_name) == CalculatingDSUM.calculationdsum2():
        importlib.reload(PlayerHand)
        importlib.reload(DealerHand)
        print(
            "Since Player's sum and The Dealer's sum are equal(" + str(
                CalculatingPSUM.calculationsum2(player_name)) + "), it's a tie!"
        )
    elif CalculatingPSUM.calculationsum2(player_name) < CalculatingDSUM.calculationdsum2():
        importlib.reload(PlayerHand)
        importlib.reload(DealerHand)
        print(
            "Player's sum is " + str(CalculatingPSUM.calculationsum2(player_name)) + "!" + '\n' +
            "The Dealer's sum is " + str(CalculatingDSUM.calculationdsum2()) + "!" + '\n'
            + "The Dealer has won!"
        )
        DealerAlgorithm.minusplayerbalancenormal(bet)
    # End of final battle
