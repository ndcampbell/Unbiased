from flask import Flask, request, redirect, url_for, render_template
import os
from werkzeug import secure_filename

UPLOAD_DIR = '/home/doug/uploads'
ALLOWED_EXT = set(['doc', 'txt'])

app = Flask("Unbiased")
app.config['UPLOAD_DIR'] = UPLOAD_DIR


@app.route("/<filename>", methods=['GET', 'POST'])
@app.route("/", methods=['GET', 'POST'], defaults={'filename': None})
def upload_file(filename):
    if request.method == 'POST':
        file = request.files['file']
        if file and check_extention(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_DIR'], filename)
            file.save(filepath)
            return redirect(url_for('upload_file', filename=filename))
    return render_template('upload.html', filename=filename)


def check_extention(filename):
    if filename.rsplit('.', 1)[1] in ALLOWED_EXT:
        return True
    else:
        print "%s does not contain approved extention" % filename
        return False
    

if __name__ == "__main__":
    app.run(debug=True)
