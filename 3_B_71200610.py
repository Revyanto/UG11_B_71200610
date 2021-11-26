def sisip (text,add,i):
    text1 = text[0:(i-1)]
    text2 = text[(i-1)::]
    text = text1 + add + text2
    print (text)

text = input("Masukkan kalimat awal: ")
add = input("Masukkan kata untuk disisipkan: ")
i = int(input("Masukkan index: "))
sisip(text, add, i)