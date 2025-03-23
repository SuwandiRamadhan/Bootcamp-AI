
# While Loop
# While loop akan diulang selama kondisinya bernilai True
count = 1
while (count < 11):
    print ("The count is: ", count)
    count += 1

print ("Good bye!")
print('\n')

# For Loop
# For loop akan diulang berdasarkan jumlah elemen yang ada di dalam list/string
listAngka = [1, 2, 3, 4, 5]

for x in listAngka:
    print(x)
print('\n')

# Nested Loop
# Nested loop adalah pengulangan bersarang, atau pengulangan di dalam pengulangan
# Nested Loop akan masuk ke looping di dalamnya ketika kondisi True jika false maka akan keluar dari looping
i = 200

while (i < 100):
    j = 2
    while (j <= (i/j)):
        print('Loop dalam loop')
        j += 1
        i += 1
print ("Good bye!")
print('\n')

# Break = Untuk menghentikan proses looping
for letter in 'Python':
    if letter == 'h':
        break
    print ('Current Letter :', letter)
print('\n')

# Continue = Untuk melanjutkan proses looping selanjutnya
for letter in 'Python':
    if letter == 'h':
        continue
    print ('Current Letter :', letter)








