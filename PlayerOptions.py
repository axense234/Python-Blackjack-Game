import importlib
import random
import PlayerHand
import DealerHand
import DealerAlgorithm
import CalculatingDSUM
import CalculatingPSUM
import sys
cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']


def hit(player_name):
    if PlayerHand.main_hand[2] in '""':
        player_hitting_file = open("PlayerHand.py", "w")
        player_hitting_file.write(
            '\n' + 'main_hand = ["' + PlayerHand.main_hand[0] + '", ' + '"' + PlayerHand.main_hand[1] + '", ' + '"'
            + random.choice(cards) + '", ' + '"", ' + '""' + ']' + '\n'
            + 'second_hand = [' + '"", ' + '"", ' + '"", ' + '"", ' + '""' + ']'
        )
        player_hitting_file.close()
        importlib.reload(PlayerHand)
        print(player_name + " decided to Hit! " + player_name + " got " + PlayerHand.main_hand[2] + '!')
    elif PlayerHand.main_hand[3] in '""':
        player_hitting_file = open("PlayerHand.py", "w")
        player_hitting_file.write(
            '\n' + 'main_hand = ["' + PlayerHand.main_hand[0] + '", ' + '"' + PlayerHand.main_hand[1] + '", ' + '"'
            + PlayerHand.main_hand[2] + '", ' + '"' + random.choice(cards) + '", ' + '""' + ']' + '\n'
            + 'second_hand = [' + '"", ' + '"", ' + '"", ' + '"", ' + '""' + ']'
        )
        player_hitting_file.close()
        importlib.reload(PlayerHand)
        print(player_name + " decided to Hit! " + player_name + " got " + PlayerHand.main_hand[3] + '!')
    elif PlayerHand.main_hand[4] in '""':
        player_hitting_file = open("PlayerHand.py", "w")
        player_hitting_file.write(
            '\n' + 'main_hand = ["' + PlayerHand.main_hand[0] + '", ' + '"' + PlayerHand.main_hand[1] + '", ' + '"'
            + PlayerHand.main_hand[2] + '", ' + '"'
            + PlayerHand.main_hand[3] + '", ' + '"' + random.choice(cards) + '"' + ']' + '\n'
            + 'second_hand = [' + '"", ' + '"", ' + '"", ' + '"", ' + '""' + ']'
        )
        player_hitting_file.close()
        importlib.reload(PlayerHand)
        print(player_name + " decided to Hit! " + player_name + " got " + PlayerHand.main_hand[4] + '!')


def stand(player_name):
    print(player_name + " chose to Stand!")



def split(player_name):
    player_splitting_file = open("PlayerHand.py", "w")
    player_splitting_file.write(
        '\n' + 'main_hand = ["' + PlayerHand.main_hand[0] + '", ' + '"", ' + '"", ' + '"", ' + '""' + ']' + '\n'
        + 'second_hand = ["' + PlayerHand.main_hand[0] + '", ' + '"", ' + '"", ' + '"", ' + '""' + ']'
    )
    player_splitting_file.close()
    importlib.reload(PlayerHand)
    print(player_name + " decided to Split! " + player_name
          + " got another hand,with the first card value of " + PlayerHand.main_hand[0] + "!")
    player_splitting_file = open('PlayerHand.py','w')
    player_splitting_file.write(
        '\n' + 'main_hand = ["' + PlayerHand.main_hand[0] + '", ' + '"' + random.choice(cards) + '", '
        + '"", ' + '"", ' + '""' + ']' + '\n'
        + 'second_hand = ["' + PlayerHand.main_hand[0] + '", ' + '"' + random.choice(cards) + '", ' + '"", '
        + '"", ' + '""' + ']'
    )
    player_splitting_file.close()
    importlib.reload(PlayerHand)
    print(
        player_name + ' drew on his first hand ' + PlayerHand.main_hand[1] + '!' + '\n'
        + player_name + ' drew on his second hand ' + PlayerHand.second_hand[1] + '!'
    )


def doubledown(player_name, bet):
    betdd = str(2 * float(bet))
    hit(player_name)
    if CalculatingPSUM.calculationsum2(player_name) >= 22:
        print(player_name + ' busted! The Dealer wins!')
        DealerAlgorithm.minusplayerbalancenormal(betdd)
        sys.exit()
    else:
        print("The Dealer revealed his card, it was " + DealerHand.main_hand[1] + '!')
        DealerAlgorithm.dealeralg(player_name, betdd)
        print("Round over! Let's see who won!")
        importlib.reload(PlayerHand)
        importlib.reload(DealerHand)
    if CalculatingPSUM.calculationsum2(player_name) > CalculatingDSUM.calculationdsum4():
        importlib.reload(PlayerHand)
        importlib.reload(DealerHand)
        print(
            "Player's sum " + str(CalculatingPSUM.calculationsum2(player_name)) + "!" + '\n' +
            "The Dealer's sum is " + str(CalculatingDSUM.calculationdsum4()) + "!" + '\n'
            + player_name + " has won!"
        )
        DealerAlgorithm.addplayerbalancenormal(betdd)
    elif CalculatingPSUM.calculationsum2(player_name) == CalculatingDSUM.calculationdsum4():
        importlib.reload(PlayerHand)
        importlib.reload(DealerHand)
        print(
            "Since Player's sum and The Dealer's sum are equal(" + str(
                CalculatingPSUM.calculationsum2(player_name)) + "), it's a tie!"
        )
    elif CalculatingPSUM.calculationsum2(player_name) < CalculatingDSUM.calculationdsum4():
        importlib.reload(PlayerHand)
        importlib.reload(DealerHand)
        print(
            "Player's sum is " + str(CalculatingPSUM.calculationsum2(player_name)) + "!" + '\n' +
            "The Dealer's sum is " + str(CalculatingDSUM.calculationdsum4()) + "!" + '\n'
            + "The Dealer has won!"
        )
        DealerAlgorithm.minusplayerbalancenormal(betdd)
    elif CalculatingPSUM.calculationsum2(player_name) > CalculatingDSUM.calculationdsum3():
        importlib.reload(PlayerHand)
        importlib.reload(DealerHand)
        print(
            "Player's sum is " + str(CalculatingPSUM.calculationsum2(player_name)) + "!" + '\n' +
            "The Dealer's sum is " + str(CalculatingDSUM.calculationdsum3()) + "!" + '\n'
            + player_name + " has won!"
        )
        DealerAlgorithm.addplayerbalancenormal(betdd)
    elif CalculatingPSUM.calculationsum2(player_name) == CalculatingDSUM.calculationdsum3():
        importlib.reload(PlayerHand)
        importlib.reload(DealerHand)
        print(
            "Since Player's sum and The Dealer's sum are equal(" + str(
                CalculatingPSUM.calculationsum2(player_name)) + "), it's a tie!"
        )
    elif CalculatingPSUM.calculationsum2(player_name) < CalculatingDSUM.calculationdsum3():
        importlib.reload(PlayerHand)
        importlib.reload(DealerHand)
        print(
            "Player's sum is " + str(CalculatingPSUM.calculationsum2(player_name)) + "!" + '\n' +
            "The Dealer's sum is " + str(CalculatingDSUM.calculationdsum3()) + "!" + '\n'
            + "The Dealer has won!"
        )
        DealerAlgorithm.minusplayerbalancenormal(betdd)
    elif CalculatingPSUM.calculationsum2(player_name) > CalculatingDSUM.calculationdsum2():
        importlib.reload(PlayerHand)
        importlib.reload(DealerHand)
        print(
            "Player's sum is " + str(CalculatingPSUM.calculationsum2(player_name)) + "!" + '\n' +
            "The Dealer's sum is " + str(CalculatingDSUM.calculationdsum2()) + "!" + '\n'
            + player_name + " has won!"
        )
        DealerAlgorithm.addplayerbalancenormal(betdd)
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
        DealerAlgorithm.minusplayerbalancenormal(betdd)