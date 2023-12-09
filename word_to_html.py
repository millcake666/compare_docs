from word_tools.ToHtmlExport import word2html
import os
from word_tools import view_html


def word_to_html(word_path: str, save_dir_path: str, html_filename: str):
    word2html(html_filename, word_path, save_dir_path)
    view_html.prepare_to_view(os.path.join(save_dir_path, html_filename + '.html'))


if __name__ == '__main__':
    word_to_html(
        word_path=r'C:\Users\millcake\PycharmProjects\compare_docs\data\diff\result\CompareDocuments.docx',
        save_dir_path=r'C:\Users\millcake\PycharmProjects\compare_docs\data\diff\result',
        html_filename='index'
    )
