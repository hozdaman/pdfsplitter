from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from wtforms.validators import DataRequired


class UploadForm(FlaskForm):
     pdffile = FileField('pdfFile', validators=[DataRequired()])
     split = SubmitField('Split PDF')


# def upload(request):
#     form = UploadForm(request.POST)
#     if form.image.data:
#         image_data = request.FILES[form.image.name].read()
#         open(os.path.join(UPLOAD_PATH, form.image.data), 'w').write(image_data)
