from PyPDF2 import PdfMerger

pdfs=['pdf_file_name01.pdf','pdf_file_name02.pdf'] #write here pdf files names , which you want to merge those files

merger=PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write('merge.pdf') #here this is the merge file name 'merge.pdf
merger.close()



































# from PyPDF2 import PdfMerger

# pdfs=['a.pdf','b.pdf']

# merger= PdfMerger()


# for pdf in pdfs:
#     merger.append(pdf)

# merger.write('merge.pdf')
# merger.close()









