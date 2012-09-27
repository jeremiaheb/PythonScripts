from RVC_Methods_2 import *
import matplotlib.pyplot as plot
from random import random
from math import sqrt


def triangular(a,b,c):
    c = float(c)
    t = (c-a)/(b-a)
    y = sqrt(random())
    d = a if random() < t else b
    return d + (c-d) * y


spp = dataEntryFile(r'C:\Users\jblondeau\Documents\Python\RVC_Merge\MergingProgram\_Data\TotalMerge\speciesmerge.txt').readFileToList()


##sppList = sorted(set([line[1] for line in spp]))

species = ['SPA AURO']

#sizeList = []
#for line in spp:
#    if line[1]== species and line[6] == '1':
#        if line[2]== '1':
#            sizeList.append(int(line[3]))
#        elif line[2] == '2':
#            sizeList.append(int(line[4]))
#            sizeList.append(int(line[5]))
#        elif line[2] == '3':
#            sizeList.append(int(line[3]))
#            sizeList.append(int(line[4]))
#            sizeList.append(int(line[5]))
#        elif line[2] == '4':
#            sizeList.append(int(line[3]))
#            sizeList.append(int(line[3]))
#            sizeList.append(int(line[4]))
#            sizeList.append(int(line[5]))
#        elif line[2] == '5':
#            sizeList.append(int(line[3]))
#            sizeList.append(int(line[4]))
#            sizeList.append(int(line[5]))
#            sizeList.append((int(line[4]) + int(line[3]))/2)
#            sizeList.append((int(line[5]) + int(line[3]))/2)
#        elif line[4] == line[5]:
#            sizes = [int(line[3]) for i in range(int(line[2]))]
#            sizeList += sizes
#        else:
#            for i in range(int(line[2])):
#                tDistSizes = triangular(int(line[4]),int(line[5]),int(line[3]))
#                sizeList.append(tDistSizes)

sizeList = []
for s in species:
    for line in spp:
        if line[1]== s and line[6] == '1':
            if line[2]== '1':
                sizeList.append(int(line[3]))
            elif line[2] == '2':
                sizeList.append(int(line[4]))
                sizeList.append(int(line[5]))
            elif line[2] == '3':
                sizeList.append(int(line[3]))
                sizeList.append(int(line[4]))
                sizeList.append(int(line[5]))
            elif line[2] == '4':
                sizeList.append(int(line[3]))
                sizeList.append(int(line[3]))
                sizeList.append(int(line[4]))
                sizeList.append(int(line[5]))
            elif line[2] == '5':
                sizeList.append(int(line[3]))
                sizeList.append(int(line[4]))
                sizeList.append(int(line[5]))
                sizeList.append((int(line[4]) + int(line[3]))/2)
                sizeList.append((int(line[5]) + int(line[3]))/2)
            elif line[4] == line[5]:
                sizes = [int(line[3]) for i in range(int(line[2]))]
                sizeList += sizes
            else:
                for i in range(int(line[2])):
                    tDistSizes = triangular(int(line[4]),int(line[5]),int(line[3]))
                    sizeList.append(tDistSizes)    
    plot.hist(sizeList, bins=20)
    plot.title(s)
    plot.xlabel('size(cm)')
    plot.ylabel('Abundance')
    #plot.boxplot(sizeList)
    plot.show()






