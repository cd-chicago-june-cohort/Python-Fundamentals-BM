sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,6,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,12,45,923]
el = []
spL = ['name','address','phone number','social security number']

def check_var (var):
    if (isinstance(var, int) == True):
        if (var>=100):
            print "That's a big number!"
        elif (var < 100):
            print "That's a small number"
    elif (isinstance(var, str) == True):
        if (len(var) >= 50):
            print "Long sentence"
        elif (len(var) < 50):
            print "Short sentence"
    elif (isinstance(var, list) == True):
        if (len(var) >= 10):
            print "Big list!"
        elif (len(var) < 10):
            print "Short list."






check_var(sI)