from spire.doc import *
from spire.doc.common import *
from word_to_html import word_to_html
import os

from paste_json_data_to_doc import paste_json


def make_diff(doc_path: str, output_html_path: str, html_filename: str, old_json_path: str, new_json_path: str):
    path_to_first_doc = os.path.join(os.getcwd(), r'data\tmp\tmp_doc_old.docx')
    path_to_second_doc = os.path.join(os.getcwd(), r'data\tmp\tmp_doc_new.docx')
    path_to_diff_doc = os.path.join(os.getcwd(), r'data\diff\result\comparedDocx.docx')
    path_to_doc2html_after_updated = os.path.join(os.getcwd(), r'data\actual_document\html_view')

    # make doc with old data from json
    paste_json(doc_path, path_to_first_doc, old_json_path, path_to_doc2html_after_updated)
    # make doc with new data from json
    paste_json(doc_path, path_to_second_doc, new_json_path, path_to_doc2html_after_updated)

    # Load the first document
    doc1 = Document()
    doc1.LoadFromFile(path_to_first_doc)
    # Load the second document
    doc2 = Document()
    doc2.LoadFromFile(path_to_second_doc)
    # Compare the two documents
    doc1.Compare(doc2, "user")
    # Save as docx file.
    doc1.SaveToFile(path_to_diff_doc, FileFormat.Docx2013)
    doc1.Close()
    doc2.Close()

    word_to_html(path_to_diff_doc, output_html_path, html_filename)

    with open(os.path.join(output_html_path, html_filename + '.css'), 'r+', encoding='utf-8-sig') as css_file:
        data_css = css_file.readlines()
        for i, k in enumerate(data_css):
            if 'ins{color:' in k and 'del{color:' in k:
                data_css[i] = '   ins{color:#000000; background: #9BFFA191;}    del{color:#000000;  background-color:#ff000040;}'
                break

        css_file.writelines(data_css)


if __name__ == '__main__':
    make_diff(
        doc_path=r'C:\Users\millcake\PycharmProjects\compare_docs\data\actual_document\Договор на поставку товара № 129-23 with scope.docx',
        output_html_path=r'C:\Users\millcake\PycharmProjects\compare_docs\data\diff\result',
        html_filename=r'diff_index',
        old_json_path=r'C:\Users\millcake\PycharmProjects\compare_docs\data\data_fields\fields_from_form.json',
        new_json_path=r'C:\Users\millcake\PycharmProjects\compare_docs\data\data_fields\fields_from_form2.json'
    )
