# Minggu ke-11 : Mengerjakan dan Menjelaskan [Tutorial Flask](https://flask.palletsprojects.com/en/2.1.x/tutorial/)
Tutorial ini akan memandu dalam membuat aplikasi blog dasar yang disebut Flaskr.Pengguna akan dapat mendaftar, masuk, membuat posting, dan mengedit atau menghapus posting mereka sendiri. Dan menginstal aplikasi di komputer lain.

# Project Layout
Buat direktori proyek dan masukkan :
```python
$ mkdir flask-tutorial
$ cd flask-tutorial
```
Ikuti petunjuk instalasi.

Buat aplikasi flask sederhana dalam satu file :
```python
hello.py 
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'
```

Direktori proyek akan berisi :
* `flaskr/`, paket Python yang berisi kode aplikasi dan file.
* `tests/`, direktori yang berisi modul pengujian.
* `venv/`, lingkungan virtual Python tempat Flask dan dependensi lainnya diinstal.
* File instalasi memberi tahu Python cara menginstal proyek.
* Konfigurasi kontrol versi, seperti git.
* File proyek lain yang mungkin ditambahkan dilain waktu.

Layout project akan terlihat seperti ini :
```python
/home/user/Projects/flask-tutorial
├── flaskr/
│   ├── __init__.py
│   ├── db.py
│   ├── schema.sql
│   ├── auth.py
│   ├── blog.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── auth/
│   │   │   ├── login.html
│   │   │   └── register.html
│   │   └── blog/
│   │       ├── create.html
│   │       ├── index.html
│   │       └── update.html
│   └── static/
│       └── style.css
├── tests/
│   ├── conftest.py
│   ├── data.sql
│   ├── test_factory.py
│   ├── test_db.py
│   ├── test_auth.py
│   └── test_blog.py
├── venv/
├── setup.py
└── MANIFEST.in
```

Abaikan file yang tidak ditulis. Misalnya, dengan git :
*.gitignore* 
```python
venv/

*.pyc
__pycache__/

instance/

.pytest_cache/
.coverage
htmlcov/

dist/
build/
*.egg-info/
```

# Application setup
Aplikasi Flask adalah turunan dari Flaskclass. Segala sesuatu tentang aplikasi, seperti konfigurasi dan URL.

## Application factory
Buat **flaskr** direktori dan tambahkan __init__.py file. Melayani tugas ganda : __init__.py itu akan berisi pabrik aplikasi, dan memberitahu Python bahwa flaskr direktori harus diperlakukan sebagai sebuah paket.
```python
$ mkdir flaskr
```

*flaskr/__init__.py*
```python
import os

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app
```
## Run the application
Mode pengembangan menampilkan debugger interaktif setiap kali halaman memunculkan pengecualian, dan memulai ulang server setiap kali membuat perubahan pada kode.
*Bash*
```python
$ export FLASK_APP=flaskr
$ export FLASK_ENV=development
$ flask run
```

Fish
```python
$ set -x FLASK_APP flaskr
$ set -x FLASK_ENV development
$ flask run
```

*CMD*
```python
> set FLASK_APP=flaskr
> set FLASK_ENV=development
> flask run
```

*Powershell*
```python
> $env:FLASK_APP = "flaskr"
> $env:FLASK_ENV = "development"
> flask run
```

Outputnya :
* Serving Flask app "flaskr"
* Environment: development
* Debug mode: on
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
* Restarting with stat
* Debugger is active!
* Debugger PIN: 855-212-761

Ketik dibrowser http://127.0.0.1:5000/hello. Maka akan muncul "Halo, Dunia!"

# Define and access the database
Aplikasi akan menggunakan database [SQLite](https://sqlite.org/about.html) untuk menyimpan pengguna dan posting. Python hadir dengan dukungan bawaan untuk SQLite dalam **sqlite3** modul.

## Connect to the database
Dalam aplikasi web, koneksi ini biasanya terkait dengan permintaan. Itu dibuat di beberapa titik saat menangani permintaan, dan ditutup sebelum respons dikirim.
*flaskr/db.py*
```python
import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()
```
## Create the table
Dalam SQLite, data disimpan dalam *tabel* dan *kolom*. Buat file dengan perintah SQL yang diperlukan untuk membuat tabel kosong :
*flaskr/schema.sql*
```python
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE post (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user (id)
);
```
Tambahkan fungsi Python yang akan menjalankan perintah SQL ini ke `db.py` :
*flaskr/db.py* 
```python
def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')
```
## Register with the application
Fungsi `close_db` dan `init_db_command` harus didaftarkan pada instance aplikasi; jika tidak, mereka tidak akan digunakan oleh aplikasi. Sebagai gantinya, tulis fungsi yang mengambil aplikasi dan melakukan pendaftaran.
*flaskr/db.py* 
```python
def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
```
Impor dan panggil fungsi ini dari pabrik. Tempatkan kode baru di akhir fungsi pabrik sebelum mengembalikan aplikasi.
*flaskr/__init__.py*
```python
def create_app():
    app = ...
    # existing code omitted

    from . import db
    db.init_app(app)

    return app
```
## Initialize the database file
Sekarang setelah `init-db` terdaftar dengan aplikasi, itu dapat dipanggil menggunakan perintah `flask`, mirip dengan runperintah dari halaman sebelumnya.
Jalankan  perintah `init-db` :
```python
$ flask init-db
Initialized the database.
```
Sekarang akan ada file `flaskr.sqlite` difolder `instance` didalam proyek.

# Blueprints and Views
Flask menggunakan pola untuk mencocokkan URL permintaan yang masuk dengan tampilan yang seharusnya menanganinya. Tampilan mengembalikan data yang diubah Flask menjadi respons keluar. Flask juga bisa pergi ke arah lain dan menghasilkan URL ke tampilan berdasarkan nama dan argumennya.

## Create a blueprint
[**Blueprint**](https://flask.palletsprojects.com/en/2.1.x/api/#flask.Blueprint) adalah cara untuk mengatur sekelompok tampilan terkait dan kode lainnya. Karena blog perlu mengetahui tentang autentikasi, diperlukan autentikasi terlebih dahulu.
*flaskr/auth.py*
```python
import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')
```
Impor dan daftarkan cetak biru dari pabrik menggunakan [**app.register_blueprint()**](https://flask.palletsprojects.com/en/2.1.x/api/#flask.Flask.register_blueprint). Tempatkan kode baru di akhir fungsi pabrik sebelum mengembalikan aplikasi.
*flaskr/__init__.py*
```python
def create_app():
    app = ...
    # existing code omitted

    from . import auth
    app.register_blueprint(auth.bp)

    return app
```
Blueprint otentikasi akan memiliki tampilan untuk mendaftarkan pengguna baru dan untuk masuk dan keluar.

## The First View: Register
Untuk saat ini hanya akan menulis kode tampilan. Pada halaman berikutnya, menulis template untuk menghasilkan formulir HTML.
*flaskr/auth.py*
```python
@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        if error is None:
            try:
                db.execute(
                    "INSERT INTO user (username, password) VALUES (?, ?)",
                    (username, generate_password_hash(password)),
                )
                db.commit()
            except db.IntegrityError:
                error = f"User {username} is already registered."
            else:
                return redirect(url_for("auth.login"))

        flash(error)

    return render_template('auth/register.html')
```
## Login
Tampilan ini mengikuti pola yang sama seperti tampilan `register` di atas.
*flaskr/auth.py*
```python
@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/login.html')
```
Sekarang setelah id pengguna disimpan di [**session**](https://flask.palletsprojects.com/en/2.1.x/api/#flask.session), itu akan tersedia pada permintaan berikutnya. Di awal setiap permintaan, jika pengguna masuk, informasi mereka harus dimuat dan tersedia untuk tampilan lain.
*flaskr/auth.py*
```python
@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()
```
[**bp.before_app_request()**](https://flask.palletsprojects.com/en/2.1.x/api/#flask.Blueprint.before_app_request) mendaftarkan fungsi yang berjalan sebelum fungsi tampilan, apa pun URL yang diminta. `load_logged_in_user` memeriksa apakah id pengguna disimpan di [**session**](https://flask.palletsprojects.com/en/2.1.x/api/#flask.session) dan mendapatkan data pengguna itu dari database, menyimpannya di [**g.user**](https://flask.palletsprojects.com/en/2.1.x/api/#flask.g), yang berlangsung selama permintaan. Jika tidak ada id pengguna, atau jika id tidak ada, `g.user` akan menjadi None.

## Logout
Untuk keluar :
*flaskr/auth.py*
```python
@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))
```

## Require authentication in other views
Membuat, mengedit, dan menghapus posting blog akan membutuhkan pengguna untuk masuk. Seorang *dekorator* dapat digunakan untuk memeriksa ini untuk setiap tampilan yang diterapkannya.
*flaskr/auth.py*
```python
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view
```

## Endpoints and URLs
Fungsi [**url_for()**](https://flask.palletsprojects.com/en/2.1.x/api/#flask.url_for) menghasilkan URL ke tampilan berdasarkan nama dan argumen. Nama yang terkait dengan tampilan juga disebut titik akhir, dan secara default sama dengan nama fungsi tampilan.

# Template
Template adalah file yang berisi data statis serta placeholder untuk data dinamis. Sebuah template diberikan dengan data tertentu untuk menghasilkan dokumen akhir. Flask menggunakan perpustakaan template Jinja untuk merender template.

## The base layout
Setiap halaman dalam aplikasi akan memiliki tata letak dasar yang sama di sekitar badan yang berbeda. Alih-alih menulis seluruh struktur HTML di setiap template, setiap template akan *memperluas* template dasar dan menimpa bagian tertentu.
*flaskr/templates/base.html*
```python
<!doctype html>
<title>{% block title %}{% endblock %} - Flaskr</title>
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
<nav>
  <h1>Flaskr</h1>
  <ul>
    {% if g.user %}
      <li><span>{{ g.user['username'] }}</span>
      <li><a href="{{ url_for('auth.logout') }}">Log Out</a>
    {% else %}
      <li><a href="{{ url_for('auth.register') }}">Register</a>
      <li><a href="{{ url_for('auth.login') }}">Log In</a>
    {% endif %}
  </ul>
</nav>
<section class="content">
  <header>
    {% block header %}{% endblock %}
  </header>
  {% for message in get_flashed_messages() %}
    <div class="flash">{{ message }}</div>
  {% endfor %}
  {% block content %}{% endblock %}
</section>
```

## Register
*flaskr/templates/auth/register.html*
```python
{% extends 'base.html' %}

{% block header %}
  <h1>{% block title %}Register{% endblock %}</h1>
{% endblock %}

{% block content %}
  <form method="post">
    <label for="username">Username</label>
    <input name="username" id="username" required>
    <label for="password">Password</label>
    <input type="password" name="password" id="password" required>
    <input type="submit" value="Register">
  </form>
{% endblock %}
```

## Log In
Ini identik dengan templat daftar kecuali untuk judul dan tombol kirim.
*flaskr/templates/auth/login.html*
```python
{% extends 'base.html' %}

{% block header %}
  <h1>{% block title %}Log In{% endblock %}</h1>
{% endblock %}

{% block content %}
  <form method="post">
    <label for="username">Username</label>
    <input name="username" id="username" required>
    <label for="password">Password</label>
    <input type="password" name="password" id="password" required>
    <input type="submit" value="Log In">
  </form>
{% endblock %}
```

## Register a user
Sekarang setelah template otentikasi ditulis, dapat mendaftarkan pengguna. Pastikan server masih berjalan ( jika tidak), lalu buka http://127.0.0.1:5000/auth/register .flask run

# Static Files
Tampilan dan template autentikasi berfungsi, tetapi saat ini terlihat sangat sederhana. Beberapa [**CSS**](https://developer.mozilla.org/docs/Web/CSS) dapat ditambahkan untuk menambahkan gaya ke tata letak HTML yang buat. Gaya tidak akan berubah, jadi ini adalah file *statis*, bukan template.
Flask secara otomatis menambahkan tampilan static yang mengambil jalur relatif ke direktori `flaskr/static` dan menyajikannya. Template base.html sudah memiliki tautan ke file `style.css` :
```python
{{ url_for('static', filename='style.css') }}
```
Tutorial ini tidak berfokus pada cara menulis CSS, jadi cukup menyalin yang berikut ke dalam file `flaskr/static/style.css` :
*flaskr/static/style.css*
```python
html { font-family: sans-serif; background: #eee; padding: 1rem; }
body { max-width: 960px; margin: 0 auto; background: white; }
h1 { font-family: serif; color: #377ba8; margin: 1rem 0; }
a { color: #377ba8; }
hr { border: none; border-top: 1px solid lightgray; }
nav { background: lightgray; display: flex; align-items: center; padding: 0 0.5rem; }
nav h1 { flex: auto; margin: 0; }
nav h1 a { text-decoration: none; padding: 0.25rem 0.5rem; }
nav ul  { display: flex; list-style: none; margin: 0; padding: 0; }
nav ul li a, nav ul li span, header .action { display: block; padding: 0.5rem; }
.content { padding: 0 1rem 1rem; }
.content > header { border-bottom: 1px solid lightgray; display: flex; align-items: flex-end; }
.content > header h1 { flex: auto; margin: 1rem 0 0.25rem 0; }
.flash { margin: 1em 0; padding: 1em; background: #cae6f6; border: 1px solid #377ba8; }
.post > header { display: flex; align-items: flex-end; font-size: 0.85em; }
.post > header > div:first-of-type { flex: auto; }
.post > header h1 { font-size: 1.5em; margin-bottom: 0; }
.post .about { color: slategray; font-style: italic; }
.post .body { white-space: pre-line; }
.content:last-child { margin-bottom: 0; }
.content form { margin: 1em 0; display: flex; flex-direction: column; }
.content label { font-weight: bold; margin-bottom: 0.5em; }
.content input, .content textarea { margin-bottom: 1em; }
.content textarea { min-height: 12em; resize: vertical; }
input.danger { color: #cc2f2e; }
input[type=submit] { align-self: start; min-width: 10em; }
```
Buka http://127.0.0.1:5000/auth/login

# Blog Blueprint
Blog harus mencantumkan semua posting, mengizinkan pengguna yang masuk untuk membuat posting, dan mengizinkan penulis posting untuk mengedit atau menghapusnya.

## The blueprint
Tentukan cetak biru dan daftarkan di pabrik aplikasi.
*flaskr/blog.py*
```python
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('blog', __name__)
```
Impor dan daftarkan cetak biru dari pabrik menggunakan [**app.register_blueprint()**](https://flask.palletsprojects.com/en/2.1.x/api/#flask.Flask.register_blueprint). Tempatkan kode baru di akhir fungsi pabrik sebelum mengembalikan aplikasi.
*flaskr/__init__.py*
```python
def create_app():
    app = ...
    # existing code omitted

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app
```

## Index
Indeks akan menampilkan semua posting, yang terbaru terlebih dahulu. `JOIN` digunakan agar informasi penulis dari `user` tabel tersedia di hasil.
*flaskr/blog.py*
```python
@bp.route('/')
def index():
    db = get_db()
    posts = db.execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()
    return render_template('blog/index.html', posts=posts)
```

*flaskr/templates/blog/index.html*
```python
{% extends 'base.html' %}

{% block header %}
  <h1>{% block title %}Posts{% endblock %}</h1>
  {% if g.user %}
    <a class="action" href="{{ url_for('blog.create') }}">New</a>
  {% endif %}
{% endblock %}

{% block content %}
  {% for post in posts %}
    <article class="post">
      <header>
        <div>
          <h1>{{ post['title'] }}</h1>
          <div class="about">by {{ post['username'] }} on {{ post['created'].strftime('%Y-%m-%d') }}</div>
        </div>
        {% if g.user['id'] == post['author_id'] %}
          <a class="action" href="{{ url_for('blog.update', id=post['id']) }}">Edit</a>
        {% endif %}
      </header>
      <p class="body">{{ post['body'] }}</p>
    </article>
    {% if not loop.last %}
      <hr>
    {% endif %}
  {% endfor %}
{% endblock %}
```

## Create
Tampilan `create` berfungsi sama dengan `register` tampilan auth. Baik formulir ditampilkan, atau data yang diposting divalidasi dan postingan ditambahkan ke database atau kesalahan ditampilkan.
*flaskr/blog.py*
```python
@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO post (title, body, author_id)'
                ' VALUES (?, ?, ?)',
                (title, body, g.user['id'])
            )
            db.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/create.html')
```

*flaskr/templates/blog/create.html*
```python
{% extends 'base.html' %}

{% block header %}
  <h1>{% block title %}New Post{% endblock %}</h1>
{% endblock %}

{% block content %}
  <form method="post">
    <label for="title">Title</label>
    <input name="title" id="title" value="{{ request.form['title'] }}" required>
    <label for="body">Body</label>
    <textarea name="body" id="body">{{ request.form['body'] }}</textarea>
    <input type="submit" value="Save">
  </form>
{% endblock %}
```

## Update
Baik tampilan `update` maupun `delete` tampilan perlu diambil post oleh id dan memeriksa apakah pembuatnya cocok dengan pengguna yang masuk. Untuk menghindari duplikasi kode, harus menulis fungsi untuk mendapatkan post dan memanggilnya dari setiap tampilan.
*flaskr/blog.py*
```python
def get_post(id, check_author=True):
    post = get_db().execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' WHERE p.id = ?',
        (id,)
    ).fetchone()

    if post is None:
        abort(404, f"Post id {id} doesn't exist.")

    if check_author and post['author_id'] != g.user['id']:
        abort(403)

    return post
```
Argumen `check_author` didefinisikan sehingga fungsi dapat digunakan untuk mendapatkan a post tanpa memeriksa pembuatnya. Ini akan berguna jika menulis tampilan untuk menampilkan kiriman individual pada halaman, di mana pengguna tidak masalah karena mereka tidak mengubah kiriman.
*flaskr/blog.py *
```python
@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE post SET title = ?, body = ?'
                ' WHERE id = ?',
                (title, body, id)
            )
            db.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/update.html', post=post)
```
Tampilan `create` dan `update` tampilannya terlihat sangat mirip. Perbedaan utama adalah bahwa `update` tampilan menggunakan objek `post` dan `UPDATE` kueri alih-alih file `INSERT`. Dengan beberapa pemfaktoran ulang yang cerdas, dapat menggunakan satu tampilan dan template untuk kedua tindakan, tetapi untuk tutorial lebih jelas memisahkannya.
*flaskr/templates/blog/update.html*
```python
{% extends 'base.html' %}

{% block header %}
  <h1>{% block title %}Edit "{{ post['title'] }}"{% endblock %}</h1>
{% endblock %}

{% block content %}
  <form method="post">
    <label for="title">Title</label>
    <input name="title" id="title"
      value="{{ request.form['title'] or post['title'] }}" required>
    <label for="body">Body</label>
    <textarea name="body" id="body">{{ request.form['body'] or post['body'] }}</textarea>
    <input type="submit" value="Save">
  </form>
  <hr>
  <form action="{{ url_for('blog.delete', id=post['id']) }}" method="post">
    <input class="danger" type="submit" value="Delete" onclick="return confirm('Are you sure?');">
  </form>
{% endblock %}
```

## Delete
Tampilan hapus tidak memiliki template sendiri, tombol hapus adalah bagian dari `update.html` dan memposting ke `/<id>/deleteURL`. Karena tidak ada template, itu hanya akan menangani metode `POST` dan kemudian mengarahkan ulang ke `index` tampilan.
*flaskr/blog.py*
```python
@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_post(id)
    db = get_db()
    db.execute('DELETE FROM post WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('blog.index'))
```

# Make the Project Installable
Membuat proyek dapat diinstal berarti dapat membangun file distribusi dan menginstalnya di lingkungan lain, sama seperti menginstal Flask di lingkungan proyek.

## Describe the project
File `setup.py` menjelaskan proyek dan file miliknya.
*setup.py*
```python
from setuptools import find_packages, setup

setup(
    name='flaskr',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)
```
`packages` memberi tahu Python direktori paket apa (dan file Python yang dikandungnya) untuk disertakan. `find_packages()` menemukan direktori ini secara otomatis sehingga tidak perlu mengetiknya. Untuk menyertakan file lain, seperti direktori statis dan template, `include_package_data` sudah diatur. Python membutuhkan file lain bernama `MANIFEST.in` untuk memberi tahu apa data lain ini.
*MANIFEST.in*
```python
include flaskr/schema.sql
graft flaskr/static
graft flaskr/templates
global-exclude *.pyc
```

## Install the project
Gunakan `pip` untuk menginstal proyek di lingkungan virtual.
```python
$ pip install -e .
```
amati bahwa proyek tersebut sekarang diinstal dengan ``.pip list`

```python
$ pip list

Package        Version   Location
-------------- --------- ----------------------------------
click          6.7
Flask          1.0
flaskr         1.0.0     /home/user/Projects/flask-tutorial
itsdangerous   0.24
Jinja2         2.10
MarkupSafe     1.0
pip            9.0.3
setuptools     39.0.1
Werkzeug       0.14.1
wheel          0.30.0
```
Tidak ada yang berubah dari cara menjalankan proyek sejauh ini. `FLASK_APP` masih disetel ke `flaskr` dan masih menjalankan aplikasi, tetapi dapat memanggilnya dari mana saja, bukan hanya direktori. `flask runflask-tutorial`

# Test Coverage
Menulis pengujian unit untuk aplikasi  memungkinkan memeriksa apakah kode yang tulis berfungsi seperti yang diharapkan. Flask menyediakan klien uji yang mensimulasikan permintaan ke aplikasi dan mengembalikan data respons.
Gunakan [pytest](https://pytest.readthedocs.io/) dan [coverage](https://coverage.readthedocs.io/) untuk menguji dan mengukur kode. Instal keduanya :
```python
$ pip install pytest coverage
```

## Setup and Fixtures
Kode tes terletak di `tests` direktori. Direktori ini berada di sebelah paket `flaskr`, bukan di dalamnya. File `tests/conftest.py` berisi fungsi pengaturan yang disebut perlengkapan yang akan digunakan setiap pengujian.
Setiap pengujian akan membuat file database sementara baru dan mengisi beberapa data yang akan digunakan dalam pengujian. Tulis file SQL untuk memasukkan data itu.
*tests/data.sql*
```python
INSERT INTO user (username, password)
VALUES
  ('test', 'pbkdf2:sha256:50000$TCI4GzcX$0de171a4f4dac32e3364c7ddc7c14f3e2fa61f2d17574483f7ffbb431b4acb2f'),
  ('other', 'pbkdf2:sha256:50000$kJPKsz6N$d2d4784f1b030a9761f5ccaeeaca413f27f2ecb76d6168407af962ddce849f79');

INSERT INTO post (title, body, author_id, created)
VALUES
  ('test title', 'test' || x'0a' || 'body', 1, '2018-01-01 00:00:00');
```
Fixture `app` akan memanggil pabrik dan lolos `test_config` untuk mengonfigurasi aplikasi dan database untuk pengujian alih-alih menggunakan konfigurasi pengembangan lokal.
*tests/conftest.py*
```python
import os
import tempfile

import pytest
from flaskr import create_app
from flaskr.db import get_db, init_db

with open(os.path.join(os.path.dirname(__file__), 'data.sql'), 'rb') as f:
    _data_sql = f.read().decode('utf8')


@pytest.fixture
def app():
    db_fd, db_path = tempfile.mkstemp()

    app = create_app({
        'TESTING': True,
        'DATABASE': db_path,
    })

    with app.app_context():
        init_db()
        get_db().executescript(_data_sql)

    yield app

    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()
```

## Factory
Tidak banyak yang bisa diuji tentang pabrik itu sendiri. Sebagian besar kode akan dieksekusi untuk setiap tes, jadi jika ada yang gagal, tes lain akan memperhatikan.
Satu-satunya perilaku yang dapat berubah adalah melewati konfigurasi pengujian. Jika konfigurasi tidak diteruskan, harus ada beberapa konfigurasi default, jika tidak, konfigurasi harus diganti.
*tests/test_factory.py*
```python
from flaskr import create_app


def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing


def test_hello(client):
    response = client.get('/hello')
    assert response.data == b'Hello, World!'
```

## Database
Dalam konteks aplikasi, `get_db` harus mengembalikan koneksi yang sama setiap kali dipanggil. Setelah konteksnya, koneksi harus ditutup.
*tests/test_db.py*
```python
import sqlite3

import pytest
from flaskr.db import get_db


def test_get_close_db(app):
    with app.app_context():
        db = get_db()
        assert db is get_db()

    with pytest.raises(sqlite3.ProgrammingError) as e:
        db.execute('SELECT 1')

    assert 'closed' in str(e.value)
```
Perintah `init-db` harus memanggil fungsi `init_db` dan mengeluarkan pesan.
*tests/test_db.py*
```python
def test_init_db_command(runner, monkeypatch):
    class Recorder(object):
        called = False

    def fake_init_db():
        Recorder.called = True

    monkeypatch.setattr('flaskr.db.init_db', fake_init_db)
    result = runner.invoke(args=['init-db'])
    assert 'Initialized' in result.output
    assert Recorder.called
```

## Authentication
Untuk sebagian besar tampilan, pengguna harus masuk. Cara termudah untuk melakukan ini dalam pengujian adalah membuat POSTpermintaan ke logintampilan dengan klien. Daripada menuliskannya setiap saat, dapat menulis kelas dengan metode untuk melakukan itu, dan menggunakan perlengkapan untuk memberikannya kepada klien untuk setiap pengujian.
*tests/conftest.py*
```python
class AuthActions(object):
    def __init__(self, client):
        self._client = client

    def login(self, username='test', password='test'):
        return self._client.post(
            '/auth/login',
            data={'username': username, 'password': password}
        )

    def logout(self):
        return self._client.get('/auth/logout')


@pytest.fixture
def auth(client):
    return AuthActions(client)
```
Tampilan `register` harus berhasil dirender pada `GET`. Aktif `POST` dengan data formulir yang valid, itu harus diarahkan ke URL login dan data pengguna harus ada di database. Data yang tidak valid harus menampilkan pesan kesalahan.
*tests/test_auth.py*
```python
import pytest
from flask import g, session
from flaskr.db import get_db


def test_register(client, app):
    assert client.get('/auth/register').status_code == 200
    response = client.post(
        '/auth/register', data={'username': 'a', 'password': 'a'}
    )
    assert response.headers["Location"] == "/auth/login"

    with app.app_context():
        assert get_db().execute(
            "SELECT * FROM user WHERE username = 'a'",
        ).fetchone() is not None


@pytest.mark.parametrize(('username', 'password', 'message'), (
    ('', '', b'Username is required.'),
    ('a', '', b'Password is required.'),
    ('test', 'test', b'already registered'),
))
def test_register_validate_input(client, username, password, message):
    response = client.post(
        '/auth/register',
        data={'username': username, 'password': password}
    )
    assert message in response.data
```
Pengujian untuk `login` tampilan sangat mirip dengan pengujian untuk `register`. Daripada menguji data dalam database, session harus `user_id` mengatur setelah login.
*tests/test_auth.py*
```python
def test_login(client, auth):
    assert client.get('/auth/login').status_code == 200
    response = auth.login()
    assert response.headers["Location"] == "/"

    with client:
        client.get('/')
        assert session['user_id'] == 1
        assert g.user['username'] == 'test'


@pytest.mark.parametrize(('username', 'password', 'message'), (
    ('a', 'test', b'Incorrect username.'),
    ('test', 'a', b'Incorrect password.'),
))
def test_login_validate_input(auth, username, password, message):
    response = auth.login(username, password)
    assert message in response.data
```
Pengujian `logout` adalah kebalikan dari `login`. sessiontidak boleh berisi `user_id` setelah `logout`.
*tests/test_auth.py*
```python
def test_logout(client, auth):
    auth.login()

    with client:
        auth.logout()
        assert 'user_id' not in session
```

# Blog
Semua tampilan blog menggunakan `auth` yang tulis sebelumnya. Panggilan `auth.login()` dan permintaan berikutnya dari klien akan masuk sebagai `test` pengguna.
*tests/test_blog.py*
```python
import pytest
from flaskr.db import get_db


def test_index(client, auth):
    response = client.get('/')
    assert b"Log In" in response.data
    assert b"Register" in response.data

    auth.login()
    response = client.get('/')
    assert b'Log Out' in response.data
    assert b'test title' in response.data
    assert b'by test on 2018-01-01' in response.data
    assert b'test\nbody' in response.data
    assert b'href="/1/update"' in response.data
```
Pengguna harus masuk untuk mengakses `create`, `update`, dan `delete` tampilan. Pengguna yang masuk harus menjadi penulis kiriman untuk mengakses `update` dan `delete`, jika tidak, status akan dikembalikan. Jika a dengan yang diberikan tidak ada, dan harus kembali. `403 Forbiddenpostidupdatedelete404 Not Found`
*tests/test_blog.py*
```python
@pytest.mark.parametrize('path', (
    '/create',
    '/1/update',
    '/1/delete',
))
def test_login_required(client, path):
    response = client.post(path)
    assert response.headers["Location"] == "/auth/login"


def test_author_required(app, client, auth):
    # change the post author to another user
    with app.app_context():
        db = get_db()
        db.execute('UPDATE post SET author_id = 2 WHERE id = 1')
        db.commit()

    auth.login()
    # current user can't modify other user's post
    assert client.post('/1/update').status_code == 403
    assert client.post('/1/delete').status_code == 403
    # current user doesn't see edit link
    assert b'href="/1/update"' not in client.get('/').data


@pytest.mark.parametrize('path', (
    '/2/update',
    '/2/delete',
))
def test_exists_required(client, auth, path):
    auth.login()
    assert client.post(path).status_code == 404
```
Tampilan `create` dan `update` harus merender dan mengembalikan status untuk permintaan. Ketika data yang valid dikirim dalam permintaan, harus memasukkan data posting baru ke dalam database, dan harus mengubah data yang ada. Kedua halaman harus menampilkan pesan kesalahan pada data yang tidak valid. `200 OKGETPOSTcreateupdate`
*tests/test_blog.py*
```python
def test_create(client, auth, app):
    auth.login()
    assert client.get('/create').status_code == 200
    client.post('/create', data={'title': 'created', 'body': ''})

    with app.app_context():
        db = get_db()
        count = db.execute('SELECT COUNT(id) FROM post').fetchone()[0]
        assert count == 2


def test_update(client, auth, app):
    auth.login()
    assert client.get('/1/update').status_code == 200
    client.post('/1/update', data={'title': 'updated', 'body': ''})

    with app.app_context():
        db = get_db()
        post = db.execute('SELECT * FROM post WHERE id = 1').fetchone()
        assert post['title'] == 'updated'


@pytest.mark.parametrize('path', (
    '/create',
    '/1/update',
))
def test_create_update_validate(client, auth, path):
    auth.login()
    response = client.post(path, data={'title': '', 'body': ''})
    assert b'Title is required.' in response.data
```
Tampilan `delete` harus dialihkan ke URL indeks dan pos seharusnya tidak ada lagi di database.
*tests/test_blog.py*
```python
def test_delete(client, auth, app):
    auth.login()
    response = client.post('/1/delete')
    assert response.headers["Location"] == "/"

    with app.app_context():
        db = get_db()
        post = db.execute('SELECT * FROM post WHERE id = 1').fetchone()
        assert post is None
```

## Running the Tests
Beberapa konfigurasi tambahan, yang tidak diperlukan tetapi membuat pengujian berjalan dengan cakupan yang lebih sedikit, dapat ditambahkan ke file proyek `setup.cfg`.
*setup.cfg*
```python
[tool:pytest]
testpaths = tests

[coverage:run]
branch = True
source =
    flaskr
```
Untuk menjalankan tes, gunakan perintah `pytest`. Ini akan menemukan dan menjalankan semua fungsi pengujian yang telah ditulis.
```python
$ pytest

========================= test session starts ==========================
platform linux -- Python 3.6.4, pytest-3.5.0, py-1.5.3, pluggy-0.6.0
rootdir: /home/user/Projects/flask-tutorial, inifile: setup.cfg
collected 23 items

tests/test_auth.py ........                                      [ 34%]
tests/test_blog.py ............                                  [ 86%]
tests/test_db.py ..                                              [ 95%]
tests/test_factory.py ..                                         [100%]

====================== 24 passed in 0.64 seconds =======================
````
Jika ada tes yang gagal, pytest akan menunjukkan kesalahan yang muncul. Dapat menjalankan untuk mendapatkan daftar setiap fungsi `pytest -v`.
Untuk mengukur cakupan kode pengujian, gunakan perintah `coverage` untuk menjalankan `pytest` alih-alih menjalankannya secara langsung.
```python
$ coverage run -m pytest
```
Melihat laporan cakupan sederhana di terminal :
```python
$ coverage report
```
```

Name                 Stmts   Miss Branch BrPart  Cover
------------------------------------------------------
flaskr/__init__.py      21      0      2      0   100%
flaskr/auth.py          54      0     22      0   100%
flaskr/blog.py          54      0     16      0   100%
flaskr/db.py            24      0      4      0   100%
------------------------------------------------------
TOTAL                  153      0     44      0   100%
```
Laporan HTML memungkinkan melihat baris mana yang tercakup dalam setiap file :
```python
$ coverage html
```
Ini menghasilkan file dalam htmlcovdirektori. Buka `htmlcov/index.html` di browser.

# Deploy to Production
Bagian ini mengasumsikan "Anda memiliki server yang ingin Anda gunakan untuk menyebarkan aplikasi Anda."

## Build and Install
Standar saat ini untuk distribusi Python adalah format *wheel*, dengan `.whl` ekstensi. Pastikan wheel library diinstal terlebih dahulu:
```python
$ pip install wheel
```
Menjalankan `setup.py` dengan Python memberi alat baris perintah untuk mengeluarkan perintah terkait build. Perintah `bdist_wheel` akan membangun file distribusi roda.
```python
$ python setup.py bdist_wheel
```
Temukan file di `dist/flaskr-1.0.0-py3-none-any.whl`. Nama file dalam format {project name}-{version}-{python tag} -{abi tag}-{platform tag}.
Salin file ini ke komputer lain, [siapkan virtualenv baru](https://flask.palletsprojects.com/en/2.1.x/installation/#install-create-env), lalu instal file dengan ekstensi `pip`.
```python
$ pip install flaskr-1.0.0-py3-none-any.whl
```
Pip akan menginstal proyek beserta dependensinya.
Karena ini adalah mesin yang berbeda,  perlu menjalankannya init-dblagi untuk membuat database di folder instance.
*Bash*
```python
$ export FLASK_APP=flaskr
$ flask init-db
```

*Fish*
```python
$ set -x FLASK_APP flaskr
$ flask init-db
```

*CMD*
```python
> set FLASK_APP=flaskr
> flask init-db
```

*Powershell*
```python
> $env:FLASK_APP = "flaskr"
> flask init-db
```

## Configure the Secret Key
Menggunakan perintah berikut untuk menampilkan kunci rahasia acak :
```python
$ python -c 'import secrets; print(secrets.token_hex())'

'192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf'
```
Buat file `config.py` di folder instance, yang akan dibaca oleh pabrik jika ada. Salin nilai yang dihasilkan ke dalamnya.
*venv/var/flaskr-instance/config.py *
```python
SECRET_KEY = '192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf'
```

## Run with a Production Server
Saat menjalankan secara publik alih-alih dalam pengembangan, tidak boleh menggunakan server pengembangan bawaan ( ). Server pengembangan disediakan oleh Werkzeug untuk kenyamanan, tetapi tidak dirancang untuk menjadi sangat efisien, stabil, atau aman. `flask run`
Sebagai gantinya, gunakan server WSGI produksi. Misalnya, untuk menggunakan Waitress , instal terlebih dahulu di lingkungan virtual :
```python
$ pip install waitress
```
Mengimpor dan memanggil pabrik aplikasi untuk mendapatkan objek aplikasi.`flask run`
```python
$ waitress-serve --call 'flaskr:create_app'

Serving on http://0.0.0.0:8080
```

# Keep Developing!
Jika ingin terus mengembangkan proyek Flaskr, berikut adalah beberapa ide untuk dicoba selanjutnya :
* Tampilan detail untuk menampilkan satu postingan. Klik judul postingan untuk membuka halamannya.
* Suka / tidak suka posting.
* Komentar.
* Tag. Mengklik tag menunjukkan semua posting dengan tag itu.
* Kotak pencarian yang memfilter halaman indeks berdasarkan nama.
* Tampilan halaman. Hanya tampilkan 5 posting per halaman.
* Unggah gambar untuk disertakan dengan postingan.
* Format posting menggunakan penurunan harga.
* Umpan RSS dari posting baru.
Terima kasih!