from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    hasil = None
    error = None

    if request.method == "POST":
        try:
            tugas = float(request.form["tugas"])
            uts = float(request.form["uts"])
            uas = float(request.form["uas"])

            # Perhitungan nilai akhir
            hasil = (tugas * 0.3) + (uts * 0.3) + (uas * 0.4)

        except ValueError:
            error = "Input tidak valid! Masukkan angka yang benar."

    return render_template("aboutsiska.html", hasil=hasil, error=error)

if __name__ == "__main__":
    app.run(debug=True)
