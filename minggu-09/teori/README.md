# Minggu ke-9 : Mempelajari Tutorial Bab 12 dan Mengerjakan [Conda-Getting Started](https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html)~ environments dan Paket Virtual

# 12.1. Pendahuluan
Aplikasi Python akan sering menggunakan paket dan modul yang tidak datang sebagai bagian dari perpustakaan standar. Aplikasi terkadang memerlukan versi perpustakaan tertentu, karena aplikasi mungkin mengharuskan bug tertentu telah diperbaiki atau aplikasi mungkin ditulis menggunakan versi antarmuka perpustakaan yang sudah usang.

Ini berarti tidak mungkin satu instalasi Python memenuhi persyaratan setiap aplikasi. Jika aplikasi A membutuhkan versi 1.0 dari modul tertentu tetapi aplikasi B membutuhkan versi 2.0, maka persyaratan tersebut bertentangan dan menginstal versi 1.0 atau 2.0 akan membuat satu aplikasi tidak dapat berjalan.

Solusi untuk masalah ini adalah dengan membuat [environments virtual](https://docs.python.org/3/glossary.html#term-virtual-environment), direktori mandiri yang berisi instalasi Python untuk versi Python tertentu, ditambah sejumlah paket tambahan.

# 12.2. Membuat environments virtual
Untuk membuat environments virtual, tentukan direktori tempat untuk meletakkannya, dan jalankan modul [venv](https://docs.python.org/3/library/venv.html#module-venv) sebagai skrip dengan jalur direktori :

Lihat file : **[12.2-1.py](https://github.com/SatriaDwiH195410229/workshop-python/blob/main/minggu-09/src/12.2-1.py)**
```python
python3 -m venv tutorial-env
```
Ini akan membuat `tutorial-env` direktori jika tidak ada, dan juga membuat direktori di dalamnya yang berisi salinan interpreter Python dan berbagai file pendukung.

Setelah membuat environments virtual, lalu mengaktifkannya.

Di Windows, jalankan :

Lihat file : **[12.2-2.py](https://github.com/SatriaDwiH195410229/workshop-python/blob/main/minggu-09/src/12.2-2.py)**
```python
tutorial-env\Scripts\activate.bat
```
Di Unix atau MacOS, jalankan :

Lihat file : **[12.2-3.py](https://github.com/SatriaDwiH195410229/workshop-python/blob/main/minggu-09/src/12.2-3.py)**
```python
source tutorial-env/bin/activate
```
(Skrip ini ditulis untuk bash shell. Jika menggunakan **csh** atau **fish shell**, ada alternatif `activate.csh` dan `activate.fish` skrip yang harus digunakan.)

Mengaktifkan environments virtual akan mengubah prompt shell untuk menunjukkan environments virtual apa yang  digunakan, dan memodifikasi environments sehingga menjalankan python akan memberitau versi instalasi Python. Sebagai contoh :

Lihat file : **[12.2-4.py](https://github.com/SatriaDwiH195410229/workshop-python/blob/main/minggu-09/src/12.2-4.py)**
```python
$ source ~/envs/tutorial-env/bin/activate
(tutorial-env) $ python
Python 3.5.1 (default, May  6 2016, 10:59:36)
  ...
>>> import sys
>>> sys.path
['', '/usr/local/lib/python35.zip', ...,
'~/envs/tutorial-env/lib/python3.5/site-packages']
>>>
```

# 12.3. Mengelola Paket dengan pip
Menginstal, memutakhirkan, dan menghapus paket menggunakan program bernama **pip**. Secara default pip akan menginstal paket dari Python Package Index, [https://pypi.org](https://pypi.org). Menelusuri Indeks Paket Python dengan membukanya di web browser.

`Pip` memiliki sejumlah sub-perintah: “install”, “uninstall”, “freeze”, dll. (Lihat panduan [Instalasi Modul Python](https://docs.python.org/3/installing/index.html#installing-index) untuk dokumentasi lengkap untuk **pip**.)

Menginstal versi terbaru dari sebuah paket dengan menentukan nama paket :

Lihat file : **[12.3-1.py](https://github.com/SatriaDwiH195410229/workshop-python/blob/main/minggu-09/src/12.3-1.py)**
```python
(tutorial-env) $ python -m pip install novas
Collecting novas
  Downloading novas-3.1.1.3.tar.gz (136kB)
Installing collected packages: novas
  Running setup.py install for novas
Successfully installed novas-3.1.1.3
```
Juga dapat menginstal versi paket tertentu dengan memberikan nama paket diikuti oleh `==` dan nomor versi :

Lihat file : **[12.3-2.py](https://github.com/SatriaDwiH195410229/workshop-python/blob/main/minggu-09/src/12.3-2.py)**
```python
(tutorial-env) $ python -m pip install requests==2.6.0
Collecting requests==2.6.0
  Using cached requests-2.6.0-py2.py3-none-any.whl
Installing collected packages: requests
Successfully installed requests-2.6.0
```
Atau dapat menjalankan untuk memutakhirkan paket ke versi terbaru:`pip install --upgrade`

Lihat file : **[12.3-3.py](https://github.com/SatriaDwiH195410229/workshop-python/blob/main/minggu-09/src/12.3-3.py)**
```python
(tutorial-env) $ python -m pip install --upgrade requests
Collecting requests
Installing collected packages: requests
  Found existing installation: requests 2.6.0
    Uninstalling requests-2.6.0:
      Successfully uninstalled requests-2.6.0
Successfully installed requests-2.7.0
```
`pip uninstall` diikuti oleh satu atau lebih nama paket akan menghapus paket dari environments virtual.

`pip show` akan menampilkan informasi tentang paket tertentu :

Lihat file : **[12.3-4.py](https://github.com/SatriaDwiH195410229/workshop-python/blob/main/minggu-09/src/12.3-4.py)**
```python
(tutorial-env) $ pip show requests
---
Metadata-Version: 2.0
Name: requests
Version: 2.7.0
Summary: Python HTTP for Humans.
Home-page: http://python-requests.org
Author: Kenneth Reitz
Author-email: me@kennethreitz.com
License: Apache 2.0
Location: /Users/akuchling/envs/tutorial-env/lib/python3.4/site-packages
Requires:
```
`pip list` akan menampilkan semua paket yang diinstal di environments virtual :

Lihat file : **[12.3-5.py](https://github.com/SatriaDwiH195410229/workshop-python/blob/main/minggu-09/src/12.3-5.py)**
```python
(tutorial-env) $ pip list
novas (3.1.1.3)
numpy (1.9.2)
pip (7.0.3)
requests (2.7.0)
setuptools (16.0)
```
`pip freeze` akan menghasilkan daftar paket yang diinstal serupa, tetapi output menggunakan format yang diharapkan. Konvensi umum adalah meletakkan daftar ini dalam file:`pip installrequirements.txt`

Lihat file : **[12.3-6.py](https://github.com/SatriaDwiH195410229/workshop-python/blob/main/minggu-09/src/12.3-6.py)**
```python
(tutorial-env) $ pip freeze > requirements.txt
(tutorial-env) $ cat requirements.txt
novas==3.1.1.3
numpy==1.9.2
requests==2.7.0
```
Kemudian `requirements.txt` dapat dikomit ke kontrol versi dan dikirimkan sebagai bagian dari aplikasi. Pengguna kemudian dapat menginstal semua paket yang diperlukan dengan :`install -r`

Lihat file : **[12.3-7.py](https://github.com/SatriaDwiH195410229/workshop-python/blob/main/minggu-09/src/12.3-7.py)**
```python
(tutorial-env) $ python -m pip install -r requirements.txt
Collecting novas==3.1.1.3 (from -r requirements.txt (line 1))
  ...
Collecting numpy==1.9.2 (from -r requirements.txt (line 2))
  ...
Collecting requests==2.7.0 (from -r requirements.txt (line 3))
  ...
Installing collected packages: novas, numpy, requests
  Running setup.py install for novas
Successfully installed novas-3.1.1.3 numpy-1.9.2 requests-2.7.0
```
`pip` memiliki lebih banyak pilihan. Lihat panduan [Instalasi Modul Python](https://docs.python.org/3/installing/index.html#installing-index) untuk dokumentasi lengkap untuk `pip`. Ketika sudah menulis sebuah paket dan ingin membuatnya tersedia di Python Package Index, lihat panduan [Mendistribusikan Modul Python](https://docs.python.org/3/distributing/index.html#distributing-index).

# Memulai dengan conda
Conda adalah pengelola paket dan pengelola environments andal yang digunakan dengan baris perintah di Anaconda Prompt untuk Windows, atau di jendela terminal untuk macOS atau Linux.

## Sebelum memulai
Diharuskan sudah menginstall [Anaconda](https://docs.anaconda.com/anaconda/install/).

## Daftar isi
* [Memulai conda](https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html#starting-conda) di Windows, macOS, atau Linux. 2 MENIT
* [Mengelola konda](https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html#managing-conda). Verifikasi bahwa Anaconda diinstal dan periksa apakah conda diperbarui ke versi saat ini. 3 MENIT
* [Mengelola environment](https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html#managing-envs). Ciptakan environments dan bergerak dengan mudah di antara mereka. 5 MENIT
* [Mengelola Python](https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html#managing-python). Buat environments yang memiliki versi Python yang berbeda. 5 MENIT
* [Mengelola paket](https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html#managing-pkgs). Temukan paket yang tersedia untuk diinstal. Instal paket. 5 MENIT
TOTAL WAKTU:20 MENIT

## Memulai conda
**Windows**
* Dari menu Start, cari dan buka "Anaconda Prompt."
![Startmenu](https://github.com/SatriaDwiH195410229/workshop-python/blob/main/minggu-09/src/gambar.png "Gambar startmenu")
Di Windows, semua perintah di bawah ini diketik ke jendela Anaconda Prompt.

**MacOS**
* Buka Launchpad, lalu klik ikon terminal.
Di macOS, semua perintah di bawah ini diketik ke jendela terminal.

**Linux**
* Buka jendela terminal.
Di Linux, semua perintah di bawah ini diketik ke jendela terminal.

## Mengelola conda
Verifikasi bahwa conda diinstal dan berjalan di sistem dengan mengetik :
```python
conda --version
```
CONTOH :
![Conda version](https://github.com/SatriaDwiH195410229/workshop-python/blob/main/minggu-09/src/condaversion.png)

Perbarui conda ke versi saat ini. Ketik berikut ini :
```python
conda update conda
```
Jika versi conda yang lebih baru tersedia, ketik `y` untuk memperbarui :
```python
Proceed ([y]/n)? y
```

## Mengelola environments
### 1. Buat environments baru dan instal paket di dalamnya.
```python
conda create --name snowflakes biopython
```
Conda memeriksa untuk melihat paket tambahan ("dependensi") apa yang dibutuhkan BioPython, dan menanyakan apakah ingin melanjutkan :
```python
Proceed ([y]/n)? y
```
Ketik "y" dan tekan Enter untuk melanjutkan.

### 2. Untuk menggunakan, atau "mengaktifkan" environments baru, ketik berikut ini :
* Windows:`conda activate snowflakes`
* macOS dan Linux:`conda activate snowflakes`

Untuk versi conda sebelum 4.6, ketik:
* Windows:`activate snowflakes`
* macOS dan Linux:`source activate snowflakes`

### 3. Untuk melihat daftar semua environments, ketik :
```python
conda info --envs
```
Daftar environments akan muncul seperti :
```python
conda environments:

    base           /home/username/Anaconda3
    snowflakes   * /home/username/Anaconda3/envs/snowflakes
```
### 4. Ubah environments saat ini kembali ke default (basis):`conda activate`
**Catatan!**
Untuk versi conda sebelum 4.6 gunakan :
* Windows:`activate`
macOS, Linux:`source activate`

## Mengelola python
### 1. Buat environments baru bernama "snakes" yang berisi Python 3.9 :
```python
conda create --name snakes python=3.9
```
Ketika conda bertanya apakah ingin melanjutkan, ketik "y" dan tekan Enter.

### 2. Aktifkan environments baru :
* Windows:`conda activate snakes`
* macOS dan Linux:`conda activate snakes`

Untuk versi conda sebelum 4.6, ketik:
* Windows:`activate snakes`
* macOS dan Linux:`source activate snakes`

### 3. Verifikasi bahwa environment snakes telah ditambahkan dan aktif :
```python
conda info --envs
```
Conda menampilkan daftar semua environment dengan tanda bintang _*_ setelah nama environments aktif :
```python
# conda environments:
#
base                     /home/username/anaconda3
snakes                *  /home/username/anaconda3/envs/snakes
snowflakes               /home/username/anaconda3/envs/snowflakes
```
Environments aktif juga ditampilkan di depan prompt di (tanda kurung) atau [kurung] seperti ini :
```python
(snakes) $
```

### 4. Verifikasi versi Python mana yang ada di lingkungan Anda saat ini :
```python
python --version
```

### 5. Nonaktifkan environment snakes dan kembali ke environments dasar:`conda activate`

## Mengelola paket
### 1. Untuk menemukan paket yang telah diinstal, aktifkan terlebih dahulu environment yang ingin dicari. Lihat di atas untuk perintah untuk mengaktifkan environment snakes.
### 2. Periksa untuk melihat apakah paket yang belum diinstal bernama "beautifulsoup4" tersedia dari repositori Anaconda (harus terhubung ke Internet) :
```python
conda search beautifulsoup4
```
### 3. Instal paket ini ke environment saat ini :
```python
conda install beautifulsoup4
```
### 4. Periksa untuk melihat apakah program yang baru diinstal ada di environment ini :
```pyton
conda list
```