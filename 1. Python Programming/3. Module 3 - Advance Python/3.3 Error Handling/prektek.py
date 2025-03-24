# Syntax Error
fruitList = ["apple", "banana", "cherry"]

# for fruit in fruitList
for fruit in fruitList:
    print(fruit)
    
print('\n')



# Logical Error
'''
nilai = 10
pembagi = 0
hasil = nilai / pembagi
print(hasil)
'''
# Cara mengatasi error dengan error handling menggunakan try except
# Dengan menggunakan try except kita tidak break program dan bisa melanjutkan program
try:
    nilai = 10
    pembagi = 0
    hasil = nilai / pembagi
    print(hasil)
except:
    print("Oops!! Terjadi error saat run pembagian")

print('Jalankan instruksi selanjutnya')

print('\n')
# Best Practice
try:
    nilai = 90
    pembagi = 0
    hasil = nilai / pembagi
    print(hasil)
except Exception as e:
    print("Oops!! Terjadi ", e.__class__, "saat run pembagian.")

print('Jalankan instruksi selanjutnya')



print('\n')
# kita bisa buat error handling untuk beberapa jenis error
class valueTooSmallError(Exception):
    pass
class valueTooLargeError(Exception):
    pass

number = 10

while True:
    try:
        inputNumber = int(input("Masukkan angka: "))
        
        if inputNumber < number:
            raise valueTooSmallError
        elif inputNumber > number:
            raise valueTooLargeError
        break
    except Exception as e:
        print("Oops!! Terjadi ", e.__class__, ".")















