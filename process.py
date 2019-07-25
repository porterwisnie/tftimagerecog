from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from statistics import mean
import re
from os import path, listdir

def openimagearr(p):
    i =  Image.open(p)

    return np.asarray(i)
def mainopen(p):

    i = Image.open(p)
    i = i.resize((1920,1080))
    i.save(p,'png',optimize=True)
    return np.asarray(i)
def plotimage(iarr):
    
    plt.imshow(iarr)
    plt.show()


def thresholder(iarr):
    barr = []
    narr = iarr.copy()
    narr[0][0][0] = 1
    for row in iarr:

        for pix in row:
            
            barr.append(mean(pix[:3]))
    balance = mean(barr)
    
    for row in narr:
        for pix in row:
            if mean(pix[:3]) > balance:
                pix[0] = 255
                pix[1] = 255
                pix[2] = 255
            else:
                pix[0] = 0 
                pix[1] = 0
                pix[2] = 0
    return narr

def createnewimg(iarr,p='new.png'):
    img = Image.fromarray(np.array(iarr))
    img.save(p)

def writearr(iarr, filename):
    ''' 
    f = open(filename+'.txt','w+')
    f.write(iarr)
    f.close()
    '''
    np.save(path.dirname(path.realpath(__file__))+'/npy/' +filename+'.txt', iarr)

def loadarr(name):
    return np.load(path.dirname(path.realpath(__file__))+'/npy/'+name + '.txt.npy')

def np3dmean(iarr):
    a = []
    for row in iarr:
        for pix in row:
            a.append(mean(pix[:3]))
    return mean(a)
def addallavgs():

    fs = listdir(path.dirname(path.realpath(__file__))+'/npy')

    for f in fs:

        addmean(re.sub('\.txt\.npy','',f),np3dmean(loadarr(re.sub('\.txt\.npy','',f))))

def addmean(name,avg):
    
    with open('shopavgs.txt','a') as f:
        
        if name not in openavgs().keys():


            f.write('{}:{}\n'.format(name,avg))

def openavgs():
    with open('shopavgs.txt') as f:
        avgs = {}

        for x in f.readlines():

            x = x.split(':')
            x[0] = re.sub('\\n','',x[0])
            x[1] = re.sub('\\n','',x[1])
            avgs[x[0]] = x[1]
    return avgs

def addnewchamp(name):

    iarr = openimagearr(path.dirname(path.realpath(__file__))+'/cards/'+name+'.png')
    writearr(iarr,name)
    addmean(name,np3dmean(iarr))
    #plotimage(iarr) 

def getcards(p,names):
    anchors = [[479,672],[680,873],[881,1074],[1083,1276],[1284,1477]]
    for n in range(len(names)):
         
        iarr = mainopen(p)
        a = iarr[927:1071].copy()
        b = []
        for row in range(len(a)):
            b.append(a[row][anchors[n][0]:anchors[n][1]])


        createnewimg(b,path.dirname(path.realpath(__file__))+'/cards/'+names[n]+'.png')

#this method is the ?everything method
def autoadd(p,names):
    
    getcards(p,names)
    for name in names:
        
        addnewchamp(name)


if __name__ == "__main__":
    
    
    
    '''
    iarr = openimagearr('yasuo.png')
    writearr(iarr,'yasuo')
    plotimage(loadarr('yasuo'))
    '''

    '''
    iarr = loadarr('lissandra')
    imean = np3dmean(iarr)

    print(imean)
    '''
    autoadd(str(path.dirname(path.realpath(__file__)) + '/tftsamples/l1fixed'),['darius','tristana','khazix','pyke','fiora']) 
    
    '''
    iarr = mainopen(str(path.dirname(path.realpath(__file__)) + '/tftsamples/League of Legends (TM) Client 7_21_2019 9_11_41 PM.png'))
    print(len(iarr))
    plotimage(iarr)
    '''
