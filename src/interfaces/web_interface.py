from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
from plugin_interface import load_model

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './uploads'

@app.route('/upload', methods=['POST'])
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Load and process the 3D model
        mesh = load_model(file_path)
        print(mesh)

        return 'File uploaded successfully'
    else:
        return 'No file uploaded'
