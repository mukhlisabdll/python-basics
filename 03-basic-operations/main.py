# Latihan 1: Math Operations
# Operasi matematika dasar dengan dua variabel.
a = 10  # Nilai variabel pertama.
b = 5   # Nilai variabel kedua.

# Mencetak hasil operasi penjumlahan, pengurangan, perkalian, dan pembagian.
print(a + b, a - b, a * b, a / b)

# Latihan 2: Logical Operations
# Operasi logika dasar dengan dua variabel boolean.
x = True   # Nilai boolean pertama.
y = False  # Nilai boolean kedua.

# Mencetak hasil operasi logika AND, OR, dan NOT.
print(x and y, x or y, not x)

# Latihan 3: String Operations
# Operasi dasar pada string, seperti mengubah huruf menjadi kapital atau kecil.
name = "Bernadhita"  # Nama sebagai string.

# Mencetak hasil string dalam huruf kapital, huruf kecil, dan panjang string.
print(name.upper(), name.lower(), len(name))

# Latihan 4: String Analysis
# Program untuk menganalisis sebuah kalimat yang dimasukkan pengguna.
sentence = input("Masukan sebuah kalimat: ")  # Meminta input kalimat dari pengguna.

# Menghitung jumlah huruf (tanpa spasi) dalam kalimat.
letter_count = len(sentence.replace(" ", ""))

# Menghitung jumlah kata dalam kalimat berdasarkan pemisahan spasi.
word_count = len(sentence.split())

# Menghitung jumlah huruf vokal dalam kalimat.
vowels = "aeiouAEIOU"  # Daftar huruf vokal (kapital dan kecil).
vowels_count = sum(1 for char in sentence if char in vowels)

# Mencetak hasil analisis kalimat: jumlah huruf, kata, dan huruf vokal.
print(f"Jumlah huruf: {letter_count}")
print(f"Jumlah kata: {word_count}")
print(f"Jumlah huruf vokal: {vowels_count}")
