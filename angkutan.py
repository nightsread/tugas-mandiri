# Inisialisasi daftar penumpang awal
penumpang = [] 

# Loop utama untuk menu
while True:
    print("==== Menu Manajemen Angkutan ====")
    print("Menu Manajemen Angkutan:")
    print("<1> Tambah Penumpang")
    print("<2> Penumpang Turun")
    print("<3> Cetak Daftar Penumpang")
    print("<4> Keluar")
    print("================================\n")

    pilihan = input("Masukkan nomor menu yang dipilih: ")

    if pilihan == "1":
        nama_penumpang = input("Masukkan nama penumpang yang ingin ditambahkan: ")
        if nama_penumpang in penumpang:
            print(f"{nama_penumpang} sudah ada dalam daftar penumpang.")
        else:
            penumpang.append(nama_penumpang)
            print(f"{nama_penumpang} berhasil ditambahkan.")
    elif pilihan == "2":
        nama_penumpang = input("Masukkan nama penumpang yang ingin turun: ")
        if nama_penumpang in penumpang:
            penumpang.remove(nama_penumpang)
            print(f"{nama_penumpang} berhasil turun dari angkutan.")
        else:
            print(f"Warning! {nama_penumpang} tidak ada dalam daftar penumpang.")
    elif pilihan == "3":
        print("\n==== Daftar Penumpang ====")
        for nama in penumpang:
            print(nama)
        print("==========================\n")
    elif pilihan == "4":
        print("Terima kasih.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih menu yang sesuai.")