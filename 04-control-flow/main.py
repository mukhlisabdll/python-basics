# Latihan 1: If-Else
# Program untuk menentukan kelulusan berdasarkan nilai.
score = 75  # Nilai yang akan diperiksa.

# Jika nilai >= 60, maka "Lulus", jika tidak, "Tidak Lulus".
if score >= 60:
    print("Lulus")
else:
    print("Tidak Lulus")

# Latihan 2: For Loop
# Program mencetak angka 1 sampai 5 menggunakan perulangan for.
for i in range(1, 6):  # range(1, 6) menghasilkan angka 1 hingga 5.
    print(i)

# Latihan 3: While Loop
# Program mencetak angka dari 5 hingga 1 menggunakan perulangan while.
x = 5  # Inisialisasi nilai awal.
while x > 0:  # Loop akan terus berjalan selama x > 0.
    print(x)
    x -= 1  # Mengurangi nilai x sebesar 1 setiap iterasi.

# Latihan 4: Number Guessing Game
# Program permainan tebak angka sederhana.

import random  # Mengimpor modul untuk menghasilkan angka acak.
print("=== Game Tebak Angka ===")

# Menghasilkan angka acak antara 1 hingga 10.
number_to_guess = random.randint(1, 10)
attempts = 0  # Menghitung jumlah percobaan.
max_attempts = 5  # Batas maksimum percobaan.

# Perulangan untuk memberikan kesempatan menebak hingga batas maksimum.
while attempts < max_attempts:
    guess = int(input("Tebak angka antara 1 sampai 10: "))  # Input tebakan.
    attempts += 1  # Menambah jumlah percobaan.

    # Memeriksa tebakan pengguna.
    if guess == number_to_guess:
        print("Selamat! Anda menebak dengan benar!")
        break  # Keluar dari loop jika tebakan benar.
    elif guess < number_to_guess:
        print("Terlalu kecil!")
    else:
        print("Terlalu besar!")

# Jika batas percobaan tercapai dan angka belum ditebak.
if attempts == max_attempts and guess != number_to_guess:
    print(f"Maaf, Anda kehabisan kesempatan. Angka yang benar adalah {number_to_guess}")
