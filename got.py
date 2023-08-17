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

import subprocess
from io import BytesIO

def convert_to_pdf(file_data):
    pdf_path = os.path.join(app.config['PDF_FOLDER'], "out.pdf")
    pdf_stream = BytesIO()
    command = ["unoconv", "-f", "pdf", "-o", pdf, "--stdin"]
    
    if isinstance(file_data, bytes):
        # If file_data is already bytes, use it directly
        process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        process.communicate(input=file_data)
    elif isinstance(file_data, str):
        # If file_data is a file path, read the file and pass its content
        with open(file_data, 'rb') as file:
            process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
            process.communicate(input=file.read())

    pdf_stream.seek(0)
    return pdf_stream



# @app.route('/upload', methods=['POST'])
# def upload_file():
#     print("hi")
#     file_data = request.data
#     print("first")
#     if not file_data:
#         print("No file data received")
    
    
#     if file_data:
#         print("received")
#     # Check if the POST request has the file part
#     # if 'file' not in request.files:
#     #     print("err1")
#     #     print(request)
#     #     return jsonify({"error": "No file part"}), 400
    
#     # file = request.files['file']
    
#     # If the user does not select a file, the browser might
#     # submit an empty part without a filename
#     print('third')

#     if file_data:
#         pdf_stream = convert_to_pdf(file_data)
#         print("last")
#         return send_file(
#             pdf_stream,
#             as_attachment=True,
#             attachment_filename="converted.pdf",
#             mimetype="application/pdf"
#         )
#     else:
#         return jsonify({"error": "Invalid file extension"}), 400

@app.route('/upload', methods=['POST'])
def upload_file():
    file_data = request.data

    if not file_data:
        print("1")
        return jsonify({"error": "No file data received"}), 400
    if file_data:
        print("2")
    pdf_stream = convert_to_pdf(file_data)
    print("3")
    return send_file(
        pdf_stream,
        as_attachment=True,
        attachment_filename="converted.pdf",
        mimetype="application/pdf"
    )

if __name__ == '__main__':
    app.run(debug=True)
