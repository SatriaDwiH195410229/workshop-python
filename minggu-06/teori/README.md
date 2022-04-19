# Minggu ke-6 : Kesalahan dan Pengecualian - Mempelajari Tutorial Bab 8

Sampai sekarang pesan kesalahan belum lebih dari yang disebutkan, ada setidaknya 2 jenis kesalahan yang dapat dibedakan: kesalahan **sintaksis** dan **exceptions**.

# 8.1. Kesalahan sintaks
Kesalahan sintaks, juga dikenal sebagai kesalahan penguraian, mungkin merupakan jenis keluhan paling umum yang di dapatkan saat masih belajar Python :
_*lihat file [8.1.py](https://github.com/SatriaDwiH195410229/workshop-python/blob/main/minggu-06/src/8.1.py)*_
```pyhton
>>> while True print('Hello world')
  File "<stdin>", line 1
    while True print('Hello world')
                   ^
SyntaxError: invalid syntax
```
Parser mengulangi baris yang menyinggung dan menampilkan 'arrow' kecil yang menunjuk pada titik paling awal di baris tempat kesalahan terdeteksi. Kesalahan disebabkan oleh token sebelum arrow: dalam contoh, kesalahan terdeteksi pada fungsi print(), karena tidak ada titik dua ( `':'`).

# 8.2. Pengecualian
Bahkan jika suatu statement atau ekspresi secara sintaksis benar, hal itu dapat menyebabkan kesalahan ketika dilakukan upaya untuk mengeksekusinya. Kesalahan yang terdeteksi selama eksekusi disebut exceptions. Namun, sebagian besar exceptions tidak ditangani oleh program, dan menghasilkan pesan kesalahan seperti yang ditunjukkan berikut ini :
_*lihat file [8.2.py](https://github.com/SatriaDwiH195410229/workshop-python/blob/main/minggu-06/src/8.2.py)*_
```python
>>> 10 * (1/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>> 4 + spam*3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'spam' is not defined
>>> '2' + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
```
Baris terakhir dari pesan kesalahan menunjukkan apa yang terjadi. Pengecualian datang dalam tipe yang berbeda, dan tipe tersebut dicetak sebagai bagian dari pesan: tipe dalam contoh adalah *ZeroDivisionError*, *NameError* dan *TypeError*. String yang dicetak sebagai tipe exceptions adalah nama exceptions bawaan. Ini berlaku untuk semua exceptions bawaan, tetapi tidak harus untuk exceptions yang ditentukan pengguna. Nama exceptions standar adalah pengidentifikasi bawaan (bukan kata kunci cadangan).

Sisa baris memberikan detail berdasarkan jenis exceptions dan apa yang menyebabkannya.

Bagian pesan kesalahan sebelumnya menunjukkan konteks di mana exceptions terjadi. Secara umum berisi baris sumber daftar traceback stack; namun, itu tidak akan menampilkan baris yang dibaca dari input standar.

# 8.3. Menangani exceptions
Memungkinkan untuk menulis program yang menangani exceptions yang dipilih. Lihat contoh berikut, yang meminta pengguna untuk memasukkan bilangan bulat, tetapi mengizinkan pengguna untuk menginterupsi program; perhatikan bahwa interupsi yang dibuat pengguna ditandai dengan memunculkan exceptions. `Control-C` *KeyboardInterrupt* :
_*lihat file [8.3-1.py](https://github.com/SatriaDwiH195410229/workshop-python/blob/main/minggu-06/src/8.3-1.py)*_
```python
>>> while True:
...     try:
...         x = int(input("Please enter a number: "))
...         break
...     except ValueError:
...         print("Oops!  That was no valid number.  Try again...")
...
```
Pernyataan `try` tersebut berfungsi sebagai berikut :
* Pertama, try clause (statement antara *try* dan kata kunci *except*) dieksekusi.
* Jika tidak ada exceptions yang terjadi, clause except dilewati dan eksekusi try.
* Jika exceptions terjadi selama eksekusi tryclause, sisa clause akan dilewati. Kemudian, jika tipenya cocok dengan exceptions yang dinamai kata kunci except, clause except dieksekusi, dan kemudian eksekusi dilanjutkan setelah blok try/except.
* Jika terjadi exceptions yang tidak cocok dengan exceptions yang disebutkan dalam clause except, akan diteruskan ke try statement luar; jika tidak ada penangan yang ditemukan, itu adalah exceptions yang tidak tertangani dan eksekusi berhenti dengan pesan seperti yang ditunjukkan di atas.

Sebuah try statement mungkin memiliki lebih dari satu clause except, untuk menentukan penangan untuk exceptions yang berbeda. Paling banyak satu handler akan dieksekusi. Penangan hanya menangani exceptions yang terjadi di clause try yang sesuai , bukan di penangan lain dari try statement yang sama. Clause exceptions dapat menyebutkan beberapa exceptions sebagai tupel dalam kurung, misalnya :
_*lihat file [8.3-2.py](https://github.com/SatriaDwiH195410229/workshop-python/blob/main/minggu-06/src/8.3-2.py)*_
```python
... except (RuntimeError, TypeError, NameError):
...     pass
```
Kelas dalam clause except kompatibel dengan exceptions jika itu adalah kelas yang sama atau kelas dasar daripadanya (tetapi tidak sebaliknya — clause exceptions yang mencantumkan kelas turunan tidak kompatibel dengan kelas dasar). Misalnya, kode berikut akan mencetak B, C, D dalam urutan itu :
_*lihat file [8.3-3.py](https://github.com/SatriaDwiH195410229/workshop-python/blob/main/minggu-06/src/8.3-3.py)*_
```python
class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")
```
Perhatikan bahwa jika clause except dibalik (dengan yang pertama), itu akan dicetak B, B, B — pencocokan pertama clause except terpicu.

Semua exceptions mewarisi dari *BaseException*, sehingga dapat digunakan sebagai karakter pengganti. Gunakan ini dengan sangat hati-hati. Itu juga dapat digunakan untuk mencetak pesan kesalahan dan kemudian menaikkan kembali exceptions (memungkinkan pemanggil untuk menangani exceptions juga) :
_*lihat file [8.3-4.py](https://github.com/SatriaDwiH195410229/workshop-python/blob/main/minggu-06/src/8.3-4.py)*_
```python
import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except BaseException as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise
```
Sebagai alternatif, clause exceptions terakhir dapat menghilangkan nama exceptions, namun nilai exceptions kemudian harus diambil dari `sys.exc_info()`.

Pernyataan try… memiliki clause else except opsional, yang jika ada, harus mengikuti semua clause except. Berguna untuk kode yang harus dijalankan jika clause try tidak memunculkan eksepsi. Sebagai contoh :
_*lihat file [8.3-5.py](https://github.com/SatriaDwiH195410229/workshop-python/blob/main/minggu-06/src/8.3-5.py)*_
```python
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
```
Penggunaan else clause lebih baik daripada menambahkan kode tambahan ke try clause karena menghindari secara tidak sengaja menangkap exceptions yang tidak dimunculkan oleh kode yang dilindungi oleh pernyataan try… except.

Ketika exceptions terjadi, itu mungkin sebagai alternatif, clause exceptions terakhir dapat menghilangkan nama exceptions, namun nilai exceptions kemudian harus diambil dari `sys.exc_info()`.

Clause except dapat menentukan variabel setelah nama exceptions. Variabel terikat ke instance exceptions dengan argumen yang disimpan di `instance.args`. Lebih baik, instance exceptions mendefinisikan `__str__()` sehingga argumen dapat dicetak secara langsung tanpa harus reference `.args`. Seseorang juga dapat membuat instance exceptions terlebih dahulu sebelum menaikkannya dan menambahkan atribut apa pun ke dalamnya seperti yang diinginkan.
_*lihat file [8.3-6.py](https://github.com/SatriaDwiH195410229/workshop-python/blob/main/minggu-06/src/8.3-6.py)*_
```python
>>> try:
...     raise Exception('spam', 'eggs')
... except Exception as inst:
...     print(type(inst))    # the exception instance
...     print(inst.args)     # arguments stored in .args
...     print(inst)          # __str__ allows args to be printed directly,
...                          # but may be overridden in exception subclasses
...     x, y = inst.args     # unpack args
...     print('x =', x)
...     print('y =', y)
...
<class 'Exception'>
('spam', 'eggs')
('spam', 'eggs')
x = spam
y = eggs
```
Jika exceptions memiliki argumen, mereka akan dicetak sebagai bagian terakhir ('detail') dari pesan untuk exceptions yang tidak ditangani.

Pengendali exceptions tidak hanya menangani exceptions jika exceptions muncul di clause try , tetapi juga jika terjadi di dalam fungsi yang dipanggil dalam clause try . Sebagai contoh:
_*lihat file [8.3-7.py](https://github.com/SatriaDwiH195410229/workshop-python/blob/main/minggu-06/src/8.3-7.py)*_
```python
>>> def this_fails():
...     x = 1/0
...
>>> try:
...     this_fails()
... except ZeroDivisionError as err:
...     print('Handling run-time error:', err)
...
Handling run-time error: division by zero
```

# 8.4. Mengangkat pengecualian
Statement *raise* memungkinkan programmer untuk memaksa exceptions tertentu terjadi. Sebagai contoh :
_*lihat file [8.4-1.py](https://github.com/SatriaDwiH195410229/workshop-python/blob/main/minggu-06/src/8.4-1.py)*_
```python
>>> raise NameError('HiThere')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: HiThere
```
Satu-satunya argumen *raise* menunjukkan exceptions yang akan diajukan. Ini harus berupa instance exceptions atau kelas exceptions (kelas yang berasal dari Exception). Jika kelas exceptions dilewatkan, itu akan secara implisit dipakai dengan memanggil konstruktornya tanpa argumen :
_*lihat file [8.4-2.py](https://github.com/SatriaDwiH195410229/workshop-python/blob/main/minggu-06/src/8.4-2.py)*_
```python
raise ValueError  # shorthand for 'raise ValueError()'
```
Jika perlu menentukan apakah exceptions telah dimunculkan tetapi tidak untuk menanganinya, bentuk statement raise yang lebih sederhana memungkinkan untuk menaikkan kembali exceptions :
_*lihat file [8.4-3.py](https://github.com/SatriaDwiH195410229/workshop-python/blob/main/minggu-06/src/8.4-3.py)*_
```python
>>> try:
...     raise NameError('HiThere')
... except NameError:
...     print('An exception flew by!')
...     raise
...
An exception flew by!
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
NameError: HiThere
```

# 8.5. Pemeliharaan pengecualian
Statement *raise* itu memungkinkan opsional from yang memungkinkan exceptions berantai. Sebagai contoh :
_*lihat file [8.5-1.py](https://github.com/SatriaDwiH195410229/workshop-python/blob/main/minggu-06/src/8.5-1.py)*_
```python
# exc must be exception instance or None.
raise RuntimeError from exc
```
Ini bisa berguna saat mengubah exceptions. Sebagai contoh :
_*lihat file [8.5-2.py](https://github.com/SatriaDwiH195410229/workshop-python/blob/main/minggu-06/src/8.5-2.py)*_
```python
>>> def func():
...     raise ConnectionError
...
>>> try:
...     func()
... except ConnectionError as exc:
...     raise RuntimeError('Failed to open database') from exc
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
  File "<stdin>", line 2, in func
ConnectionError

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
RuntimeError: Failed to open database
```
Rantai exceptions terjadi secara otomatis ketika exceptions dinaikkan di dalam *except* atau bagian *finally*. Ini dapat dinonaktifkan dengan menggunakan `idiom:from None`.
_*lihat file [8.5-3.py](https://github.com/SatriaDwiH195410229/workshop-python/blob/main/minggu-06/src/8.5-3.py)*_
```python
>>> try:
...   open('database.sqlite')
... except OSError:
...     raise RuntimeError from None
...
Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
RuntimeError
```

# 8.6. Pengecualian yang ditentukan pengguna
Program dapat memberi nama exceptions mereka sendiri dengan membuat kelas exceptions baru. Exceptions biasanya harus diturunkan dari kelas exception, baik secara langsung maupun tidak langsung.

Kelas exceptions dapat didefinisikan yang melakukan apa pun yang dapat dilakukan kelas lain, tetapi biasanya dibuat sederhana, hanya menawarkan sejumlah atribut yang memungkinkan informasi tentang kesalahan diekstraksi oleh penangan untuk exceptions.

Sebagian besar exceptions didefinisikan dengan nama yang diakhiri dengan "Error", mirip dengan penamaan exceptions standar.

Banyak modul standar mendefinisikan exceptions mereka sendiri untuk melaporkan kesalahan yang mungkin terjadi dalam fungsi yang mereka tetapkan. Informasi lebih lanjut tentang kelas disajikan dalam bab Kelas.

# 8.7. Mendefinisikan tindakan pembersihan
Statement try tersebut memiliki clause opsional lain yang dimaksudkan untuk mendefinisikan tindakan pembersihan yang harus dilakukan dalam semua keadaan. Sebagai contoh :
_*lihat file [8.7-1.py](https://github.com/SatriaDwiH195410229/workshop-python/blob/main/minggu-06/src/8.7-1.py)*_
```python
>>> try:
...     raise KeyboardInterrupt
... finally:
...     print('Goodbye, world!')
...
Goodbye, world!
KeyboardInterrupt
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
```
Jika ada finally clause, finally clause akan dieksekusi sebagai tugas terakhir sebelum statement try selesai. Clause finally berjalan apakah statement try menghasilkan exceptions atau tidak. Poin-poin berikut membahas kasus yang lebih kompleks ketika exceptions terjadi :

* Jika exceptions terjadi selama eksekusi try clause, exceptions dapat ditangani oleh except clause. Jika eksepsi tidak ditangani oleh except clause, eksepsi dimunculkan kembali setelah finally clause dieksekusi.

* Exceptions dapat terjadi selama eksekusi suatu *except* atau else clause. Sekali lagi, exceptions dinaikkan kembali setelah finally clause dieksekusi.

* Jika finally clause mengeksekusi *break*, *continue* atau statement *return*, exceptions tidak dimunculkan kembali.

* Jika statement try mencapai *break*, *continue* atau statement *return*, finally clause akan dieksekusi tepat sebelum eksekusi *break*, *continue* atau statement *return*.

* Jika finally clause menyertakan statement *return*, nilai yang dikembalikan akan menjadi nilai dari pernyataan finally clause *return*, bukan nilai dari pernyataan try clause *return*.

Sebagai contoh :
_*lihat file [8.7-2.py](https://github.com/SatriaDwiH195410229/workshop-python/blob/main/minggu-06/src/8.7-2.py)*_
```python
>>> def bool_return():
...     try:
...         return True
...     finally:
...         return False
...
>>> bool_return()
False
```
Contoh yang lebih rumit :
_*lihat file [8.7-3.py](https://github.com/SatriaDwiH195410229/workshop-python/blob/main/minggu-06/src/8.7-3.py)*_
```python
>>> def divide(x, y):
...     try:
...         result = x / y
...     except ZeroDivisionError:
...         print("division by zero!")
...     else:
...         print("result is", result)
...     finally:
...         print("executing finally clause")
...
>>> divide(2, 1)
result is 2.0
executing finally clause
>>> divide(2, 0)
division by zero!
executing finally clause
>>> divide("2", "1")
executing finally clause
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in divide
TypeError: unsupported operand type(s) for /: 'str' and 'str'
```
Seperti yang dilihat, finally clause dieksekusi dalam event apa pun. Dibangkitkan *TypeError* dengan membagi dua string tidak ditangani oleh except clause dan karena itu dinaikkan kembali setelah finally clause dieksekusi.

Dalam aplikasi dunia nyata, finally clause ini berguna untuk melepaskan sumber daya eksternal (seperti file atau koneksi jaringan), terlepas dari apakah penggunaan sumber daya itu berhasil.

# 8.8. Tindakan pembersihan yang telah ditentukan
Beberapa objek menentukan tindakan pembersihan standar yang harus dilakukan ketika objek tidak lagi diperlukan, terlepas dari apakah operasi menggunakan objek berhasil atau gagal. Lihat contoh berikut, yang mencoba membuka file dan mencetak isinya ke layar.
_*lihat file [8.8-1.py](https://github.com/SatriaDwiH195410229/workshop-python/blob/main/minggu-06/src/8.8-1.py)*_
```python
for line in open("myfile.txt"):
    print(line, end="")
```
Masalah dengan kode ini adalah membiarkan file terbuka untuk waktu yang tidak ditentukan setelah bagian kode ini selesai dieksekusi. Ini bukan masalah dalam skrip sederhana, tetapi bisa menjadi masalah untuk aplikasi yang lebih besar. Statement *with* tersebut memungkinkan objek seperti file untuk digunakan dengan cara yang memastikan mereka selalu dibersihkan dengan cepat dan benar.
_*lihat file [8.8-2.py](https://github.com/SatriaDwiH195410229/workshop-python/blob/main/minggu-06/src/8.8-2.py)*_
```python
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
```
Setelah statement dieksekusi, file `f` selalu ditutup, bahkan jika ada masalah saat memproses baris. Objek yang, seperti file, menyediakan tindakan pembersihan yang telah ditentukan sebelumnya dan akan menunjukkan hal ini dalam dokumentasinya.