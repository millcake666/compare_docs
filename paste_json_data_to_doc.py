from spire.doc import *
from spire.doc.common import *
import os
import json

DOC_PATH_OLD = r'C:\Users\millcake\PycharmProjects\compare_docs\data\actual_document\Договор на поставку товара № 129-23 with scope.docx'
DOC_PATH_NEW = r'C:\Users\millcake\PycharmProjects\compare_docs\data\actual_document\Договор на поставку товара № 129-23 with scope2.docx'
JSNO_PATH = r'C:\Users\millcake\PycharmProjects\compare_docs\data\data_fields\fields_from_form.json'

# actual doc
document1 = Document()
document1.LoadFromFile(DOC_PATH_OLD)

# new actual doc
document2 = Document()

with open(JSNO_PATH, 'r', encoding='utf-8') as f:
    json_data = json.load(f)


def get_item(data: dict, key: int, keys: list):
    if key == len(keys) - 1:
        return data
    return get_item(data[keys[key]], key + 1, keys)


for sect in range(document1.Sections.Count):
    s1 = document1.Sections[sect]

    for para in range(s1.Paragraphs.Count):
        p1 = s1.Paragraphs[para]
        text: str = p1.Text

        if '$' in text:
            p_data = text.split('$')[1:3]
            j_keys = p_data[0].split('-')

            target_data = get_item(json_data, 0, j_keys)
            str_to_replace = target_data[j_keys[-1]]

            s1.Paragraphs[para].Text = text.replace(p_data[1], str_to_replace)
            print(s1.Paragraphs[para].Text)

document1.SaveToFile(DOC_PATH_NEW, FileFormat.Docx2013)
