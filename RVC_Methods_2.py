

class dataEntryFile:
    def __init__(self, entryFile):
        self.entryFile = entryFile

    def readFileToList(self):
        return [line.strip().split('~') for line in open(self.entryFile).readlines() if line.strip()]

    def create_diver_dictionary(self, diversList):
        diverDict = {}
        for diver in diversList:
            diverDict[diver[0]] = diver[1]
        return diverDict

class QualityControl:
    def __init__(self, sampleList, speciesList, substrateList, diverDictionary ):
        self.diverDictionary = diverDictionary
        self.sampleList = sampleList
        self.speciesList = speciesList
        self.substrateList = substrateList
        self.msnSamples =[msn[0] for msn in sampleList]
        self.msnSpecies = list(set([msn[0] for msn in speciesList]))
        self.msnSubstrate = [msn[0] for msn in substrateList]
        self.diverList = list(set([diver[1] for diver in sampleList]))

    def check_sample_substrates(self):
        missingSubstrateFiles = []
        missingSampleFiles = []
        for msn in self.msnSamples:
            if not msn in self.msnSubstrate:
                missingSubstrateFiles.append(msn)
        print "(" + str(len(missingSubstrateFiles)) + ")" + " missing from substrate files"
        for item in missingSubstrateFiles:
            print item + " not found in substrate list"
        for msn in self.msnSubstrate:
            if not msn in self.msnSamples:
                missingSampleFiles.append(msn)
        print "(" + str(len(missingSampleFiles)) + ")" + " missing from sample files"
        for item in missingSampleFiles:
            print item + " not found in sample list"
        print "Check Complete"
        print '\n'

    def check_sample_species(self):
        missingSpeciesFiles = []
        missingSampleFiles = []
        for msn in self.msnSamples:
            if not msn in self.msnSpecies:
                missingSpeciesFiles.append(msn)
        print "(" + str(len(missingSpeciesFiles)) + ")" + " missing from species files"
        for item in missingSpeciesFiles:
            print item + " not found in species list"
        for msn in set(self.msnSpecies):
            if not msn in self.msnSamples:
                missingSampleFiles.append(msn)
        print "(" + str(len(set(missingSampleFiles))) + ")" + " missing from sample files"
        for item in missingSampleFiles:
            print item + " not found in sample list"
        print "Check Complete"
        print '\n'

    def check_duplicate_mastersample_numbers(self):
        sampleDict = {}
        for msn in self.msnSamples:
            if msn in sampleDict:
                sampleDict[msn] += 1
            else:
                sampleDict[msn] = 1
        
        print "List of Duplicate MSN in Samples file"
        print [ key for key, value in sampleDict.items() if value > 1]
        print '\n'

    def check_duplicate_fieldid(self):
        fieldidDict = {}
        for line in self.sampleList:
            if line[20] in fieldidDict:
                fieldidDict[line[20]] += 1
            else:
                fieldidDict[line[20]] = 1
        
        print "List of Duplicate Field_IDs in Samples file"
        print [ key for key, value in sorted(fieldidDict.items()) if value > 1]
        print '\n'

    def print_counts_by_diver(self):
        diverCount = {}
        for diver in self.diverList:
            diverCount[self.diverDictionary[diver]] = len( [ d[0] for d in self.sampleList if d[1] == diver])
        for key, value in sorted(diverCount.items()):
            print key, '\t',  value
        
        print '\n'




