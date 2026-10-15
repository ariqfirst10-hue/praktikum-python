# halo.py - program Python pertama
from datetime import date

nama = input("Masukkan nama Anda: ")
print(f"Halo, {nama}! Selamat datang di praktikum Python.")

tahun_ini = date.today().year
while True:
    try:
        tahun_lahir = int(input("Masukkan tahun lahir Anda: "))
    except ValueError:
        print("Input tidak valid. Masukkan tahun lahir dalam bentuk angka, contoh: 2004.")
        continue
    if tahun_lahir < 1900 or tahun_lahir > tahun_ini:
        print(f"Tahun lahir harus antara 1900 dan {tahun_ini}.")
        continue
    break

usia = tahun_ini - tahun_lahir
print(f"Perkiraan usia Anda saat ini {usia} tahun.")
print("Semoga sukses!")
