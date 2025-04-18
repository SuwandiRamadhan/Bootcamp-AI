# Grandparent Class
class Makhluk:
    pass

# Parent Class
class Animal:
    def __init__(self):
        self.tipe = 'Mamalia'
        self.kecepatan = 'Lambat'
        
    def grow(self):
        print(f'Mamalia ini bertumbuh ...')
        print(f'Mamalia ini ({self.nama}) bertumbuh ...')
        
    
# Child Class
class Cat(Animal):
    # Karena ada 2 (__init__) maka (__init__) pada child harus kita tambahkan super init
    def __init__(self, nama, tipe):
        #penambahan super init
        super().__init__()
        self.nama = nama
        self.tipe = tipe
    def run(self):
        print(f'kucing {self.tipe} sedang berlari ...')
        
# Child Class 2
class Dog(Animal):
    pass

# Grandchild Class
class Ayam(Makhluk):
    pass
    
kinako = Cat(nama='kinako', tipe='anggora')
minto = Cat(nama='minto', tipe='persia')

print(kinako.kecepatan)
print(kinako.tipe)

'''
nah jadi ketika di print ke terminal yang keluar
lambat
anggora
'''
'''
jadi ketika ada 2 method yang sama maka ia akan mengambil method yang ada pada child kalau kita print childnya
'''

kinako.run()
minto.run()

kinako.grow()
minto.grow()

