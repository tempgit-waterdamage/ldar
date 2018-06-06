def channel_order(number):
    return {
        0 : 0,
        1 : 2,
        2 : 4,
        3 : 6,
        4 : 8,
        5 : 10,
        6 : 12,
        7 : 14,
        8 : 1,
        9 : 3,
        10 : 5,
        11 : 7,
        12 : 9,
        13 : 11,
        14 : 13,
        15 : 15
    }[number]

def make_pharma(number,head,tail):
    a = bin(12)
    a = list(a[2:])
    np.asarray(a,dtype=int)

    head = np.asarray([1,1,0],dtype=int)
    tail = np.asarray([0,1,1],dtype=int)

    middle = np.append(head,a)
    final = np.append(middle,tail)
    return final
