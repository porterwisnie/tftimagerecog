import shelve
from process import mainopen
from os import path


#put test files into tftsamples
def testimage(filename):



    iarr = mainopen(path.dirname(path.realpath(__file__))+'/tftsamples/'+filename)
    with shelve.open(path.dirname(path.realpath(__file__))+'/rgbtochampdict/rgbtochampdict') as dat:
        anchors = [[479,672],[680,873],[881,1074],[1083,1276],[1284,1477]]
        print(dat['rgbchamp'])
        for n in range(5):

            a = iarr[927:1071].copy()
            b = []
            for row in range(len(a)):
                b.append(a[row][anchors[n][0]:anchors[n][1]])
             
            bmod = list(b[44][51])[:3]
            print(bmod)
            bmod2 = list(b[85][170])[:3]
            try:
                print(dat['rgbchamp'][str(bmod)])
            except:
                try:
                    print(dat['rgbchamp2'][str(bmod2)])
                except:
                    print('error')
if __name__ == "__main__":

    testimage('ltest4.png')
