def tampilkan_data_barang(stok):
    if not stok:
        print("Data Stok Barang Kosong")
    else:
        for idx, barang in enumerate(stok):
            print(f"{idx}.{barang['nama']} - {barang['jumlah']}")

def hitung_jumlah_data_barang(stok):
    return len(stok)

def pencarian_data_barang(stok,nama_barang):
    hasil = [barang for barang in stok if barang['nama'].lower() == nama_barang.lower()]
    return hasil

def edit_data_barang(stok, indeks, nama_baru, jumlah_baru):
    if 0 <= indeks < len(stok):
        stok[indeks]['nama'] = nama_baru
        stok[indeks]['jumlah'] = jumlah_baru
        return True
    else:
        return False
    
def tambah_data_barang(stok,nama_barang,jumlah):
    stok.append({'nama': nama_barang, 'jumlah':jumlah})

def hapus_data_barang(stok,indeks):
    if 0 <= indeks < len(stok):
        stok.pop(indeks)
        return True
    else:
        return False

def main():
    stok_barang = []

    while True:
        print("\n")
        print("Selamat datang di program Manajemen Stok Barang!")
        print("Pilihan:")
        print("1. Tambah Data Barang")
        print("2. Edit Data")
        print("3. Hapus Data Barang")
        print("4. Cari Data")
        print("5. Tampilkan Data Barang")
        print("6. Tampilkan Jumlah Data")
        print("7. Keluar")

        pilihan = input("Masukkan Pilihan: ")

        if pilihan == '1':
            nama_barang = input("Masukkan nama barang: ")
            jumlah = int(input("Masukkan jumlah barang: "))
            tambah_data_barang(stok_barang, nama_barang, jumlah)
            print("Data barang telah berhasil diinputkan")
        elif pilihan == '2':
            indeks = int(input("Masukkan indeks data yang ingin diedit: "))
            nama_baru = input("Masukkan nama baru: ")
            jumlah_baru = int(input("Masukkan jumlah baru: "))
            if edit_data_barang(stok_barang, indeks, nama_baru, jumlah_baru):
                print("Data telah berhasil diedit")
            else:
                print("Indeks tidak valid")
        elif pilihan == '3':
            indeks = int(input("Masukkan indeks data yang ingin di hapus: "))
            if hapus_data_barang(stok_barang, indeks):
                print("Data telah berhasil dihapus")
            else:
                print("Indeks tidak valid")
        elif pilihan == '4':
            nama_barang = input("Masukkan nama barang yang dicari: ")
            hasil = pencarian_data_barang(stok_barang, nama_barang)
            if hasil:
                for barang in hasil:
                    print(f"Nama:{barang['nama']}, Jumlah:{barang['jumlah']}")
                else:
                    print("Barang tidak ditemukan")
        elif pilihan == '5':
            tampilkan_data_barang(stok_barang)
        elif pilihan == '6':
            jumlah = hitung_jumlah_data_barang(stok_barang)
            print(f"Jumlah data yang tersimpan: {jumlah}")
        elif pilihan == '7':
            print("Terima kasih, Anda telah mencoba program ini")
            break
        else:
            print("Maaf pilihan Anda tidak valid, silahkan Anda boleh mencoba lagi nanti")
if __name__ == "__main__":
    main()



            
    
