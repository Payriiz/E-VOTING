# Simulasi E-Voting Pemilihan Ketua Organisasi Mahasiswa

Sistem ini merupakan simulasi pemilu elektronik (e-voting) berbasis Python yang digunakan untuk memilih ketua. Sistem ini mencakup pencatatan data pemilih dan calon ketua, proses pemungutan suara, serta statistik hasil pemilu.

---

✨ Fitur Utama
Manajemen Data Pemilih dan Calon Ketua
Menambah dan menyimpan data pemilih serta calon dalam file .json.

Pemungutan Suara (Voting)
Validasi ID pemilih dan calon. Pemilih hanya dapat memilih satu kali.

Hasil Sementara dan Statistik
Menampilkan hasil perolehan suara dan statistik partisipasi pemilu.

---

## 🗂️ Struktur Proyek

```plaintext
e_voting/
│
├── main.py            # Menu utama CLI
│
├── modul/
│   ├── __pycache__/   # Cache Python otomatis
│   ├── utils.py       # Fungsi bantu: load_data, save_data
│   ├── pemilih.py     # Tambah data pemilih
│   ├── calon.py       # Tambah data calon ketua
│   ├── voting.py      # Proses pemungutan suara dan hasil perolehan suara
│   └── statistik.py   # Statistik partisipasi
│
├── data/
│   ├── pemilih.json   # Data pemilih (list of dict)
│   └── calon.json     # Data calon ketua
│
└── README.md          # Dokumentasi proyek
