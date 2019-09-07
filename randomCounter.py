import random as rd

starting_amount = 10
current_amount = starting_amount
bet = 1
for i in range(1000):
    y = rd.randint(1, 6)
    x = rd.randint(1, 6)
    if y == x:
        current_amount += 6*bet
    else:
        current_amount -= bet

    print(current_amount, end=' ')
