import os
from PIL import Image
from flask import Blueprint, render_template,  request,send_file
# from flask_wtf import FlaskForm
from werkzeug.utils import secure_filename
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
import stepic
from flask import Flask
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/files'

code = Blueprint("code", __name__)

class UploadFileForm(FlaskForm):
    file = FileField("File")
    submit = SubmitField("Upload File")


@code.route('/encode',methods=['GET', "POST"])
def en():
    form = UploadFileForm()
    
    if form.validate_on_submit():
        
        file = form.file.data # First grab the file
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename))) # Then save the file
        name= file.filename
        global Gname
        Gname = name
        im = Image.open(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename)))
        data = request.form['u']
        imgConv = im.convert("RGB")
        im1 = stepic.encode(imgConv, bytes(str(data), encoding='utf-8'))
        os.remove(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename)))
        im1.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename)))
        
        return render_template("download.html")
    return render_template("encode.html", form=form)


@code.route('/decode',methods=['GET', "POST"])
def de():
    form = UploadFileForm()
    
    if form.validate_on_submit():
        
        file = form.file.data # First grab the file
        
        name= file.filename

        im2 = Image.open(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename)))
        stegoImage = stepic.decode(im2)
        return stegoImage
    return render_template("decode.html", form=form)

@code.route('/download',methods=['GET', "POST"])
def do():
    p = os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(Gname))
    return send_file(p,as_attachment=True)
