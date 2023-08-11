from flask import Flask, request, send_file, Response
import subprocess
import os

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        print('start')
        uploaded_file = request.files['document']
        
        # Save the uploaded file
        file_path = 'uploaded.pptx'
        uploaded_file.save(file_path)
        print('mid')
        # Convert the uploaded PPTX file to PDF using unoconv and LibreOffice
        pdf_file_path = 'uploaded.pdf'
        subprocess.run(['unoconv', '--format=pdf', file_path])
        print('fin')
        # Send the converted PDF as a response
        # return send_file(pdf_file_path, as_attachment=True)
        with open(pdf_file_path, 'rb') as pdf_file:
            response = Response(pdf_file.read(), content_type='application/pdf')
            response.headers['Content-Disposition'] = 'attachment; filename=result.pdf'
            return response
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
