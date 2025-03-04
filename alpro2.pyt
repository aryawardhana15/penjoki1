import math

def hitung_kubus():
    print("\n=== KUBUS ===")
    sisi = float(input("Masukkan panjang sisi kubus: "))
    volume = sisi ** 3
    luas_permukaan = 6 * (sisi ** 2)
    print(f"Volume Kubus: {volume}")
    print(f"Luas Permukaan Kubus: {luas_permukaan}")

def hitung_balok():
    print("\n=== BALOK ===")
    panjang = float(input("Masukkan panjang balok: "))
    lebar = float(input("Masukkan lebar balok: "))
    tinggi = float(input("Masukkan tinggi balok: "))
    volume = panjang * lebar * tinggi
    luas_permukaan = 2 * ((panjang * lebar) + (panjang * tinggi) + (lebar * tinggi))
    print(f"Volume Balok: {volume}")
    print(f"Luas Permukaan Balok: {luas_permukaan}")

def hitung_bola():
    print("\n=== BOLA ===")
    jari_jari = float(input("Masukkan jari-jari bola: "))
    volume = (4/3) * math.pi * (jari_jari ** 3)
    luas_permukaan = 4 * math.pi * (jari_jari ** 2)
    print(f"Volume Bola: {volume}")
    print(f"Luas Permukaan Bola: {luas_permukaan}")

def main():
    while True:
        print("\n=== PROGRAM PERHITUNGAN BANGUN RUANG BY ADHI ===")
        print("Pilih bangun ruang:")
        print("1. Kubus")
        print("2. Balok")
        print("3. Bola")
        print("4. Keluar")
        pilihan = input("Masukkan pilihan (1/2/3/4): ")

        if pilihan == '1':
            hitung_kubus()
        elif pilihan == '2':
            hitung_balok()
        elif pilihan == '3':
            hitung_bola()
        elif pilihan == '4':
            print("Terima kasih telah menggunakan program ini. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()