cardlist = []
suits = ['clubs', 'spades', 'diamonds', 'hearts']
for _ in range(2,10+1):
    for suit in suits:
        cardlist.append(str(_) + "_of_" + str(suit))
royal = ['jack', 'king', 'queen', 'ace']
for _ in royal:
    for suit in suits:
        cardlist.append(str(_) + "_of_" + str(suit))

with open('cardlist.txt', 'w') as file:
    for card in cardlist:
        file.write(card + "\n")