from textfiles import TextFileReader

fr = TextFileReader('satcat.txt')
print('Lendo arquivo', fr)
print('Conteudo:')
print('-----------------------')
print(fr.text)