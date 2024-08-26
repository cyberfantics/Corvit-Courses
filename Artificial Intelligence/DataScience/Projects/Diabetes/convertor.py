import os
from nbconvert import PDFExporter
import nbformat

def convert_notebook_to_pdf(notebook_path, output_path):
    # Load the notebook
    with open(notebook_path, 'r', encoding='utf-8') as notebook_file:
        notebook_content = notebook_file.read()

    # Convert notebook content to a notebook object
    notebook_node = nbformat.reads(notebook_content, as_version=4)

    # Create a PDF exporter instance
    pdf_exporter = PDFExporter()

    # Export notebook to PDF
    pdf_data, _ = pdf_exporter.from_notebook_node(notebook_node)

    # Write PDF data to file
    with open(output_path, 'wb') as pdf_file:
        pdf_file.write(pdf_data)

    print(f'Notebook successfully converted to PDF and saved as {output_path}')

# Example usage
notebook_path = 'Patient Health Analysis.ipynb'  # Replace with your notebook file path
output_path = 'your_notebook.pdf'      # Replace with desired output file path
convert_notebook_to_pdf(notebook_path, output_path)
