from word_tools.ToHtmlExport import word2html
import os
from word_tools import view_html

# !pip install plum-dispatch


def main():
    base_dir = os.path.join(os.path.abspath(os.getcwd()), 'data')
    docx_path = 'Договор на поставку товара № 129-23.docx'
    save_dir = 'html_doc'
    export_filename = 'index'
    word2html(export_filename, os.path.join(base_dir, docx_path), os.path.join(base_dir, save_dir))

    view_html.prepare_to_view(os.path.join(base_dir, save_dir, export_filename + '.html'))


if __name__ == '__main__':
    main()
