from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os, subprocess

app = Flask(__name__)

# Specify the directory where uploaded files will be stored
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

PDF_FOLDER = 'pdfs'
app.config['PDF_FOLDER'] = PDF_FOLDER


# Limit the allowed file extensions (you can customize this list)
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','pptx','docx'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def convert_to_pdf(input_file):
    output_file = os.path.splitext(input_file)[0] + ".pdf"
    pdf_path = os.path.join(app.config['PDF_FOLDER'], output_file)
    command = ["unoconv", "-f", "pdf", "-o", pdf_path, input_file]
    subprocess.run(command)
    return pdf_path

@app.route('/upload', methods=['POST'])
def upload_file():
    # Check if the POST request has the file part
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['file']
    
    # If the user does not select a file, the browser might
    # submit an empty part without a filename
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save((file_path))
        
        pdf_file = convert_to_pdf(file_path)

        
        return jsonify({"message": "File uploaded successfully"}), 200
    else:
        return jsonify({"error": "Invalid file extension"}), 400

if __name__ == '__main__':
    app.run(debug=True)
