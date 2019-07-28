import shelve
from os import path

def addchampkey(keystring,champ):
    with shelve.open(path.dirname(path.realpath(__file__))+'/rgbtochampdict/rgbtochampdict') as d:

        temp = d['rgbchamp']
    
        temp[keystring] =  champ

        d['rgbchamp'] = temp
        
        print(d['rgbchamp'])

if __name__ == "__main__":

    addchampkey('[14, 17, 8]','warwick')
