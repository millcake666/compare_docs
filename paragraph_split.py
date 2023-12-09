from spire.doc import *
from spire.doc.common import *
import os


def get_paragraph_list(file_path: str, is_save_txt_file: bool = False) -> list:
    # Create Word document1.
    document1 = Document()

    # Load the file from disk.
    document1.LoadFromFile(file_path)

    # Create a new document.
    document2 = Document()

    # Get paragraph 1 and paragraph 2 in document1.
    for sect in range(document1.Sections.Count):
        s = document1.Sections[sect]
        for para in range(s.Paragraphs.Count):
            p1 = s.Paragraphs[para]
            if p1.Text.isupper():
                continue
            # Copy p1 and p2 to document2.
            s2 = document2.AddSection()
            NewPara1 = p1.Clone()
            s2.Paragraphs.Add(NewPara1)

    # Save the file.
    document2.SaveToFile(os.path.join(os.getcwd(), r'data\temp\file.txt'), FileFormat.Txt)
    document2.Close()

    with open(os.path.join(os.getcwd(), r'data\temp\file.txt'), 'r+', encoding='utf-8') as file:
        txt = file.readlines()[1:]

    result = [t for t in txt if t != '\n']

    if is_save_txt_file:
        with open(os.path.join(os.getcwd(), r'data\txt_doc\extracted_txt_paragraph.txt'), 'w', encoding='utf-8') as f:
            f.writelines(result)

    return result


if __name__ == '__main__':
    res = get_paragraph_list(
        file_path=r"C:\Users\millcake\PycharmProjects\compare_docs\data\Договор на поставку товара № 129-23.docx",
        is_save_txt_file=False
    )

    print(res)
