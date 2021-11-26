def check_data_type(a,b):
    tipe = str(type(a))[8:11]
    if b.lower() == tipe:
        print ("Jawaban Anda benar")
        return True
    else:
        print ("Jawaban Anda salah, seharusya adalah:",tipe)
        return False

print(check_data_type("Kevin","STr"))
print(check_data_type("Kevin","str"))
print(check_data_type(12345,"str"))
print(check_data_type("9347","int"))
print(check_data_type(9876,"int"))