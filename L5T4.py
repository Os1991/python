from googletrans import Translator

with open('translator.txt', 'r') as tr:
    contents = tr.read()
    print(contents)
    tr.seek(0)
    file_translate = Translator()
    result = file_translate.translate(contents, dest='ru')
    print(result.text)
    with open('googletr', 'w') as f:
        f.write(result.text)
