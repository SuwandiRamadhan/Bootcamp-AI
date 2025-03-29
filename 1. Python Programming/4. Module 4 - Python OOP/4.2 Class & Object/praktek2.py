class Employee():
    '''
    ini adalah class untuk memanipulasi data employee
    '''
    
    def __init__(self, lokasi_file):
        self.data_employee = open(f'{lokasi_file}, 'r', encoding='utf-8')
        self.data_per_sesi = 10
    
    def baca_data(self):
        self.data_employee = self.data_employee[:self.data_per_sesi]
        return self.data_employee
        
    def hapus_data(self, data_baru):
        del.self.data_employee[bars][kolom]
        
    def tambah_data(self, data_baru):
        it = Employee.objects.all()

# Membuat object
it = Employee(lokasi_file='./data/karyawan_IT.xls')   # misalkan diisi dengan lokasi tersebut data karyawan ITnya
marketing = Employee(lokasi_file='./data/karyawan_marketing.xlsx')
product = Employee(lokasi_file='./product/product_2025.csv')
    
    
    
    
    
    
    
    
    