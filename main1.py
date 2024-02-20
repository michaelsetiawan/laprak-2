

# Pertama, minta inputan berupa bmi dan berat badan
# dari pengguna

bmi = float(input("Masukkan BMI: "))
berat = float(input("Masukkan berat badan Anda: "))

# Proses perhintungan:
# Karena rumus BMI = berat / tinggi^2,
# maka tinggi bisa dicari dengan: akar dari BMI/berat

tinggi = bmi / berat
tinggi = tinggi**(0.5)

print(f"Tinggi badan Anda: {tinggi} ")