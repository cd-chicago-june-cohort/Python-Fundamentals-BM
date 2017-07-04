import random

def coin_toss ():
    heads = 0
    tails = 0
    
    for i in range (1,5001):
        

        toss = random.choice(['Heads', 'Tails'])

        if (toss == 'Heads'):
            heads += 1
        elif (toss == 'Tails'):
            tails += 1

        print "Attempt #", i, ": Throwing a coin... It's ", toss, "... Got ", heads, " Heads so far and ", tails, " Tails so far"

        if i == 5000:
            print "Ending the program, thank you!"



coin_toss()