def foo_bar ():

    x = 10
    

    for i in range (100, 100001):
        prime = True

        for k in range (i/2, 1, -1):
            if (i%k == 0):
                prime = False
            
        if  prime:
            print i, 'foo'

        if ((i/x)==x):
            print i, 'bar (of ', x, ')'
            x += 1
        
        else: print i 
            
foo_bar()

