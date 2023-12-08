import os
from word_tools.pretty_word import STRING


def prepare_to_view(file_path: str):
    with open(file_path, 'r', encoding='utf-8-sig') as file_read:
        html = file_read.readlines()
        html[0] = html[0].replace(STRING, '')

    with open(file_path, 'w', encoding='utf-8-sig') as file_write:
        file_write.writelines(html)


if __name__ == '__main__':
    base_dir = os.path.join(os.path.abspath(os.getcwd()), '../data')
    save_dir = 'html_doc'
    export_filename = 'index'

    prepare_to_view(os.path.join(base_dir, save_dir, export_filename + '.html'))
