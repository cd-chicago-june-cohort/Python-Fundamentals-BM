from types import *

def draw_stars(arr):

    
    for i in range (0, len(arr)):

        if type (arr[i]) is IntType:
            print (arr[i]*'*')

        elif type (arr[i]) is StringType:
            print (arr[i][0].lower() * len(arr[i]))
            
draw_stars([4, 'Tom', 1, 'Michael', 5, 7, 'Jimmy Smits'])



