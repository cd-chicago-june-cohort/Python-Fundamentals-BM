

def mult_table (r, c):

    table = []
    r = 1
    for i in range (r-r, c, r):
        i = i + r 
        table.append (i)
    print 'x', table

    table = []
    r = 1
    for i in range (r-r, c, r):
        i = i + r 
        table.append (i)
    print r, table
    
    
    for row in range (1, 12):
        r = r + 1
        table = []
        for i in range (r-r, c*r, r):
        
            i = i + r
            table.append (i)
        print r, table
        row = row + 1



mult_table(1, 12)        