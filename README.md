🚀 Aplikasi Flask Routing Sederhana
Aplikasi ini adalah web sederhana berbasis Flask yang berfungsi untuk menampilkan beberapa route dasar (GET, POST, DELETE) serta route dinamis dengan parameter nama.
Proyek ini dibuat untuk latihan memahami konsep routing dan endpoint API dasar menggunakan framework Flask di Python.

🧠 Tujuan Proyek
Untuk membantu memahami :
Cara membuat aplikasi web dengan Flask
Cara mendefinisikan dan mengatur route dengan decorator @app.route()
Cara mengelola parameter dinamis di URL
Aplikasi ini cocok sebagai dasar untuk membangun API RESTful sederhana atau latihan backend sebelum menghubungkannya ke database.

⚙️ Fitur Utama
Route	Fungsi	Deskripsi
/get	GET	Menampilkan pesan teks untuk request GET
/post	POST	Menampilkan pesan teks untuk request POST
/delete	DELETE	Menampilkan pesan bahwa data dihapus
/detail/<nama>	Dynamic route	Menampilkan halaman personal sesuai nama di URL

Contoh penggunaan:
http://127.0.0.1:5000/detail/Ani
→ Output: "Halo Ani, ini halaman detail spesial buat kamu!"

🧩 Struktur Project
flask-routing/
│
├── main.py     # File utama yang berisi logika routing
└── README.md   # Dokumentasi proyek

▶️ Cara Menjalankan

Pastikan Python sudah terinstall

Install Flask:

pip install flask


Jalankan aplikasi:

python main.py


Buka di browser:

http://127.0.0.1:5000/

📜 Kesimpulan

Project ini adalah contoh dasar pemahaman Flask routing, di mana setiap endpoint memiliki respon berbeda.
Meskipun sederhana, konsep di sini bisa dikembangkan menjadi API CRUD, sistem login, atau aplikasi web dinamis.
