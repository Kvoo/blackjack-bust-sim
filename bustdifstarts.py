#bust.py --- Simulates multiple games of blackjack with each possible dealer starting card and estimates
#   the probability that the dealer will bust

import random

def intro():
    pass

def takecard():
    card = random.randint(1, 10)
    has_ace = False
    #Randomly choose if the 1 is an ace
    if card == 1:
        has_ace = random.choice([True, False])
    return card, has_ace

def sim_one_game(starter):
    #For simulating the ace
    if starter == 12:
        starter = 1
        has_ace = True

    total = starter

    while total <= 17:
        card, has_ace = takecard()
        total += card

        #Ace is valued at 11 when it would produce a stopping total
        if has_ace == True and total + 10 >= 17 and total + 10 <= 21:
            total += 10

    return total

def sim_n_games(starter, game_count):
    busts = 0
    for i in range(game_count):
        score = sim_one_game(starter)
        if score > 21:
            busts += 1
    return busts

def sim_each_card(game_count):
    bustsls = []
    for i in range(1, 12):
        bustsls.append(sim_n_games(i, game_count))

    return bustsls

def output(bustsls, game_count):
    print("Busts for Starting Card A: {} out of {} games. ({:0.1%})".format(bustsls[10], game_count, bustsls[10] / game_count))
    for card in range(1, 11):
        print("Busts for Starting Card {}: {} out of {} games. ({:0.1%})".format(card, bustsls[card - 1], game_count, bustsls[card - 1] / game_count))

def main():
    intro()
    game_count = int(input("\nHow many rounds to simulate? "))
    bustsls = sim_each_card(game_count)
    output(bustsls, game_count)

if __name__ == "__main__": main()
