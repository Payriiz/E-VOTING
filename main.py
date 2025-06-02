from modul import pemilih, calon, voting, statistik

def main():
    while True:
        print("""
              \n===== SISTEM E-VOTING =====
              1. Daftar Pemilih
              2. Daftar Calon Ketua
              3. Voting
              4. Tampilkan Hasil Sementara
              5. Statistik Pemilu
              6. Keluar
              """)
        
        pilihan = int(input("Pilih Menu (1-6): "))
        
        if pilihan == 1:
            pemilih.tambah_pemilih()
        elif pilihan == 2:
            calon.tambah_calon()
        elif pilihan == 3:
            voting.lakukan_voting()
        elif pilihan == 4:
            voting.tampilkan_hasil()
        elif pilihan == 5:
            statistik.tampilkan_statistik()
        elif pilihan == 6:
            print("TERIMA KASIH TELAH MENGGUNAKAN E_VOTING!")
            break
            
            
if __name__ == "__main__":
    main()