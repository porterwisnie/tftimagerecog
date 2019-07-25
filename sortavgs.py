

global x 
with open('shopavgs.txt') as f:

    x = f.readlines()
    for z in sorted(x):
        print(z)
    print(len(x))


    '''
with open('shopavgs.txt', 'w') as f:
    f.write(''.join(x))
    '''
