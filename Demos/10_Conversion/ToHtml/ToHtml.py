
from spire.doc import *
from spire.doc.common import *

inputFile = r"C:\Users\millcake\PycharmProjects\compare_docs\data\Договор поставки Товара (ООО ТОЧИНВЕСТ-ШЗМК - покупатель) 2022.docx"
outputFile = "ToHtml.html"
        
#Create word document
document = Document()
document.LoadFromFile(inputFile)
#Save doc file.
document.SaveToFile(outputFile, FileFormat.Html)
document.Close()

