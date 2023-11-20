import os

def main():
    while True:
  
        bil = []
        for i in range(5):
            angka = int(input(f"Masukkan angka ke-{i+1}: "))
            bil.append(angka)


        pilihan = input("Pilih pengurutan (ascending / descending): ").lower()


        if pilihan == 'ascending':
            bil.sort()
        elif pilihan == 'descending':
            bil.sort(reverse=True)
        else:
            print("Pilihan tidak valid. Silakan masukkan 'ascending' atau 'descending'.")
            continue


        angkabesar = max(bil)
        angkakecil = min(bil)
        rata = sum(bil) / len(bil)

        print("\nHasil pengurutan:", bil)
        print("Angka Terbesar =", angkabesar)
        print("Angka Terkecil =", angkakecil)
        print("Nilai Rata-rata =", rata)


        ulang = input("Apakah Anda ingin mengulangi program? (yes/no): ").lower()
        os.system ("clear")
        if ulang != 'yes':
            continue
        elif ulang == 'no':
          print("\nTerima kasih telah menggunakan layanan kami.")
          break

if __name__ == "__main__":
    main()