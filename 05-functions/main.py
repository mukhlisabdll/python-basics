# Latihan 1: Basic Functions
# Fungsi sederhana tanpa parameter.
def greet():
    print("Hello, Bernadhita!")  # Mencetak sapaan.
greet()  # Memanggil fungsi greet.

# Latihan 2: Functions with Parameter
# Fungsi dengan parameter untuk menerima input nama.
def greet(name):
    print(f"Hello, {name}!")  # Mencetak sapaan menggunakan parameter name.
greet("Mukhlis")  # Memanggil fungsi dengan argumen "Mukhlis".

# Latihan 3: Return Values
# Fungsi untuk menjumlahkan dua angka dan mengembalikan hasilnya.
def add(a, b):
    return a + b  # Mengembalikan hasil penjumlahan a dan b.
print(add(10, 9))  # Mencetak hasil fungsi add dengan argumen 10 dan 9.

# Latihan 4: Fibbonacci Function
# Fungsi untuk menghasilkan deret Fibbonacci hingga jumlah elemen tertentu.
def fibbonacci(n):
    fib_sequence = [0, 1]  # Inisialisasi dua angka pertama dalam deret.
    while len(fib_sequence) < n:  # Menambah elemen ke deret hingga panjangnya mencapai n.
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])  # Menambahkan elemen baru sebagai jumlah dua elemen terakhir.
    return fib_sequence  # Mengembalikan deret Fibbonacci.

# Meminta input jumlah bilangan Fibbonacci yang diinginkan.
n = int(input("Masukan jumlah bilangan Fibbonacci yang diinginkan: "))

# Mencetak deret Fibbonacci yang dihasilkan oleh fungsi.
print(f"Deret Fibbonacci: {fibbonacci(n)}")
