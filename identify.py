from process import loadarr, openavgs
import shelve
#needs to examine every pixel of every array and see if any one location has unique values for every character
#returns locations of unique pixels
#not worth running anymore as takes a while to process and data is held in pixeldata.txt for reference
def singleidentifier():
    
    poss = []

    holder = []

    champs = openavgs().keys()
    #all champs images same size doesn't matter which i pick
    for row in range(len(loadarr('aatrox'))):

        for col in range(len(loadarr('aatrox')[0])):

            poss.append([col,row])
            
            for champ in champs:
                cpix = ''.join(str(loadarr(champ)[row][col][:3].tolist()))
                if cpix not in holder:

                    holder.append(cpix)
                else:
                    holder.clear()
                    poss.pop()
                    break
    
    with open('pixeldata.txt','w+') as op:

        op.write(str(poss))


        


    
#sending the index of interest responds with a dictionary of values for each character at that location
#champion name : [red,green,blue]

def allchampsatpix(col,row):

    champrgb = {}
    champs = openavgs().keys()

    for champ in champs:

        champrgb[champ] = loadarr(champ).tolist()[row][col][:3]

    return champrgb

if __name__ == "__main__":
    
    singleidentifier()
