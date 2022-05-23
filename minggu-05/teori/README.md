# Minggu ke-5 : Input dan Output - Mempelajari Tutorial Bab 7
Bab ini akan membahas beberapa kemungkinan. Ada beberapa cara untuk menampilkan output dari suatu program, data dapat dicetak dalam bentuk yang dapat dibaca, atau ditulis ke file untuk digunakan kedepannya.

## 7.1. Pemformatan output yang lebih menarik
Sejauh ini kita telah menemukan dua cara untuk menulis nilai: pernyataan *ekspresi* dan **print()** fungsi.

Seringkali kita ingin lebih mengontrol pemformatan output daripada sekadar mencetak nilai yang dipisahkan oleh spasi. Ada beberapa cara untuk memformat output.
* Di dalam string ini, dapat menulis ekspresi Python antara *{end}* karakter yang dapat merujuk ke variabel atau nilai literal. Mulailah string dengan **f** atau **F** sebelum tanda kutip pembuka atau tanda kutip tiga.
```python
>>> year = 2016
>>> event = 'Referendum'
>>> f'Results of the {year} {event}'
'Results of the 2016 Referendum'
```
* Metode **str.format()** string membutuhkan lebih banyak upaya manual.
```python
>>> yes_votes = 42_572_654
>>> no_votes = 43_132_495
>>> percentage = yes_votes / (yes_votes + no_votes)
>>> '{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage)
' 42572654 YES votes  49.67%'
```
* Terakhir adalah melakukan semua penanganan string sendiri dengan menggunakan operasi pengirisan string dan penggabungan untuk membuat tata letak apa pun yang diinginkan. Tipe string memiliki beberapa metode yang melakukan operasi yang berguna untuk mengisi string ke lebar kolom tertentu.

Fungsi **str()** ini dimaksudkan untuk mengembalikan representasi nilai yang cukup dapat dibaca manusia, sedangkan repr()dimaksudkan untuk menghasilkan representasi yang dapat dibaca oleh penerjemah. Untuk objek yang tidak memiliki representasi khusus untuk dipahami, str()akan mengembalikan nilai yang sama dengan repr(). Banyak nilai, seperti angka atau struktur seperti daftar dan kamus, memiliki representasi yang sama menggunakan salah satu fungsi. String, khususnya, memiliki dua representasi yang berbeda.
Contoh:
```python
>>> s = 'Hello, world.'
>>> str(s)
'Hello, world.'
>>> repr(s)
"'Hello, world.'"
>>> str(1/7)
'0.14285714285714285'
>>> x = 10 * 3.25
>>> y = 200 * 200
>>> s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
>>> print(s)
The value of x is 32.5, and y is 40000...
>>> # The repr() of a string adds string quotes and backslashes:
... hello = 'hello, world\n'
>>> hellos = repr(hello)
>>> print(hellos)
'hello, world\n'
>>> # The argument to repr() may be any Python object:
... repr((x, y, ('spam', 'eggs')))
"(32.5, 40000, ('spam', 'eggs'))"
```
Modul **string** berisi **template** kelas yang menawarkan cara lain untuk mengganti nilai menjadi string, menggunakan placeholder seperti **$x** dan menggantinya dengan nilai dari kamus

### 7.1.1. Literal string
Literal string yang diformat (disingkat juga disebut f-string) memungkinkan untuk memasukkan nilai ekspresi Python di dalam string dengan mengawali string dengan **f** or **F** dan menulis ekspresi sebagai **{expression}**.
Contoh berikut membulatkan pi ke tiga tempat setelah desimal :
```python
>>> import math
>>> print(f'The value of pi is approximately {math.pi:.3f}.')
The value of pi is approximately 3.142.
```
Melewati bilangan bulat setelah **':'** akan menyebabkan bidang itu menjadi jumlah karakter minimum. Berguna untuk membuat kolom berbaris.
```python
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
>>> for name, phone in table.items():
...     print(f'{name:10} ==> {phone:10d}')
...
Sjoerd     ==>       4127
Jack       ==>       4098
Dcab       ==>       7678
```
Dapat menggunakan modifikasi lain untuk mengonversi nilai sebelum diformat. **'!a'** berlaku *ascii()*, *'!s'* berlaku *str()*, dan *'!r'* berlaku *repr()* :
```python
>>> animals = 'eels'
>>> print(f'My hovercraft is full of {animals}.')
My hovercraft is full of eels.
>>> print(f'My hovercraft is full of {animals!r}.')
My hovercraft is full of 'eels'.
```

### 7.1.2. Format string()
Penggunaan dasar **str.format()** metode ini terlihat seperti ini :
```python
>>> print('We are the {} who say "{}!"'.format('knights', 'Ni'))
We are the knights who say "Ni!"
```
Tanda kurung dan karakter di dalamnya (disebut bidang format) diganti dengan objek yang diteruskan ke **str.format()**. Angka dalam kurung dapat digunakan untuk merujuk ke posisi objek yang dilewatkan ke dalam **str.format()**.
```python
>>> print('{0} and {1}'.format('spam', 'eggs'))
spam and eggs
>>> print('{1} and {0}'.format('spam', 'eggs'))
eggs and spam
```
Jika argumen kata kunci digunakan dalam **str.format()**.
```python
>>> print('This {food} is {adjective}.'.format(
...       food='spam', adjective='absolutely horrible'))
This spam is absolutely horrible.
```
Argumen posisi dan kata kunci dapat digabungkan.
```python
>>> print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',
                                                       other='Georg'))
The story of Bill, Manfred, and Georg.
```
Jika memiliki string format yang sangat panjang yang tidak ingin pisahkan,  lebih baik mereferensikan variabel yang akan diformat berdasarkan nama berdasarkan posisi.
```python
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
>>> print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
...       'Dcab: {0[Dcab]:d}'.format(table))
Jack: 4098; Sjoerd: 4127; Dcab: 8637678
```
Dapat dilakukan dengan meneruskan tabel sebagai argumen kata kunci dengan notasi '**'
```python
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
>>> print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
Jack: 4098; Sjoerd: 4127; Dcab: 8637678
```
Sangat berguna dalam kombinasi dengan fungsi bawaan **vars()**, yang mengembalikan kamus yang berisi semua variabel lokal.
Sebagai contoh, baris berikut menghasilkan kumpulan kolom yang tersusun rapi yang memberikan bilangan bulat dan kuadrat serta kubusnya :
```python
>>> for x in range(1, 11):
...     print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
...
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000
```

### 7.1.3. Pemformatan string
Berikut tabel kotak dan kubus yang sama, diformat secara manual :
```python
>>> for x in range(1, 11):
...     print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
...     # Note use of 'end' on previous line
...     print(repr(x*x*x).rjust(4))
...
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000
```
(Perhatikan bahwa satu spasi di antara setiap kolom ditambahkan dengan cara **print()** kerjanya: selalu menambahkan spasi di antara argumennya.)
Metode **str.rjust()** objek string membenarkan string di bidang dengan lebar tertentu dengan mengisinya dengan spasi di sebelah kiri.
Ada metode lain, **str.zfill()**, yang mengisi string numerik di sebelah kiri dengan nol. Metode ini mengerti tentang tanda plus dan minus :
```python
>>> '12'.zfill(5)
'00012'
>>> '-3.14'.zfill(7)
'-003.14'
>>> '3.14159265359'.zfill(5)
'3.14159265359'
```
Operator % (modulo) juga dapat digunakan untuk pemformatan string. Mengingat , contoh di diganti dengan nol atau lebih elemen dari . Operasi ini biasa disebut dengan interpolasi string. Sebagai contoh :**'string' % values%stringvalues**
```python
>>> import math
>>> print('The value of pi is approximately %5.3f.' % math.pi)
The value of pi is approximately 3.142.
```

## 7.2. File
**open()** mengembalikan objek file , dan paling sering digunakan dengan dua argumen: **.open(filename, mode)**
```python
>>> f = open('workfile', 'w')
```
Menggunakan with juga jauh lebih pendek :
```python
>>> with open('workfile') as f:
...     read_data = f.read()

>>> # We can check that the file has been automatically closed.
>>> f.closed
True
```
*```Peringatan ketika memanggil f.write() tanpa menggunakan kata kunci with atau panggilan f.close() dapat mengakibatkan argumen f.write() tidak sepenuhnya ditulis ke disk, bahkan jika program berhasil keluar.```*

Setelah objek file ditutup, baik dengan pernyataan with atau dengan memanggil **f.close()**, upaya untuk menggunakan objek file secara otomatis, gagal.
```python
>>> f.close()
>>> f.read()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: I/O operation on closed file.
```

### 7.2.1. Metode dari file objek
Contoh lainnya di bagian ini akan mengasumsikan bahwa objek file yang dipanggil *f* telah dibuat.

Untuk membaca konten file, panggil **f.read(size)**, yang membaca sejumlah data dan mengembalikannya sebagai string atau objek byte. Jika akhir file telah tercapai, **f.read()** akan mengembalikan string kosong ('').
```python
>>> f.read()
'This is the entire file.\n'
>>> f.read()
''
```
**f.readline()** membaca satu baris dari file, karakter baris baru (**\n**) ditinggalkan di akhir string, dan hanya dihilangkan pada baris terakhir file jika file tidak diakhiri dengan baris baru.
```python
>>> f.readline()
'This is the first line of the file.\n'
>>> f.readline()
'Second line of the file\n'
>>> f.readline()
''
```
Untuk membaca baris dari file, harus mengulang objek file. Ini hemat memori, cepat, dan mengarah ke kode sederhana :
```python
>>> for line in f:
...     print(line, end='')
...
This is the first line of the file.
Second line of the file
```
Jika ingin membaca semua baris file dalam daftar, dapat menggunakan **list(f)** atau **f.readlines()**.

**f.write(string)** menulis isi string ke file, mengembalikan jumlah karakter yang ditulis.
```python
>>> f.write('This is a test\n')
15
```
Jenis objek lain perlu dikonversi – baik menjadi string atau objek byte.
```python
>>> value = ('the answer', 42)
>>> s = str(value)  # convert the tuple to string
>>> f.write(s)
18
```
f.tell()mengembalikan bilangan bulat yang memberikan posisi objek file saat ini dalam file yang direpresentasikan sebagai jumlah byte dari awal file saat dalam mode biner dan angka buram saat dalam mode teks.
Untuk mengubah posisi objek file. gunakan **f.seek(offset, whence)**. Nilai dari whence 0 mengukur dari awal file, 1 menggunakan posisi file saat ini, dan 2 menggunakan akhir file sebagai referensi. *Whence* dapat dihilangkan dan default ke 0, menggunakan awal file sebagai referensi **f.seek(offset, whence)**.
```python
>>> f = open('workfile', 'rb+')
>>> f.write(b'0123456789abcdef')
16
>>> f.seek(5)      # Go to the 6th byte in the file
5
>>> f.read(1)
b'5'
>>> f.seek(-3, 2)  # Go to the 3rd byte before the end
13
>>> f.read(1)
b'd'
```

### 7.2.2. Menyimpan data terstruktur dengan *json*
String dapat dengan mudah ditulis dan dibaca dari sebuah file. Angka membutuhkan lebih banyak usaha, karena method **read()** ini hanya mengembalikan string, yang harus diteruskan ke fungsi seperti **int()**, yang mengambil seperti string **'123'** dan mengembalikan nilai numeriknya 123. Saat ingin menyimpan tipe data yang lebih kompleks seperti daftar bersarang dan kamus, parsing dan serialisasi dengan akan menjadi rumit.

*```Catatan Format JSON biasanya digunakan oleh aplikasi modern untuk memungkinkan pertukaran data. Banyak programmer sudah mengetahuinya, yang menjadikannya pilihan yang baik untuk interoperabilitas.```*

Jika kita mempunyai objek x, kita dapat melihat representasi JSON. Berikut kode programnya :
```python
>>> import json
>>> x = [1, 'simple', 'list']
>>> json.dumps(x)
'[1, "simple", "list"]'
```
Varian lain dari **dumps()**, yang disebut **dump()**, hanya membuat serial objek ke file teks.
```python
json.dump(x, f)
```
**f** adalah objek file teks yang telah dibuka untuk dibaca :
```python
x = json.load(f)
```

### 7.2.3. Selesai
Terima Kasih Teman!