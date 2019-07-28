import liverecog
import os
import re
#this file is for running a test onto several images and seeing if certain slots cause more errors than others in the shop

def maintest():
    path = os.getcwd()+'/tftsamples/' 

    files = []
    for r, d, f in os.walk(path):
        for fi in f:
            #files.append(os.path.join(r, fi))
            files.append(fi)
    return files
def readresults():

    with open('testresults.txt') as f:

        data = f.readlines()
        
        totals = [[0,0],[0,0],[0,0,],[0,0],[0,0]]

        for res in data:

            spl = re.search(r'([0-4])\. (\w+)',res) 


            totals[int(spl.group(1))][1] += 1

            if spl.group(2) != 'error':

                totals[int(spl.group(1))][0] += 1
        sums = [0,0]
        for x in totals:
            sums[0] += x[0]
            sums[1] += x[1]
            print((x[0]/x[1]) * 100)
        print('total accuracy: %{}'.format((sums[0]/sums[1])* 100))
if __name__ == "__main__":
    for img in maintest():
        with open('testresults.txt','a+') as out:

            out.write(liverecog.testimage(img))
    readresults()
