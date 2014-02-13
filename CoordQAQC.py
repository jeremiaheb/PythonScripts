
import math
from collections import defaultdict



def DefaultDict():
    return defaultdict(DefaultDict)

def DminToDdeg(degree, minute):
    return degree + (minute/60)

    
def distBtStns(lat1, lon1, lat2, lon2):
    y1 = math.fabs(lat1) * 3.141593/180
    y2 = math.fabs(lat2) * 3.141593/180
    x1 = math.fabs(lon1) * 3.141593/180
    x2 = math.fabs(lon2) * 3.141593/180
    v = math.sin(y1)* math.sin(y2)+ math.cos(y1)* math.cos(y2)* math.cos(x2-x1)
    return 6371000 * (math.atan ( -v / math.sqrt ( -v * v+1 ) ) + 2 * math.atan ( 1 ))


coordsFromTextFile = [ line.strip().split() for line in open(r'C:\Users\jblondeau\Desktop\FromKirk\sefcri2013_verify\actual_latlon_sef2013.txt').readlines()]

sampleIDCoordDict = DefaultDict()

#for row in coordsFromTextFile:
#    sampleIDCoordDict[row[2]][row[3]]= DminToDdeg(float(row[4]),float(row[5])), DminToDdeg(float(row[6]), float(row[7]))

for row in coordsFromTextFile:
    sampleIDCoordDict[row[1]][row[2]]= float(row[3]), float(row[4])

sampleIDDistanceBetweenStations = {}
   
for sampleID in sampleIDCoordDict:
    try:
        sampleIDDistanceBetweenStations[sampleID] = distBtStns(sampleIDCoordDict[sampleID]['1'][0],sampleIDCoordDict[sampleID]['1'][1],sampleIDCoordDict[sampleID]['2'][0],sampleIDCoordDict[sampleID]['2'][1])   
    except ZeroDivisionError:
        if sampleIDCoordDict[sampleID]['1'][0] == sampleIDCoordDict[sampleID]['2'][0] and sampleIDCoordDict[sampleID]['1'][1] == sampleIDCoordDict[sampleID]['2'][1]:
            sampleIDDistanceBetweenStations[sampleID] = 0
    except TypeError:
        print 'Type error on   ', sampleID
    except ValueError:
        print 'ValueError   ', sampleID

        
for site in sorted(sampleIDDistanceBetweenStations, key=sampleIDDistanceBetweenStations.get, reverse=True):
    if sampleIDDistanceBetweenStations[site] > 100:
        print site,'-----', sampleIDDistanceBetweenStations[site]


    
