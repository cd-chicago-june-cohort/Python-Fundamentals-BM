word_list = ['hello','world','my','name','is','anna']
char = 'o'
new_list = []

def find_char (list, char):
    for i in list:
        if char in i:
            new_list.append(i)

    print new_list



find_char (word_list, char)
