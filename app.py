from flask import Flask, request, redirect, url_for
import os
from werkzeug import secure_filename

UPLOAD_DIR = '/home/doug/uploads'
ALLOWED_EXT = set(['doc', 'txt'])

app = Flask("Unbiased")
app.config['UPLOAD_DIR'] = UPLOAD_DIR


@app.route("/", methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and check_extention(file.filename):
            filename = secure_file(file.filename)
            file.save(os.path.join(app.config['UPLOAD_DIR'], filename))
            return redirect(url_for('upload_file', filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''
    


def check_extention(filename):
    if filename.rsplit('.', 1)[1] in ALLOWED_EXT:
        return

if __name__ == "__main__":
    app.run(debug=True)
