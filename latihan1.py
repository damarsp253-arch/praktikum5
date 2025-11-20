data_mahasiswa = {}

def hitung_nilai_akhir(tugas, uts, uas):
    return (tugas * 0.30) + (uts * 0.35) + (uas * 0.35)

while True:
    print("\n=== PROGRAM DATA MAHASISWA ===")
    print("1. Tambah Data")
    print("2. Ubah Data")
    print("3. Hapus Data")
    print("4. Tampilkan Data")
    print("5. Cari Data")
    print("6. Keluar")

    menu = input("Pilih menu (1-6): ")

    # Tambah Data
    if menu == "1":
        nama = input("Nama: ")
        tugas = float(input("Nilai Tugas: "))
        uts = float(input("Nilai UTS: "))
        uas = float(input("Nilai UAS: "))
        akhir = hitung_nilai_akhir(tugas, uts, uas)

        data_mahasiswa[nama] = {
            "tugas": tugas,
            "uts": uts,
            "uas": uas,
            "akhir": akhir
        }
        print("Data berhasil ditambahkan!")

    # Ubah Data
    elif menu == "2":
        nama = input("Masukkan nama mahasiswa yang akan diubah: ")
        if nama in data_mahasiswa:
            tugas = float(input("Nilai Tugas baru: "))
            uts = float(input("Nilai UTS baru: "))
            uas = float(input("Nilai UAS baru: "))
            akhir = hitung_nilai_akhir(tugas, uts, uas)

            data_mahasiswa[nama] = {
                "tugas": tugas,
                "uts": uts,
                "uas": uas,
                "akhir": akhir
            }
            print("Data berhasil diubah!")
        else:
            print("Data tidak ditemukan!")

    # Hapus Data
    elif menu == "3":
        nama = input("Masukkan nama mahasiswa yang akan dihapus: ")
        if nama in data_mahasiswa:
            del data_mahasiswa[nama]
            print("Data berhasil dihapus!")
        else:
            print("Data tidak ditemukan!")

    # Tampilkan Data
    elif menu == "4":
        if data_mahasiswa:
            print("\n=== Daftar Data Mahasiswa ===")
            for nama, nilai in data_mahasiswa.items():
                print(f"Nama: {nama}")
                print(f"  Tugas: {nilai['tugas']}")
                print(f"  UTS  : {nilai['uts']}")
                print(f"  UAS  : {nilai['uas']}")
                print(f"  Akhir: {nilai['akhir']:.2f}\n")
        else:
            print("Belum ada data.")

    # Cari Data
    elif menu == "5":
        nama = input("Masukkan nama mahasiswa yang dicari: ")
        if nama in data_mahasiswa:
            nilai = data_mahasiswa[nama]
            print("\n=== Data Ditemukan ===")
            print(f"Nama: {nama}")
            print(f"Tugas: {nilai['tugas']}")
            print(f"UTS  : {nilai['uts']}")
            print(f"UAS  : {nilai['uas']}")
            print(f"Akhir: {nilai['akhir']:.2f}")
        else:
            print("Data tidak ditemukan!")

    # Keluar
    elif menu == "6":
        print("Program selesai.")
        break

    else:
        print("Menu tidak valid!")
