
class Cat:
    def __init__(self):
        self.nama = 'Meong'
        self.tipe = 'Anggora'
    
    def forward(self):   #forward berarti bergerak ke depan
        print('Kucing berlari ....')

class Bird:
    def __init__(self):
        self.nama = 'Erago'
        self.tipe = 'Elang'
    
    def forward(self):    #forward berarti bergerak ke depan
        print('Burung terbang .....')

#Menerapkan polimorhism pada OOP
#tambahkan fungsi umum yang menampung objek sebagai parameter dan kita panggil methodnya dari class yang ada
def melaju(objek):
    objek.forward()
    
meong = Cat(); erago = Bird()  #Penulisan 1 line code ini karena merupakan memudahakn peningkatan keterbacaan
                               #apabila code panjang maka tidak direkomendasikan oleh pep 8

melaju(meong)
melaju(erago)
