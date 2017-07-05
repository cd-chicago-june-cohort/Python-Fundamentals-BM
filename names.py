students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

def print_name (arr):

    for i in arr:
         print (i.get('first_name') + ' ' + i.get('last_name'))



print_name (students)

# Part Deux

users = {

    'Students': [
        {'first_name': 'Michael', 'last_name': 'Jordan'},
        {'first_name': 'John', 'last_name': 'Rosales'},
        {'first_name': 'Mark', 'last_name': 'Guillen'},
        {'first_name': 'KB', 'last_name': 'Tonel'}
    ],
    'Instructors': [
        {'first_name': 'Michael', 'last_name': 'Choi'},
        {'first_name': 'Martin', 'last_name': 'Puryear'}
    ]
}

def print_users (arr):

    for key, val in arr.items():
        click = 1
        print key
        for key in val:
            print (str(click) + ' - ' + key['first_name'].upper() + ' ' + key['last_name'].upper() + ' - ' + str(len((key['first_name'] + key['last_name']))))
            click += 1

            
print_users(users)