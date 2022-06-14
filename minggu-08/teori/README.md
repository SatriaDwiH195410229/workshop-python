# Minggu ke-8 : Mempelajari Tutorial Bab 10 ~ Standard Library

# 10.1. Antarmuka sistem operasi
Modul [os](https://docs.python.org/3/library/os.html#module-os) menyediakan lusinan fungsi untuk berinteraksi dengan sistem operasi :

Lihat file : **[10.1-1.py](https://github.com/SatriaDwiH195410229/workshop-python/blob/main/minggu-08/src/10.1-1.py)**
```python
>>> import os
>>> os.getcwd()      # Return the current working directory
'C:\\Python310'
>>> os.chdir('/server/accesslogs')   # Change current working directory
>>> os.system('mkdir today')   # Run the command mkdir in the system shell
0
```
Pastikan untuk menggunakan gaya `import os` alih-alih dari `os import *`. Ini akan mencegah [os.open()](https://docs.python.org/3/library/os.html#os.open) membayangi fungsi [open()](https://docs.python.org/3/library/functions.html#open) bawaan yang beroperasi jauh berbeda.
Built-in [dir()](https://docs.python.org/3/library/functions.html#dir) dan [help()](https://docs.python.org/3/library/functions.html#help) fungsi berguna sebagai alat bantu interaktif untuk bekerja dengan modul besar seperti [os](https://docs.python.org/3/library/os.html#module-os) :

Lihat file : **[10.1-2.py](https://github.com/SatriaDwiH195410229/workshop-python/blob/main/minggu-08/src/10.1-2.py)**
```python
>>> import os
>>> dir(os)
<returns a list of all module functions>
>>> help(os)
<returns an extensive manual page created from the module's docstrings>
```
Untuk tugas manajemen file dan direktori harian, [shutil](https://docs.python.org/3/library/shutil.html#module-shutil) modul ini menyediakan antarmuka tingkat tinggi yang lebih mudah digunakan :

Lihat file : **[10.1-3.py](https://github.com/SatriaDwiH195410229/workshop-python/blob/main/minggu-08/src/10.1-3.py)**
```python
>>> import shutil
>>> shutil.copyfile('data.db', 'archive.db')
'archive.db'
>>> shutil.move('/build/executables', 'installdir')
'installdir'
```

# 10.2. File wildcard
Modul [glob](https://docs.python.org/3/library/glob.html#module-glob) menyediakan fungsi untuk membuat daftar file dari pencarian direktori wildcard :

Lihat file : **[10.2.py](https://github.com/SatriaDwiH195410229/workshop-python/blob/main/minggu-08/src/10.2.py)**
```python
>>> import glob
>>> glob.glob('*.py')
['primes.py', 'random.py', 'quote.py']
```

# 10.3. Argumen baris perintah
Skrip utilitas umum sering kali perlu memproses argumen baris perintah. Argumen ini disimpan dalam atribut *argv*[sys](https://docs.python.org/3/library/sys.html#module-sys) modul sebagai daftar. Misalnya hasil keluaran berikut dari menjalankan di baris perintah:`python demo.py one two three`

Lihat file : **[10.3-1.py](https://github.com/SatriaDwiH195410229/workshop-python/blob/main/minggu-08/src/10.3-1.py)**
```python
>>> import sys
>>> print(sys.argv)
['demo.py', 'one', 'two', 'three']
```
Modul [argparse](https://docs.python.org/3/library/argparse.html#module-argparse) menyediakan mekanisme yang lebih canggih untuk memproses argumen baris perintah. Skrip berikut mengekstrak satu atau lebih nama file dan sejumlah baris opsional yang akan ditampilkan :

Lihat file : **[10.3-2.py](https://github.com/SatriaDwiH195410229/workshop-python/blob/main/minggu-08/src/10.3-2.py)**
```python
import argparse

parser = argparse.ArgumentParser(
    prog='top',
    description='Show top lines from each file')
parser.add_argument('filenames', nargs='+')
parser.add_argument('-l', '--lines', type=int, default=10)
args = parser.parse_args()
print(args)
```
Saat dijalankan pada baris perintah dengan , skrip disetel ke dan ke `.python top.py --lines=5 alpha.txt beta.txtargs.lines5args.filenames['alpha.txt', 'beta.txt']`

# 10.4. Pengalihan output kesalahan dan penghentian program
Modul [sys](https://docs.python.org/3/library/sys.html#module-sys) juga memiliki atribut untuk *stdin* , *stdout* , dan *stderr*. Yang terakhir ini berguna untuk memancarkan peringatan dan pesan kesalahan agar terlihat bahkan ketika stdout telah dialihkan :

Lihat file : **[10.4.py](https://github.com/SatriaDwiH195410229/workshop-python/blob/main/minggu-08/src/10.4.py)**
```python
>>> sys.stderr.write('Warning, log file not found starting a new one\n')
Warning, log file not found starting a new one
```
Cara paling langsung untuk menghentikan skrip adalah dengan menggunakan `sys.exit()`.

# 10.5. Pencocokan pola string
Modul [re](https://docs.python.org/3/library/re.html#module-re) menyediakan alat ekspresi reguler untuk pemrosesan string tingkat lanjut. Untuk pencocokan dan manipulasi yang kompleks, ekspresi reguler menawarkan solusi yang ringkas dan dioptimalkan :

Lihat file : **[10.5-1.py](https://github.com/SatriaDwiH195410229/workshop-python/blob/main/minggu-08/src/10.5-1.py)**
```python
>>> import re
>>> re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
['foot', 'fell', 'fastest']
>>> re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
'cat in the hat'
```
Ketika hanya kemampuan sederhana yang diperlukan, metode string lebih disukai karena lebih mudah dibaca dan di-debug :

Lihat file : **[10.5-2.py](https://github.com/SatriaDwiH195410229/workshop-python/blob/main/minggu-08/src/10.5-2.py)**
```python
>>> 'tea for too'.replace('too', 'two')
'tea for two'
```

# 10.6. Matematika _
Modul [math](https://docs.python.org/3/library/math.html#module-math) memberikan akses ke fungsi pustaka C yang mendasari untuk matematika floating point :

Lihat file : **[10.6-1.py](https://github.com/SatriaDwiH195410229/workshop-python/blob/main/minggu-08/src/10.6-1.py)**
```python
>>> import math
>>> math.cos(math.pi / 4)
0.70710678118654757
>>> math.log(1024, 2)
10.0
```
Modul [random](https://docs.python.org/3/library/random.html#module-random) menyediakan alat untuk membuat pilihan acak :

Lihat file : **[10.6-2.py](https://github.com/SatriaDwiH195410229/workshop-python/blob/main/minggu-08/src/10.6-2.py)**
```python
>>> import random
>>> random.choice(['apple', 'pear', 'banana'])
'apple'
>>> random.sample(range(100), 10)   # sampling without replacement
[30, 83, 16, 4, 8, 81, 41, 50, 18, 33]
>>> random.random()    # random float
0.17970987693706186
>>> random.randrange(6)    # random integer chosen from range(6)
4
```
Modul [statistics](https://docs.python.org/3/library/statistics.html#module-statistics) menghitung properti statistik dasar (rata-rata, median, varians, dll.) dari data numerik :

Lihat file : **[10.6-3.py](https://github.com/SatriaDwiH195410229/workshop-python/blob/main/minggu-08/src/10.6-3.py)**
```python
>>> import statistics
>>> data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
>>> statistics.mean(data)
1.6071428571428572
>>> statistics.median(data)
1.25
>>> statistics.variance(data)
1.3720238095238095
```
Proyek SciPy < [https://scipy.org](https://scipy.org) > memiliki banyak modul lain untuk perhitungan numerik.

# 10.7. Akses internet
Ada sejumlah modul untuk mengakses internet dan memproses protokol internet. Dua yang paling sederhana adalah [urllib.request](https://docs.python.org/3/library/urllib.request.html#module-urllib.request) untuk mengambil data dari URL dan [smtplib](https://docs.python.org/3/library/smtplib.html#module-smtplib) untuk mengirim email :

Lihat file : **[10.7.py](https://github.com/SatriaDwiH195410229/workshop-python/blob/main/minggu-08/src/10.7.py)**
```python
>>> from urllib.request import urlopen
>>> with urlopen('http://worldtimeapi.org/api/timezone/etc/UTC.txt') as response:
...     for line in response:
...         line = line.decode()             # Convert bytes to a str
...         if line.startswith('datetime'):
...             print(line.rstrip())         # Remove trailing newline
...
datetime: 2022-01-01T01:36:47.689215+00:00

>>> import smtplib
>>> server = smtplib.SMTP('localhost')
>>> server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
... """To: jcaesar@example.org
... From: soothsayer@example.org
...
... Beware the Ides of March.
... """)
>>> server.quit()
```
(Perhatikan bahwa contoh kedua membutuhkan server surat yang berjalan di localhost.)

# 10.8. Tanggal dan waktu
Modul [datetime](https://docs.python.org/3/library/datetime.html#module-datetime) menyediakan kelas untuk memanipulasi tanggal dan waktu dengan cara yang sederhana dan kompleks. Sementara aritmatika tanggal dan waktu didukung, fokus implementasinya adalah pada ekstraksi anggota yang efisien untuk pemformatan dan manipulasi keluaran. Modul ini juga mendukung objek yang sadar zona waktu.

Lihat file : **[10.8.py](https://github.com/SatriaDwiH195410229/workshop-python/blob/main/minggu-08/src/10.8.py)**
```python
>>> # dates are easily constructed and formatted
>>> from datetime import date
>>> now = date.today()
>>> now
datetime.date(2003, 12, 2)
>>> now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
'12-02-03. 02 Dec 2003 is a Tuesday on the 02 day of December.'

>>> # dates support calendar arithmetic
>>> birthday = date(1964, 7, 31)
>>> age = now - birthday
>>> age.days
14368
```

# 10.9. Kompresi data
Pengarsipan data umum dan format kompresi secara langsung didukung oleh modul termasuk: [zlib](https://docs.python.org/3/library/zlib.html#module-zlib), [gzip](https://docs.python.org/3/library/gzip.html#module-gzip), [bz2](https://docs.python.org/3/library/bz2.html#module-bz2), [lzma](https://docs.python.org/3/library/lzma.html#module-lzma), [zipfile](https://docs.python.org/3/library/zipfile.html#module-zipfile) dan [tarfile](https://docs.python.org/3/library/tarfile.html#module-tarfile).

Lihat file : **[10.9.py](https://github.com/SatriaDwiH195410229/workshop-python/blob/main/minggu-08/src/10.9.py)**
```python
>>> import zlib
>>> s = b'witch which has which witches wrist watch'
>>> len(s)
41
>>> t = zlib.compress(s)
>>> len(t)
37
>>> zlib.decompress(t)
b'witch which has which witches wrist watch'
>>> zlib.crc32(s)
226805979
```

# 10.10. Pengukuran kinerja
Beberapa pengguna Python mengembangkan minat yang mendalam untuk mengetahui kinerja relatif dari pendekatan yang berbeda untuk masalah yang sama. Python menyediakan alat pengukuran yang menjawab pertanyaan-pertanyaan itu dengan segera.

Misalnya, mungkin tergoda untuk menggunakan fitur pengepakan dan pembongkaran Tuple alih-alih pendekatan tradisional untuk bertukar argumen. Modul [timeit](https://docs.python.org/3/library/timeit.html#module-timeit) dengan cepat menunjukkan keunggulan kinerja sederhana :

Lihat file : **[10.10.py](https://github.com/SatriaDwiH195410229/workshop-python/blob/main/minggu-08/src/10.10.py)**
```python
>>> from timeit import Timer
>>> Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
0.57535828626024577
>>> Timer('a,b = b,a', 'a=1; b=2').timeit()
0.54962537085770791
```
Berbeda dengan timeit tingkat granularitas yang bagus, modul profile and pstats menyediakan alat untuk mengidentifikasi bagian kritis waktu dalam blok kode yang lebih besar.

# 10.11. Kontrol kualitas
Modul [doctest](https://docs.python.org/3/library/doctest.html#module-doctest) menyediakan alat untuk memindai modul dan memvalidasi tes yang tertanam dalam dokumen program. Konstruksi pengujian sesederhana memotong dan menempelkan panggilan biasa beserta hasilnya ke dalam docstring. Ini meningkatkan dokumentasi dengan memberikan contoh kepada pengguna dan memungkinkan modul doctest untuk memastikan kode tetap sesuai dengan dokumentasi :

Lihat file : **[10.11-1.py](https://github.com/SatriaDwiH195410229/workshop-python/blob/main/minggu-08/src/10.11-1.py)**
```python
def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest
doctest.testmod()   # automatically validate the embedded tests
```
Modul [unittest](https://docs.python.org/3/library/unittest.html#module-unittest) ini tidak semudah modul [doctest](https://docs.python.org/3/library/doctest.html#module-doctest), tetapi memungkinkan serangkaian pengujian yang lebih komprehensif untuk dipertahankan dalam file terpisah :

Lihat file : **[10.11-2.py](https://github.com/SatriaDwiH195410229/workshop-python/blob/main/minggu-08/src/10.11-2.py)**
```python
import unittest

class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)

unittest.main()  # Calling from the command line invokes all tests
```

# 10.12. Baterai
Python memiliki filosofi "termasuk baterai". Ini paling baik dilihat melalui kemampuan canggih dan kuat dari paket-paketnya yang lebih besar. Sebagai contoh:
* Modul [xmlrpc.client](https://docs.python.org/3/library/xmlrpc.client.html#module-xmlrpc.client) dan [xmlrpc.server](https://docs.python.org/3/library/xmlrpc.server.html#module-xmlrpc.server) membuat penerapan panggilan prosedur jarak jauh menjadi tugas yang hampir sepele. Terlepas dari nama modul, tidak ada pengetahuan langsung atau penanganan XML yang diperlukan.
* Paket [email](https://docs.python.org/3/library/email.html#module-email) adalah perpustakaan untuk mengelola pesan email, termasuk MIME dan lainnyaDokumen pesan berbasis **[RFC 2822](https://datatracker.ietf.org/doc/html/rfc2822.html)** . Tidak seperti [smtplib](https://docs.python.org/3/library/smtplib.html#module-smtplib) dan [poplib](https://docs.python.org/3/library/poplib.html#module-poplib) yang benar-benar mengirim dan menerima pesan, paket email memiliki perangkat lengkap untuk membangun atau mendekode struktur pesan yang kompleks (termasuk lampiran) dan untuk menerapkan pengkodean internet dan protokol header.
* Paket [json](https://docs.python.org/3/library/json.html#module-json) menyediakan dukungan kuat untuk menguraikan format pertukaran data populer ini. Modul [csv](https://docs.python.org/3/library/csv.html#module-csv) mendukung pembacaan dan penulisan file secara langsung dalam format Comma-Separated Value, umumnya didukung oleh database dan spreadsheet. Pemrosesan XML didukung oleh [xml.etree.ElementTree](https://docs.python.org/3/library/xml.etree.elementtree.html#module-xml.etree.ElementTree), [xml.dom](https://docs.python.org/3/library/xml.dom.html#module-xml.dom) dan [xml.saxpaket](https://docs.python.org/3/library/xml.sax.html#module-xml.sax). Bersama-sama, modul dan paket ini sangat menyederhanakan pertukaran data antara aplikasi Python dan alat lainnya.
* Modul [sqlite3](https://docs.python.org/3/library/sqlite3.html#module-sqlite3) adalah pembungkus untuk pustaka database SQLite, menyediakan database persisten yang dapat diperbarui dan diakses menggunakan sintaks SQL yang sedikit tidak standar.
* Internasionalisasi didukung oleh sejumlah modul termasuk [gettext](https://docs.python.org/3/library/gettext.html#module-gettext), [locale](https://docs.python.org/3/library/locale.html#module-locale), dan [codecs](https://docs.python.org/3/library/codecs.html#module-codecs) paket.