from collections import defaultdict


##################################
nsppFile = r'C:\Users\jblondeau\Desktop\Temp\rvc_species_fk10.csv'
outfile = r'C:\Users\jblondeau\Desktop\Temp\FK_2010_Mis2.txt'
sppList = ['OCY CHRY', 'LUT APOD', 'LUT GRIS', 'LAC MAXI', 'LUT SYNA', 'MYC BONA', 'LUT BUCC', 'EPI MORI', 'LUT ANAL', 'LUT CYAN', 'LUT JOCU', 'LUT MAHO']
##################################




def readFileToList(nsppFile):
    return [line.strip().split(',') for line in open(nsppFile).readlines()]

def DefaultDict():
    return defaultdict(DefaultDict)

def PercMisCount(spp, Species):
    spp = readFileToList(nsppFile)
    Species = Species

    
    sppFilter = []
    for line in spp:
        if line[1] == Species:
            sppFilter.append(line)

    sppMis = []
    for line in sppFilter:
        if line[4] == line[5]:
            continue
        elif int(line[2]) > 3 and int(line[2]) < 10:
            sppMis.append(line[0])

    msnDict = DefaultDict()
    for line in sppFilter:
        if msnDict.has_key(line[0]):
            msnDict.setdefault(line[0], []).append(int(line[2]))
        else:
            msnDict[line[0]] = [int(line[2])]

    
    sppDenom = 0
    for msn in msnDict:
        if sum(msnDict[msn]) > 3 and sum(msnDict[msn]) < 10:
            sppDenom += 1
    print len(set(sppMis))
    print sppDenom
    return (int(len(set(sppMis))) / float(sppDenom)) *100.0


    

##def main():
##    text_File = open(outfile, 'w')
##    outDict = {}
##    
##    for species in sppList:
##        try:
##            outDict[species] = PercMisCount(nsppFile, species)
##        except ZeroDivisionError:
##            outDict[species] = 0
##        
##    for k,v in outDict.items():
##        text_File.write('%s,%f' % (k,v))
##        text_File.write('\n')
##    text_File.close()
##
##
##if __name__=="__main__":
##    main()
