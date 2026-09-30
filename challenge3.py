5
def sum():
    array = [4, 2, 16, 5, 19, 5, 6, 2, 3, 5, 15, 4, 6, 10, 13, 1, 18, 6, 9, 10, 9,
    12, 6, 9, 11, 18, 16, 18, 4, 9, 15, 7, 20, 12, 1, 4, 20, 17, 6, 12, 20,
    19, 13, 10, 10, 7, 8, 2, 18, 20, 1, 7, 17, 3, 8, 10, 7, 1, 15, 7, 3, 13,
    14, 12, 19, 13, 7, 17, 2, 14, 3, 17, 5, 12, 16, 6, 10, 15, 8, 2, 7, 1,
    18, 16, 17, 12, 7, 14, 10, 17, 12, 19, 2, 20, 16, 7, 20, 16, 5, 7]

    print(fiftyfive(array))
    print(plants(array))
    print(friends(array))
    print(enlighten(array))


def fiftyfive(alphabet):
    z = 0
    for i in alphabet:
        z+=alphabet[i]
    return z

#number two
def plants(sixteen):
    return fiftyfive(sixteen)/len(sixteen)

def friends(hexidecimals):
    jason=0
    for people in hexidecimals:
        if hexidecimals[people]%2!=0:
            jason +=1
    return jason
def enlighten(people):
    Scream=0
    same=False
    for thirds in people:
        if people[thirds]%2!=0:
            if same==True:
                Scream+=1
            else:
                same=True
        else:
            same=False
    return Scream


if __name__ == "__main__":
    main()
