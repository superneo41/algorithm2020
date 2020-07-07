'''
simple full house game
5 cards

1. 4 of a kind
2. 3 of a kind 2 pairs(full house)
3. 3 of a kind
4. 2 pairs
5. 5 different

'''

def fullhouse(p1, p2):
    '''
    p1, p2: list[int], len = 5
    if p1 > p2: return 1
    if p1 < p2: return -1
    if p1 = p2: return 0
    
    '''
    # get the frequency
    dic1 = {}
    dic2 = {}
    for i in p1:
        dic1[i] = dic1.get(i,0) + 1
    for j in p2:
        dic2[j] = dic2.get(j,0) + 1
    l1 = list(dic1.items())
    l2 = list(dic2.items())
    
    print(l1)
    print(l2)
    # compare
    def compare(l1,l2):
        l1.sort(key = lambda x: (x[1], x[0]))
        l2.sort(key = lambda x: (x[1], x[0]))
        while l1 and l2:
            pair1 = l1.pop()
            pair2 = l2.pop()
            type1, value1 = pair1[1], pair1[0]
            type2, value2 = pair2[1], pair2[0]
            if type1 > type2:
                return 1
            elif type1 < type2:
                return -1
            else:     
                if value1 > value2:
                    return 1
                elif value1 < value2:
                    return -1
        return 0

    return compare(l1,l2)
    