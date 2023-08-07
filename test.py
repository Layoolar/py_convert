import os
import subprocess

def convert_to_pdf(input_file):
    output_file = os.path.splitext(input_file)[0] + ".pdf"
    command = ["unoconv", "-f", "pdf", input_file]
    subprocess.run(command, shell=True)
    return output_file

# Example usage:
input_file_path = "pptxm.pptx"  # Replace with the path to your PPTX or DOC file
output_pdf = convert_to_pdf(input_file_path)
print(f"File converted to PDF: {output_pdf}")