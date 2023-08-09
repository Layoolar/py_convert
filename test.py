from flask import Flask, request, jsonify, send_file
from werkzeug.utils import secure_filename
import os, subprocess
from io import BytesIO

app = Flask(__name__)

# Specify the directory where uploaded files will be stored
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

PDF_FOLDER = 'pdfs'
app.config['PDF_FOLDER'] = PDF_FOLDER

# Limit the allowed file extensions (you can customize this list)
ALLOWED_EXTENSIONS = {'pptx', 'docx'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def convert_to_pdf(file_stream):
    pdf_stream = BytesIO()
    command = ["unoconv", "-f", "pdf", "-o", pdf_stream.name, "--stdin"]
    process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    process.communicate(input=file_stream.read())
    pdf_stream.seek(0)
    return pdf_stream

@app.route('/upload', methods=['POST'])
def upload_file():
    # Check if the POST request has the file part
    if 'file' not in request.files:
        print(request)
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['file']
    
    # If the user does not select a file, the browser might
    # submit an empty part without a filename
    if file.filename == '':
        print("err2")
        return jsonify({"error": "No selected file"}), 400
    
    if file and allowed_file(file.filename):
        pdf_stream = convert_to_pdf(file)
        
        return send_file(
            pdf_stream,
            as_attachment=True,
            attachment_filename="converted.pdf",
            mimetype="application/pdf"
        )
    else:
        return jsonify({"error": "Invalid file extension"}), 400

if __name__ == '__main__':
    app.run(debug=True)
