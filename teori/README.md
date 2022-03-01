# Minggu ke-4 : Modul - Mempelajari Tutorial Bab 6

## 6. Modul
Jika kita keluar dari interpreter Python dan memasukkannya lagi, definisi yang telah dibuat (fungsi dan variabel) akan hilang. Oleh karena itu, jika ingin menulis program yang lebih panjang, sebaiknya menggunakan editor teks untuk menyiapkan input untuk penerjemah dan menjalankannya dengan file tersebut sebagai input. Ini dikenal sebagai membuat *skrip*. Saat program semakin panjang, dan mungkin ingin membaginya menjadi beberapa file untuk perawatan yang lebih mudah. Atau mungkin juga ingin menggunakan fungsi praktis yang telah ditulis di beberapa program tanpa menyalin definisinya ke setiap program.

Modul adalah file yang berisi definisi dan pernyataan Python. Nama file adalah nama modul dengan akhiran **.py**ditambahkan. Dalam sebuah modul, nama modul (sebagai string) tersedia sebagai nilai dari variabel global __name__. Misalnya, gunakan editor teks favorit Anda untuk membuat file bernama **fibo.py** di direktori saat ini dengan konten berikut:
```python
# Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
```

Sekarang masukkan interpreter Python dan impor modul ini dengan perintah berikut:
```python
>>> import fibo
```

Ini tidak memasukkan nama fungsi yang didefinisikan dalam **fibo** secara langsung di tabel simbol saat ini; itu hanya memasukkan nama modul **fibo** di sana. Menggunakan nama modul Anda dapat mengakses fungsi:
```python
>>> fibo.fib(1000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
>>> fibo.fib2(100)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
>>> fibo.__name__
'fibo'
```

Jika Anda ingin sering menggunakan suatu fungsi, Anda dapat menetapkannya ke nama lokal:
```python
>>> fib = fibo.fib
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

## 6.1. Lebih lanjut tentang Module
Modul dapat berisi pernyataan yang dapat dieksekusi serta definisi fungsi. Pernyataan ini dimaksudkan untuk menginisialisasi modul. Mereka dieksekusi hanya saat *pertama* kali nama modul ditemukan dalam pernyataan impor.

Setiap modul memiliki tabel simbol pribadinya sendiri, yang digunakan sebagai tabel simbol global oleh semua fungsi yang didefinisikan dalam modul. Dengan demikian, pembuat modul dapat menggunakan variabel global dalam modul tanpa mengkhawatirkan bentrokan yang tidak disengaja dengan variabel global pengguna. Di sisi lain, jika kita tahu apa yang kita lakukan, kita dapat menyentuh variabel global modul dengan notasi yang sama yang digunakan untuk merujuk ke fungsinya, **modname.itemname.**


Ada varian dari pernyataan impor yang mengimpor nama dari modul langsung ke tabel simbol modul pengimpor. Sebagai contoh:
```python
>>> from fibo import fib, fib2
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

Ini tidak memperkenalkan nama modul dari mana impor diambil dalam tabel simbol lokal (jadi dalam contoh, **fibo** tidak didefinisikan).

Bahkan ada varian untuk mengimpor semua nama yang didefinisikan oleh modul:
```python
>>> from fibo import *
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

Jika nama modul diikuti oleh as, maka nama berikut sebagai terikat langsung ke modul yang diimpor.
```python
>>> import fibo as fib
>>> fib.fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

Ini secara efektif mengimpor modul dengan cara yang sama seperti **import fibo**, dengan satu-satunya perbedaan tersedia sebagai **fib**.

Itu juga dapat digunakan saat memanfaatkan dari dengan efek serupa:
```python
>>> from fibo import fib as fibonacci
>>> fibonacci(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

*```Catatan : Untuk alasan efisiensi, setiap modul hanya diimpor sekali per sesi juru bahasa. Oleh karena itu, jika Anda mengubah modul, Anda harus memulai ulang penerjemah – atau, jika hanya satu modul yang ingin Anda uji secara interaktif, gunakan importlib.reload(), mis. impor lib; importlib.reload (nama modul).```*

* ### 6.1.1. Menjalankan modul sebagai skrip
  Saat menjalankan modul Python dengan :

``` python
python fibo.py <arguments>
```

  kode dalam modul akan dieksekusi, sama seperti jika Anda mengimpornya, tetapi dengan __name__ disetel ke "__main__". Itu berarti dengan menambahkan kode ini di akhir modul :
``` python
if __name__ == "__main__":
  import sys
  fib(int(sys.argv[1]))
```

  Anda dapat membuat file dapat digunakan sebagai skrip serta modul yang dapat diimpor, karena kode yang mem-parsing baris perintah hanya berjalan jika modul dijalankan sebagai file **"main"**:
```python
python$ python fibo.py 50
0 1 1 2 3 5 8 13 21 34
```
  Jika modul diimpor, kode tidak dijalankan :
```python
>>> import fibo
>>>
```

  Ini sering digunakan baik untuk menyediakan antarmuka pengguna yang nyaman ke modul, atau untuk tujuan pengujian (menjalankan modul saat skrip mengeksekusi rangkaian pengujian).

* ### 6.1.2. Jalur Pencarian Modul
  Saat modul bernama spam diimpor, penerjemah pertama-tama mencari modul bawaan dengan nama itu. Jika tidak ditemukan, maka akan mencari file bernama **spam.py** dalam daftar direktori yang diberikan oleh variabel **sys.path. sys.path** diinisialisasi dari lokasi ini:
1. Direktori yang berisi skrip input (atau direktori saat ini ketika tidak ada file yang ditentukan).
2. *PYTHONPATH* (daftar nama direktori, dengan sintaks yang sama dengan variabel shell PATH).
3. Default yang bergantung pada penginstalan (menurut konvensi termasuk direktori *site-packages*, ditangani oleh modul *situs*).

* ### 6.1.3. File Python "Dikompilasi"
  Untuk mempercepat pemuatan modul, Python menyimpan versi kompilasi dari setiap modul di direktori __pycache__ di bawah nama **module.*version*.pyc**, di mana versi mengkodekan format file yang dikompilasi; biasanya berisi nomor versi Python. Misalnya, di CPython rilis 3.3 versi kompilasi dari spam.py akan di-cache sebagai __pycache__/spam.cpython-33.pyc. Konvensi penamaan ini memungkinkan modul yang dikompilasi dari rilis yang berbeda dan versi Python yang berbeda untuk hidup berdampingan.

## 6.2. Modul Standar
Python hadir dengan pustaka modul standar, yang dijelaskan dalam dokumen terpisah, Referensi Pustaka Python (“Library Reference” hereafter). Beberapa modul dibangun ke dalam juru bahasa; ini menyediakan akses ke operasi yang bukan bagian dari inti bahasa tetapi tetap dibangun, baik untuk efisiensi atau untuk menyediakan akses ke sistem operasi primitif seperti panggilan sistem. Kumpulan modul tersebut adalah opsi konfigurasi yang juga bergantung pada platform yang mendasarinya. Misalnya, modul *winreg* hanya tersedia di sistem Windows. Satu modul tertentu patut mendapat perhatian: *sys*, yang dibangun ke dalam setiap juru bahasa Python. Variabel **sys.ps1** dan **sys.ps2** mendefinisikan string yang digunakan sebagai prompt primer dan sekunder:
```python
>>> import sys
>>> sys.ps1
'>>> '
>>> sys.ps2
'... '
>>> sys.ps1 = 'C> '
C> print('Yuck!')
Yuck!
C>
```

Kedua variabel ini hanya ditentukan jika interpreter dalam mode interaktif.

Variabel **sys.path** adalah daftar string yang menentukan jalur pencarian interpreter untuk modul. Ini diinisialisasi ke jalur default yang diambil dari variabel lingkungan *PYTHONPATH*, atau dari default bawaan jika *PYTHONPATH* tidak disetel. Anda dapat memodifikasinya menggunakan operasi daftar standar:
```python
>>> import sys
>>> sys.path.append('/ufs/guido/lib/python')
```

## 6.3. Fungsi dir()
Fungsi bawaan **dir()** digunakan untuk mengetahui nama yang didefinisikan oleh modul. Ini mengembalikan daftar string yang diurutkan:
_*lihat [6.3.py](https://github.com/SatriaDwiH195410229/workshop-python/blob/main/minggu-04/src/6.3.py)*_

Tanpa argumen, dir() mencantumkan nama yang telah Anda tetapkan saat ini:
```python
a = [1, 2, 3, 4, 5]
import fibo
fib = fibo.fib
dir()
['__builtins__', '__name__', 'a', 'fib', 'fibo', 'sys']
```

Perhatikan bahwa ini mencantumkan semua jenis nama: variabel, modul, fungsi, dll.

**dir()** tidak mencantumkan nama fungsi dan variabel bawaan. Jika Anda ingin daftarnya, mereka didefinisikan dalam modul standar bawaan **builtins**:
_*lihat [builtins 6.3.py](https://github.com/SatriaDwiH195410229/workshop-python/blob/main/minggu-04/src/builtins6.3.py)*_

## 6.4. Paket
Paket adalah cara menyusun namespace modul Python dengan menggunakan "nama modul bertitik". Misalnya, nama modul A.B menunjuk submodule bernama **B** dalam paket bernama **A**. Sama seperti penggunaan modul menyelamatkan penulis modul yang berbeda dari harus khawatir tentang nama variabel global masing-masing, penggunaan nama modul bertitik menyelamatkan penulis paket multi-modul seperti NumPy atau Bantal karena harus khawatir tentang nama modul masing-masing.

Misalkan Anda ingin merancang kumpulan modul (a "package") untuk penanganan file suara dan data suara yang seragam. Ada banyak format file suara yang berbeda (biasanya dikenali dari ekstensinya, misalnya: **.wav, .aiff, .au**), jadi Anda mungkin perlu membuat dan memelihara koleksi modul yang terus bertambah untuk konversi antara berbagai format file. Ada juga banyak operasi berbeda yang mungkin ingin Anda lakukan pada data suara (seperti mencampur, menambahkan gema, menerapkan fungsi equalizer, membuat efek stereo buatan), jadi selain itu Anda akan menulis aliran modul yang tidak pernah berakhir untuk dilakukan operasi ini. Berikut adalah kemungkinan struktur untuk paket Anda (dinyatakan dalam sistem file hierarkis):
```python
>sound/                          Top-level package
      __init__.py               Initialize the sound package
      formats/                  Subpackage for file format conversions
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  Subpackage for sound effects
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  Subpackage for filters
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...
```

Saat mengimpor paket, Python mencari melalui direktori di sys.path mencari subdirektori paket. File __init__.py diperlukan untuk membuat Python memperlakukan direktori yang berisi file sebagai paket. Ini mencegah direktori dengan nama umum, seperti **string**, secara tidak sengaja menyembunyikan modul valid yang muncul kemudian di jalur pencarian modul. Dalam kasus yang paling sederhana, __init__.py hanya dapat berupa file kosong, tetapi juga dapat mengeksekusi kode inisialisasi untuk paket atau mengatur variabel __all__, yang akan dijelaskan nanti.

Pengguna paket dapat mengimpor modul individual dari paket, misalnya:
```python
import sound.effects.echo
```
Ini memuat submodule *sound.effects.echo*. Itu harus dirujuk dengan nama lengkapnya.
```python
sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)
```

Cara alternatif untuk mengimpor submodule adalah:
```python
from sound.effects import echo
```

Ini juga memuat submodul echo, dan membuatnya tersedia tanpa awalan paketnya, sehingga dapat digunakan sebagai berikut:
```python
echo.echofilter(input, output, delay=0.7, atten=4)
```

Namun variasi lain adalah mengimpor fungsi atau variabel yang diinginkan secara langsung:
```python
from sound.effects.echo import echofilter
```

Sekali lagi, ini memuat submodule echo, tetapi ini membuat fungsinya echofilter() langsung tersedia:
```python
echofilter(input, output, delay=0.7, atten=4)
```
Perhatikan bahwa saat **from package import item**, item dapat berupa submodul (atau subpaket) paket, atau nama lain yang ditentukan dalam paket, seperti fungsi, kelas, atau variabel. Pernyataan **import** pertama-tama menguji apakah item tersebut didefinisikan dalam paket; jika tidak, ia menganggapnya sebagai modul dan mencoba memuatnya. Jika gagal menemukannya, pengecualian ImportError dimunculkan.

Sebaliknya, saat menggunakan sintaks seperti **import item.subitem.subsubitem**, setiap item kecuali yang terakhir harus berupa paket; item terakhir dapat berupa modul atau paket tetapi tidak dapat berupa kelas atau fungsi atau variabel yang ditentukan dalam item sebelumnya.

* ### 6.4.1. Mengimpor Dari Paket
Sekarang apa yang terjadi ketika pengguna menulis dari sound.effects import ? Idealnya, orang akan berharap bahwa ini entah bagaimana keluar ke sistem file, menemukan submodul mana yang ada dalam paket, dan mengimpor semuanya. Ini bisa memakan waktu lama dan mengimpor sub-modul mungkin memiliki efek samping yang tidak diinginkan yang seharusnya hanya terjadi ketika sub-modul diimpor secara eksplisit.

Satu-satunya solusi adalah bagi pembuat paket untuk memberikan indeks eksplisit dari paket tersebut. Pernyataan impor menggunakan konvensi berikut: jika kode __init__.py paket mendefinisikan daftar bernama __all__, itu dianggap sebagai daftar nama modul yang harus diimpor ketika **dari paket** __import *__ ditemukan. Terserah pembuat paket untuk tetap memperbarui daftar ini ketika versi baru dari paket dirilis. Pembuat paket juga dapat memutuskan untuk tidak mendukungnya, jika mereka tidak melihat gunanya mengimpor * dari paket mereka. Misalnya, file **sound/effects/__init__.py** dapat berisi kode berikut:
```python
__all__ = ["echo", "surround", "reverse"]
```

Ini berarti bahwa from sound.effects import * akan mengimpor tiga submodul yang bernama dari paket suara.

Jika __all__ tidak ditentukan, pernyataan dari **sound.effects** __import *__ tidak mengimpor semua submodul dari paket sound.effects ke dalam namespace saat ini; itu hanya memastikan bahwa paket sound.effects telah diimpor (mungkin menjalankan kode inisialisasi apa pun di **__init__.py**) dan kemudian mengimpor nama apa pun yang ditentukan dalam paket. Ini termasuk nama yang ditentukan (dan submodul yang dimuat secara eksplisit) oleh **__init__.py**. Ini juga mencakup submodul apa pun dari paket yang dimuat secara eksplisit oleh pernyataan impor sebelumnya. Pertimbangkan kode ini:
```python
import sound.effects.echo
import sound.effects.surround
from sound.effects import *
```

* ### 6.4.2. Referensi Intra-paket
Ketika paket disusun menjadi subpaket (seperti paket suara dalam contoh), Anda dapat menggunakan impor absolut untuk merujuk ke submodul paket saudara kandung. Sebagai contoh, jika modul sound.filters.vocoder perlu menggunakan modul echo dalam paket sound.effects, modul tersebut dapat menggunakan dari **sound.effect import echo**.

Anda juga dapat menulis impor relatif, dengan bentuk nama impor modul dari pernyataan impor. Impor ini menggunakan titik awal untuk menunjukkan paket saat ini dan induk yang terlibat dalam impor relatif. Dari modul surround misalnya, Anda dapat menggunakan:
```python
from . import echo
from .. import formats
from ..filters import equalizer
```

* ### 6.4.3. Paket di Beberapa Direktori
Paket mendukung satu atribut khusus lagi, __path__. Ini diinisialisasi menjadi daftar yang berisi nama direktori yang menyimpan **__init__.py** paket sebelum kode dalam file itu dieksekusi. Variabel ini dapat dimodifikasi; hal itu akan memengaruhi pencarian modul dan subpaket di masa mendatang yang terdapat dalam paket.

Meskipun fitur ini tidak sering diperlukan, fitur ini dapat digunakan untuk memperluas kumpulan modul yang ditemukan dalam sebuah paket.
