# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
text = 'wwbbbwwbbbbbbrrnnn'
new_text = ''
count =1
for i in range (1, len(text)):
    num = str(count)
    if text[i]==text[i-1]:
        count+=1
        
    if text[i]!=text[i-1]:
        count+=1
        new_text += num+text[i-1]
        count=1

if text[-1]==text[-2]:            #записывается последний элемент, который не попал в цикл
    count+=1
    new_text += num+text[-1]
if text[-1]!=text[-2]:
    new_text += '1'+text[-1]

print(new_text)


