from spire.doc import *
from spire.doc.common import *
import os
import json
from word_to_html import word_to_html


def get_item(data: dict, key: int, keys: list):
    if key == len(keys) - 1:
        return data
    return get_item(data[keys[key]], key + 1, keys)


def remove_tags_from_html(html_path: str, tags_list_path: str):
    with open(tags_list_path, 'r+', encoding='utf-8') as tags_file:
        tags_list = [q[:-1] for q in tags_file.readlines()]
        # print(tags_list)

    with open(html_path, 'r+', encoding='utf-8') as file:
        html = file.readlines()

        for i, h in enumerate(html):
            if '$' in h:
                for tag in tags_list:
                    if tag in h:
                        html[i] = h.replace(tag, '')
                        html[i] = html[i].replace('$', '')

    with open(html_path, 'w', encoding='utf-8') as f:
        f.writelines(html)


def paste_json(doc_old_path: str, doc_new_path: str, json_path: str, html_view_dir: str):
    # actual doc
    document1 = Document()
    document1.LoadFromFile(doc_old_path)

    with open(json_path, 'r', encoding='utf-8') as f:
        json_data = json.load(f)

    for sect in range(document1.Sections.Count):
        s1 = document1.Sections[sect]

        for para in range(s1.Paragraphs.Count):
            p1 = s1.Paragraphs[para]
            text: str = p1.Text

            if '$' in text:
                dollar_count = text.count('$') // 3

                for i in range(1, 1 + 3 * (dollar_count - 1) + 1, 3):
                    p_data = text.split('$')[i:i + 2]
                    j_keys = p_data[0].split('-')

                    target_data = get_item(json_data, 0, j_keys)
                    str_to_replace = str(target_data[j_keys[-1]])

                    s1.Paragraphs[para].Text = text.replace(p_data[1], str_to_replace)

        # ... добавить изменение данных в таблицах

    document1.SaveToFile(doc_new_path, FileFormat.Docx2013)

    word_to_html(doc_new_path, html_view_dir, 'actual_index')

    remove_tags_from_html(os.path.join(html_view_dir, 'actual_index.html'), os.path.join(html_view_dir, 'tags_list.txt'))




if __name__ == '__main__':
    DOC_PATH_OLD = r'C:\Users\millcake\PycharmProjects\compare_docs\data\actual_document\Договор на поставку товара № 129-23 with scope.docx'
    DOC_PATH_NEW = r'C:\Users\millcake\PycharmProjects\compare_docs\data\actual_document\Договор на поставку товара № 129-23 with scope2.docx'
    JSON_PATH = r'C:\Users\millcake\PycharmProjects\compare_docs\data\data_fields\fields_from_form.json'

    paste_json(
        doc_old_path=DOC_PATH_OLD,
        doc_new_path=DOC_PATH_NEW,
        json_path=JSON_PATH,
        html_view_dir=r'C:\Users\millcake\PycharmProjects\compare_docs\data\actual_document\html_view'
    )
