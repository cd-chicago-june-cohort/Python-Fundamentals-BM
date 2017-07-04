from types import *

a = ['magical unicorns', 19, 'hello', 98, 98, 'world']
b = [2,3,1,7,4,12]
c = ['magical', 'unicorns']

def test_tell (listvar):
    sumvar = 0
    sumstring = ""
    words = False
    nums = False

    for items in listvar:

        if (isinstance(items, int) == True):
            sumvar = sumvar + items
            nums = True
        elif (isinstance(items, str) == True):
            sumstring = sumstring + ' ' + items
            words = True

    print "sum: ", sumvar
    print "String: ", sumstring
    if (nums == True and words == True):
        print "This is a mixed string"
    elif (nums == True and words == False):
        print "These are integers"
    elif (words == True and nums == False):
        print "These are strings"




test_tell(c)



# def isType (list, type_of):
#     type_of = True
#     for items in list:
#         if (type_of == IntType):


