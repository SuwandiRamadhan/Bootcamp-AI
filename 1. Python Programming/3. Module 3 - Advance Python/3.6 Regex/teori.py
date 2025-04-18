# REGEX = Regular expression
'''
satu fungsi khusus untuk mendefinisikan pola tertentu melalui SERANGAKIAN KARAKTER yang
kemudian diolah oleh bahasa pemrograman. modul khusu bernama "re"
'''

'''
RE ini digunakan untuk menangkap pola contoh :
pattern = '^s...t$'
nah jadi "^" itu untuk menandakan awalan
kalau "$" menandakan akhiran
untuk s...t berarti teks yang diawali dengan s diakhiri dengan t dengan kata itu harus 5 karakter
'''

# RegEx mengembalikan nilai Boolean

'''
contohnya beberapa karakter re

[]    = Sekumpulan karakter           = [a-m]
\     = menggunakan karakter spesial  = \d, \n
.     = karakter apapun               =  he..o
^     = Dimulai dengan                = ^hello
$     = Diakhiri dengan               = planet$
*     = 0 atau lebih keberadaan       = he.*o
+     = Satu atau lebih keberadaan    = he.+o
?     = 0 atau 1 keberadaan           = he.?o
{}    = Sejumlah keberadaan           = he/{2}o
|     = Atau                          = falls|stays
dll.
'''