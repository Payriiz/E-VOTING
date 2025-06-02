import json

def tambah_pemilih():
    id_pemilih = input("Masukkan ID pemilih: ")
    nama = input("Masukkan nama pemilih: ")
    jurusan = input("Masukkan jurusan pemilih: ")
    
    file = open("data/pemilih.json", "r")
    content = file.read()
    file.close()
    
    if content.strip() == "":
        daftar_pemilih = []
    else:
        daftar_pemilih = json.loads(content)
        
    for pemilih in daftar_pemilih:
        if pemilih["id_pemilih"] == id_pemilih:
            print("ID pemilih sudah tersedia! Silakan masukkan ID pemilih yang berbeda.")
            return
        
    pemilih_baru = {
        "id_pemilih" : id_pemilih,
        "nama" : nama,
        "jurusan" : jurusan,
        "sudah_memilih" : False
    }
    
    daftar_pemilih.append(pemilih_baru)
    file = open("data/pemilih.json", "w")
    json.dump(daftar_pemilih, file)
    file.close()
    
    print("PEMILIH BERHASIL DITAMBAHKAN!")