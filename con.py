from flask import Flask, request, send_file, Response
import subprocess
import os

app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def convert_file():
    try:
        uploaded_file = request.files['file']
        
        # name = request.form['name']
        # new_name = name.replace(".pptx", ".pdf")
        # print(new_name)
        # Save the uploaded file
        file_path = 'uploaded.pptx'
        print(file_path)
        new_name = file_path.replace(".pptx", ".pdf")
        print(new_name)
        uploaded_file.save(file_path)

        # Convert the file using unoconv
        subprocess.run(['unoconv', '--format=pdf', file_path])

        # Send the converted PDF as a response stream
        def generate_pdf():
            with open('uploaded.pdf', 'rb') as pdf_file:
                while True:
                    chunk = pdf_file.read()
                    if not chunk:
                        break
                    yield chunk

            os.remove(file_path)  # Remove temporary files after streaming
        return Response(generate_pdf(), content_type='application/pdf')

    except Exception as e:
        return str(e)
    

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
