
# # importing the required modules
# import PyPDF2


# def PDFsplit(pdf, splits):
#     # creating input pdf file object
#     pdfFileObj = open(pdf, 'rb')

#     # creating pdf reader object
#     pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

#     # starting index of first slice
#     start = 0

#     # starting index of last slice
#     end = splits[0]

#     for i in range(len(splits)+1):
#         # creating pdf writer object for (i+1)th split
#         pdfWriter = PyPDF2.PdfFileWriter()

#         # output pdf file name
#         outputpdf = pdf.split('.pdf')[0] + str(i) + '.pdf'

#         # adding pages to pdf writer object
#         for page in range(start, end):
#             pdfWriter.addPage(pdfReader.getPage(page))

#         # writing split pdf pages to pdf file
#         with open(outputpdf, "wb") as f:
#             pdfWriter.write(f)

#         # interchanging page split start position for next split
#         start = end
#         try:
#             # setting split end position for next split
#             end = splits[i+1]
#         except IndexError:
#             # setting split end position for last split
#             end = pdfReader.numPages

#     # closing the input pdf file object
#     pdfFileObj.close()


# def main():
#     # pdf file to split
#     pdf = '/Users/hozdaman/Downloads/example.pdf'

#     # split page positions
#     splits = [1, 2, 3, 4, 5, 6, 7]

#     # calling PDFsplit function to split pdf
#     PDFsplit(pdf, splits)


# if __name__ == "__main__":
#     # calling the main function
#     main()


# pdf_splitter.py

# import os
# from PyPDF2 import PdfFileReader, PdfFileWriter


# def pdf_splitter(path):
#     fname = os.path.splitext(os.path.basename(path))[0]

#     pdf = PdfFileReader(path)
#     for page in range(pdf.getNumPages()):
#         pdf_writer = PdfFileWriter()
#         pdf_writer.addPage(pdf.getPage(page))

#         output_filename = '{}_page_{}.pdf'.format(
#             fname, page+1)

#         with open(output_filename, 'wb') as out:
#             pdf_writer.write(out)

#         print('Created: {}'.format(output_filename))


# if __name__ == '__main__':
#     path = 'example.pdf'
#     pdf_splitter(path)
