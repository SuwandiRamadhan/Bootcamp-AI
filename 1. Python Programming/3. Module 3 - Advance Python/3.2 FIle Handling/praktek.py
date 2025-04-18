#read 
data = open('1. Python Programming/3. Module 3 - Advance Python/3.2 FIle Handling/fileData.txt', 'r')

print(data.read())
data.close()

'''
open('1. Python Programming/3. Module 3 - Advance Python/3.2 FIle Handling/fileData.txt', 'r', encoding='utf-8')
penggunaan encoding= 'utf-8' direkomendasikan untuk menghindari error UnicodeDecodeError
'''

# Jadinya seperti di bawah
data = open('1. Python Programming/3. Module 3 - Advance Python/3.2 FIle Handling/fileData.txt', 'r', encoding='utf-8') 
print(data.read())
data.close()



# Append
data = open('1. Python Programming/3. Module 3 - Advance Python/3.2 FIle Handling/fileData.txt', 'a', encoding='utf-8')
print(data.write('\nIni adalah data tambahan'))
data.close()



# Write
data = open('1. Python Programming/3. Module 3 - Advance Python/3.2 FIle Handling/fileData.txt', 'w', encoding='utf-8')
print(data.write('\nIni adalah data yang ditulis menggunakan metode write'))
# Write menghapus data yang ada dan mengganti dengan data yang baru kita input


# Better Practice
try:
    f = open('1. Python Programming/3. Module 3 - Advance Python/3.2 FIle Handling/fileData.txt', 'r', encoding='utf-8')
finally:
    f.close()
    
# Best Practice
with open('1. Python Programming/3. Module 3 - Advance Python/3.2 FIle Handling/fileData.txt', 'r', encoding='utf-8') as f:
    # bisa dooso codingan apa saja
    print(f.read())
















