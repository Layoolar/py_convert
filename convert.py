# # import os
# # import subprocess

# # def convert_to_pdf(input_file):
# #     output_file = os.path.splitext(input_file)[0] + ".pdf"
# #     command = ["unoconv", "-f", "pdf", input_file]
# #     subprocess.run(command)
# #     return output_file

# # # Example usage:
# # input_file_path = "pptxm.pptx"  # Replace with the path to your PPTX or DOC file
# # output_pdf = convert_to_pdf(input_file_path)
# # print(f"File converted to PDF: {output_pdf}")


# import os
# import subprocess
# from flask import Flask, request, jsonify,flash,redirect
# from werkzeug.utils import secure_filename

# app = Flask(__name__)
# app.secret_key = b'_your_secret_key_here_'


# ALLOWED_EXTENSIONS = set([ 'pdf', 'pptx', 'docx'])

# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# path = os.getcwd()
# UPLOAD_FOLDER = os.path.join(path, 'uploads')

# if not os.path.isdir(UPLOAD_FOLDER):
#     os.mkdir(UPLOAD_FOLDER)

# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# # def convert_to_pdf(input_file):
# #     output_file = os.path.splitext(input_file)[0] + ".pdf"
# #     command = ["unoconv", "-f", "pdf", input_file]
# #     subprocess.run(command)
# #     return output_file

# # def convert_to_pdf(file_storage):
# #     input_file = os.path.join(app.config['UPLOAD_FOLDER'], file_storage.filename)
# #     output_file = os.path.splitext(input_file)[0] + ".pdf"
# #     # file_storage.save(input_file)  # Save the uploaded file
# #     command = ["unoconv", "-f", "pdf", input_file]
# #     subprocess.run(command)
# #     return output_file


# # @app.route('/convert', methods=['POST'])
# # def convert_file():
# #     try:
        
# #         if 'file' not in request.files:
# #             flash('No file part')
# #             return redirect(request.url)

# #         file = request.files['file']

# #         if file.filename == '':
# #             flash('No file selected for uploading')
# #             return redirect(request.url)

# #         if file and allowed_file(file.filename):
# #             # dee = convert_to_pdf(file)
# #             filename = secure_filename(file.filename)
# #             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
# #             flash('File successfully uploaded')
# #             return redirect('/')
# #         else:
# #             flash('Allowed file types are txt, pdf, png, jpg, jpeg, gif')
# #             return redirect(request.url)

# @app.route('/', methods=['GET','POST'])
# def upload_file():
#     if request.method == 'POST':

#         if 'file' not in request.files:
#             flash('No file part')
#             return redirect(request.url)

#         file = request.files['file']

#         if file.filename == '':
#             flash('No file selected for uploading')
#             return redirect(request.url)

#         if file and allowed_file(file.filename):
#             filename = secure_filename(file.filename)
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#             flash('File successfully uploaded')
#             return redirect('/')
#         else:
#             flash('Allowed file types are txt, pdf, png, jpg, jpeg, gif')
#             return redirect(request.url)


# if __name__ == "__main__":
#     app.run(host='127.0.0.1',port=5000)

