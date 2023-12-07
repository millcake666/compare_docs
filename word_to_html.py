import mammoth

f = open("data/Договор поставки Товара (ООО ТОЧИНВЕСТ-ШЗМК - покупатель) 2022.docx", 'rb')
b = open('filename.html', 'wb')
document = mammoth.convert_to_html(f)
b.write(document.value.encode('utf8'))
f.close()
b.close()
