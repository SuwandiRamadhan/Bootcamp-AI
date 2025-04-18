class Mobil:
    def __init__(self, plat):
        self.plat = plat
        self.tipe = 'avanza'
        self.__bensin = 40  #liter
        
    #getter
    def getMaksimumBensin(self):
        print(f'Maksimum bensin avanza yaitu : {self.__bensin} liter')
    
    #setter
    def setMaksimumBensin(self, bensin):
        self.__bensin = bensin   #untuk membuat parameter yang nanti bisa dilempar ke dalam function
    
avanza = Mobil(plat='B 7185 XC')

'''
dengan kita buat class seperti ini kita bisa merubah atribut yang ada di dalam class dengan 
memasukkan nilai terbaru misal kita ubah bensin
'''

avanza.__bensin = 35
print(avanza.__bensin)


avanza.getMaksimumBensin()  #sebelum diubah
# Nah kalau kita coba akses untuk lihat saja tidak bisa jadi untuk melihatnya kita masukkan fungsi getter
# maka nilainya tidak akan berubah jadi 35 karena 35 diatas hanya mengakses dirinya sendiri (avanza.__bensin)

# Jadi gimana kalau kita mau ubah nilainya? naik ke atas kita masuk ke fungsi setter
avanza.setMaksimumBensin(bensin=60)
avanza.getMaksimumBensin()













