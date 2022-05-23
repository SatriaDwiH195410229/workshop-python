5. Bab ini menjelaskan beberapa hal yang telah Anda pelajari secara lebih rinci, dan menambahkan beberapa hal baru juga.

5.1 More on list :
Daftar tipe data daftar memiliki beberapa metode lagi. Berikut adalah daftar semua metode objek.

list. append ( x )
Tambahkan item ke akhir daftar. Setara dengan .a[len(a):] = [x]

list. extend (iterable)
Perluas daftar dengan menambahkan semua item dari iterable. Setara dengan .a[len(a):] = iterable

list. insert (i, x )
Masukkan item pada posisi tertentu. Argumen pertama adalah indeks elemen yang akan disisipkan sebelumnya,
jadi disisipkan di bagian depan daftar, dan sama dengan .a.insert(0, x)a.insert(len(a), x)a.append(x)

list. remove ( x )
Hapus item pertama dari daftar yang nilainya sama dengan x . Ini menimbulkan ValueErrorjika tidak ada item seperti itu.

list. pop ( [ i ] )
Hapus item pada posisi yang diberikan dalam daftar, dan kembalikan.
Jika tidak ada indeks yang ditentukan, a.pop()hapus dan kembalikan item terakhir dalam daftar.
(Kurung siku di sekitar i dalam tanda tangan metode menunjukkan bahwa parameternya opsional,
bukan berarti Anda harus mengetikkan tanda kurung siku pada posisi itu. Anda akan sering melihat notasi ini di Referensi Pustaka Python.)

list. clear ( )
Hapus semua item dari daftar. Setara dengan .del a[:]

list. index ( x [ , start [ , end ] ] )
Kembalikan indeks berbasis nol dalam daftar item pertama yang nilainya sama dengan x . Menaikkan a ValueErrorjika tidak ada item seperti itu.

Argumen opsional mulai dan akhir ditafsirkan seperti dalam notasi irisan dan digunakan untuk membatasi pencarian ke urutan daftar tertentu.
Indeks yang dikembalikan dihitung relatif terhadap awal urutan penuh daripada argumen awal .

list. count ( x )
Kembalikan berapa kali x muncul dalam daftar.

list. sort (*, key=None, reverse=False)]
Urutkan item dari daftar di tempat (argumen dapat digunakan untuk penyesuaian pengurutan, lihat sorted()penjelasannya).

list. reverse ( )
Balikkan elemen daftar di tempatnya.

list. copy ( )
Kembalikan salinan daftar yang dangkal. Setara dengan a[:].

5.1.1 Using Lists as Stacks
Metode daftar membuatnya sangat mudah untuk menggunakan daftar sebagai tumpukan, di mana elemen terakhir
yang ditambahkan adalah elemen pertama yang diambil (“last-in, first-out”). Untuk menambahkan item ke bagian atas tumpukan, gunakan append().

5.1.2 Using List as Queues
Dimungkinkan juga untuk menggunakan daftar sebagai antrian, di mana elemen pertama yang ditambahkan adalah elemen pertama yang diambil ("first-in, first-out");
namun, daftar tidak efisien untuk tujuan ini. Sementara menambahkan dan muncul dari akhir daftar cepat,
melakukan sisipan atau muncul dari awal daftar lambat (karena semua elemen lain harus digeser satu).

5.1.3 List Comprehensions
Pemahaman daftar menyediakan cara ringkas untuk membuat daftar.
Aplikasi umum adalah untuk membuat daftar baru di mana setiap elemen adalah hasil dari beberapa operasi yang diterapkan ke setiap anggota dari urutan lain atau iterable,
atau untuk membuat suburutan dari elemen-elemen yang memenuhi kondisi tertentu.

5.1.4 Nested List Comprehensions
Ekspresi awal dalam pemahaman daftar dapat berupa ekspresi arbitrer, termasuk pemahaman daftar lainnya.

5.2. The del statement
Ada cara untuk menghapus item dari daftar yang diberikan indeksnya alih-alih nilainya: delpernyataan.
Ini berbeda dari pop()metode yang mengembalikan nilai.
Pernyataan deljuga dapat digunakan untuk menghapus irisan dari daftar atau menghapus seluruh daftar (yang kita lakukan sebelumnya dengan menetapkan daftar kosong ke irisan)

5.3. Tuples and Sequences
Mereka adalah dua contoh tipe data urutan (lihat Jenis Urutan — daftar, tupel, rentang ).
Karena Python adalah bahasa yang berkembang, tipe data urutan lainnya dapat ditambahkan. Ada juga tipe data urutan standar lainnya: tuple .

5.4. Sets
Python juga menyertakan tipe data untuk set . Himpunan adalah kumpulan yang tidak berurutan tanpa elemen duplikat.
Penggunaan dasar termasuk pengujian keanggotaan dan menghilangkan entri duplikat.
Set objek juga mendukung operasi matematika seperti serikat pekerja, persimpangan, perbedaan, dan perbedaan simetris.

5.5. Dictionaries
Tipe data lain yang berguna yang dibangun ke dalam Python adalah kamus (lihat Jenis Pemetaan — dict ).
Kamus kadang-kadang ditemukan dalam bahasa lain sebagai "ingatan asosiatif" atau "array asosiatif".
Tidak seperti urutan, yang diindeks oleh rentang angka, kamus diindeks oleh kunci , yang dapat berupa tipe apa pun yang tidak dapat diubah; string dan angka selalu bisa menjadi kunci.
Tuple dapat digunakan sebagai kunci jika hanya berisi string, angka, atau tupel; jika sebuah tuple berisi objek yang bisa berubah baik secara langsung maupun tidak langsung,
itu tidak dapat digunakan sebagai kunci. Anda tidak dapat menggunakan daftar sebagai kunci,
karena daftar dapat dimodifikasi di tempat menggunakan penetapan indeks, penetapan irisan, atau metode seperti append()dan extend().

5.6. Looping Techniques
Saat mengulang melalui kamus, kunci dan nilai yang sesuai dapat diambil pada saat yang sama menggunakan items()metode ini.

5.7. More on Conditions
Kondisi yang digunakan dalam whiledan ifpernyataan dapat berisi operator apa pun, bukan hanya perbandingan.

5.8. Comparing Sequences and Other Types
Objek urutan biasanya dapat dibandingkan dengan objek lain dengan jenis urutan yang sama. Perbandingannya menggunakan leksikografispemesanan:
pertama dua item pertama dibandingkan, dan jika berbeda, ini menentukan hasil perbandingan; jika mereka sama, dua item berikutnya dibandingkan, dan seterusnya,
sampai salah satu urutan habis.