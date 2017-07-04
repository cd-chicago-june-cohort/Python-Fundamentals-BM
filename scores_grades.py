import random

def scores_grades ():
       
    for i in range (1,10):

        random_num = random.randint(60,100)
        
        if (random_num <= 69):
            print 'Score: ', random_num, '; your grade is D'

        elif (random_num >= 70 and random_num <= 79):
            print 'Score: ', random_num, '; your grade is C'

        elif (random_num >= 80 and random_num <= 89):
            print 'Score: ', random_num, '; your grade is B'

        elif (random_num >= 90):
            print 'Score: ', random_num, '; your grade is A!'





scores_grades()