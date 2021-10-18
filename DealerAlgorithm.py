import CalculatingDSUM
import DealerHand
import random
import importlib
import sys
import PlayerBalance
cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']


def addplayerbalancenormal(bet):
    addbet1_file = open("PlayerBalance.py", 'w')
    addbet1_file.write(
        'balance = ' + '"' + str(float(bet) + float(PlayerBalance.balance)) + '"' + '\n'
        'player_name = ' + '"' + PlayerBalance.player_name + '"'
    )
    addbet1_file.close()


def addplayerbalanceblackjack(bet):
    addbet3_file = open('PlayerBalance.py', 'w')
    addbet3_file.write(
        'balance = ' + '"' + str(1.5 * float(bet) + float(PlayerBalance.balance)) + '"' + '\n'
        'player_name = ' + '"' + PlayerBalance.player_name + '"'
    )
    addbet3_file.close()


def minusplayerbalancenormal(bet):
    addbet1_file = open("PlayerBalance.py", 'w')
    addbet1_file.write(
        'balance = ' + '"' + str(float(PlayerBalance.balance) - float(bet)) + '"' + '\n'
        'player_name = ' + '"' + PlayerBalance.player_name + '"'
    )
    addbet1_file.close()


def hitdealer():
    if DealerHand.main_hand[2] in '""':
        dealer_hitting_file = open("DealerHand.py", "w")
        dealer_hitting_file.write(
            '\n' + 'main_hand = ["' + DealerHand.main_hand[0] + '", ' + '"' + DealerHand.main_hand[1] + '", ' + '"'
            + random.choice(cards) + '", ' + '"", ' + '""' + ']'
        )
        dealer_hitting_file.close()
        importlib.reload(DealerHand)
        print("The Dealer decided to Hit! The Dealer got " + DealerHand.main_hand[2] + '!')
    elif DealerHand.main_hand[3] in '""':
        dealer_hitting_file = open("DealerHand.py", "w")
        dealer_hitting_file.write(
            '\n' + 'main_hand = ["' + DealerHand.main_hand[0] + '", ' + '"' + DealerHand.main_hand[1] + '", ' + '"'
            + DealerHand.main_hand[2] + '", ' + '"' + random.choice(cards) + '", ' + '""' + ']'
        )
        dealer_hitting_file.close()
        importlib.reload(DealerHand)
        print("The Dealer decided to Hit! The Dealer got " + DealerHand.main_hand[3] + '!')
    elif DealerHand.main_hand[4] in '""':
        dealer_hitting_file = open("DealerHand.py", "w")
        dealer_hitting_file.write(
            '\n' + 'main_hand = ["' + DealerHand.main_hand[0] + '", ' + '"' + DealerHand.main_hand[1] + '", ' + '"'
            + DealerHand.main_hand[2] + '", ' + '"'
            + DealerHand.main_hand[3] + '", ' + '"' + random.choice(cards) + '"' + ']'
        )
        dealer_hitting_file.close()
        importlib.reload(DealerHand)
        print("The Dealer decided to Hit! The Dealer got " + DealerHand.main_hand[4] + '!')


def standdealer():
    print("The Dealer chose to stand!")


def dealeralg(player_name, bet):
    if CalculatingDSUM.calculationdsum1() >= 17:
        standdealer()
    elif CalculatingDSUM.calculationdsum1() < 17:
        hitdealer()
        if CalculatingDSUM.calculationdsum2() >= 17:
            if CalculatingDSUM.calculationdsum2() >= 22:
                print("The Dealer busts,so " + player_name + ' wins!')
                addplayerbalancenormal(bet)
                sys.exit()
            else:
                standdealer()
        elif CalculatingDSUM.calculationdsum2() < 17:
            hitdealer()
            if CalculatingDSUM.calculationdsum3() >= 17:
                if CalculatingDSUM.calculationdsum3() >= 22:
                    print("The Dealer busts,so " + player_name + ' wins!')
                    addplayerbalancenormal(bet)
                    sys.exit()
            else:
                standdealer()
        elif CalculatingDSUM.calculationdsum3() < 17:
                hitdealer()
                if CalculatingDSUM.calculationdsum4() >= 17:
                    if CalculatingDSUM.calculationdsum4() >= 22:
                        print("The Dealer busts,so " + player_name + ' wins!')
                        addplayerbalancenormal(bet)
                        sys.exit()
                else:
                    standdealer()
        elif CalculatingDSUM.calculationdsum4() < 17:
            hitdealer()
        else:
            print('--------------------------------------------------------------------------')















