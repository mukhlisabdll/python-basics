# Latihan 1: Menulis File
# Membuka file dalam mode tulis ('w') untuk menulis teks ke dalam file.
# Jika file tidak ada, file akan dibuat secara otomatis.
with open('file/example.txt', 'w') as file:
    file.write("Halo, nama saya Mukhlis Abdillah. Saya umur 17 tahun. ")  # Menulis teks ke dalam file.

# Latihan 2: Membaca File
# Membuka file dalam mode baca ('r') untuk membaca isinya.
with open('file/example.txt', 'r') as file:
    teks = file.read()  # Membaca seluruh isi file ke dalam variabel teks.
    print(teks)  # Menampilkan isi file ke layar.

# Latihan 3: Menghitung Jumlah Kata dalam File
# Menghitung jumlah kata dalam file dengan pemrosesan tambahan.
try:
    with open('file/example.txt', 'r') as file:
        teks = file.read()  # Membaca isi file.
        words = teks.split()  # Memisahkan teks menjadi daftar kata berdasarkan spasi.
        print(f"Jumlah kata dalam file: {len(words)}")  # Menampilkan jumlah kata.
except FileNotFoundError:
    # Menangani kasus di mana file tidak ditemukan.
    print("File tidak ditemukan. Pastikan file berada di direktori yang benar.")
