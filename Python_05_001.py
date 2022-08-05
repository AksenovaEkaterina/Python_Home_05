# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

def DelFrag (text):
    fragment = "абв"
    words = text.split(" ")
    new_text = []
    for i in words:
        if fragment not in i:
            new_text.append(i)

    new_text = " ".join(new_text)
    print(new_text)

text = "абв вамдукщзмь зщкплзцудщ абвпрмимн ооабв уацлоут"
DelFrag (text)
