from flask import Flask, render_template, request, flash, redirect, url_for
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = 'static'
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__, template_folder='templates')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'A301DMdm1@'


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/edit', methods=['GET','POST'])
def edit ():
    if request.method=='POST':
        return 'yet to complete'
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)

        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('File uploaded successfully')
            return redirect(url_for('hello_world'))

    return render_template("upload.html")




if __name__ == '__main__':
    app.run(debug=True)
