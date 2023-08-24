# from flask import Flask, request

# app = Flask(__name__)

# @app.route("/")
# def index():
#     return "Hello, World!"

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", debug=True)

from flask import Flask, request, send_file, Response, after_this_request
import subprocess
import os
import secrets
import atexit

app = Flask(__name__)

@app.route('/convert-docx', methods=['POST'])
def convert_file():
    try:
        uploaded_file = request.files['document']
        file_path = f'uploaded_{secrets.token_hex(8)}.docx'
        new_name = file_path.replace(".docx", ".pdf")

        uploaded_file.save(file_path)
        subprocess.run(['unoconv', '--format=pdf', file_path])

        def generate_pdf():
            with open(new_name, 'rb') as pdf_file:
                while True:
                    chunk = pdf_file.read(4096)
                    if not chunk:
                        break
                    yield chunk

        response = Response(
            generate_pdf(),
            content_type='application/pdf',
            headers={'Content-Disposition': f'attachment; filename={new_name}'}
        )

        @response.call_on_close
        def remove_file():
            if os.path.exists(new_name):
                os.remove(new_name)


        os.remove(file_path)

        atexit.register(lambda: os.remove(new_name))

        return response
    except Exception as e:
        return str(e)

@app.route('/convert-pptx', methods=['POST'])
def convert_pptx_file():
    try:
        uploaded_file = request.files['document']
        file_path = f'uploaded_{secrets.token_hex(8)}.pptx'
        new_name = file_path.replace(".pptx", ".pdf")
        uploaded_file.save(file_path)
        subprocess.run(['unoconv', '--format=pdf', file_path])       

        def generate_pdf_from_pptx():
            with open(new_name, 'rb') as pdf_file:
                while True:
                    chunk = pdf_file.read()
                    if not chunk:
                        break
                    yield chunk

        response = Response(generate_pdf_from_pptx(), content_type='application/pdf')

        @response.call_on_close
        def remove_file():
            if os.path.exists(new_name):
                os.remove(new_name)


        os.remove(file_path)

        atexit.register(lambda: os.remove(new_name))

        return response

        # os.remove(file_path) 
            
        # atexit.register(lambda: os.remove(new_name))

        # return Response(generate_pdf_from_pptx(), content_type='application/pdf')

    except Exception as e:
        return str(e)
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)
