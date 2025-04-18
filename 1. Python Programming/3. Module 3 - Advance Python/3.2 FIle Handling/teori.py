# File Handling in Python

# Read    (r)  = Membaca file
# Append  (a)  = Menambahkan data ke file
# Write   (w)  = Mengubah/menulis data ke file


# Read
file = open(./teori.txt, mode='r') # mode='r' bisa dihilangkan bisa diganti dengan 'r'
print(file.read())
file.close()

# Append
file = open(./teori.txt, 'a')
print(file.write('ini adalah data yang ditambahkan'))
file.close() # Close ini tujuaanya agar file tidak terus terbuka dan menghapus memorya yang digunakan

# Write
file = open(.'teori.txt', 'w')
print(file.write('ini adalah data yang ditulis'))
file.close()











