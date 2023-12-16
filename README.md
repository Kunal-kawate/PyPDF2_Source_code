# PyPDF2_Source_code
PyPDF2 is a free and open-source pure-python PDF library capable of splitting, merging, cropping, and transforming the pages of PDF files.

# PDF Merger using PyPDF2

This Python script utilizes the PyPDF2 library to merge multiple PDF files into a single PDF file. It is a straightforward tool that can be easily customized based on your requirements.

## Usage

1. Install PyPDF2 using the following command:

    ```bash
    pip install PyPDF2
    ```

2. Update the script with the names of the PDF files you want to merge. Modify the `pdfs` list by replacing 'Enter_your_pdf_file_name01.pdf' and 'Enter_your_pdf_file_name02.pdf' with your actual PDF file names.

    ```python
    from PyPDF2 import PdfMerger

    pdfs = ['Enter_your_pdf_file_name01.pdf', 'Enter_your_pdf_file_name02.pdf']
    merger = PdfMerger()

    for pdf in pdfs:
        merger.append(pdf)

    merger.write('merge.pdf')  # Output merged file name 'merge.pdf'
    merger.close()
    ```

3. Run the script to execute the PDF merging:

    ```bash
    python pypdf.py
    ```

## Requirements

- Python 3.x
- PyPDF2 library

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to contribute, report issues, or suggest improvements!


