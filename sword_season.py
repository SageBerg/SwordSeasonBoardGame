import random
import sys

player_count = int(sys.argv[1])

deck = []

deck_multipliers = {1:(30,30), 2:(20,20), 3:(15,15), 4:(12,13), 5:(11,12),
                    6:(11,11), 7:(10,11)}

if player_count < 8:
    card_count = deck_multipliers[player_count][0] + \
                 deck_multipliers[player_count][1]
    demon_multiplier = deck_multipliers[player_count][0]
    no_op_multiplier = deck_multipliers[player_count][1]
else:
    card_count = 20
    demon_multiplier = 10
    no_op_multiplier = 10

deck += ["Spawn a demon for each player"]*demon_multiplier
deck += ["No new demons!"]*no_op_multiplier
random.shuffle(deck)

print "press any key to draw a card"
for i in range(1, len(deck) + 1):
    raw_input()
    if i < len(deck):
        print deck[i] 
    print str(card_count - i) + " rounds remaining."

print "Game over"
