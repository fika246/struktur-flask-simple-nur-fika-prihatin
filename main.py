from flask import Flask

app = Flask(__name__)

@app.route("/get")
def hello_get():
    return "Halo orang keren, ini halaman GET!"

@app.route("/post")
def hello_post():
    return "Halo pejuang coding, ini halaman POST!"

@app.route("/delete")
def hello_delete():
    return "Halo petualang, data kamu dihapus lewat DELETE!"

@app.route("/detail/<nama>")
def hello_detail(nama):
    return f"Halo {nama}, ini halaman detail spesial buat kamu!"

if __name__ == "__main__":
    app.run(debug=True)
