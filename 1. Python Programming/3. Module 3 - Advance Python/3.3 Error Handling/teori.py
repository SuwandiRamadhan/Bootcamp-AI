# Tipe Error

# 1. Syntax Error
# 2. Logical Error


# Syntax Error
# Error yang terjadi ketika ada kesalahan dalam penulisan kode program
# Contoh:
'''
nama = ['Andi', 'Budi', 'Caca'
print(nama) # SyntaxError: '[' was never closed 
'''


# Logical Error
# Error yang terjadi ketika program tidak berjalan sesuai dengan yang diharapkan
# Contoh:
'''
nilai = 90
pembagi = 0
hasil = nilai / pembagi
print(hasil) # ZeroDivisionError: division by zero
'''


# Exception Handling
# Exception adalah error yang terjadi ketika program dijalankan

try:
    # kode yang mungkin terjadi error
    print(10/0)
except:
    # kode yang akan dijalankan jika terjadi error
    print('Error terjadi')















