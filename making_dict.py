name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas", "chickens"]

def make_dict(arr1, arr2):
    new_dict = {}

    if (len(arr1) >= len(arr2)):

        for i in range (0, len(arr1)):
            new_dict[arr1[i]] = arr2[i]
    
    else:
        
        for i in range (0, len(arr1)):
            new_dict[arr2[i]] = arr1[i]

    print new_dict

make_dict(name, favorite_animal)

