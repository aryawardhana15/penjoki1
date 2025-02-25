def manajemen_inventaris():
    print("\n=== Manajemen Inventaris ===")
    stok_minimum = int(input("Masukkan stok minimum: "))
    stok_maksimum = int(input("Masukkan stok maksimum: "))
    stok_sekarang = int(input("Masukkan stok saat ini: "))

    if stok_sekarang <= stok_minimum:
        jumlah_pesanan = stok_maksimum - stok_sekarang
        print(f"Stok hampir habis! Pesan {jumlah_pesanan} unit.")
    else:
        print("Stok aman, tidak perlu memesan.")

def analisis_break_even():
    print("\n=== Analisis Break-Even Point ===")
    biaya_tetap = float(input("Masukkan biaya tetap (dalam USD): "))
    biaya_variabel = float(input("Masukkan biaya variabel per unit (dalam USD): "))
    harga_jual = float(input("Masukkan harga jual per unit (dalam USD): "))

    break_even_point = biaya_tetap / (harga_jual - biaya_variabel)
    print(f"Break-even point: {break_even_point:.2f} unit")

def prediksi_inflasi():
    print("\n=== Prediksi Inflasi ===")
    inflasi_tahun_sebelumnya = list(map(float, input("Masukkan data inflasi tahun-tahun sebelumnya (pisahkan dengan spasi, contoh: 3.5 4.0 3.8): ").split()))
    jumlah_tahun = len(inflasi_tahun_sebelumnya)
    rata_rata_inflasi = sum(inflasi_tahun_sebelumnya) / jumlah_tahun
    print(f"Prediksi inflasi tahun depan: {rata_rata_inflasi:.2f}%")

def main():
    while True:
        print("\n=== Program Gabungan ===")
        print("1. Manajemen Inventaris")
        print("2. Analisis Break-Even Point")
        print("3. Prediksi Inflasi")
        print("4. Keluar")
        pilihan = input("Pilih menu (1/2/3/4): ")

        if pilihan == "1":
            manajemen_inventaris()
        elif pilihan == "2":
            analisis_break_even()
        elif pilihan == "3":
            prediksi_inflasi()
        elif pilihan == "4":
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()