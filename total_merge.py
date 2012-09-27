


####  Directions ###
#    Place this script in the same directory as your Sample, Species and Substrate
#    folders.  You will also need the diverlist.noaa file in there as well.
#    Execute script will result in a new _Data folder being created and populated with merged 
#    files by diver and total merges for all divers.



import os
import sys
import shutil

script_path = sys.path [0] + '/'
			
mergeDir = script_path

proofingDate = '10012012'

computerName = 'LOF_'

###Delete contents of the _Data folder if it exists
if os.path.exists(mergeDir + '_Data'):
    shutil.rmtree(mergeDir + '_Data')


###Create a list of Diver names based on the updated diverlist.noaa file
###This makes an iterable list of diver names 
cleanDiverNames = [line.strip().split('~')[1] for line in open(mergeDir + 'diverlist.noaa','r')]



### Create Sample,Species,Substrate folder (if not already created) and drop them in the _Data directory

if not os.path.exists(mergeDir + '_Data/sample'):
    os.makedirs(mergeDir + '_Data/sample')
if not os.path.exists(mergeDir + '_Data/species'):    
    os.makedirs(mergeDir + '_Data/species')
if not os.path.exists(mergeDir + '_Data/substrate'):
    os.makedirs(mergeDir + '_Data/substrate')
if not os.path.exists(mergeDir + '_Data/TotalMerge'):
    os.makedirs(mergeDir + '_Data/TotalMerge')

### Create a folder for each diver in the diverlist.noaa file (if not already created) and drop them
### into the _Data directory

for name in cleanDiverNames:
    if not os.path.exists(mergeDir + '_Data/%s' % name):
        os.makedirs(mergeDir + '_Data/%s' % name)

### Merge Sample files
samplefiles = os.listdir(mergeDir + 'sample')
for file in samplefiles:
    for name in cleanDiverNames:
        if name in file:
            outPutFile = open(mergeDir + '_Data/%s/%s%ssample%s.nsam' % (name,computerName,name,proofingDate),'a')
            outPutFile2 = open(mergeDir + '_Data/sample/%s%ssample%s.nsam' % (computerName,name,proofingDate), 'a')
            outPutFile3 = open(mergeDir + '_Data/TotalMerge/samplemerge.txt', 'a')                       
            linesReadFromFile = [line for line in open(mergeDir + 'sample/%s' % file,'r').readlines() if line.strip()]
            formattedLines = "".join(line for line in linesReadFromFile)
            outPutFile.write(formattedLines)
            outPutFile2.write(formattedLines)
            outPutFile3.write(formattedLines)
            outPutFile.close()
            outPutFile2.close()
            outPutFile3.close()


##Merge Species files

speciesfiles = os.listdir(mergeDir + 'species')
for file in speciesfiles:
    for name in cleanDiverNames:
        if name in file:
            outPutFile = open(mergeDir + '_Data/%s/%s%sspecies%s.nspe' % (name,computerName,name,proofingDate),'a')
            outPutFile2 = open(mergeDir + '_Data/species/%s%sspecies%s.nspe' % (computerName,name,proofingDate), 'a')
            outPutFile3 = open(mergeDir + '_Data/TotalMerge/speciesmerge.txt', 'a')
            linesReadFromFile = [line for line in open(mergeDir + 'species/%s' % file,'r').readlines() if line.strip()]
            formattedLines = "".join(line for line in linesReadFromFile)
            outPutFile.write(formattedLines)
            outPutFile2.write(formattedLines)
            outPutFile3.write(formattedLines)
            outPutFile.close()
            outPutFile2.close()
            outPutFile3.close()


##Merge Substrate files

substratefiles = os.listdir(mergeDir + 'substrate')
for file in substratefiles:
    for name in cleanDiverNames:
        if name in file:
            outPutFile = open(mergeDir + '_Data/%s/%s%ssubstrate%s.nsub' % (name,computerName,name,proofingDate),'a')
            outPutFile2 = open(mergeDir + '_Data/substrate/%s%ssubstrate%s.nsub' % (computerName,name,proofingDate), 'a')
            outPutFile3 = open(mergeDir + '_Data/TotalMerge/substratemerge.txt', 'a')
            linesReadFromFile = [line for line in open(mergeDir + 'substrate/%s' % file,'r').readlines() if line.strip()]
            formattedLines = "".join(line for line in linesReadFromFile)
            outPutFile.write(formattedLines)
            outPutFile2.write(formattedLines)
            outPutFile3.write(formattedLines)
            outPutFile.close()
            outPutFile2.close()
            outPutFile3.close()
			

##Delete Empty Directories
##Ealier in the script, a folder was created for every diver in the diver.noaa file.
##this part deletes any empty folder

for name in cleanDiverNames:
    try:
        os.removedirs(mergeDir + '_Data/%s' % name)
    except WindowsError:
        pass
			



