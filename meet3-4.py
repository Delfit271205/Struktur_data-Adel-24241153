def hitung_luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi

def gambar_segitiga(tinggi):
    for i in range(1, tinggi + 1):
        print(' ' * (tinggi - i) + '*' * (2 * i - 1))

alas = int(input("Masukkan alas segitiga: "))
tinggi = int(input("Masukkan tinggi segitiga: "))


luas = hitung_luas_segitiga(alas, tinggi)
print(f"\nLuas segitiga adalah: {luas:.2f}\n")

print("Gambar segitiga:")
gambar_segitiga(tinggi)