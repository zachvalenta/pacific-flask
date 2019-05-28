import csv
import os

from dotenv import find_dotenv, load_dotenv
from flask import Flask, flash, request, redirect, url_for, send_from_directory, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename

app = Flask(__name__)

# conf for msg flash
load_dotenv(find_dotenv())
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY").encode()

# uploads
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['UPLOAD_FOLDER'] = os.path.join(basedir, 'uploads')
ALLOWED_EXTENSIONS = set(['txt', 'csv'])

# db
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, 'local.db')
db = SQLAlchemy(app)
import models
db.create_all()


def parse_upload(path):
    with open(path, 'r') as f:
        data = list(csv.reader(f, delimiter='\t'))
        for row in data:
            record = models.Input(
                name_first=row[1],
                name_last=row[2],
                address=row[3],
                state=row[4],
                zip=row[5],
                status=row[6],
                product_id=row[7],
                product_name=row[8],
                product_amount=row[9],
            )
            db.session.add(record)
            db.session.commit() 


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            parse_upload(filepath)
            flash('uploaded file')
            return redirect(url_for('upload_file'))
    return render_template('index.html')
    

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

