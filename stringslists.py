
# Find and Replace
words = "It's Thanksgiving Day.  It's my birthday, too!"
print words.find('Day')
print words.replace('Day', 'month')


# Min and Max
x = [2,54,-2,7,12,98]
print max(x)
print min(x)


# First and Last
x = ["hello",2,54,-2,7,12,98]
print sorted (x)
a = x[0]
b = x[-1]

print a
print b

newlist = [a, b]
print newlist


# New List
x = [19,2,54,-2,7,12,98,32,10,-3,6]

xsort = sorted (x)



y = xsort[:len(xsort)/2]
print y



z = xsort[len(xsort)/2:]

newarr = [y]
print newarr + z

