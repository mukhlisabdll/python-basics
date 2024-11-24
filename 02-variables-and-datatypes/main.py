# Latihan 1: Variables
# Mendeklarasikan variabel dengan berbagai tipe data.
name = "Mukhlis"   # Tipe data string
age = 17           # Tipe data integer
height = 171.5     # Tipe data float

# Mencetak nilai variabel ke layar.
print(name, age, height)

# Latihan 2: Data Types
# Contoh variabel dengan berbagai tipe data dasar.
int_var = 19       # Integer
float_var = 3.14   # Float
str_var = "Hello"  # String
bool_var = True    # Boolean

# Mencetak tipe data dari setiap variabel.
print(type(int_var), type(float_var), type(str_var), type(bool_var))

# Latihan 3: Type Casting
# Mengonversi string ke integer menggunakan type casting.
num = "123"                    # Tipe data awal adalah string.
converted_num = int(num)       # Mengonversi ke integer.

# Mencetak hasil konversi dan tipe datanya.
print(converted_num, type(converted_num))

# Latihan 4: Calculator with Input
# Program kalkulator sederhana dengan input angka dari pengguna.

# Meminta input dua angka dari pengguna (dikonversi ke float).
num1 = float(input("Masukan angka pertama: "))
num2 = float(input("Masukan angka kedua: "))

# Menampilkan hasil operasi matematika (penjumlahan, pengurangan, perkalian, pembagian).
print(f"Hasil penjumlahan: {num1 + num2}")
print(f"Hasil pengurangan: {num1 - num2}")
print(f"Hasil perkalian: {num1 * num2}")
print(f"Hasil pembagian: {num1 / num2}")
