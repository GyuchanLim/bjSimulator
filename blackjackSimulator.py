# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 22:27:00 2022

1. IMPLEMENT GITHUB
2. AM I DOING IT RIGHT?
3. I AM NOT DOING IT RIGHT

@author: Gyuchan
"""
import random
import os

game_stats = {
    'p_bust': 0,
    'draw': 0,
    'd_bust': 0,
    'p_win': 0,
    'd_win': 0
}

testing_deck = [6, 11]
fresh_deck = [
    #2,3,4,5,6,7,8,9,10, J, Q, K, A,
    2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
    2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
    2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
    2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
]

number_of_decks = 8
reshuffle = 0.6  # when only 60% of cards remain in deck, use new shuffled deck


def new_deck():

    blackJack_deck = fresh_deck * number_of_decks
    random.shuffle(blackJack_deck)

    return blackJack_deck


def dealing(deck, strategy):
    player_hand = []
    dealer_hand = []

    player_hand.append(deck.pop(0))
    dealer_hand.append(deck.pop(0))
    player_hand.append(deck.pop(0))
    dealer_hand.append(deck.pop(0))

    #--------------STRATEGY1-----------------#
    if strategy == 1:
        # IMPLEMENT MY STRATEGY
        # Strategy 1, play like the dealer
        # H17 Rule, draw until 16
        while sum(player_hand) < 18:
            stop = False
            if sum(player_hand) == 17:
                stop = True
                for i, card in enumerate(player_hand):
                    if card == 11:
                        player_hand[i] = 1
                        stop = False
            if stop:
                break
            player_hand.append(deck.pop(0))
    #--------------STRATEGY2-----------------#
    player_sum = sum(player_hand)

    if strategy == 2:
        while player_sum < 12:
            card_popped = deck.pop(0)
            if card_popped == 11 and player_sum + card_popped > 21:
                player_hand.append(1)
                player_sum += 1
            else:
                player_hand.append(card_popped)
                player_sum += card_popped

    if strategy == 3:
        while player_sum < 13:
            card_popped = deck.pop(0)
            if card_popped == 11 and player_sum + card_popped > 21:
                player_hand.append(1)
                player_sum += 1
            else:
                player_hand.append(card_popped)
                player_sum += card_popped

    #----------------------------------------#
    player_sum = sum(player_hand)
    if player_sum > 21:
        #print('player bust with {}'.format(player_sum))
        return 'p_bust'
    #----------------------------------------#
    # THIS IS DEFAULT DEALER STRATEGY AND SHOULD NOT BE CHANGED
    while sum(dealer_hand) < 18:
        stop = False
        if sum(dealer_hand) == 17:
            stop = True
            for i, card in enumerate(dealer_hand):
                if card == 11:
                    dealer_hand[i] == 1
                    stop = False
        if stop:
            break
        dealer_hand.append(deck.pop(0))

    dealer_sum = sum(dealer_hand)
    # draw
    if player_sum == dealer_sum:
        # print('draw')
        return 'draw'
    # dealer bust
    if dealer_sum > 21:
        #print('dealer bust with {}'.format(dealer_sum))
        return 'd_bust'
    # player win
    if player_sum > dealer_sum:
        #print('player wins with {}'.format(player_sum))
        return 'p_win'
    # dealer win
    if player_sum < dealer_sum:
        #print('dealer trumps player with {}'.format(dealer_sum))
        return 'd_win'


def strategy(strategy_number, number_of_games):
    results_file = open('results.txt', 'a')
    blackjack_deck = new_deck()
    for game in range(number_of_games):
        result = dealing(blackjack_deck, strategy_number)
        if len(blackjack_deck)/(52*number_of_decks) < reshuffle:
            #print(len(blackjack_deck), "RESHUFLING")
            blackjack_deck = new_deck()
        game_stats[result] += 1

    str_format = ""
    for key in game_stats:
        str_format += str(game_stats[key])+','
        game_stats[key] = 0
    results_file.write(str_format[:-1]+"\n")
    results_file.close()


if __name__ == '__main__':
    try:
        os.remove("results.txt")
    except FileNotFoundError:
        pass

    strategy(1, 1000000)
    strategy(2, 1000000)
    strategy(3, 1000000)

    results_file = open('results.txt', 'r')
    for i, line in enumerate(results_file.read().splitlines()):
        result = line.split(',')
        print('Strategy {}'.format(i+1))
        print('Player win = {}'.format(int(result[2])+int(result[3])))
        print('Player win = {}'.format(int(result[0])+int(result[4])))
        print('Draw = {}'.format(int(result[1])))
        print('=============================')
    results_file.close()
