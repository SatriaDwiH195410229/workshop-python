# Minggu ke-7 : Kelas - Mempelajari Tutorial Bab 9
Kelas menyediakan sarana untuk menggabungkan data dan fungsionalitas bersama-sama. Membuat kelas baru membuat tipe objek baru, memungkinkan instance baru dari tipe itu dibuat. Setiap instance kelas dapat memiliki atribut yang dilampirkan untuk mempertahankan statusnya. Instance kelas juga dapat memiliki metode (didefinisikan oleh kelasnya) untuk memodifikasi statusnya.

# 9.1. Sepatah kata tentang nama dan objek
Objek memiliki individualitas, dan beberapa nama (dalam beberapa cakupan) dapat diikat ke objek yang sama. Ini dikenal sebagai aliasing dalam bahasa lain.Dapat diabaikan dengan aman ketika berhadapan dengan tipe dasar yang tidak dapat diubah (angka, string, tupel). Namun, aliasing memiliki efek yang mungkin mengejutkan pada semantik kode Python yang melibatkan objek yang bisa berubah seperti daftar, kamus, dan sebagian besar jenis lainnya. Ini biasanya digunakan untuk kepentingan program, karena alias berperilaku seperti pointer dalam beberapa hal. Misalnya, melewatkan sebuah objek adalah murah karena hanya sebuah pointer yang dilewatkan oleh implementasi; dan jika suatu fungsi memodifikasi objek yang diteruskan sebagai argumen, pemanggil akan melihat perubahannya — ini menghilangkan kebutuhan akan dua mekanisme penerusan argumen yang berbeda seperti dalam Pascal.

# 9.2. Lingkup python dan ruang nama
Sebelum memperkenalkan kelas, pertama-tama kita harus tahu tentang aturan ruang lingkup Python. Definisi kelas memainkan beberapa trik rapi dengan ruang nama, dan kita perlu mengetahui cara kerja ruang lingkup dan ruang nama untuk memahami sepenuhnya apa yang terjadi.

Mari kita mulai dengan beberapa definisi.

Namespace adalah pemetaan dari nama ke objek. Sebagian besar ruang nama saat ini diimplementasikan sebagai kamus Python, tetapi itu biasanya tidak terlihat dengan cara apa pun (kecuali untuk kinerja), dan mungkin berubah di masa mendatang. Contoh ruang nama adalah: kumpulan nama bawaan (berisi fungsi seperti *abs()*, dan nama pengecualian bawaan); nama global dalam modul; dan nama lokal dalam pemanggilan fungsi. Dalam arti set atribut dari suatu objek juga membentuk namespace. Hal penting yang perlu diketahui tentang namespace adalah bahwa sama sekali tidak ada hubungan antara nama di namespace yang berbeda; misalnya, dua modul berbeda dapat mendefinisikan suatu fungsi maximizetanpa kebingungan — pengguna modul harus mengawalinya dengan nama modul.

*Lingkup* adalah wilayah tekstual dari program Python di mana namespace dapat diakses secara langsung. “Dapat diakses secara langsung” di sini berarti bahwa referensi yang tidak memenuhi syarat untuk sebuah nama mencoba menemukan nama tersebut di namespace.

Meskipun cakupan ditentukan secara statis, mereka digunakan secara dinamis. Setiap saat selama eksekusi, ada 3 atau 4 cakupan bersarang yang ruang namanya dapat diakses secara langsung:
* lingkup terdalam, yang dicari terlebih dahulu, berisi nama-nama lokal
* cakupan dari setiap fungsi terlampir, yang dicari mulai dengan lingkup terlampir terdekat, berisi nama non-lokal, tetapi juga non-global
* lingkup berikutnya-ke-terakhir berisi nama global modul saat ini
* lingkup terluar (dicari terakhir) adalah namespace yang berisi nama bawaan

### 9.2.1. Contoh ruang lingkup dan ruang nama
Ini adalah contoh yang menunjukkan cara mereferensikan cakupan dan ruang nama yang berbeda, serta bagaimana *global* dan *nonlocal* memengaruhi pengikatan variabel :

Lihat file : **[9.2.1.py](https://github.com/SatriaDwiH195410229/workshop-python/blob/main/minggu-07/src/9.2.1.py)**
```python
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)
```
Output dari kode contoh diatas adalah :
```python
After local assignment: test spam
After nonlocal assignment: nonlocal spam
After global assignment: nonlocal spam
In global scope: global spam
```
Perhatikan bagaimana penetapan *lokal* (yang merupakan default) tidak mengubah pengikatan spam scope_test . Penugasan mengubah *pengikatan scope_test dari spam*, dan penugasan mengubah pengikatan tingkat modul.*nonlocalglobal*

## 9.3. Pandangan pertama di kelas
Kelas memperkenalkan sedikit sintaks baru, tiga tipe objek baru, dan beberapa semantik baru.

### 9.3.1. Kelas definisi sintaks
Bentuk paling sederhana dari definisi kelas terlihat seperti ini :

Lihat file : **[9.3.1.py](https://github.com/SatriaDwiH195410229/workshop-python/blob/main/minggu-07/src/9.3.1.py)**
```python
class ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>
```
Definisi kelas, seperti definisi fungsi ( *def* pernyataan) harus dieksekusi sebelum memiliki efek apa pun. (kita bisa menempatkan definisi kelas di cabang *if* pernyataan, atau di dalam fungsi.)

### 9.3.2. Objek kelas
Objek kelas mendukung dua jenis operasi: referensi atribut dan instantiasi.

Referensi atribut menggunakan sintaks standar yang digunakan untuk semua referensi atribut di Python: `obj.name.` Nama atribut yang valid adalah semua nama yang ada di ruang nama kelas saat objek kelas dibuat. Jadi, jika definisi kelas terlihat seperti ini :

Lihat file : **[9.3.2-1.py](https://github.com/SatriaDwiH195410229/workshop-python/blob/main/minggu-07/src/9.3.2-1.py)**
```python
class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'
```
kemudian `MyClass.i` dan `MyClass.f` adalah referensi atribut yang valid, masing-masing mengembalikan bilangan bulat dan objek fungsi. Atribut kelas juga dapat ditetapkan, sehingga kita dapat mengubah nilai `MyClass.i` berdasarkan tugas. __doc__ juga merupakan atribut yang valid, mengembalikan docstring milik kelas: .`"A simple example class"`
*Instansiasi* kelas menggunakan notasi fungsi. Anggap saja objek kelas adalah fungsi tanpa parameter yang mengembalikan instance baru dari kelas. Misalnya (dengan asumsi kelas di atas) :

Lihat file : **[9.3.2-2.py](https://github.com/SatriaDwiH195410229/workshop-python/blob/main/minggu-07/src/9.3.2-2.py)**
```python
x = MyClass()
```
Operasi instantiasi ("memanggil" objek kelas) membuat objek kosong. Banyak kelas suka membuat objek dengan instance yang disesuaikan dengan keadaan awal tertentu. Oleh karena itu, sebuah kelas dapat mendefinisikan metode khusus bernama __init__(), seperti ini :

Lihat file : **[9.3.2-3.py](https://github.com/SatriaDwiH195410229/workshop-python/blob/main/minggu-07/src/9.3.2-3.py)**
```python
def __init__(self):
    self.data = []
```
Ketika sebuah kelas mendefinisikan sebuah __init__()metode, instantiasi kelas secara otomatis memanggil __init__()instance kelas yang baru dibuat. Jadi dalam contoh ini, instance baru yang diinisialisasi dapat diperoleh dengan:

Lihat file : **[9.3.2-4.py](https://github.com/SatriaDwiH195410229/workshop-python/blob/main/minggu-07/src/9.3.2-4.py)**
```python
x = MyClass()
```
Tentu saja, __init__()metode ini mungkin memiliki argumen untuk fleksibilitas yang lebih besar. Dalam hal ini, argumen yang diberikan kepada operator instantiasi kelas diteruskan ke __init__(). Sebagai contoh :

Lihat file : **[9.3.2-5.py](https://github.com/SatriaDwiH195410229/workshop-python/blob/main/minggu-07/src/9.3.2-5.py)**
```python
>>> class Complex:
...     def __init__(self, realpart, imagpart):
...         self.r = realpart
...         self.i = imagpart
...
>>> x = Complex(3.0, -4.5)
>>> x.r, x.i
(3.0, -4.5)
```

### 9.3.3. Objek instance
*Atribut* data sesuai dengan "variabel instan" di Smalltalk, dan "anggota data" di C++. Atribut data tidak perlu dideklarasikan; seperti variabel lokal, mereka muncul saat pertama kali ditugaskan. Misalnya, jika xadalah instance yang MyClass dibuat di atas, potongan kode berikut akan mencetak nilai `16`, tanpa meninggalkan jejak :

Lihat file : **[9.3.3.py](https://github.com/SatriaDwiH195410229/workshop-python/blob/main/minggu-07/src/9.3.3.py)**
```python
x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter
```

### 9.3.4. Objek method
Biasanya, suatu metode dipanggil tepat setelah terikat :

Lihat file : **[9.3.4-1.py](https://github.com/SatriaDwiH195410229/workshop-python/blob/main/minggu-07/src/9.3.4-1.py)**
```python
x.f()
```
Dalam MyClass contoh, ini akan mengembalikan string. Namun, tidak perlu memanggil metode segera: adalah objek metode, dan dapat disimpan dan dipanggil di lain waktu. Sebagai contoh:`'hello world'x.f`

Lihat file : **[9.3.4-2.py](https://github.com/SatriaDwiH195410229/workshop-python/blob/main/minggu-07/src/9.3.4-2.py)**
```python
xf = x.f
while True:
    print(xf())
```
akan terus mencetak hingga akhir waktu `hello world`

### 9.3.5. Variabel kelas dan instance
Secara umum, variabel instan adalah untuk data yang unik untuk setiap instance dan variabel kelas untuk atribut dan metode yang dibagikan oleh semua instance kelas :

Lihat file : **[9.3.5-1.py](https://github.com/SatriaDwiH195410229/workshop-python/blob/main/minggu-07/src/9.3.5-1.py)**
```python
class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.kind                  # shared by all dogs
'canine'
>>> e.kind                  # shared by all dogs
'canine'
>>> d.name                  # unique to d
'Fido'
>>> e.name                  # unique to e
'Buddy'
```
Seperti yang dibahas dalam *A Word About Names and Objects*, data bersama dapat memiliki efek yang mungkin mengejutkan dengan melibatkan objek yang bisa berubah seperti daftar dan kamus. Misalnya, daftar *trik* dalam kode berikut tidak boleh digunakan sebagai variabel kelas karena hanya satu daftar yang akan dibagikan oleh semua instance *Anjing* :

Lihat file : **[9.3.5-2.py](https://github.com/SatriaDwiH195410229/workshop-python/blob/main/minggu-07/src/9.3.5-2.py)**
```python
class Dog:

    tricks = []             # mistaken use of a class variable

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.add_trick('roll over')
>>> e.add_trick('play dead')
>>> d.tricks                # unexpectedly shared by all dogs
['roll over', 'play dead']
```
Desain kelas yang benar harus menggunakan variabel instan sebagai gantinya :

Lihat file : **[9.3.5-3.py](https://github.com/SatriaDwiH195410229/workshop-python/blob/main/minggu-07/src/9.3.5-3.py)**
```python
class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.add_trick('roll over')
>>> e.add_trick('play dead')
>>> d.tricks
['roll over']
>>> e.tricks
['play dead']
```

## 9.4. Komentar acak
Jika nama atribut yang sama terjadi di kedua instance dan di kelas, maka pencarian atribut memprioritaskan instance:

Lihat file : **[9.4-1.py](https://github.com/SatriaDwiH195410229/workshop-python/blob/main/minggu-07/src/9.4-1.py)**
```python
>>> class Warehouse:
        purpose = 'storage'
        region = 'west'

>>> w1 = Warehouse()
>>> print(w1.purpose, w1.region)
storage west
>>> w2 = Warehouse()
>>> w2.region = 'east'
>>> print(w2.purpose, w2.region)
storage east
```
Objek fungsi apa pun yang merupakan atribut kelas mendefinisikan metode untuk instance kelas itu. Definisi fungsi tidak perlu secara tekstual dilampirkan dalam definisi kelas: menetapkan objek fungsi ke variabel lokal di kelas juga tidak masalah. Sebagai contoh :

Lihat file : **[9.4-2.py](https://github.com/SatriaDwiH195410229/workshop-python/blob/main/minggu-07/src/9.4-2.py)**
```python
# Function defined outside the class
def f1(self, x, y):
    return min(x, x+y)

class C:
    f = f1

    def g(self):
        return 'hello world'

    h = g
```
Sekarang `f`, `g` dan `h` adalah semua atribut kelas C yang merujuk ke objek fungsi, dan akibatnya mereka semua adalah metode turunan dari C—`h` yang sama persis dengan `g`. Perhatikan bahwa praktik ini biasanya hanya berfungsi untuk membingungkan pembaca suatu program.

Metode dapat memanggil metode lain dengan menggunakan atribut metode dari `self`argumen :

Lihat file : **[9.4-3.py](https://github.com/SatriaDwiH195410229/workshop-python/blob/main/minggu-07/src/9.4-3.py)**
```python
class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)
```

## 9.5. Pewarisan _
Tentu saja, fitur bahasa tidak akan layak disebut "kelas" tanpa mendukung pewarisan. Sintaks untuk definisi kelas turunan terlihat seperti ini :

Lihat file : **[9.5-1.py](https://github.com/SatriaDwiH195410229/workshop-python/blob/main/minggu-07/src/9.5-1.py)**
```python
class DerivedClassName(BaseClassName):
    <statement-1>
    .
    .
    .
    <statement-N>
```
Nama BaseClassName harus didefinisikan dalam lingkup yang berisi definisi kelas turunan. Di tempat nama kelas dasar, ekspresi arbitrer lainnya juga diperbolehkan. Ini bisa berguna, misalnya, ketika kelas dasar didefinisikan di modul lain :

Lihat file : **[9.5-2.py](https://github.com/SatriaDwiH195410229/workshop-python/blob/main/minggu-07/src/9.5-2.py)**
```python
class DerivedClassName(modname.BaseClassName):
```
Python memiliki dua fungsi bawaan yang bekerja dengan pewarisan:
* Gunakan *isinstance()* untuk memeriksa jenis instance: hanya jika adalah atau beberapa kelas yang berasal dari .`isinstance(obj, int)Trueobj.__class__` *int int*
* Gunakan *issubclass()* untuk memeriksa pewarisan kelas: adalah karena merupakan subkelas dari . Namun, is Since bukanlah subkelas dari .`issubclass(bool, int)True` *bool int* `issubclass(float, int)False` *float int*

### 9.5.1. Banyak warisan
Python juga mendukung bentuk pewarisan berganda. Definisi kelas dengan beberapa kelas dasar terlihat seperti ini :

Lihat file : **[9.5.1.py](https://github.com/SatriaDwiH195410229/workshop-python/blob/main/minggu-07/src/9.5.1.py)**
```python
class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    .
    .
    .
    <statement-N>
```

## 9.6. Variabel pribadi
Variabel instan "Pribadi" yang tidak dapat diakses kecuali dari dalam objek tidak ada di Python. Namun, ada konvensi yang diikuti oleh sebagian besar kode Python: nama yang diawali dengan garis bawah (misalnya `_spam`) harus diperlakukan sebagai bagian non-publik dari API (apakah itu fungsi, metode, atau anggota data). Ini harus dianggap sebagai detail implementasi dan dapat berubah tanpa pemberitahuan.
Name mangling berguna untuk membiarkan subclass menimpa metode tanpa memutus panggilan metode intraclass. Sebagai contoh :

Lihat file : **[9.6.py](https://github.com/SatriaDwiH195410229/workshop-python/blob/main/minggu-07/src/9.6.py)**
```python
class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)
```
Contoh di atas akan berfungsi bahkan jika `MappingSubclass` kita memperkenalkan `__update` pengidentifikasi karena masing-masing diganti dengan `_Mapping__update` di `Mapping` kelas dan `_MappingSubclass__update` di `MappingSubclass` kelas.

## 9.7. ODDS dan Ends
Terkadang berguna untuk memiliki tipe data yang mirip dengan "record" Pascal atau "struct" C, menggabungkan beberapa item data bernama. Definisi kelas kosong akan berfungsi dengan baik :

Lihat file : **[9.7.py](https://github.com/SatriaDwiH195410229/workshop-python/blob/main/minggu-07/src/9.7.py)**
```python
class Employee:
    pass

john = Employee()  # Create an empty employee record

# Fill the fields of the record
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000
```

## 9.8. Iterator _
Sekarang kita mungkin telah memperhatikan bahwa sebagian besar objek kontainer dapat diulang menggunakan statement for :

Lihat file : **[9.8-1.py](https://github.com/SatriaDwiH195410229/workshop-python/blob/main/minggu-07/src/9.8-1.py)**
```python
for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {'one':1, 'two':2}:
    print(key)
for char in "123":
    print(char)
for line in open("myfile.txt"):
    print(line, end='')
```
Gaya akses ini jelas, ringkas, dan nyaman. Penggunaan iterator meliputi dan menyatukan Python. Di balik layar, *for* pernyataan tersebut memanggil *iter()* objek container. Fungsi mengembalikan objek iterator yang mendefinisikan metode `__next__()` yang mengakses elemen dalam wadah satu per satu. Ketika tidak ada lagi elemen, `__next__()` memunculkan *StopIteration* pengecualian yang memberitahu forloop untuk berhenti. kita dapat memanggil `__next__()` metode menggunakan `next()` fungsi bawaan; contoh ini menunjukkan cara kerjanya :

Lihat file : **[9.8-2.py](https://github.com/SatriaDwiH195410229/workshop-python/blob/main/minggu-07/src/9.8-2.py)**
```python
>>> s = 'abc'
>>> it = iter(s)
>>> it
<str_iterator object at 0x10c90e650>
>>> next(it)
'a'
>>> next(it)
'b'
>>> next(it)
'c'
>>> next(it)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    next(it)
StopIteration
```
Setelah melihat mekanisme di balik protokol iterator, mudah untuk menambahkan perilaku iterator ke kelas Anda. Tentukan `__iter__()`metode yang mengembalikan objek dengan `__next__()` metode. Jika kelas mendefinisikan `__next__()`, maka `__iter__()` bisa saja mengembalikan `self` :

Lihat file : **[9.8-3.py](https://github.com/SatriaDwiH195410229/workshop-python/blob/main/minggu-07/src/9.8-3.py)**
```python
class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
```

Lihat file : **[9.8-4.py](https://github.com/SatriaDwiH195410229/workshop-python/blob/main/minggu-07/src/9.8-4.py)**
```python
>>> rev = Reverse('spam')
>>> iter(rev)
<__main__.Reverse object at 0x00A1DB50>
>>> for char in rev:
...     print(char)
...
m
a
p
s
```

## 9.9. Generator _
*Generator* adalah alat yang sederhana dan kuat untuk membuat iterator. Mereka ditulis seperti fungsi biasa tetapi menggunakan *yield* pernyataan setiap kali mereka ingin mengembalikan data. Setiap kali `next()` dipanggil, generator melanjutkan dari tempat terakhirnya (ia mengingat semua nilai data dan pernyataan mana yang terakhir dieksekusi). Sebuah contoh menunjukkan bahwa generator dapat dengan mudah dibuat :

Lihat file : **[9.9-1.py](https://github.com/SatriaDwiH195410229/workshop-python/blob/main/minggu-07/src/9.9-1.py)**
```python
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]
```

Lihat file : **[9.9-2.py](https://github.com/SatriaDwiH195410229/workshop-python/blob/main/minggu-07/src/9.9-2.py)**
```python
>>> for char in reverse('golf'):
...     print(char)
...
f
l
o
g
```

## 9.10. Ekspresi generator
Beberapa generator sederhana dapat dikodekan secara ringkas sebagai ekspresi menggunakan sintaks yang mirip dengan pemahaman daftar tetapi dengan tanda kurung alih-alih tanda kurung siku. Ekspresi ini dirancang untuk situasi di mana generator digunakan langsung oleh fungsi terlampir. Ekspresi generator lebih ringkas tetapi kurang fleksibel daripada definisi generator lengkap dan cenderung lebih ramah memori daripada pemahaman daftar yang setara.

Contoh :

Lihat file : **[9.10.py](https://github.com/SatriaDwiH195410229/workshop-python/blob/main/minggu-07/src/9.10.py)**
```python
>>> sum(i*i for i in range(10))                 # sum of squares
285

>>> xvec = [10, 20, 30]
>>> yvec = [7, 5, 3]
>>> sum(x*y for x,y in zip(xvec, yvec))         # dot product
260

>>> unique_words = set(word for line in page  for word in line.split())

>>> valedictorian = max((student.gpa, student.name) for student in graduates)

>>> data = 'golf'
>>> list(data[i] for i in range(len(data)-1, -1, -1))
['f', 'l', 'o', 'g']
```