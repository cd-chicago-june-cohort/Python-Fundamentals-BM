# list_one = [1,2,5,6,3]
# list_two = [1,2,5,6,8]

# list_one = [1,2,5,6,5,3]
# list_two = [1,2,5,6,5,6]

# list_one = [1,2,5,6,5,16)
# list_two = [1,2,5,6,5]

list_one = ['celery','carrots','bread','mike']
list_two = ['celery','carrots','bread','cream']


def compare (x,y):
    match = True
    if (len(x) == len(y)):
        for i in range (0, len(x)):
            if (x[i]!=y[i]):
                match = False

    elif (len(x) != len(y)):
        match = False


    if (match == False):
        print "These do not match"

    elif (match == True):
        print "These lists match!"


compare (list_one, list_two)