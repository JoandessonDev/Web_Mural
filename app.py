import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__, template_folder='templates', static_folder='static') 
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'upload')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():

    file = request.files['arquivo']
    savePath = os.path.join(UPLOAD_FOLDER, secure_filename(file.filename))
    file.save(savePath)
    return '<p><strong>Upload efetuado com sucesso!</strong></p>'

if (__name__ == '__main__'):  
    app.run(debug = True)