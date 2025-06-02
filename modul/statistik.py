import json

def tampilkan_statistik():
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
        
    total_pemilih = len(daftar_pemilih)
    sudah_memilih = sum(1 for pemilih in daftar_pemilih if pemilih["sudah_memilih"])
    belum_memilih = total_pemilih - sudah_memilih
     
    partisipasi = (sudah_memilih / total_pemilih) * 100 if total_pemilih > 0 else 0
    
    calon_terbanyak = None
    suara_terbanyak = -1
    for calon in daftar_calon:
        if calon["jumlah_suara"] > suara_terbanyak:
            calon_terbanyak = calon
            suara_terbanyak = calon["jumlah_suara"]
            
    print(f"""
          \n===== STATISTIK PEMILIHAN KETUA =====
          total pemilih:    {total_pemilih}
          Sudah memilih:    {sudah_memilih}
          Belum memilih:    {belum_memilih}
          Partisipan   :    {partisipasi}
          """)
    
    #print("\nHasil Suara:")
    #for calon in daftar_calon:
        #print(f"- {calon['nama']} ({calon['id']}): {calon['jumlah_suara']} suara.")
        
    #if calon_terbanyak:
        #print(f"\nPemenang sementara: {calon_terbanyak['nama']} ({calon_terbanyak['id']}) dengan {calon_terbanyak['jumlah_suara']} suara.")