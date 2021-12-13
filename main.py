from itertools import permutations


def per(N):
    zero = ''
    numb = ''
    for i in range(N+1):
        if i != N:
            zero += '0'
        if i != 0:
            numb += str(i)
    data = permutations(zero + numb)
    print(*data)
    f = open('res.txt', 'w+')
    for i in data:
        f.write(*i)
    f.close()
    print('Strings - ', len(*data))


per(7)
