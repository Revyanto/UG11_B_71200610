def hitung (text):
    tot = len(text) * 2/3
    re = int(tot)
    return re

kalimat = input("Masukkan kalimat untuk dihitung: ")
print(hitung (kalimat))