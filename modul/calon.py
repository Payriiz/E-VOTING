import json

def tambah_calon():
    id_calon = input("Masukkan ID calon: ")
    nama = input("Masukkan nama calon: ")
    visi = input("Masukkan Visi Misi: ")
    
    file = open("data/calon.json", "r")
    content = file.read()
    file.close()
    if content.strip() == "":
        daftar_calon = []
    else :
        daftar_calon = json.loads(content)
        
    for calon in daftar_calon:
        if calon["id_calon"] == id_calon:
            print("ID calon sudah tersedia! Silakan masukkan ID calon yang berbeda.")
            return
        
    calon_baru = {
        "id_calon": id_calon,
        "nama": nama,
        "visi" : visi,
        "jumlah_suara": 0
    }
    
    daftar_calon.append(calon_baru)
    file = open("data/calon.json", "w")
    json.dump(daftar_calon, file)
    file.close()
    
    print("CALON BERHASIL DITAMBAHKAN!")