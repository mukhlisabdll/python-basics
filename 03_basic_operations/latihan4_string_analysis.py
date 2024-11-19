sentence = input("Masukan sebuah kalimat: ")

letter_count = len(sentence.replace(" ",""))
word_count = len(sentence.split())
vowels = "aeiouAEIOU"
vowels_count = sum(1 for char in sentence if char in vowels)

print(f"Jumlah huruf: {letter_count}")
print(f"Jumlah kata: {word_count}")
print(f"Jumlah huruf vokal: {vowels_count}")