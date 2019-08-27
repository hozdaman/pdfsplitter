from flask import render_template, flash, redirect
from app import app
from app.forms import UploadForm
import os
from PyPDF2 import PdfFileReader, PdfFileWriter

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = UploadForm()
    if form.validate_on_submit():
        pdfsplit = form.pdffile
        pdf = PdfFileReader([pdfsplit])
        
        for page in range(pdf.getNumPages()):
            pdf_writer = PdfFileWriter()
            pdf_writer.addPage(pdf.getPage(page))

            output_filename = '{}_page_{}.pdf'.format(
                pdfsplit, page+1)

            with open(output_filename, 'wb') as out:
                pdf_writer.write(out)

            print('Created: {}'.format(output_filename))

        return redirect('/index')











    return render_template('index.html', title='Home', form=form)
