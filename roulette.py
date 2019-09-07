# roulette spin

import matplotlib.pyplot as plt

def spin():
    import random as rd
    x = rd.randint(0, 36)
    y = rd.randint(0, 36)
    if x == y:
        # print('Spin was correct')
        return True
    if x != y:
        # print('Spin was incorrect')
        return False

def multiple_spins(intialamount, wager, wager_count, N): # multiple repetions of "games" of a roulette wheel
    from math import sqrt
    results = []
    for i in range(N):
        value = intialamount
        for i in range(wager_count):
            if spin():
                value += wager*35
            else:
                value -= wager




        results.append(value)
    mean = sum(results)/N # stats analysis on mean and variance
    print(mean)
    s = 0
    for i in results:
        x = results[i]
        term = (x - mean)**2
        s += term
    print(sqrt(s/N))


    return results
