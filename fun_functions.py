# def odd_even ():
#     for i in range (1,2001):
#         if (i%2==1):
#             print 'Number is ', i, '. This is an odd number.'
#         else:
#             print 'Number is ', i, '. This is an even number.'

# odd_even()



def multiply (arr,n):
    new_arr = []

    for items in arr:
        items *= n
        new_arr.append(items)

    print new_arr    
    return new_arr

# multiply([2,4,5],3)
# will return [6,12,15]

def layered_multiples (array):
    layered_array = []

    for items in array:
        items *=[1]
        layered_array.append(items)

    print layered_array



layered_multiples(multiply([2,4,5],3))
