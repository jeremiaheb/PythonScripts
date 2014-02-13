import matplotlib.pyplot as plot
import xlrd
from matplotlib.backends.backend_pdf import PdfPages
import time
from collections import defaultdict

xls = r'C:\Users\jblondeau\Desktop\FromKirk\sefcri2013_verify\SEFCRI2013_All_Data.xlsx'
masterSppxls = r'C:\Users\jblondeau\Desktop\FromKirk\sefcri2013_verify\species_master_FL.xls'
sheet = u"species_corrected"
outFigure = r'C:\Users\jblondeau\Desktop\FromKirk\sefcri2013_verify\pdfs\SppQAQC_Graphs09.pdf'

wb = xlrd.open_workbook(xls)
sppSheet = wb.sheet_by_name(sheet)

masterSppWb = xlrd.open_workbook(masterSppxls)
masterSppSheet = masterSppWb.sheet_by_name(u'species')
masterSppDict = defaultdict()
for row in range(1, masterSppSheet.nrows):
    masterSppDict[masterSppSheet.cell_value(row, 0)] = masterSppSheet.cell_value(row, 2), masterSppSheet.cell_value(row, 7)
    

SpeciesList = sorted(list(set([sppSheet.cell_value(row,1) for row in range(1, sppSheet.nrows)])))
##SpeciesList = sorted(list(set([sppSheet.cell_value(row,1) for row in range(1, 50)])))
##SpeciesList = ['EPI MORI']

def SppPlots():
    pp = PdfPages(outFigure)
    for Species in SpeciesList[250:300]:
        sppFilter =[sppSheet.row_values(row, start_colx=0, end_colx=8) for row in range(1, sppSheet.nrows) if sppSheet.cell_value(row, 1)== Species]
        abundList = [line[2] for line in sppFilter]
        meanList = [line[3] for line in sppFilter]
        minList = [line[4] for line in sppFilter]
        maxList = [line[5] for line in sppFilter]
        fig = plot.figure()
        abund = fig.add_subplot(221)
        abund.hist(abundList, lw = .5, bins=20)
        plot.title(Species)
        plot.xlabel('N')
        mean = fig.add_subplot(222)
        mean.hist(meanList, lw = .5, bins=20)
        plot.title(masterSppDict[Species][0])
        plot.xlabel('Mean')
        mini = fig.add_subplot(223)
        mini.hist(minList, lw = .5, bins=20)
        plot.xlabel('Min')
        maxi = fig.add_subplot(224)
        maxi.hist(maxList, lw = .5, bins=20)
        plot.xlabel('Max')
        plot.annotate('Max Size', xy=(.70,.85), xycoords='axes fraction')
        plot.annotate(masterSppDict[Species][1], xy=(.70, .75), xycoords='axes fraction')
        plot.savefig(pp, format='pdf')
    pp.close()

def main():
    start = time.time()
    SppPlots()
    ##print len(SpeciesList)
    print str(time.time() - start) + ' seconds to execute script'

if __name__=='__main__':
    main()





