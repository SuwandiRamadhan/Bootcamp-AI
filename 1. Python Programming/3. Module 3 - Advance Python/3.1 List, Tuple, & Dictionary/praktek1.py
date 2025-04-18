list1 = ['apple', 'banana', 'watermelon', 'alpukat']
print(list1)

list2 = [2, 1, 2,  7, 4, 10]
print(list2)

list3 = [True, False, True, True]
print(list3)

list4 = [2, 'apple', False, 3.0]
print(list4)

# Menggabungkan list
print (list1 + list2 + list3 + list4) # Menggabungkan list

# Mengurutkan elemen di dalam list ASC
list1.sort()
list2.sort()
list3.sort()
print(list1, list2, list3)

# Mengurutkan elemen di dalam list DESC
list1.sort(reverse=True) #.sort(reverse=True) = Mengurutkan elemen di dalam list DESC dengan memperhatikan nilai
list2.reverse() # .reverse() = Mengurutkan elemen di dalam list DESC tanpa memperhatikan nilai hanya membalikkan urutan
print(list1, list2)

# Menghitung jumalah elemen di dalam list
print(len(list1), len(list2), len(list3), len(list4))

# Menghitung jumlah elemen tertentu di dalam list
print(list2.count(2))
print(list1.count('apple'))
print(list3.count(True))


# Membership test
print('apple' in list1) # Balikannya Boolean (True)
print('apple' not in list1) # Balikannya Boolean(False)















