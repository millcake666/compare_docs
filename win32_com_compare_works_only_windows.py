import win32com.client

path = r'C:\Users\senio\PycharmProjects\compare_docs\data\\'
# note the \\ at the end of the path name to prevent a SyntaxError

# Create the Application word
Application = win32com.client.gencache.EnsureDispatch("Word.Application")

# Compare documents
Application.CompareDocuments(Application.Documents.Open(path + "Договор поставки Товара (ООО ТОЧИНВЕСТ-ШЗМК - покупатель) 2022.docx"),
                             Application.Documents.Open(path + "Договор поставки Товара (ООО ТОЧИНВЕСТ-ШЗМК - покупатель) 2022 новый.docx"))

# Save the comparison document as "Comparison.docx"
Application.ActiveDocument.SaveAs(FileName=path + "diff/Comparison.docx")
# Don't forget to quit your Application
Application.Quit()
