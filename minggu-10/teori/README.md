# Minggu ke-10 : Akses Ke Basis Data dan Mengerjakan Akses Ke Basis Data [CockroachDB Menggunakan psycopg2](https://www.cockroachlabs.com/docs/stable/build-a-python-app-with-cockroachdb.html) Dan Menggunakan [SQLAlchemy](https://www.cockroachlabs.com/docs/stable/build-a-python-app-with-cockroachdb-sqlalchemy.html)

Membuka dan mempelajari [PEP-249](https://www.python.org/dev/peps/pep-0249/), [dokumentasi psycopg](https://www.psycopg.org/), [PyMongo](https://github.com/mongodb/mongo-python-driver), [SQLAlchemy](https://www.sqlalchemy.org/). Kemudian mengerjakan langkah-langkah dibawah ini. 

# Bangun Aplikasi Python dengan CockroachDB dan psycopg2
Tutorial ini menunjukkan bagaimana membangun aplikasi Python sederhana dengan CockroachDB dan driver psycopg2 .

# Menggunakan CockroachDB tanpa server(beta)
## Langkah 1. Mulai CockroachDB

**Buat Cluster Gratis**
1. [Daftar akun CockroachDB Cloud](https://translate.google.com/website?sl=en&tl=id&hl=id&client=webapp&u=https://cockroachlabs.cloud/signup?referralId%3Ddocs_python_psycopg2)
2. [Masuk](https://translate.google.com/website?sl=en&tl=id&hl=id&client=webapp&u=https://cockroachlabs.cloud/) ke akun Cloud CockroachDB.
3. Pada halaman Cluster, klik Buat Cluster.
4. Pada halaman Buat kluster, pilih Tanpa Server.
5. Klik Buat kluster.

**Untuk Pengguna SQL**
1. Masukkan nama pengguna di bidang pengguna SQL atau gunakan yang disediakan secara default.
2. Klik Buat & simpan kata sandi.
3. Salin kata sandi yang dihasilkan dan simpan di lokasi yang aman.
4. Klik Berikutnya.

**Dapat Sertifikat Root**
1. Pilih String koneksi umum dari dropdown Pilih opsi.
2. Buka terminal baru di komputer lokal, dan jalankan perintah unduhan CA Cert yang disediakan di bagian Unduh CA Cert . Driver klien yang digunakan dalam tutorial ini memerlukan sertifikat ini untuk terhubung ke CockroachDB Cloud.

**Dapatkan Koneksi String**
Buka bagian General connection string, lalu salin connection string yang disediakan dan simpan di lokasi yang aman.

## Langkah 2. Dapatkan kode sampel
Kloning repo GitHub kode sampel :
```python
git clone https://github.com/cockroachlabs/hello-world-python-psycopg2
```
Kode sampel di *example.py* melakukan hal berikut :
* Membuat *accounts* tabel dan menyisipkan beberapa baris.
* Mentransfer dana antara dua akun dalam suatu [transaksi](https://www-cockroachlabs-com.translate.goog/docs/v21.2/transactions?_x_tr_sl=en&_x_tr_tl=id&_x_tr_hl=id&_x_tr_pto=wapp).
* Hapus akun dari tabel sebelum keluar sehingga dapat menjalankan kembali kode contoh.

## Langkah 3. Instal driver psycopg2
*psycopg2-binary* adalah satu-satunya dependensi modul pihak ketiga aplikasi sampel.
Untuk menginstal *psycopg2-binary*, jalankan perintah berikut :
```python
pip install psycopg2-binary
```
Untuk cara lain menginstal psycopg2, lihat [dokumentasi resmi](https://translate.google.com/website?sl=en&tl=id&hl=id&client=webapp&u=http://initd.org/psycopg/docs/install.html).

## Langkah 4. Jalankan kode
1. Setel *DATABASE_URL* variabel lingkungan ke string koneksi ke cluster CockroachDB Cloud :
```python
export DATABASE_URL="{connection-string}"
```
Di mana {connection-string}string koneksi yang diperoleh dari CockroachDB Cloud Console.
Aplikasi menggunakan string koneksi yang disimpan ke *DATABASE_URL* variabel lingkungan untuk terhubung ke cluster dan mengeksekusi kode.

2. Jalankan kode :
```python
cd hello-world-python-psycopg2
```
```python
python example.py
```
Output harus menunjukkan saldo akun sebelum dan sesudah transfer dana :
```python
Balances at Fri Oct 30 18:27:00 2020:
(1, 1000)
(2, 250)
Balances at Fri Oct 30 18:27:00 2020:
(1, 900)
(2, 350)
```

# Menggunakan cluster lokal
## Langkah 1. Mulai CockroachDB
1. [unduh biner CockroachDB.](https://www-cockroachlabs-com.translate.goog/docs/v21.2/install-cockroachdb?_x_tr_sl=en&_x_tr_tl=id&_x_tr_hl=id&_x_tr_pto=wapp)
2. Jalankan perintah [cockroach start-single-node](https://www-cockroachlabs-com.translate.goog/docs/v21.2/cockroach-start-single-node?_x_tr_sl=en&_x_tr_tl=id&_x_tr_hl=id&_x_tr_pto=wapp) :
```python
cockroach start-single-node --advertise-addr 'localhost' --insecure
```
Ini memulai cluster node tunggal yang tidak aman.

3. Perhatikan informasi koneksi berikut dalam teks sambutan shell SQL :
```python
CockroachDB node starting at 2021-08-30 17:25:30.06524 +0000 UTC (took 4.3s)
build:               CCL v21.1.6 @ 2021/07/20 15:33:43 (go1.15.11)
webui:               http://localhost:8080
sql:                 postgresql://root@localhost:26257?sslmode=disable
```
Akan menggunakan *sql* string koneksi untuk terhubung ke cluster nanti dalam tutorial ini.

## Langkah 2. Dapatkan kode sampel
Kloning repo GitHub kode sampel :
```python
Kloning repo GitHub kode sampel:
```
Kode sampel di *example.py* melakukan hal berikut :
* Membuat *accounts* tabel dan menyisipkan beberapa baris
* Mentransfer dana antara dua akun dalam suatu [transaksi](https://www-cockroachlabs-com.translate.goog/docs/v21.2/transactions?_x_tr_sl=en&_x_tr_tl=id&_x_tr_hl=id&_x_tr_pto=wapp)
* Hapus akun dari tabel sebelum keluar sehingga dapat menjalankan kembali kode contoh.

## Langkah 3. Instal driver psycopg2
Untuk menginstal psycopg2-binary, jalankan perintah berikut :
```python
pip install psycopg2-binary
```
Untuk cara lain menginstal psycopg2, lihat dokumentasi resmi.

## Langkah 4. Jalankan kode
1. Setel *DATABASE_URL* variabel lingkungan ke string koneksi ke cluster CockroachDB Cloud :
```python
export DATABASE_URL="postgresql://root@localhost:26257?sslmode=disable"
```
2. Jalankan kode :
```python
cd hello-world-python-psycopg2
```
```python
python example.py
```
Output harus menunjukkan saldo akun sebelum dan sesudah transfer dana :
```python
Balances at Fri Oct 30 18:27:00 2020:
(1, 1000)
(2, 250)
Balances at Fri Oct 30 18:27:00 2020:
(1, 900)
(2, 350)
```

# Bangun Aplikasi Python CRUD Sederhana dengan CockroachDB dan SQLAlchemy
Tutorial ini menunjukkan bagaimana membangun aplikasi Python CRUD sederhana dengan CockroachDB dan SQLAlchemy ORM.

# Menggunakan CockroachDB tanpa server(beta)
## Langkah 1. Mulai CockroachDB
**Buat cluster gratis**
1. [Daftar akun CockroachDB Cloud.](https://translate.google.com/website?sl=en&tl=id&hl=id&client=webapp&u=https://cockroachlabs.cloud/signup?referralId%3Ddocs_python_sqlalchemy)
2. [Masuk](https://translate.google.com/website?sl=en&tl=id&hl=id&client=webapp&u=https://cockroachlabs.cloud/) ke akun Cloud CockroachDB.
3. Pada halaman Cluster, klik Buat Cluster.
4. Pada halaman Buat kluster, pilih Tanpa Server.
5. Klik Buat kluster .
Cluster akan dibuat dalam beberapa detik dan dialog Buat pengguna SQL akan ditampilkan.

**Buat pengguna SQL**
Dialog Buat pengguna SQL memungkinkan membuat pengguna dan kata sandi SQL baru.
1. Masukkan nama pengguna di bidang pengguna SQL atau gunakan yang disediakan secara default.
2. Klik Buat & simpan kata sandi.
3. Salin kata sandi yang dihasilkan dan simpan di lokasi yang aman.
4. Klik Berikutnya.

**Dapatkan sertifikat root**
1. Pilih String koneksi umum dari dropdown Pilih opsi .
2. Buka terminal baru di komputer lokal, dan jalankan perintah unduhan CA Cert yang disediakan di bagian Unduh CA Cert . Driver klien yang digunakan dalam tutorial ini memerlukan sertifikat ini untuk terhubung ke CockroachDB Cloud.
3. 
**Dapatkan string koneksi**
Buka bagian General connection string, lalu salin connection string yang disediakan dan simpan di lokasi yang aman.

## Langkah 2. Dapatkan kodenya
Kloning kode repo GitHub :
```python
git clone https://github.com/cockroachlabs/example-app-python-sqlalchemy/
```
Proyek ini memiliki struktur direktori berikut :
```python
├── README.md
├── dbinit.sql
├── main.py
├── models.py
└── requirements.txt
```
File *requirements.txt* tersebut menyertakan pustaka yang diperlukan untuk terhubung ke CockroachDB dengan SQLAlchemy, termasuk sqlalchemy-cockroachdbpaket Python, yang menjelaskan beberapa perbedaan antara CockroachDB dan PostgreSQL :
```python
psycopg2-binary
sqlalchemy
sqlalchemy-cockroachdb
```
File *dbinit.sql* menginisialisasi skema database yang digunakan aplikasi :
```python
Menggunakan SQLAlchemy models.pyuntuk memetakan Accountstabel ke objek Python:
```
Menggunakan SQLAlchemy models.pyuntuk memetakan Accountstabel ke objek Python :
```python
from sqlalchemy import Column, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Account(Base):
    """The Account class corresponds to the "accounts" database table. """
    __tablename__ = 'accounts'
    id = Column(UUID(as_uuid=True), primary_key=True)
    balance = Column(Integer)
```
Menggunakan SQLAlchemy main.pyuntuk memetakan metode Python ke operasi SQL :
```python
"""This simple CRUD application performs the following operations sequentially: 1. Creates 100 new accounts with randomly generated IDs and randomly-computed balance amounts. 2. Chooses two accounts at random and takes half of the money from the first and deposits it into the second. 3. Chooses five accounts at random and deletes them. """

from math import floor
import os
import random
import uuid

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_cockroachdb import run_transaction
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

from models import Account

# The code below inserts new accounts. 

def create_accounts(session, num):
    """Create N new accounts with random account IDs and account balances. """
    print("Creating new accounts...")
    new_accounts = []
    while num > 0:
        account_id = uuid.uuid4()
        account_balance = floor(random.random()*1_000_000)
        new_accounts.append(Account(id=account_id, balance=account_balance))
        seen_account_ids.append(account_id)
        print(f"Created new account with id {account_id} and balance {account_balance}.")
        num = num - 1
    session.add_all(new_accounts)


def transfer_funds_randomly(session, one, two):
    """Transfer money between two accounts. """
    try:
        source = session.query(Account).filter(Account.id == one).one()
    except NoResultFound:
        print("No result was found")
    except MultipleResultsFound:
        print("Multiple results were found")
    dest = session.query(Account).filter(Account.id == two).first()
    print(f"Random account balances:\nAccount {one}: {source.balance}\nAccount {two}: {dest.balance}")

    amount = floor(source.balance/2)
    print(f"Transferring {amount} from account {one} to account {two}...")

    # Check balance of the first account.     if source.balance < amount:
        raise ValueError(f"Insufficient funds in account {one}")
    source.balance -= amount
    dest.balance += amount

    print(f"Transfer complete.\nNew balances:\nAccount {one}: {source.balance}\nAccount {two}: {dest.balance}")


def delete_accounts(session, num):
    """Delete N existing accounts, at random. """
    print("Deleting existing accounts...")
    delete_ids = []
    while num > 0:
        delete_id = random.choice(seen_account_ids)
        delete_ids.append(delete_id)
        seen_account_ids.remove(delete_id)
        num = num - 1

    accounts = session.query(Account).filter(Account.id.in_(delete_ids)).all()

    for account in accounts:
        print(f"Deleted account {account.id}.")
        session.delete(account)


if __name__ == '__main__':
    # For cockroach demo:     # DATABASE_URL=postgresql://demo:<demo_password>@127.0.0.1:26257?sslmode=require     # For CockroachCloud:     # DATABASE_URL=postgresql://<username>:<password>@<globalhost>:26257/<cluster_name>.defaultdb?sslmode=verify-full&sslrootcert=<certs_dir>/<ca.crt>     db_uri = os.environ['DATABASE_URL'].replace("postgresql://", "cockroachdb://")
    try:
        engine = create_engine(db_uri)
    except Exception as e:
        print("Failed to connect to database.")
        print(f"{e}")

    seen_account_ids = []

    run_transaction(sessionmaker(bind=engine),
                    lambda s: create_accounts(s, 100))

    from_id = random.choice(seen_account_ids)
    to_id = random.choice([id for id in seen_account_ids if id != from_id])

    run_transaction(sessionmaker(bind=engine),
                    lambda s: transfer_funds_randomly(s, from_id, to_id))

    run_transaction(sessionmaker(bind=engine), lambda s: delete_accounts(s, 5))
```
*main.py* juga mengeksekusi mainmetode program.

## Langkah 3. Instal persyaratan aplikasi
Tutorial ini digunakan virtualenvuntuk manajemen ketergantungan.
1. Instal *virtualenv* :
```python
Instal virtualenv:
```
2. Di tingkat atas direktori proyek aplikasi, buat lalu aktifkan lingkungan virtual :
```python
virtualenv env
```
```python
source env/bin/activate
```
3. Instal modul yang diperlukan ke lingkungan virtual :
```python
pip install -r requirements.txt
```

## Langkah 4. Inisialisasi database
1. Setel *DATABASE_URL* variabel lingkungan ke string koneksi untuk cluster :
```python
export DATABASE_URL="{connection-string}"
```
2. Untuk menginisialisasi database contoh, gunakan perintah cockroach sql untuk mengeksekusi pernyataan SQL dalam *dbinit.sql* file :
```python
cat dbinit.sql | cockroach sql --url $DATABASE_URL
```
Pernyataan SQL dalam file inisialisasi harus dijalankan :
```python
CREATE TABLE

Time: 102ms
```

## Langkah 5. Jalankan kodenya
Jalankan aplikasi :
```python
Langkah 5. Jalankan kodenya
```
Aplikasi akan terhubung ke CockroachDB, dan kemudian melakukan beberapa penyisipan baris sederhana, pembaruan, dan penghapusan.

Outputnya akan terlihat seperti berikut :
```python
Creating new accounts...
Created new account with id 3a8b74c8-6a05-4247-9c60-24b46e3a88fd and balance 248835.
Created new account with id c3985926-5b77-4c6d-a73d-7c0d4b2a51e7 and balance 781972.
...
Created new account with id 7b41386c-11d3-465e-a2a0-56e0dcd2e7db and balance 984387.
Random account balances:
Account 7ad14d02-217f-48ca-a53c-2c3a2528a0d9: 800795
Account 4040aeba-7194-4f29-b8e5-a27ed4c7a297: 149861
Transferring 400397 from account 7ad14d02-217f-48ca-a53c-2c3a2528a0d9 to account 4040aeba-7194-4f29-b8e5-a27ed4c7a297...
Transfer complete.
New balances:
Account 7ad14d02-217f-48ca-a53c-2c3a2528a0d9: 400398
Account 4040aeba-7194-4f29-b8e5-a27ed4c7a297: 550258
Deleting existing accounts...
Deleted account 41247e24-6210-4032-b622-c10b3c7222de.
Deleted account 502450e4-6daa-4ced-869c-4dff62dc52de.
Deleted account 6ff06ef0-423a-4b08-8b87-48af2221bc18.
Deleted account a1acb134-950c-4882-9ac7-6d6fbdaaaee1.
Deleted account e4f33c55-7230-4080-b5ac-5dde8a7ae41d.
```
Dalam shell SQL yang terhubung ke cluster, dapat memverifikasi bahwa baris berhasil dimasukkan, diperbarui, dan dihapus :
```python
SELECT COUNT(*) FROM accounts;
```
```python
  count
---------
     95
(1 row)
```

# Menggunakan cluster lokal
## Langkah 1. Mulai CockroachDB
1. [Unduh biner CockroachDB.](https://www-cockroachlabs-com.translate.goog/docs/v21.2/install-cockroachdb?_x_tr_sl=en&_x_tr_tl=id&_x_tr_hl=id&_x_tr_pto=wapp)
2. Jalankan cockroach perintah start-single-node :
```python
cockroach start-single-node --advertise-addr 'localhost' --insecure
```
3. Perhatikan informasi koneksi berikut dalam teks sambutan shell SQL :
```python
CockroachDB node starting at 2021-08-30 17:25:30.06524 +0000 UTC (took 4.3s)
build:               CCL v21.1.6 @ 2021/07/20 15:33:43 (go1.15.11)
webui:               http://localhost:8080
sql:                 postgresql://root@localhost:26257?sslmode=disable
```
Akan menggunakan sqlstring koneksi untuk terhubung ke cluster nanti dalam tutorial ini.

## Langkah 2. Dapatkan kodenya
Kloning kode repo GitHub :
```python
git clone https://github.com/cockroachlabs/example-app-python-sqlalchemy/
```
Proyek ini memiliki struktur direktori berikut :
```python
├── README.md
├── dbinit.sql
├── main.py
├── models.py
└── requirements.txt
```
File *requirements.txt* tersebut menyertakan pustaka yang diperlukan untuk terhubung ke CockroachDB dengan SQLAlchemy, termasuk sqlalchemy-cockroachdbpaket Python, yang menjelaskan beberapa perbedaan antara CockroachDB dan PostgreSQL :
```python
psycopg2-binary
sqlalchemy
sqlalchemy-cockroachdb
```
File *dbinit.sql* menginisialisasi skema database yang digunakan aplikasi :
```python
Menggunakan SQLAlchemy models.pyuntuk memetakan Accountstabel ke objek Python:
```
Menggunakan SQLAlchemy models.pyuntuk memetakan Accountstabel ke objek Python :
```python
from sqlalchemy import Column, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Account(Base):
    """The Account class corresponds to the "accounts" database table. """
    __tablename__ = 'accounts'
    id = Column(UUID(as_uuid=True), primary_key=True)
    balance = Column(Integer)
```
Menggunakan SQLAlchemy main.pyuntuk memetakan metode Python ke operasi SQL :
```python
"""This simple CRUD application performs the following operations sequentially: 1. Creates 100 new accounts with randomly generated IDs and randomly-computed balance amounts. 2. Chooses two accounts at random and takes half of the money from the first and deposits it into the second. 3. Chooses five accounts at random and deletes them. """

from math import floor
import os
import random
import uuid

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_cockroachdb import run_transaction
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

from models import Account

# The code below inserts new accounts. 

def create_accounts(session, num):
    """Create N new accounts with random account IDs and account balances. """
    print("Creating new accounts...")
    new_accounts = []
    while num > 0:
        account_id = uuid.uuid4()
        account_balance = floor(random.random()*1_000_000)
        new_accounts.append(Account(id=account_id, balance=account_balance))
        seen_account_ids.append(account_id)
        print(f"Created new account with id {account_id} and balance {account_balance}.")
        num = num - 1
    session.add_all(new_accounts)


def transfer_funds_randomly(session, one, two):
    """Transfer money between two accounts. """
    try:
        source = session.query(Account).filter(Account.id == one).one()
    except NoResultFound:
        print("No result was found")
    except MultipleResultsFound:
        print("Multiple results were found")
    dest = session.query(Account).filter(Account.id == two).first()
    print(f"Random account balances:\nAccount {one}: {source.balance}\nAccount {two}: {dest.balance}")

    amount = floor(source.balance/2)
    print(f"Transferring {amount} from account {one} to account {two}...")

    # Check balance of the first account.     if source.balance < amount:
        raise ValueError(f"Insufficient funds in account {one}")
    source.balance -= amount
    dest.balance += amount

    print(f"Transfer complete.\nNew balances:\nAccount {one}: {source.balance}\nAccount {two}: {dest.balance}")


def delete_accounts(session, num):
    """Delete N existing accounts, at random. """
    print("Deleting existing accounts...")
    delete_ids = []
    while num > 0:
        delete_id = random.choice(seen_account_ids)
        delete_ids.append(delete_id)
        seen_account_ids.remove(delete_id)
        num = num - 1

    accounts = session.query(Account).filter(Account.id.in_(delete_ids)).all()

    for account in accounts:
        print(f"Deleted account {account.id}.")
        session.delete(account)


if __name__ == '__main__':
    # For cockroach demo:     # DATABASE_URL=postgresql://demo:<demo_password>@127.0.0.1:26257?sslmode=require     # For CockroachCloud:     # DATABASE_URL=postgresql://<username>:<password>@<globalhost>:26257/<cluster_name>.defaultdb?sslmode=verify-full&sslrootcert=<certs_dir>/<ca.crt>     db_uri = os.environ['DATABASE_URL'].replace("postgresql://", "cockroachdb://")
    try:
        engine = create_engine(db_uri)
    except Exception as e:
        print("Failed to connect to database.")
        print(f"{e}")

    seen_account_ids = []

    run_transaction(sessionmaker(bind=engine),
                    lambda s: create_accounts(s, 100))

    from_id = random.choice(seen_account_ids)
    to_id = random.choice([id for id in seen_account_ids if id != from_id])

    run_transaction(sessionmaker(bind=engine),
                    lambda s: transfer_funds_randomly(s, from_id, to_id))

    run_transaction(sessionmaker(bind=engine), lambda s: delete_accounts(s, 5))
```
*main.py* juga mengeksekusi mainmetode program.

## Langkah 3. Instal persyaratan aplikasi
Tutorial ini digunakan virtualenvuntuk manajemen ketergantungan.
1. Instal *virtualenv* :
```python
Instal virtualenv:
```
2. Di tingkat atas direktori proyek aplikasi, buat lalu aktifkan lingkungan virtual :
```python
virtualenv env
```
```python
source env/bin/activate
```
3. Instal modul yang diperlukan ke lingkungan virtual :
```python
pip install -r requirements.txt
```

## Langkah 4. Inisialisasi database
1. Setel *DATABASE_URL* variabel lingkungan ke string koneksi untuk cluster :
```python
export DATABASE_URL="{connection-string}"
```
2. Untuk menginisialisasi database contoh, gunakan perintah cockroach sql untuk mengeksekusi pernyataan SQL dalam *dbinit.sql* file :
```python
cat dbinit.sql | cockroach sql --url $DATABASE_URL
```
Pernyataan SQL dalam file inisialisasi harus dijalankan :
```python
CREATE TABLE

Time: 102ms
```

## Langkah 5. Jalankan kodenya
Jalankan aplikasi :
```python
$ python main.py
```
Aplikasi akan terhubung ke CockroachDB, dan kemudian melakukan beberapa penyisipan baris sederhana, pembaruan, dan penghapusan.

Outputnya akan terlihat seperti berikut :
```python
Creating new accounts...
Created new account with id 3a8b74c8-6a05-4247-9c60-24b46e3a88fd and balance 248835.
Created new account with id c3985926-5b77-4c6d-a73d-7c0d4b2a51e7 and balance 781972.
...
Created new account with id 7b41386c-11d3-465e-a2a0-56e0dcd2e7db and balance 984387.
Random account balances:
Account 7ad14d02-217f-48ca-a53c-2c3a2528a0d9: 800795
Account 4040aeba-7194-4f29-b8e5-a27ed4c7a297: 149861
Transferring 400397 from account 7ad14d02-217f-48ca-a53c-2c3a2528a0d9 to account 4040aeba-7194-4f29-b8e5-a27ed4c7a297...
Transfer complete.
New balances:
Account 7ad14d02-217f-48ca-a53c-2c3a2528a0d9: 400398
Account 4040aeba-7194-4f29-b8e5-a27ed4c7a297: 550258
Deleting existing accounts...
Deleted account 41247e24-6210-4032-b622-c10b3c7222de.
Deleted account 502450e4-6daa-4ced-869c-4dff62dc52de.
Deleted account 6ff06ef0-423a-4b08-8b87-48af2221bc18.
Deleted account a1acb134-950c-4882-9ac7-6d6fbdaaaee1.
Deleted account e4f33c55-7230-4080-b5ac-5dde8a7ae41d.
```
Dalam shell SQL yang terhubung ke cluster, dapat memverifikasi bahwa baris berhasil dimasukkan, diperbarui, dan dihapus :
```python
SELECT COUNT(*) FROM accounts;
```
```python
  count
---------
     95
(1 row)
```