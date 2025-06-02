import json

def lakukan_voting():
    id_pemilih = input("Masukkan ID Pemilih: ")
    
    file = open("data/pemilih.json", "r")
    content = file.read()
    file.close()
    if content.strip() == "":
        daftar_pemilih = []
    else:
        daftar_pemilih = json.loads(content)
    
    file = open("data/calon.json", "r")
    content = file.read()
    file.close()
    if content.strip() == "":
        daftar_calon = []
    else :
        daftar_calon = json.loads(content)
        
    for pem in daftar_pemilih:
        if pem['id_pemilih'] == id_pemilih:
            if pem["sudah_memilih"]:
                print("ANDA SUDAH MEMILIH SEBELUMNYA!")
                return
            
            else:
                print("\nDaftar Calon Ketua:")
                for urut, nama in enumerate(daftar_calon):
                    print(f"{urut + 1}. {nama['nama']} (ID: {nama['id_calon']})")
                pilihan = int(input("Masukkan pilihan anda: ")) -1
                if 0 <= pilihan < len(daftar_calon):
                    daftar_calon[pilihan]['jumlah_suara'] += 1
                    pem['sudah_memilih'] = True
                    
                    file = open("data/pemilih.json", "w")
                    json.dump(daftar_pemilih, file)
                    file.close()
                    
                    file = open("data/calon.json", "w")
                    json.dump(daftar_calon, file)
                    file.close()
                    
                    print("VOTING BERHASIL! Terima kasih telah menggunakan hak suara anda.")
                    break
                else:
                    print("PILIHAN ANDA TIDAK VALID!")
                    return
                
                print("ID PEMILIH TIDAK DITEMUKAN!")
                break
    
def tampilkan_hasil():
    try:
        with open("data/calon.json", "r") as file:
            content = file.read()
            if content.strip() == "":
                print("TIDAK ADA DATA CALON")
                return
            daftar_calon = json.loads(content)
    except FileNotFoundError:
        print("FILE data/calon.json TIDAK DITEMUKAN!")
        return

    print("\n=====HASIL SEMENTARA=====")
    print("\nHasil Suara:")
    for calon in daftar_calon:
        print(f"\n{calon['nama']} ({calon['id_calon']}) dengan {calon['jumlah_suara']} suara.")