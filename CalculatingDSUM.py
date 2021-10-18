import DealerHand


def calculationdsum1():
    if DealerHand.main_hand[0] in "Jack, Queen, King" and not DealerHand.main_hand[1] in "Jack, Queen, King, Ace":
        dealer_sum = 10 + int(DealerHand.main_hand[1])
    elif DealerHand.main_hand[1] in "Jack, Queen, King" and not DealerHand.main_hand[0] in "Jack, Queen, King, Ace":
        dealer_sum = int(DealerHand.main_hand[0]) + 10
    elif DealerHand.main_hand[0] in "Jack, Queen, King" and DealerHand.main_hand[1] in "Jack, Queen, King, Ace":
        dealer_sum = 10 + 10
    elif DealerHand.main_hand[0] in "Ace" and not DealerHand.main_hand[1] in "Ace, Queen, King, Jack":
        dealer_sum = 11 + int(DealerHand.main_hand[1])
    elif DealerHand.main_hand[1] in "Ace" and not DealerHand.main_hand[0] in "Ace, Queen, King, Jack":
        dealer_sum = int(DealerHand.main_hand[0]) + 11
    elif DealerHand.main_hand[0] in "Ace" and DealerHand.main_hand[1] in "Ace":
        dealer_sum = 11 + 1
    elif DealerHand.main_hand[0] in "Ace" and DealerHand.main_hand[1] in "10":
        dealer_sum = 11 + 10
    elif DealerHand.main_hand[1] in "Ace" and DealerHand.main_hand[0] in "10":
        dealer_sum = 10 + 11
    elif DealerHand.main_hand[0] in "Ace" and DealerHand.main_hand[1] in "10":
        dealer_sum = 10 + 11
    elif DealerHand.main_hand[0] in "Ace" and DealerHand.main_hand[1] in "Jack, Queen, King":
        dealer_sum = 11 + 10
    elif DealerHand.main_hand[1] in "Ace" and DealerHand.main_hand[0] in "Jack, Queen, King":
        dealer_sum = 10 + 11
    elif DealerHand.main_hand[0] in "2, 3, 4, 5, 6, 7, 8, 9, 10" and DealerHand.main_hand[1] not in "Ace, King, Queen, Jack":
        dealer_sum = int(DealerHand.main_hand[0]) + int(DealerHand.main_hand[1])
    elif DealerHand.main_hand[0] in "2, 3, 4, 5, 6, 7, 8, 9, 10" and DealerHand.main_hand[1] in "Ace":
        dealer_sum = int(DealerHand.main_hand[0]) + 11
    elif DealerHand.main_hand[0] in "Jack, Queen, King" and DealerHand.main_hand[1] in "Ace":
        dealer_sum = 10 + 11
    return dealer_sum


def calculationdsum2():
    # This is the case for the third card,if the dealer didn't bust or win,the program continues for the other cases
    if DealerHand.main_hand[2] in '""':
        dealer_total_sum = calculationdsum1()
    elif DealerHand.main_hand[2] not in '""':
        if DealerHand.main_hand[2] in '2, 3, 4, 5, 6, 7, 8, 9, 10':
            dealer_total_sum = calculationdsum1() + int(DealerHand.main_hand[2])
        elif DealerHand.main_hand[2] in 'Jack, King, Queen':
            dealer_total_sum = calculationdsum1() + 10
        elif DealerHand.main_hand[2] in 'Ace':
            if calculationdsum1() >= 11:
                dealer_total_sum = calculationdsum1() + 1
            elif calculationdsum1() < 11:
                dealer_total_sum = calculationdsum1() + 11
    return dealer_total_sum


def calculationdsum3():
    # This is the case for the fourth card,if the dealer didn't bust or win,the program continues for the other cases
    if DealerHand.main_hand[3] in '""':
        dealer_total_sum2 = calculationdsum2()
    elif DealerHand.main_hand[3] not in '""':
        if DealerHand.main_hand[3] in '2, 3, 4, 5, 6, 7, 8, 9, 10':
            dealer_total_sum2 = calculationdsum2() + int(DealerHand.main_hand[3])
        elif DealerHand.main_hand[3] in 'Jack, King, Queen':
            dealer_total_sum2 = calculationdsum2() + 10
        elif DealerHand.main_hand[3] in 'Ace':
            if calculationdsum2() >= 11:
                dealer_total_sum2 = calculationdsum2() + 1
            elif calculationdsum2() < 11:
                dealer_total_sum2 = calculationdsum2() + 11
    return dealer_total_sum2


def calculationdsum4():
    # This is the case for the fifth card,if the dealer didn't bust or win,the program continues for the other cases
    if DealerHand.main_hand[4] in '""':
        dealer_total_sum3 = calculationdsum2()
    elif DealerHand.main_hand[4] not in '""':
        if DealerHand.main_hand[4] in '2, 3, 4, 5, 6, 7, 8, 9, 10':
            dealer_total_sum3 = calculationdsum2() + int(DealerHand.main_hand[4])
        elif DealerHand.main_hand[4] in 'Jack, King, Queen':
            dealer_total_sum3 = calculationdsum2() + 10
        elif DealerHand.main_hand[4] in 'Ace':
            if calculationdsum3() >= 11:
                dealer_total_sum3 = calculationdsum2() + 1
            elif calculationdsum3() < 11:
                dealer_total_sum3 = calculationdsum2() + 11
    return dealer_total_sum3