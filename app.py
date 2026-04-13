from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    hasil = None
    error = None

    if request.method == "POST":
        try:
            laju = float(request.form["laju"])
            durasi = float(request.form["durasi"])

            # Perhitungan
            hasil = laju * durasi

        except ValueError:
            error = "Input tidak valid! Masukkan angka yang benar."

    return render_template("aboutsiska.html", hasil=hasil, error=error)

if __name__ == "__main__":
    app.run(debug=True)
