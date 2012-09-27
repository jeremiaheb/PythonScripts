


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

proofingDate = '09012012'

computerName = 'spree'

###Delete contents of the _Data folder if it exists
if os.path.exists(mergeDir + '_Data'):
    shutil.rmtree(mergeDir + '_Data')


###Create a list of Diver names based on the updated diverlist.noaa file
###This makes an iterable list of diver names 
cleanDiverNames = [line.strip().split('~')[1] for line in open(mergeDir + 'diverlist.noaa','r')]



### Create Sample,Species,Substrate folder (if not already created) and drop them in the _Data directory

if not os.path.exists(mergeDir + '_Data/Sample'):
    os.makedirs(mergeDir + '_Data/Sample')
if not os.path.exists(mergeDir + '_Data/Species'):    
    os.makedirs(mergeDir + '_Data/Species')
if not os.path.exists(mergeDir + '_Data/Substrate'):
    os.makedirs(mergeDir + '_Data/Substrate')
if not os.path.exists(mergeDir + '_Data/TotalMerge'):
    os.makedirs(mergeDir + '_Data/TotalMerge')

### Create a folder for each diver in the diverlist.noaa file (if not already created) and drop them
### into the _Data directory

for name in cleanDiverNames:
    if not os.path.exists(mergeDir + '_Data/%s' % name):
            os.makedirs(mergeDir + '_Data/%s' % name)

### Merge Sample files
samplefiles = os.listdir(mergeDir + 'Sample')
for file in samplefiles:
	for name in cleanDiverNames:
		if name in file:
			outPutFile = open(mergeDir + '_Data/%s/%s%ssample%s.nsam' % (name,computerName,name,proofingDate),'a')
			outPutFile2 = open(mergeDir + '_Data/Sample/%s%ssample%s.nsam' % (computerName,name,proofingDate), 'a')
                        outPutFile3 = open(mergeDir + '_Data/TotalMerge/samplemerge.txt', 'a')                       
                        linesReadFromFile = open(mergeDir + 'Sample/%s' % file,'r').read()
			outPutFile.write(linesReadFromFile)
			outPutFile2.write(linesReadFromFile)
                        outPutFile3.write(linesReadFromFile)
			outPutFile.close()
			outPutFile2.close()
                        outPutFile3.close()


##Merge Species files

speciesfiles = os.listdir(mergeDir + 'Species')
for file in speciesfiles:
	for name in cleanDiverNames:
		if name in file:
			outPutFile = open(mergeDir + '_Data/%s/%s%sspecies%s.nspe' % (name,computerName,name,proofingDate),'a')
			outPutFile2 = open(mergeDir + '_Data/Species/%s%sspecies%s.nspe' % (computerName,name,proofingDate), 'a')
                        outPutFile3 = open(mergeDir + '_Data/TotalMerge/speciesmerge.txt', 'a')
			linesReadFromFile = open(mergeDir + 'Species/%s' % file,'r').read()
                        outPutFile.write(linesReadFromFile)
			outPutFile2.write(linesReadFromFile)
                        outPutFile3.write(linesReadFromFile)
			outPutFile.close()
			outPutFile2.close()
			outPutFile3.close()


##Merge Substrate files

substratefiles = os.listdir(mergeDir + 'Substrate')
for file in substratefiles:
	for name in cleanDiverNames:
		if name in file:
			outPutFile = open(mergeDir + '_Data/%s/%s%ssubstrate%s.nsub' % (name,computerName,name,proofingDate),'a')
			outPutFile2 = open(mergeDir + '_Data/Substrate/%s%ssubstrate%s.nsub' % (computerName,name,proofingDate), 'a')
                        outPutFile3 = open(mergeDir + '_Data/TotalMerge/substratemerge.txt', 'a')
			linesReadFromFile = open(mergeDir + 'Substrate/%s' % file,'r').read()
                        outPutFile.write(linesReadFromFile)
			outPutFile2.write(linesReadFromFile)
			outPutFile3.write(linesReadFromFile)
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
			



