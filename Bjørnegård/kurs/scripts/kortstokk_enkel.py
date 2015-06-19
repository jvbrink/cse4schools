from random import shuffle

deck = [
's2', 'c2', 'd2', 'h2', 's3', 'c3', 'd3', 'h3',
's4', 'c4', 'd4', 'h4', 's5', 'c5', 'd5', 'h5',
's6', 'c6', 'd6', 'h6', 's7', 'c7', 'd7', 'h7',
's8', 'c8', 'd8', 'h8', 's9', 'c9', 'd9', 'h9', 
'sT', 'cT', 'dT', 'hT', 'sJ', 'cJ', 'dJ', 'hJ', 
'sQ', 'cQ', 'dQ', 'hQ', 'sK', 'cK', 'dK', 'hK', 
'sA', 'cA', 'dA', 'hA']

shuffle(deck)

print deck[0]
hand = []
hand.append(deck.pop(0))
hand.append(deck.pop(0))
hand.append(deck.pop(0))
hand.append(deck.pop(0))
hand.append(deck.pop(0))
print hand

