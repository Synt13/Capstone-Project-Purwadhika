from prettytable import PrettyTable

kamusIklan = [
     ['Harga Produk', 'Harga jual dari produk Anda'],
     ['Profit Produk', 'Jumlah keuntungan bersih dari harga jual produk Anda'],
     ['Persentase Profit', 'Persentase Profit Produk terhadap Harga Produk'],
     ['Biaya Iklan', 'Total biaya yang sudah Anda keluarkan untuk beriklan'],
     ['Penjualan', 'Total penjualan atau omzet yang dihasilkan dari iklan Anda'],
     ['Persentase ACOS', 'Persentase Biaya Iklan terhadap Penjualan (Ad Cost of Sales), semakin kecil semakin baik']
]

iklanAnda = []
simulasiAnda = []

def printKamus():
    print('Kamus Iklan\n')
    # print('No| Kata          \t| Keterangan')
    tabKamusIklan = PrettyTable()
    tabKamusIklan.field_names = ['No', 'Kata', 'Keterangan']
    for i in range(len(kamusIklan)) :
        # print(f'{i+1} | {kamusIklan[i][0]}  \t| {kamusIklan[i][1]}')
        tabKamusIklan.add_row([i+1, kamusIklan[i][0], kamusIklan[i][1]])
    
    tabKamusIklan.align = 'l'
    print(tabKamusIklan)

def printTabel(dataIklan):
    tabDataAnda = PrettyTable()
    tabDataAnda.field_names = ['No', 'SKU Produk', 'Harga Produk', 'Profit Produk', 'Biaya Iklan', 'Penjualan', 'Persentase Profit', 'Persentase ACOS']
    for i in range(len(dataIklan)) :
        # print(f'{i+1} | {dataIklan[i][0]}  \t| {dataIklan[i][1]}   \t| {dataIklan[i][2]}      \t| {dataIklan[i][3]}   \t| {dataIklan[i][4]}     \t| {dataIklan[i][5]}%      \t| {dataIklan[i][6]}%')
        tabDataAnda.add_row([i+1, dataIklan[i][0], dataIklan[i][1], dataIklan[i][2], dataIklan[i][3], dataIklan[i][4], f'{dataIklan[i][5]}%', f'{dataIklan[i][6]}%'])
        
    tabDataAnda.align = 'l'    
    print(tabDataAnda)

def isDigit (angka):
    return angka.isdigit()

def inputAngka(teks):
    userInput = input(teks)
    while not isDigit(userInput):
        print('Input harus berupa angka. Coba lagi.')
        userInput = input(teks)
    return userInput

def userData(userInput):
    while True:
        skuProduk = input('Masukkan nama/nomor SKU produk Anda: ').upper()
        if any(data[0] == skuProduk for data in userInput):
            print(f"SKU produk '{skuProduk}' sudah terdaftar. Silakan pilih opsi lain.")
            continue

        hargaProduk = inputAngka('Masukkan harga jual produk Anda: ')
        while not int(hargaProduk) >= 1000:
            print('Harga jual produk minimal 1000. Coba lagi.')
            hargaProduk = inputAngka('Masukkan harga jual produk Anda: ')

        profitProduk = inputAngka('Berapa jumlah profit per produk Anda: ')
        while not int(profitProduk) < int(hargaProduk):
            print('Profit tidak mungkin sama atau lebih besar dari harga jual. Coba lagi')
            profitProduk = inputAngka('Berapa jumlah profit per produk Anda: ')

        persenProfit = round(int(profitProduk) / int(hargaProduk) * 100, 2)
        biayaIklan = inputAngka('Masukkan total biaya iklan yang sudah Anda keluarkan: ')
        penjualan = inputAngka('Berapa total penjualan dari iklan Anda: ')
        persenAcos = 0.0 if penjualan == '0' else round(int(biayaIklan) / int(penjualan) * 100, 2)

        while True:
            confirmed = input('Apakah data yang anda input sudah benar? (y/n):').upper()
            if confirmed == 'Y':
                userInput.append([skuProduk, hargaProduk, profitProduk, biayaIklan, penjualan, persenProfit, persenAcos])
                print('\nData produk dan iklan Anda sudah disimpan\n')
                printTabel(userInput)
                return
            elif confirmed == 'N':
                print("Data batal disimpan.")
                break
            else:
                print('Silakan pilih y/n untuk konfirmasi')

def matchingData(dataset, target):
    target = target.upper()
    dataMatch = [data for data in dataset if data[0].upper() == skuTarget]
    return dataMatch


while True :
    menuIklan = inputAngka('''
        Selamat datang di RoboAds
        
        Menu :
        1. Kamus Iklan 
        2. Masukkan Data Produk dan Iklan
        3. Menampilkan Data Produk dan Iklan Anda
        4. Menghapus Data Produk dan Iklan
        5. Analisa Iklan
        6. Simulasi Iklan
        0. Keluar
                 
        Masukkan menu yang ingin dijalankan : ''')
    
    if(menuIklan == '1') :
        while True :
            menuIklan1 = inputAngka('''
            1. Kamus Iklan
            0. Menu Utama
                               
            Masukkan Menu yang ingin dijalankan : ''')
            if(menuIklan1 == '1'):
                printKamus()
            elif(menuIklan1 == '0'):
                 break
            else :
                 print('\nPilih menu yang sesuai. Coba lagi')

    elif(menuIklan == '2') :
        while True:
            menuIklan2 = inputAngka('''
            1. Input Data Produk dan Iklan Anda
            0. Menu Utama
                               
            Masukkan Menu yang ingin dijalankan : ''')
            if(menuIklan2 == '1'):
                userData(iklanAnda)
            elif(menuIklan2 == '0'):
                break
            else :
                print('\nPilih menu yang sesuai. Coba lagi')

    elif(menuIklan == '3'):
        while True:
            menuIklan3 = inputAngka('''
            1. Lihat Seluruh Data Produk dan Iklan Anda
            2. Lihat Data per SKU Produk
            0. Menu Utama
                               
            Masukkan Menu yang ingin dijalankan : ''')
            if(menuIklan3 == '1'):
                if iklanAnda:    
                    print('\nData Produk dan Iklan Anda\n')
                    printTabel(iklanAnda)
                else :
                    print('\nTidak ada data')
            elif(menuIklan3 == '2'):
                if iklanAnda:
                    skuTarget = input("Masukkan SKU produk yang ingin Anda lihat datanya: ").upper()
                    result = matchingData(iklanAnda, skuTarget)
                    if result:
                        printTabel(result)
                    else:
                        print(f'\nTidak ada data dengan SKU produk "{skuTarget}"')
                else :
                    print('\nTidak ada data')       
            elif(menuIklan3 == '0'):
                break
            else:
                print('\nPilih menu yang sesuai. Coba lagi')

    elif(menuIklan == '4'):
        while True:
            menuIklan4 = inputAngka('''
            1. Hapus Seluruh Data Produk dan Iklan Anda
            2. Hapus Data per SKU Produk
            0. Menu Utama
                               
            Masukkan Menu yang ingin dijalankan : ''')
            if(menuIklan4 == '1'):
                if iklanAnda:
                    print('\nData Produk dan Iklan Anda\n')
                    printTabel(iklanAnda)
                    while True:
                        konfirmasi = input('Anda yakin untuk menghapus seluruh data? (y/n)').upper()
                        if(konfirmasi == 'Y'):
                            iklanAnda.clear()
                            print('Seluruh data produk dan iklan Anda telah dihapus')
                            break
                        elif(konfirmasi == 'N') :
                            print('Penghapusan data dibatalkan')
                            break
                        else :
                            print('Silakan pilih y/n untuk konfirmasi')
                    if iklanAnda:
                        printTabel(iklanAnda)
                    else:
                        print("\nTidak ada data.")
                else :
                    print('\nTidak ada data')
            elif(menuIklan4 == '2'):
                if iklanAnda:
                    deleteSKU = input('Masukkan SKU produk yang ingin dihapus : ').upper()
                    if any(data[0].upper() == deleteSKU for data in iklanAnda):
                        while True :
                            konfirmSKU = input(f"Anda yakin ingin menghapus data dengan SKU produk '{deleteSKU}'? (y/n): ").upper()
                            if(konfirmSKU == 'Y') :
                                iklanAnda = [data for data in iklanAnda if data[0].upper() != deleteSKU]
                                print(f'Data dengan SKU produk "{deleteSKU}" telah dihapus.')
                                break
                            elif(konfirmSKU == 'N') :
                                print("Penghapusan data dibatalkan.")
                                break
                            else :
                                print('Silakan pilih y/n untuk konfirmasi')                           
                        if iklanAnda:
                            printTabel(iklanAnda)
                        else:
                            print("\nTidak ada data.")
                    else:
                        print(f"\nTidak ada data dengan SKU produk '{deleteSKU}'.")
                else :
                    print("\nTidak ada data.")
            elif(menuIklan4 == '0'):
                break
            else:
                print('\nPilih menu yang sesuai. Coba lagi')

    elif(menuIklan == '5') :
        while True:
            menuIklan5 = inputAngka('''
            1. Analisa Performa Iklan Saya
            2. Analisa Iklan Per SKU
            0. Menu Utama
                            
            Masukkan Menu yang ingin dijalankan : ''')
            if(menuIklan5 == '1') :
                if iklanAnda :
                    totalPenjualan = sum(int(data[4]) for data in iklanAnda)
                    totalBiayaIklan = sum(int(data[3]) for data in iklanAnda)
                    totalPersenAcos = 0.0 if totalPenjualan == 0 else round((totalBiayaIklan / totalPenjualan) * 100, 2)
                    totalPersenProfit = sum(data[5] for data in iklanAnda) / len(iklanAnda)

                    print("\nAnalisis Performa Iklan Saya")
                    print(f"Total Penjualan: {totalPenjualan}")
                    print(f"Total Biaya Iklan: {totalBiayaIklan}")
                    print(f"Persentase ACOS Keseluruhan: {totalPersenAcos}%")
                    print(f"Persentase Profit Keseluruhan: {totalPersenProfit}%")

                    printTabel(iklanAnda)

                    if totalPersenAcos == 0:
                        print("Iklan Anda belum menghasilkan penjualan sama sekali\nMulai setting kata kunci pada iklan pencarian Anda untuk mendapatkan trafik.")
                    elif totalPersenAcos > totalPersenProfit:
                        print("Iklan Anda Rugi (Boncos), pastikan kata kunci yang Anda masukkan relevan dengan produk Anda agar trafik berkualitas.\nPerhatikan biaya per klik dan hindari settingan otomatis agar performa setiap kata kunci dapat diperhatikan.")
                    elif totalPersenAcos >= totalPersenProfit - 5:
                        print("Iklan Anda berada di titik impas, hampir seluruh keuntungan Anda dialokasikan untuk iklan.\nRiset kata kunci baru dan hapus kata kunci yang tidak relevan atau tidak berpotensi menghasilkan penjualan.")
                    elif totalPersenAcos <= totalPersenProfit - 6:
                        print('Iklan Anda sudah bisa dikatakan efektif, lakukan maintenance iklan mingguan agar ACOS Anda stabil dan lakukan scale up secara bertahap dalam beriklan\nuntuk mendapatkan profit margin yang lebih besar.')
                else:
                    print("\nTidak ada data iklan untuk dianalisis.")

            elif(menuIklan5 == '2'):
                if iklanAnda :
                    skuTarget = input("Masukkan SKU produk yang ingin dianalisis: ").upper()
                    result = matchingData(iklanAnda, skuTarget)

                    if result:
                        print(f'\nAnalisis Performa Iklan SKU "{skuTarget}"')
                        print(f"Penjualan: {result[0][4]}")
                        print(f"Biaya Iklan: {result[0][3]}")
                        print(f"Persentase ACOS SKU {skuTarget}: {result[0][6]}%")
                        print(f"Persentase Profit SKU {skuTarget}: {result[0][5]}%")
                    
                        printTabel(result)

                        if result[0][6] == 0:
                            print(f"Iklan Anda untuk SKU {skuTarget} belum menghasilkan penjualan sama sekali\nMulai setting kata kunci pada iklan pencarian Anda untuk mendapatkan trafik.")       
                        elif result[0][6] > result[0][5]:
                            print(f"Iklan Anda untuk SKU {skuTarget} mengalami kerugian (Boncos), perhatikan biaya perklik dari setiap kata kunci.\nHindari settingan otomatis agar performa setiap kata kunci dapat diperhatikan.")
                        elif result[0][6] >= result[0][5] - 5:
                            print(f"Iklan Anda untuk SKU {skuTarget} berada di titik impas. Perhatikan biaya per-klik dari iklan Anda agar ACOS bisa lebih ditekan,\nhapus kata kunci yang tidak efektif dan masukkan kata kunci relevan yang berpotensi menghasilkan penjualan.")
                        elif result[0][6] <= result[0][5] - 6:
                            print(f"Iklan Anda untuk SKU {skuTarget} Sudah Efektif. Lakukan maintenance iklan mingguan agar ACOS Anda stabil\nLakukan scale up secara bertahap dalam beriklan untuk mendapatkan profit margin yang lebih besar.")
                    else:
                        print(f'\nTidak ada data iklan dengan SKU "{skuTarget}".')
                else:
                    print("\nTidak ada data iklan untuk dianalisis.")

            elif(menuIklan5 == '0'):
                break
            else:
                print('\nPilih menu yang sesuai. Coba lagi')

    elif(menuIklan == '6'):
        while True:
            menuIklan6 = inputAngka('''
            1. Simulasi Iklan
            2. Edit Data Simulasi
            0. Menu Utama
                            
            Masukkan Menu yang ingin dijalankan : ''')
            if(menuIklan6 == '1') :
                    print('\nMasukkan data simulasi Anda dibawah, data simulasi tidak akan merubah data asli.\n')
                    userData(simulasiAnda)

                    print(f'\nHasil simulasi iklan untuk SKU "{simulasiAnda[0][0]}":')
                    print(f'Persentase Profit Simulasi: {simulasiAnda[0][5]}%')
                    print(f'Persentase ACOS Simulasi: {simulasiAnda[0][6]}%\n')

                    if simulasiAnda[0][6] == 0:
                        print(f"Iklan Anda untuk SKU {simulasiAnda[0][0]} belum menghasilkan penjualan sama sekali\nMulai setting kata kunci pada iklan pencarian Anda untuk mendapatkan trafik.")       
                    elif simulasiAnda[0][6] > simulasiAnda[0][5]:
                        print(f"Iklan Anda untuk SKU {simulasiAnda[0][0]} mengalami kerugian (Boncos), perhatikan biaya perklik dari setiap kata kunci.\nHindari settingan otomatis agar performa setiap kata kunci dapat diperhatikan.")
                    elif simulasiAnda[0][6] >= simulasiAnda[0][5] - 5:
                        print(f"Iklan Anda untuk SKU {simulasiAnda[0][0]} berada di titik impas. Perhatikan biaya per-klik dari iklan Anda agar ACOS bisa lebih ditekan,\nhapus kata kunci yang tidak efektif dan masukkan kata kunci relevan yang berpotensi menghasilkan penjualan.")
                    elif simulasiAnda[0][6] <= simulasiAnda[0][5] - 6:
                        print(f"Iklan Anda untuk SKU {simulasiAnda[0][0]} Sudah Efektif. Lakukan maintenance iklan mingguan agar ACOS Anda stabil\nLakukan scale up secara bertahap dalam beriklan untuk mendapatkan profit margin yang lebih besar.")

            elif(menuIklan6 == '2'):
                if simulasiAnda:
                    print("\nData simulasi yang sudah disimpan:")
                    printTabel(simulasiAnda)

                    skuTarget = input("Masukkan SKU produk yang ingin diedit: ").upper()
                    result = matchingData(simulasiAnda, skuTarget)

                    if result:
                        print(f"\nData simulasi untuk SKU produk '{skuTarget}':")
                        printTabel(result)

                        dataSimulasi = result
                        simulasiHargaProduk = inputAngka('Masukkan harga jual baru untuk simulasi: ')          
                        simulasiProfitProduk = inputAngka('Masukkan jumlah profit baru untuk simulasi: ')
                        while not int(simulasiProfitProduk) < int(simulasiHargaProduk):
                            print('Profit tidak mungkin sama atau lebih besar dari harga jual. Coba lagi')
                            simulasiProfitProduk = inputAngka('Masukkan jumlah profit baru untuk simulasi: ')

                        simulasiBiayaIklan = inputAngka("Masukkan biaya iklan baru untuk simulasi: ")
                        simulasiPenjualan = inputAngka("Masukkan total penjualan baru untuk simulasi: ")
                        dataSimulasi[0][1] = simulasiHargaProduk
                        dataSimulasi[0][2] = simulasiProfitProduk
                        dataSimulasi[0][3] = simulasiBiayaIklan
                        dataSimulasi[0][4] = simulasiPenjualan
                        dataSimulasi[0][5] = round(int(simulasiProfitProduk) / int(simulasiHargaProduk) * 100, 2)
                        dataSimulasi[0][6] = 0.0 if simulasiPenjualan == '0' else round(int(simulasiBiayaIklan) / int(simulasiPenjualan) * 100, 2)

                        print("\nData simulasi berhasil diperbarui.")
                        print("\nData simulasi setelah diedit:")
                        printTabel(dataSimulasi)

                        print(f'\nHasil simulasi iklan untuk SKU "{dataSimulasi[0][0]}":')
                        print(f'Persentase Profit Simulasi: {dataSimulasi[0][5]}%')
                        print(f'Persentase ACOS Simulasi: {dataSimulasi[0][6]}%\n')


                        if dataSimulasi[0][6] == 0:
                            print(f"Iklan Anda untuk SKU {dataSimulasi[0][0]} belum menghasilkan penjualan sama sekali\nMulai setting kata kunci pada iklan pencarian Anda untuk mendapatkan trafik.")       
                        elif dataSimulasi[0][6] > dataSimulasi[0][5]:
                            print(f"Iklan Anda untuk SKU {dataSimulasi[0][0]} mengalami kerugian (Boncos), perhatikan biaya perklik dari setiap kata kunci.\nHindari settingan otomatis agar performa setiap kata kunci dapat diperhatikan.")
                        elif dataSimulasi[0][6] >= dataSimulasi[0][5] - 5:
                            print(f"Iklan Anda untuk SKU {dataSimulasi[0][0]} berada di titik impas. Perhatikan biaya per-klik dari iklan Anda agar ACOS bisa lebih ditekan,\nhapus kata kunci yang tidak efektif dan masukkan kata kunci relevan yang berpotensi menghasilkan penjualan.")
                        elif dataSimulasi[0][6] <= dataSimulasi[0][5] - 6:
                            print(f"Iklan Anda untuk SKU {dataSimulasi[0][0]} Sudah Efektif. Lakukan maintenance iklan mingguan agar ACOS Anda stabil\ndan scale up secara bertahap dalam beriklan untuk mendapatkan profit margin yang lebih besar.")
                    else:
                        print(f"\nTidak ada data simulasi untuk SKU produk '{skuTarget}'.")
                else:
                    print("\nBelum ada data simulasi yang disimpan.")
                    
            elif(menuIklan6 == '0'):
                break
            else:
                print('\nPilih menu yang sesuai. Coba lagi')

    elif(menuIklan == '0'):
        break
    else :
        print('\nPilih angka menu yang tersedia, pilihan menu hanya 0-6')
