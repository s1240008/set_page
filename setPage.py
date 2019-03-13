import PyPDF2
'''
merger = PyPDF2.PdfFileMerger()

merger.append('sample1.pdf',pages=(1,2))
merger.append('sample2.pdf')
merger.append('sample3.pdf')

merger.write('sample_merge.pdf')
merger.close()
'''

#readfp="jikobunsekiWithNull.pdf"
#readfp="kigyoukenkyuuWithNull.pdf"
readfp="mensetsujyunbiWithNull.pdf"

#writefp="jikobunseki.pdf"
#writefp="kigyoukenkyuu.pdf"
writefp="mensetsujyunbi.pdf"
'''
lastP=37
nullP=38
allP=38

lastP=33
nullP=34
allP=34
'''
lastP=40
nullP=41
allP=41


useP=int(allP/4)
if allP%4:
    useP+=1

print useP

reader1 = PyPDF2.PdfFileReader(readfp)
#reader2 = PyPDF2.PdfFileReader('sample2.pdf')

writer = PyPDF2.PdfFileWriter()

for i in range(0,useP):
    p0=4*useP-(2*i)
    p1=2*i+1
    p2=2*i+2
    p3=4*useP-(2*i+1)
    
    if lastP!=0:
        if p0==lastP:
            p0=nullP
        elif p1==lastP:
            p1=nullP
        elif p2==lastP:
            p2=nullP
        elif p3==lastP:
            p3=nullP

    if p0>allP:
        p0=nullP
    if i==0 and lastP!=0:
        p0=lastP
    if p3>allP:
        p3=nullP

    p0-=1
    p1-=1
    p2-=1
    p3-=1

    '''
    print p0
    print p1
    print p2
    print p3
    '''



    writer.addPage(reader1.getPage(p0))
    writer.addPage(reader1.getPage(p1))
    writer.addPage(reader1.getPage(p2))
    writer.addPage(reader1.getPage(p3))


#writer.addPage(reader2.getPage(2))

with open(writefp, 'wb') as f:
    writer.write(f)
