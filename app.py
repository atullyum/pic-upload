from flask import Flask, render_template, request , flash,    url_for
from werkzeug.utils import secure_filename
import os
UPLOAD_FOLDER = 'static'
ALLOWED_EXTENSIONS = { 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')
@app.route('/about')
def about() :
    return render_template("about.html")
@app.route('/edit', methods=['GET','POST'])
def edit ():
    if request.method=='POST':
        @app.route('/', methods=['GET', 'POST'])
        def upload_file():
            if request.method == 'POST':

                if 'file' not in request.files:
                    flash('No file part')
                    return render_template("error.html")
                file = request.files['file']
                # If the user does not select a file, the browser submits an
                # empty file without a filename.
                if file.filename == '':
                    flash('No selected file')
                    return "error "#file agar nhi upload ki toh
                if file and allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    file.save(os.path.join(app.config['static'], filename))
                    return render_template("index.html")
            return
if __name__ == '__main__':
    app.run(debug=True)
