import os
import win32com.client

def convert_to_pdf(input_file):
    output_file = os.path.splitext(input_file)[0] + ".pdf"
    
    powerpoint = win32com.client.Dispatch("PowerPoint.Application")
    presentation = powerpoint.Presentations.Open(input_file)
    presentation.SaveAs(output_file, 32)  # 32 represents PDF format
    presentation.Close()
    
    powerpoint.Quit()
    
    return output_file

# Example usage:
input_file_path = "pptxm.pptx"  # Replace with the path to your PPTX file
output_pdf = convert_to_pdf(input_file_path)
print(f"File converted to PDF: {output_pdf}")


# pip install pywin32