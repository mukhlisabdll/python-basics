# Latihan 1: Penanganan Kesalahan
# Mencoba mengonversi input menjadi integer dan menangani kesalahan jika input bukan angka.
try:
    num = int(input("Masukan angka: "))  # Meminta input dari pengguna dan mencoba mengonversinya ke integer.
    print(f"Anda memasukan angka {num}")  # Menampilkan angka yang berhasil dimasukkan.
except ValueError:
    print("Input bukan angka!")  # Pesan error jika input tidak dapat dikonversi ke integer.

# Latihan 2: Menangani Beberapa Kesalahan
# Menangani kesalahan pembagian dengan nol menggunakan blok try-except.
try: 
    num = 10 / 0  # Operasi pembagian dengan nol yang akan memicu ZeroDivisionError.
except ZeroDivisionError:
    print("Tidak bisa membagi dengan nol!")  # Menangani error untuk mencegah program berhenti.

# Latihan 3: Penanganan Kesalahan Pembagian
# Mengelola beberapa jenis kesalahan, seperti pembagian dengan nol dan input tidak valid.
try: 
    numerator = float(input("Masukan angka pembilang: "))  # Meminta input angka pembilang.
    detominator = float(input("Masukan angka penyebut: "))  # Meminta input angka penyebut.
    result = numerator / detominator  # Melakukan pembagian.
    print(f"Hasil pembagian: {result}")  # Menampilkan hasil jika tidak ada error.
except ZeroDivisionError:
    print("Kesalahan: Tidak bisa membagi dengan nol.")  # Menangani pembagian dengan nol.
except ValueError:
    print("Kesalahan: Input harus berupa angka.")  # Menangani input yang tidak valid.