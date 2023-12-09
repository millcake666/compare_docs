import aspose.words as aw
from datetime import date

dir_path = 'data/'

# load first document
doc = aw.Document(dir_path + 'Договор поставки Товара (ООО ТОЧИНВЕСТ-ШЗМК - покупатель) 2022.docx')

# load second document
doc2 = aw.Document(dir_path + 'Договор поставки Товара (ООО ТОЧИНВЕСТ-ШЗМК - покупатель) 2022 новый.docx')

# compare documents
doc.compare(doc2, 'user', date.today())

# save the document to get the revisions
if doc.revisions.count > 0:
    doc.save(dir_path + 'diff/compared2.docx')
else:
    print('Documents are equal')
