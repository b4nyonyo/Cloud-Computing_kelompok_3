from flask import Flask, render_template

app = Flask(__name__)

# Data profil anggota kelompok dengan foto
profiles = [

    {
        'name': 'Muhamad Arsya Pamungkas',
        'NIM': '22.83.0835',
        'Education': 'S1 Teknik Komputer. Universitas AMIKOM Yogyakarta.',
        'bio': 'Saya seorang mahasiswa teknik komputer, saya memiliki minat dalam desain grafis. saya juga memiliki hobi bermain game online',
        'photo': 'static/images/arsya.jpg'  # Path ke foto
    },

    {
        'name': 'Zakiya Fazila Salsabila',
        'NIM': '22.83.0850',
        'Education': 'S1 Teknik Komputer. Universitas AMIKOM Yogyakarta.',
        'bio': 'Saya adalah mahasiswi amikom yang sedang menempuh pendidikan S1 Teknik Komputer dengan menguasai kemampuan web programing, jaringan komputer dan juga kriptografi. ',
        'photo': 'static/images/zakiya.jpg'  # Path ke foto
    },

    {
        'name': 'Deny Tri Yulianto',
        'NIM': '22.83.0851',
        'Education': 'S1 Teknik Komputer. Universitas AMIKOM Yogyakarta.',
        'bio': 'Saya Seorang Mahaiswa yang mempunyai kemampuan di beberapa bidang seperti programing (python HTML), IOT (Microcontroller), Networking (Mikrotik), 3D Printing dan masih banyak lainya',
        'photo': 'static/images/deny.jpg'  # Path ke foto
    },

    {
        'name': 'Intan Utami',
        'NIM': '22.83.0874',
        'Education': 'S1 Teknik Komputer. Universitas AMIKOM Yogyakarta.',
        'bio': 'Saya seorang perempuan berusia 20 tahun yang sedang menempuh pendidikan S1 di bidang Teknik Komputer. Saat ini, saya menguasai beberapa bahasa pemrograman seperti Python dan HTML, serta memiliki sedikit pemahaman tentang database. Selain itu, saya juga memiliki pengetahuan dasar tentang jaringan komputer. ',
        'photo': 'static/images/intan.jpg'  # Path ke foto
    }
]

@app.route('/')
def index():
    return render_template('index.html', profiles=profiles)

if __name__ == '__main__':
    app.run(debug=True)
