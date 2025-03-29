class AlatMusic():
    def __init__(self, nama, caraMain, warna):
        self.nama = nama
        self.caraMain = caraMain
        self.warna = warna
        
    def playMusic(self):
        print(f'{self.nama} berwarna {self.warna} dimainkan dengan cara {self.caraMain}')
    
alat = AlatMusic(nama='guitar', caraMain='dipetik', warna='brown')
alat = AlatMusic(nama='piano', caraMain='ditekan', warna='black')

alat.playMusic()