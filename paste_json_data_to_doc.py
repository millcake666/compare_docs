from spire.doc import *
from spire.doc.common import *
import os
import json
from word_to_html import word_to_html


def get_item(data: dict, key: int, keys: list):
    if key == len(keys) - 1:
        return data
    return get_item(data[keys[key]], key + 1, keys)


def paste_json(doc_old_path: str, doc_new_path: str, json_path: str, html_view_dir: str, export_to_html=False):
    with open(os.path.join(os.getcwd(), r'data\actual_document\html_view\tags_list.txt'), 'r+', encoding='utf-8') as tags_file:
        tags_list = [q[:-1] for q in tags_file.readlines()]

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

                    # вот тут заменили данные в полях
                    tmp_text = text.replace(p_data[1], str_to_replace)

                    # далее удаляем теги из полей
                    for tag in tags_list:
                        if tag in tmp_text:
                            tmp_text = tmp_text.replace(tag, '')
                    tmp_text = tmp_text.replace('$', '')

                    # пишем обновленный параграф в документ
                    s1.Paragraphs[para].Text = tmp_text

        for tab in range(s1.Tables.Count):
            for row in range(s1.Tables[tab].Rows.Count):
                for cell in range(s1.Tables[tab].Rows[row].Cells.Count):
                    for par in range(s1.Tables[tab].Rows[row].Cells[cell].Paragraphs.Count):
                        table_p = s1.Tables[tab].Rows[row].Cells[cell].Paragraphs[par]
                        table_text: str = table_p.Text

                        if '$' in table_text:
                            dollar_count = table_text.count('$') // 3

                            for i in range(1, 1 + 3 * (dollar_count - 1) + 1, 3):
                                p_data = table_text.split('$')[i:i + 2]
                                j_keys = p_data[0].split('-')

                                target_data = get_item(json_data, 0, j_keys)
                                str_to_replace = str(target_data[j_keys[-1]])

                                # вот тут заменили данные в полях
                                tmp_text = table_text.replace(p_data[1], str_to_replace)

                                # далее удаляем теги из полей
                                for tag in tags_list:
                                    if tag in tmp_text:
                                        tmp_text = tmp_text.replace(tag, '')
                                tmp_text = tmp_text.replace('$', '')

                                # пишем обновленный параграф в документ
                                s1.Tables[tab].Rows[row].Cells[cell].Paragraphs[par].Text = tmp_text

    document1.SaveToFile(doc_new_path, FileFormat.Docx2013)

    if export_to_html:
        word_to_html(doc_new_path, html_view_dir, 'actual_index')


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
