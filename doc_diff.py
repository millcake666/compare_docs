from spire.doc import *
from spire.doc.common import *
from word_to_html import word_to_html
import os


def make_diff(file1_path: str, file2_path: str, output_file_path: str, html_filename: str):
    # Load the first document
    doc1 = Document()
    doc1.LoadFromFile(file1_path)
    # Load the second document
    doc2 = Document()
    doc2.LoadFromFile(file2_path)
    # Compare the two documents
    doc1.Compare(doc2, "user")
    # Save as docx file.
    doc1.SaveToFile(output_file_path, FileFormat.Docx2013)
    doc1.Close()
    doc2.Close()

    word_to_html(output_file_path, os.path.join(os.getcwd(), r'data\diff\result'), html_filename)

    with open(os.path.join(os.getcwd(), r'data\diff\result', html_filename + '.css'), 'r+', encoding='utf-8-sig') as css_file:
        data_css = css_file.readlines()
        for i, k in enumerate(data_css):
            if 'ins{color:' in k and 'del{color:' in k:
                data_css[i] = '   ins{color:#000000; background: #9BFFA191;}    del{color:#000000;  background-color:#ff000040;}'
                break

        css_file.writelines(data_css)


if __name__ == '__main__':
    inputFile1 = r"C:\Users\millcake\PycharmProjects\compare_docs\data\diff\Договор на поставку товара № 129-23.docx"
    inputFile2 = r"C:\Users\millcake\PycharmProjects\compare_docs\data\diff\Договор на поставку товара № 129-23 новый.docx"
    outputFile = r"C:\Users\millcake\PycharmProjects\compare_docs\data\diff\result\CompareDocuments.docx"

    make_diff(
        file1_path=inputFile1,
        file2_path=inputFile2,
        output_file_path=outputFile,
        html_filename='index'
    )
