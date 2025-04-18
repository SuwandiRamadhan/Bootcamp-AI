class cat:
    '''
    ini adalah class untuk membuat object kucing
    melalui kelas ini kita bisa mendefinisikan nama dan juga tipe dari kucing yang dibuat
    '''
    
    spesies = "kucing"
    def __init__(self, nama, tipe):      # __init__ berfungsi sebagai konstraktor
        self.nama = nama
        self.tipe = tipe
        
    def run(self, speed):
        print(f"{self.nama} berjalan dengan kecepatan {speed} km/jam")
    
    def play(self):
        print(f"{self.nama} sedang bermain dengan kucing lainnya ....")
        
    def eat(self):
        pass

# Membuat object
kinako = cat(nama="kinako", tipe = "anggora")
minto = cat(nama="minto", tipe = "persia")

print(kinako.nama)
print(kinako.tipe)
print(minto.nama)    
print(minto.tipe)    

kinako.run('cepat')
kinako.play()

print(f'kinako adalah seekor {kinako.__class__.spesies}')
print(f'{kinako.nama} merupakan kucing jenis {kinako.tipe}')
print(f'{minto.nama} merupakan kucing jenis {minto.tipe}')





