from random import shuffle, sample

val = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
farg = ["s", "c", "d", "h"]

deck = []
for v in val:
    for f in farg:
        deck.append(f+v)

print deck

# deck = []

# for v in val:
# 	for f in farg:
# 		deck.append(f+v)

# shuffle(deck)

# # Make an empty list for our hand, so we have somewhere to put our cards
# hand = []

# # Draw 5 cards from the deck and put them into our hand
# hand.append(deck.pop())
# hand.append(deck.pop())
# hand.append(deck.pop())
# hand.append(deck.pop())
# hand.append(deck.pop())

# # Look at our hand
# print hand