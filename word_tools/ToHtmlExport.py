from spire.doc import *
from spire.doc.common import *
import os


def word2html(html_filename: str, file_word_path: str, file_html_path_to_save: str):
    inputFile = file_word_path
    outputFile = html_filename + '.html'
    # Open a Word document.
    document = Document()
    document.LoadFromFile(inputFile)
    # Set whether the css styles are embeded or not.
    document.HtmlExportOptions.CssStyleSheetFileName = html_filename + '.css'
    document.HtmlExportOptions.CssStyleSheetType = CssStyleSheetType.External
    # Set whether the images are embeded or not.
    document.HtmlExportOptions.ImageEmbedded = False
    document.HtmlExportOptions.ImagesPath = "./"
    # Set the option whether to export form fields as plain text or not.
    document.HtmlExportOptions.IsTextInputFormFieldAsText = True
    # Save the document to a html file.
    document.SaveToFile(os.path.join(file_html_path_to_save, outputFile), FileFormat.Html)
    document.Close()
