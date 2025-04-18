# Case study: Virtual assistant using Python (Assistant.py)

import smtplib as smtp
import random as rm
import sys


class Assistant():
    def __init__(self, nama):
        self.nama = nama
        
    def change_name(self):
        print(f'''Silahkan masukkan nama untuk Virtual Assistant yang kamu inginkan!''')
        nama_baru = input('Masukkan nama baru yang kamu inginkan : ')
        self.nama = nama_baru
        return self.nama
    
    def run(self):
        is_running = True
        while is_running:
            print('''New Virtual Assistant has been created successfully
                - Press ENTER - ''')
            while input() == '':
                print(f'''***************************************************
Hello Suwan, my name is {self.nama}, how can i help you??
1. Change My Name
2. Create Schedule
3. View Schedule
4. Random Jokes
5. Send Mail
0. Exit
''')
                pilihan_fitur = input('''Fitur mana yang ingin kamu gunakan? \npilihan : ''')
                if pilihan_fitur == '0':   # Exit program
                    print(f'Thanks for using {self.nama} suwandi!')
                    is_running = False
                    sys.exit()
                elif pilihan_fitur == '1':    # Change name
                    self.change_name()
                    print(f'''Oke sekarang namaku adalah {self.nama} ''')
                    opsi_lanjut = input(f'Apakah kamu ingin melanjutkan? Y / N ?? \nPilihan :').upper()
                    if opsi_lanjut == 'Y':
                        self.run()
                    elif opsi_lanjut == 'N':
                        print(f'Terima kasih sudah menggunakan {self.nama}. Senang bisa membantu!')
                        is_running = False
                        sys.exit()
                    else:
                        print(f'Kamu memasukkan inputan yang salah')
                        sys.exit()
                elif pilihan_fitur == '2':
                    try:
                        open_file = open('1. Python Programming/5. Case Study/db_jadwal.txt', 'a')
                        jumlah_catatan = int(input(f'Masukkan jumlah catatan yang ingin anda tambahkan : '))
                        for i in range(jumlah_catatan):
                            nomor = i + 1
                            catatan = input(f'Masukkan catatan ke-{nomor} : ')
                            open_file.write(f'{nomor}. {catatan}\n')
                        print("Catatan berhasil dibuat")
                        open_file.close()
                    except ValueError:
                        print('Input harus berupa angka!')
                    except IOError:
                        print('Terjadi kesalahan saat menulis file!')
                elif pilihan_fitur == '3':
                    try:
                        baca_jadwal = open('1. Python Programming/5. Case Study/db_jadwal.txt', 'r')
                        opsi_lanjut = input(f'Apakah kamu ingin membuka jadwal? Y / N ?? \nPilihan :').upper()
                        if opsi_lanjut == 'Y':
                            print(baca_jadwal.read())
                            baca_jadwal.close()
                        elif opsi_lanjut == 'N':
                            print(f'Terima kasih sudah menggunakan {self.nama}. Senang bisa membantu!')
                            is_running = False
                            sys.exit()
                        else:
                            print(f'Kamu memasukkan inputan yang salah')
                            sys.exit()
                    except Exception as e:
                        print(f'Terjadi kesalahan', e.__class__)
                elif pilihan_fitur == '4':
                    try:
                        with open('1. Python Programming/5. Case Study/db_jokes.txt', 'r') as file:
                            jokes = file.readlines()
                            random_jokes = rm.choice(jokes)
                            print(random_jokes)
                    except Exception as e:
                        print('Terjadi kesalahan', e.__class__)
                elif pilihan_fitur == '5':
                    try:
                        #Data email
                        email_pengirim = input('Masukkan email pengirim : ')
                        password_pengirim = 'gywf msdd tska jvbk'   # buat app password untuk email pengirim
                        email_penerima = input('Masukkan email penerima : ')
                        subject = input('Masukkan subject email : ')
                        body = input('Masukkan isi email : ')
                        
                        #Format email
                        email = f'Subject : {subject}\n \n{body}'
                        
                        #koneksi ke server SMTP
                        with smtp.SMTP_SSL('smtp.gmail.com', 465, timeout=60) as server:    #server SMTP gmail  #gunakan port SSL dengan port 465
                            server.login(email_pengirim, password_pengirim)     #login ke email pengirim\
                            server.sendmail(email_pengirim, email_penerima, email)    #kirim email
                            server.close()
                            print('Email berhasil dikirim!')
                            
                    except smtp.SMTPAuthenticationError:
                        print("Gagal login! Periksa email dan password Anda.")
                    except smtp.SMTPConnectError:
                        print("Gagal terhubung ke server SMTP. Periksa koneksi internet Anda.")
                    except smtp.SMTPException as e:
                        print(f"Terjadi kesalahan saat mengirim email: {e}")
                    except Exception as e:
                        print(f'Error: {e}')
                    
                    
                    #  gywf msdd tska jvbk
                    
                    '''
                    try:
                        email_pengirim = input('Masukkan email pengirim : ')
                        password_pengirim = 'gywf msdd tska jvbk'
                        email_penerima = input('Masukkan email penerima : ')
                        email_subject = input('Masukkan subject : ')
                        email_body = input('Masukkan body : ')

                        email = f'Subject : {email_subject}\n\n{email_body}'
                        with smtp.SMTP_SSL('smtp.gmail.com', 465, timeout=60) as server:
                            server.login(email_pengirim, password_pengirim)
                            server.sendmail(email_pengirim, email_penerima, email)
                            server.close()
                            print('Email berhasil dikirim')
                    except smtp.SMTPAuthenticationError:
                        print('Email atau password salah')
                    except smtp.SMTPConnectError:
                        print('Gagal terhubung ke server SMTP')
                    except smtp.SMTPException as e:
                        print(f'Gagal mengirim email: {e}')
                    except Exception as e:
                        print(f'Error: {e}')
                    
                    
                    
                    '''
                else:
                    print('Kamu memasukkan inputan yang salah !')
                    is_running = False
                    sys.exit()








        print(f'Press ENTER jangan yang lain cok!')
        opsi_lanjut = input(f'''Gimana? masih mau lanjut cobain fiturnya? Y / N \nMasukkan pilihan : ''').upper()
        if opsi_lanjut == 'Y':
            self.run()
        elif opsi_lanjut == 'N':
            print(f'Program akan keluar, terima kasih!')
            is_running = False
        else:
            print(f'Kamu memasukkan inputan yang salah. PROGRAM AKAN KELUAR')
            is_running = False
                














# CLUE: create multiple function here