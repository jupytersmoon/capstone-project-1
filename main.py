def main():
    print("Selamat Datang di Toko Indoapril")
    print("==MENU UTAMA==\n")
    print("1. Lihat daftar penjualan")
    print("2. Tambah data")
    print("3. Ubah data")
    print("4. Hapus data")
    print("5. Keluar")
    
    choice = int(input("Masukkan pilihan (1-5):"))
    while choice not in [1,2,3,4,5]:
        print("\nUlangi input Anda.")
        choice = int(input("Masukkan pilihan (1-5):"))
    if choice == 1:
        view()
    elif choice == 2:
        tambah()
    elif choice == 3:
        ubah()
    elif choice == 4:
        hapus()
    else:
        print("Sampai jumpa!")
        exit()

def akhir():
    ex = input("\nKembali ke Menu? (y/n):")
    if ex == "y":
        main()
    elif ex == "n":
        print("\nSampai Jumpa!")
        exit()
    else:
        print("Input tidak valid!")
        akhir()

def view():
    print("\n=Menu Lihat Daftar Penjualan=\n")
    print("1. Lihat seluruh data")
    print("2. Lihat data tertentu")
    choice = int(input("Masukkan pilihan (1-2):"))
    while choice not in [1,2]:
        print("\nUlangi input Anda.")
        choice = int(input("Masukkan pilihan (1-2):"))

    if choice == 1:
        print("\n=Berikut adalah data penjualan Toko Indoapril=")
        sum = 0
        for tanggal,detail in data.items():
            print(f"\nTanggal {tanggal}")
            for item, isi in detail.items():
                jual = isi['Sales']
                harga = isi['Harga']
                sum+= jual*harga
                print(f"{item} terjual {jual}, harga jual {harga}, pendapatan sebanyak {jual*harga}")
        print(f"\nTotal penjualan adalah {sum}")
    else:
        print("\n=Menu Detail=\n")
        print("1. Tanggal tertentu")
        print("2. Item tertentu")
        choice2 = int(input("Masukkan pilihan (1-2):"))
        while choice2 not in [1,2]:
            print("\nUlangi input Anda.")
            choice2 = int(input("Masukkan pilihan (1-2):"))
        
        if choice2 == 1:
            tgl = str(input("Masukkan tanggal (ddmmyyy):"))
            try:
                getdata = data[tgl]
            except:
                print("\n!!Tanggal yang dimaksud tidak ada di data.!!")
                print(">>Kembali ke Menu Lihat Daftar Penjualan")
                view()

            print("\n")
            sum = 0
            for item, isi in getdata.items():
                jual = isi['Sales']
                harga = isi['Harga']
                sum += jual*harga
                print(f"{item} terjual {jual}, harga jual {harga}, pendapatan sebanyak {jual*harga}")
            print(f"\nTotal penjualan adalah {sum}")
            akhir()
        else:
            brg = str(input("Masukkan barang yang dicari:"))
            for key in data.keys():
                if brg not in data[key]:
                    print("\n!!Barang yang dimaksud tidak ada di data.!!")
                    print(">>Kembali ke Menu Lihat Daftar Penjualan")
                    view()
            print("\n")
            sum = 0
            for tanggal,detail in data.items():
                if brg in detail.keys():
                    print(f"\nTanggal {tanggal}")
                    isi = detail[brg]
                    jual = isi['Sales']
                    harga = isi['Harga']
                    sum += jual*harga
                    print(f"{brg} terjual {jual}, harga jual {harga}, pendapatan sebanyak {jual*harga}")
            print(f"\nTotal penjualan adalah {sum}")
    akhir()

def tambah():
    global data
    print("\n=Menu Tambah Data=\n")
    print("1. Tambah data harian")
    print("2. Tambah data barang")
    print("3. Kembali ke Menu Utama")
    choice = int(input("Masukkan pilihan (1-3):"))
    while choice not in [1,2,3]:
        print("\nUlangi input Anda.")
        choice = int(input("Masukkan pilihan (1-3):"))
    
    if choice == 1:
        tanggal = str(input("Masukkan tanggal (ddmmyyy):"))
        while tanggal in data.keys():
            print("!!Tanggal sudah ada!!")
            tanggal = str(input("Masukkan tanggal (ddmmyyy):"))
        iter = int(input("Berapa data yang ingin dimasukkan?"))

        data[tanggal]={}

    elif choice == 2:
        tanggal = str(input("Masukkan tanggal (ddmmyyy):"))
        while tanggal not in data.keys():
            print("!!Tanggal tidak ada!!")
            tanggal = str(input("Masukkan tanggal (ddmmyyy):"))
        iter = int(input("Berapa data yang ingin dimasukkan?"))

    else:
        main()
    
    for i in range(iter):
        detail = input("Masukkan nama barang yang ingin ditambahkan: ")
        while detail in data[tanggal].keys():
            print(f"Sudah ada {detail} di data.")
            detail = input("Masukkan nama barang yang ingin ditambahkan: ")
        data[tanggal][detail] = {}
        data[tanggal][detail]['Sales'] = int(input("Banyak terjual: "))
        data[tanggal][detail]['Harga'] = int(input("Harga jual: "))

    save = input("\nSimpan data? (y/n)")
    if save == 'y':
        print("Data tersimpan!")
    elif save =='n':
        print("Data tidak tersimpan!")
        del data[tanggal]
    else:
        print("Input tidak valid. Kembali ke Menu Tambah Data.")
        del data[tanggal]
        tambah()

    back = input("\nTambah data selesai. Kembali ke Menu Tambah Data? (y/n)")
    if back == 'y':
        tambah()
    elif back =='n':
        akhir()
    else:
        print("Input tidak valid. Kembali ke Menu Utama.")
        main()

def ubah():
    global data
    print("\n=Menu Ubah Data=\n")
    print("1. Ubah data")
    print("2. Kembali ke Menu Utama")
    choice = int(input("Masukkan pilihan (1-2):"))
    while choice not in [1,2]:
        print("\nUlangi input Anda.")
        choice = int(input("Masukkan pilihan (1-2):"))

    if choice == 1:
        tanggal = input("Masukkan tanggal data yang ingin diubah (ddmmyyy): ")
        if tanggal not in data.keys():
            print("Tidak ditemukan data untuk tanggal tersebut.")
            ubah()

        sum = 0
        for item, isi in data[tanggal].items():
            jual = isi['Sales']
            harga = isi['Harga']
            sum += jual*harga
            print(f"{item} terjual {jual}, harga jual {harga}, pendapatan sebanyak {jual*harga}")
        print(f"\nTotal penjualan adalah {sum}")

        u = input("\nIngin ubah data di atas?(y/n)")
        if u == 'n':
            print("Kembali ke Menu Ubah Data.")
            ubah()
        elif u != 'y':
            print("Input tidak valid. Kembali ke Menu Ubah Data.")
            ubah()
        
        print("\n1. Ubah nama barang")
        print("2. Ubah jumlah terjual dan harga barang")
        temp = int(input("Masukkan pilihan (1-2):"))
        while temp not in [1,2]:
            print("\nUlangi input Anda.")
            temp = int(input("Masukkan pilihan (1-2):"))
        
        ubahbarang(temp,tanggal)
    else:
        main()

def ubahbarang(a:int, tgl:str):
    global data
    items = data[tgl].keys()
    if a == 1:
        barang = input("Masukkan nama barang yang ingin diubah: ")
        if barang not in items:
            print(f"Tidak ditemukan {barang} di data.")
            ubahbarang(a,tgl)
        barang_new = input("Masukkan nama barang baru: ")
        while barang_new in items:
            print(f"Ditemukan {barang_new} di data.")
            barang_new = input("Masukkan nama barang baru: ")

        dum = input("Yakin untuk update data? (y/n)")
        if dum == 'n':
            print("Kembali ke Menu Ubah Data.")
            ubah()
        elif dum != 'y':
            print("Input tidak valid.")
            ubahbarang(a,tgl)
        data[tgl][barang_new] = data[tgl][barang]
        del data[tgl][barang]

        print("\nData berhasil diubah.")
        sum = 0
        for item, isi in data[tgl].items():
            jual = isi['Sales']
            harga = isi['Harga']
            sum += jual*harga
            print(f"{item} terjual {jual}, harga jual {harga}, pendapatan sebanyak {jual*harga}")
        print(f"\nTotal penjualan adalah {sum}")

        next = input("\nLanjut ubah detail barang? (y/n)")
        if next == 'n':
            akhir()
        elif next != 'y':
            print("Input tidak valid.")
            ubah()
        else:
            a = 2
            ubahbarang(a,tgl)
    else:
        barang = input("Masukkan nama barang: ")
        if barang not in items:
            print(f"Tidak ditemukan {barang} di data.")
            ubahbarang(a,tgl)
        
        jual = int(input("Masukkan banyak barang terjual: "))
        harga = int(input("Masukkan harga jual barang: "))
        print(f"{barang} terjual {jual}, harga jual {harga}, pendapatan sebanyak {jual*harga}")

        dum = input("\nApakah data di atas sudah benar? (y/n)")
        if dum == 'n':
            print("Kembali ke Menu Ubah Data.")
            ubahbarang(a,tgl)
        elif dum != 'y':
            print("Input tidak valid.")
            ubah()

        data[tgl][barang]['Sales'] = jual
        data[tgl][barang]['Harga'] = harga

        print("\nData berhasil diubah!")
        akhir()

def hapus():
    global data
    print("\n=Menu Hapus Data=\n")
    print("1. Hapus data")
    print("2. Kembali ke Menu Utama")
    choice = int(input("Masukkan pilihan (1-2):"))
    while choice not in [1,2]:
        print("\nUlangi input Anda.")
        choice = int(input("Masukkan pilihan (1-2):"))

    if choice == 1:
        tanggal = input("Masukkan tanggal data yang ingin dihapus (ddmmyyy): ")
        if tanggal not in data.keys():
            print("Tidak ditemukan data untuk tanggal tersebut.")
            hapus()
        
        sum = 0
        for item, isi in data[tanggal].items():
            jual = isi['Sales']
            harga = isi['Harga']
            sum += jual*harga
            print(f"{item} terjual {jual}, harga jual {harga}, pendapatan sebanyak {jual*harga}")
        print(f"\nTotal penjualan adalah {sum}\n")

        print("1. Hapus semua data satu hari")
        print("2. Hapus data tertentu")
        print("3. Batal")
        dum = int(input("Masukkan pilihan (1-3):"))
        while dum not in [1,2,3]:
            print("\nUlangi input Anda.")
            dum = int(input("Masukkan pilihan (1-3):"))
        
        if dum == 1:
            print(f"Anda akan menghapus seluruh data untuk tanggal {tanggal}.")
            next = input("Yakin? (y/n)")
            if next == 'n':
                akhir()
            elif next != 'y':
                print("Input tidak valid. Kembali ke Menu Hapus Data.")
                hapus()
            else:
                del data[tanggal]
        elif dum == 2:
            barang = input("Masukkan data barang yang ingin dihapus: ")
            if barang not in data[tanggal]:
                print("Tidak ditemukan data untuk tanggal tersebut.")
                hapus()

            print(f"Anda akan menghapus {barang} dari data tanggal {tanggal}.")
            next = input("Yakin? (y/n)")
            if next == 'n':
                akhir()
            elif next != 'y':
                print("Input tidak valid. Kembali ke Menu Hapus Data.")
                hapus()
            else:
                del data[tanggal][barang]
        else:
            print("Perintah dibatalkan.")
            hapus()
        print("\nHapus data berhasil.")
        akhir()
            
    else:
        main()
        
data = {
    '02092024':{
        'Susu':{'Sales': 4,'Harga': 5000},'Kopi':{'Sales': 3, 'Harga': 3000},'Teh' :{'Sales': 6, 'Harga': 2500},
        'Roti':{'Sales': 4,'Harga': 3000},'Permen':{'Sales': 6, 'Harga': 1000},'Es krim' :{'Sales': 3, 'Harga': 5000}
    },
    '03092024':{
        'Susu':{'Sales': 19,'Harga': 5000},'Kopi':{'Sales': 4, 'Harga': 3000},'Teh' :{'Sales': 12, 'Harga': 2500},
        'Roti':{'Sales': 5,'Harga': 3000},'Permen':{'Sales': 6, 'Harga': 1000},'Es krim' :{'Sales': 3, 'Harga': 5000}
        
    },
    '04092024':{
        'Susu':{'Sales': 15,'Harga': 5000},'Kopi':{'Sales': 10, 'Harga': 3000},'Teh' :{'Sales': 15, 'Harga': 2500},
        'Roti':{'Sales': 20,'Harga': 3000},'Permen':{'Sales': 5, 'Harga': 1000},'Es krim' :{'Sales': 6, 'Harga': 5000}
        
    },
    '05092024':{
        'Susu':{'Sales': 20,'Harga': 5000},'Kopi':{'Sales': 16, 'Harga': 3000},'Teh' :{'Sales': 10, 'Harga': 2500},
        'Roti':{'Sales': 8,'Harga': 3000},'Permen':{'Sales': 3, 'Harga': 1000},'Es krim' :{'Sales': 7, 'Harga': 5000}
        
    },
    '06092024':{
        'Susu':{'Sales': 9,'Harga': 5000},'Kopi':{'Sales': 6, 'Harga': 3000},'Teh' :{'Sales': 4, 'Harga': 2500},
        'Roti':{'Sales': 7,'Harga': 3000},'Permen':{'Sales': 0, 'Harga': 1000},'Es krim' :{'Sales': 12, 'Harga': 5000}

    },
    '07092024':{
        'Susu':{'Sales': 14,'Harga': 5000},'Kopi':{'Sales': 16, 'Harga': 3000},'Teh' :{'Sales': 1, 'Harga': 2500},
        'Roti':{'Sales': 10,'Harga': 3000},'Permen':{'Sales': 0, 'Harga': 1000},'Es krim' :{'Sales': 11, 'Harga': 5000}

    },
    '08092024':{
        'Susu':{'Sales': 5,'Harga': 5000},'Kopi':{'Sales': 13, 'Harga': 3000},'Teh' :{'Sales':0, 'Harga': 2500},
        'Roti':{'Sales': 6,'Harga': 3000},'Permen':{'Sales': 2, 'Harga': 1000},'Es krim' :{'Sales': 9, 'Harga': 5000}

    },

}

# Data penjualan toko Indoapril selama 1 minggu (02092024 - 08092024)
main()

