import os
import subprocess
import datetime

def convert_to_pdf(input_file):
    time=datetime.datetime.now()
    print("started:", time)
    output_file = os.path.splitext(input_file)[0] + ".pdf"
    command = ["unoconv", "-f", "pdf", input_file]
    subprocess.run(command)
    end=datetime.datetime.now()
    print("ed:", end)
    return output_file

# Example usage:
input_file_path = "pptxm.pptx"  # Replace with the path to your PPTX or DOC file
output_pdf = convert_to_pdf(input_file_path)
print(f"File converted to PDF: {output_pdf}")
