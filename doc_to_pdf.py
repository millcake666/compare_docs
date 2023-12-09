from spire.doc import *
from spire.doc.common import *
import os


def doc_to_pdf(word_path: str, save_dir_path: str, pdf_filename: str):
    # Create word document
    document = Document()
    document.LoadFromFile(word_path)
    # Save the document to a PDF file.
    document.SaveToFile(os.path.join(save_dir_path, pdf_filename + '.pdf'), FileFormat.PDF)
    document.Close()


if __name__ == '__main__':
    doc_to_pdf(
        word_path=r'C:\Users\millcake\PycharmProjects\compare_docs\data\diff\Договор на поставку товара № 129-23.docx',
        save_dir_path=r'C:\Users\millcake\PycharmProjects\compare_docs\data\pdf_doc',
        pdf_filename='result'
    )
