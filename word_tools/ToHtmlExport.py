from spire.doc import *
from spire.doc.common import *
import os


def word2html(export_filename: str, file_open_path: str, file_save_path: str):
    inputFile = file_open_path
    outputFile = export_filename + '.html'
    #Open a Word document.
    document = Document()
    document.LoadFromFile(inputFile)
    #Set whether the css styles are embeded or not.
    document.HtmlExportOptions.CssStyleSheetFileName = export_filename + '.css'
    document.HtmlExportOptions.CssStyleSheetType = CssStyleSheetType.External
    #Set whether the images are embeded or not.
    document.HtmlExportOptions.ImageEmbedded = False
    document.HtmlExportOptions.ImagesPath = "./"
    #Set the option whether to export form fields as plain text or not.
    document.HtmlExportOptions.IsTextInputFormFieldAsText = True
    #Save the document to a html file.
    document.SaveToFile(os.path.join(file_save_path, outputFile), FileFormat.Html)
    document.Close()
