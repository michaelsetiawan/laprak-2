

gaji = float(input("Masukkan gaji per jam"))
jam = float(input("Total jam kerja"))
total_minggu = 5
pajak = 14/100

gaji_kotor = gaji * jam * total_minggu
gaji_bersih = gaji_kotor - gaji_kotor * pajak

baju = gaji_bersih * 10/100
alat_tulis = gaji_bersih * 1/100
sedekah = (gaji_bersih*89/100)  * 25/100
anak_yatim = (sedekah//1000) * 30/100
anak_dhuafa = (sedekah//100) * 70/100

print(gaji_kotor)
print(gaji_bersih)
print(baju)
print(sedekah)
print(anak_yatim)
print(anak_dhuafa)

