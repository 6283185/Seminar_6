# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


txt = "съешь абвещё этих мягких франабвцузских булок, даабв выпей чаю"

def del_abv(txt):
    txt = list(filter(lambda x: 'абв' not in x, txt.split()))
    return " ".join(txt)

txt = del_abv(txt)
print(txt)