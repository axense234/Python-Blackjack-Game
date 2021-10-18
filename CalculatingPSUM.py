import PlayerHand


def calculationpsum1(player_name):
    if PlayerHand.main_hand[0] in "Jack, Queen, King" and not PlayerHand.main_hand[1] in "Jack, Queen, King, Ace":
        player_sum = 10 + int(PlayerHand.main_hand[1])
    elif PlayerHand.main_hand[1] in "Jack, Queen, King" and not PlayerHand.main_hand[0] in "Jack, Queen, King, Ace":
        player_sum = int(PlayerHand.main_hand[0]) + 10
    elif PlayerHand.main_hand[0] in "Jack, Queen, King" and PlayerHand.main_hand[1] in "Jack, Queen, King":
        player_sum = 10 + 10
    elif PlayerHand.main_hand[0] in "Ace" and not PlayerHand.main_hand[1] in "Ace, Queen, King, Jack":
        player_sum = 11 + int(PlayerHand.main_hand[1])
    elif PlayerHand.main_hand[1] in "Ace" and not PlayerHand.main_hand[0] in "Ace, Queen, King, Jack":
        player_sum = int(PlayerHand.main_hand[0]) + 11
    elif PlayerHand.main_hand[0] in "Ace" and PlayerHand.main_hand[1] in "Ace":
        player_sum = 11 + 1
    elif PlayerHand.main_hand[0] in "Ace" and PlayerHand.main_hand[1] in "10":
        player_sum = 11 + 10
    elif PlayerHand.main_hand[1] in "Ace" and PlayerHand.main_hand[0] in "10":
        player_sum = 10 + 11
    elif PlayerHand.main_hand[0] in "Ace" and PlayerHand.main_hand[1] in "10":
        player_sum = 10 + 11
    elif PlayerHand.main_hand[0] in "Ace" and PlayerHand.main_hand[1] in "Jack, Queen, King":
        player_sum = 11 + 10
    elif PlayerHand.main_hand[1] in "Ace" and PlayerHand.main_hand[0] in "Jack, Queen, King":
        player_sum = 10 + 11
    elif PlayerHand.main_hand[0] in "2, 3, 4, 5, 6, 7, 8, 9, 10" and PlayerHand.main_hand[1] not in "Ace, King, Queen, Jack":
        player_sum = int(PlayerHand.main_hand[0]) + int(PlayerHand.main_hand[1])
    elif PlayerHand.main_hand[0] in "2, 3, 4, 5, 6, 7, 8, 9, 10" and PlayerHand.main_hand[1] in "Ace":
        player_sum = int(PlayerHand.main_hand[0]) + 11
    elif PlayerHand.main_hand[0] in "Jack, Queen, King" and PlayerHand.main_hand[1] in "Ace":
        player_sum = 10 + 11
    return player_sum


def calculationsum2(player_name):
    # This is the case for the third card,if the player didn't bust or win,the program continues for the other cases
    if PlayerHand.main_hand[2] in '""':
        player_total_sum = calculationpsum1(player_name)
    elif PlayerHand.main_hand[2] not in '""':
        if PlayerHand.main_hand[2] in '2, 3, 4, 5, 6, 7, 8, 9, 10':
            player_total_sum = calculationpsum1(player_name) + int(PlayerHand.main_hand[2])
        elif PlayerHand.main_hand[2] in 'Jack, King, Queen':
            player_total_sum = calculationpsum1(player_name) + 10
        elif PlayerHand.main_hand[2] in 'Ace':
            if calculationpsum1(player_name) >= 11:
                player_total_sum = calculationpsum1(player_name) + 1
            elif calculationpsum1(player_name) < 11:
                player_total_sum = calculationpsum1(player_name) + 11
    return player_total_sum


def calculationsum3(player_name):
    # This is the case for the fourth card,if the player didn't bust or win,the program continues for the other cases
    if PlayerHand.main_hand[3] in '""':
        player_total_sum2 = calculationsum2(player_name)
    elif PlayerHand.main_hand[3] not in '""':
        if PlayerHand.main_hand[3] in '2, 3, 4, 5, 6, 7, 8, 9, 10':
            player_total_sum2 = calculationsum2(player_name) + int(PlayerHand.main_hand[3])
        elif PlayerHand.main_hand[3] in 'Jack, King, Queen':
            player_total_sum2 = calculationsum2(player_name) + 10
        elif PlayerHand.main_hand[3] in 'Ace':
            if calculationsum2(player_name) >= 11:
                player_total_sum2 = calculationsum2(player_name) + 1
            elif calculationsum2(player_name) < 11:
                player_total_sum2 = calculationsum2(player_name) + 11
    return player_total_sum2


def calculationsum4(player_name):
    # This is the case for the fifth card,if the player didn't bust or win,the program continues for the other cases
    if PlayerHand.main_hand[4] in '""':
        player_total_sum3 = calculationsum3(player_name)
    elif PlayerHand.main_hand[4] not in '""':
        if PlayerHand.main_hand[4] in '2, 3, 4, 5, 6, 7, 8, 9, 10':
            player_total_sum3 = calculationsum3(player_name) + int(PlayerHand.main_hand[4])
        elif PlayerHand.main_hand[4] in 'Jack, King, Queen':
            player_total_sum3 = calculationsum3(player_name) + 10
        elif PlayerHand.main_hand[4] in 'Ace':
            if calculationsum3(player_name) >= 11:
                player_total_sum3 = calculationsum3(player_name) + 1
            elif calculationsum3(player_name) < 11:
                player_total_sum3 = calculationsum3(player_name) + 11
    return player_total_sum3


def calculationpsum1s(player_name):
    if PlayerHand.second_hand[0] in "Jack, Queen, King" and not PlayerHand.second_hand[1] in "Jack, Queen, King, Ace":
        player_sum1 = 10 + int(PlayerHand.second_hand[1])
    elif PlayerHand.second_hand[1] in "Jack, Queen, King" and not PlayerHand.second_hand[0] in "Jack, Queen, King, Ace":
        player_sum1 = int(PlayerHand.second_hand[0]) + 10
    elif PlayerHand.second_hand[0] in "Jack, Queen, King" and PlayerHand.second_hand[1] in "Jack, Queen, King":
        player_sum1 = 10 + 10
    elif PlayerHand.second_hand[0] in "Ace" and not PlayerHand.second_hand[1] in "Ace, Queen, King, Jack":
        player_sum1 = 11 + int(PlayerHand.second_hand[1])
    elif PlayerHand.second_hand[1] in "Ace" and not PlayerHand.second_hand[0] in "Ace, Queen, King, Jack":
        player_sum1 = int(PlayerHand.main_hand[0]) + 11
    elif PlayerHand.second_hand[0] in "Ace" and PlayerHand.second_hand[1] in "Ace":
        player_sum1 = 11 + 1
    elif PlayerHand.second_hand[0] in "Ace" and PlayerHand.second_hand[1] in "10":
        player_sum1 = 11 + 10
    elif PlayerHand.second_hand[1] in "Ace" and PlayerHand.second_hand[0] in "10":
        player_sum1 = 10 + 11
    elif PlayerHand.second_hand[0] in "Ace" and PlayerHand.second_hand[1] in "10":
        player_sum1 = 10 + 11
    elif PlayerHand.second_hand[0] in "Ace" and PlayerHand.second_hand[1] in "Jack, Queen, King":
        player_sum1 = 11 + 10
    elif PlayerHand.second_hand[1] in "Ace" and PlayerHand.second_hand[0] in "Jack, Queen, King":
        player_sum1 = 10 + 11
    elif PlayerHand.second_hand[0] in "2, 3, 4, 5, 6, 7, 8, 9, 10" and PlayerHand.second_hand[1] in "2, 3, 4, 5, 6, 7, 8, 9, 10":
        player_sum1 = int(PlayerHand.main_hand[0]) + int(PlayerHand.main_hand[1])
    elif PlayerHand.second_hand[0] in "2, 3, 4, 5, 6, 7, 8, 9, 10" and PlayerHand.second_hand[1] in "Ace":
        player_sum1 = int(PlayerHand.main_hand[0]) + 11
    elif PlayerHand.second_hand[0] in "Jack, Queen, King" and PlayerHand.second_hand[1] in "Ace":
        player_sum1 = 10 + 11
    return player_sum1