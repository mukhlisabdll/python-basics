# Latihan 1: List Basics
# List adalah struktur data yang dapat menyimpan berbagai elemen yang dapat diubah (mutable).
# Contoh list berisi nama buah.
fruits = ["apple", "banana", "cherry"]
print(fruits[0], fruits[-1])  # Mengakses elemen pertama dan terakhir dari list menggunakan indeks.

# Latihan 2: Tuple Basics
# Tuple adalah struktur data yang mirip dengan list tetapi bersifat tidak dapat diubah (immutable).
# Contoh tuple berisi warna.
colors = ("red", "green", "blue")
print(colors)  # Mencetak seluruh elemen tuple.

# Latihan 3: Dictionary Basics
# Dictionary adalah struktur data yang menyimpan pasangan key-value.
# Contoh dictionary untuk menyimpan informasi seseorang.
person = {"name": "Bernadhita", "age": 25}
print(person["name"])  # Mengakses nilai berdasarkan key "name".

# Latihan 4: Count Unique Words
# Menghitung jumlah kata unik dalam sebuah paragraf.
paragraph = input("Masukan sebuah paragraf: ").lower()  # Meminta input dari pengguna dan mengubahnya menjadi huruf kecil.
words = paragraph.split()  # Memecah paragraf menjadi list kata berdasarkan spasi.
unique_words = set(words)  # Menggunakan set untuk mendapatkan kata-kata unik (tidak ada duplikat).

# Menampilkan jumlah dan daftar kata unik.
print(f"Jumlah kata unik: {len(unique_words)}")  # Menghitung jumlah kata unik.
print(f"Kata-kata unik: {unique_words}")  # Menampilkan kata-kata unik.
