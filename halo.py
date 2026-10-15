# halo.py - program Python pertama
from datetime import date

nama = input("Masukkan nama Anda: ")
print(f"Halo, {nama}! Selamat datang di praktikum Python.")

tahun_lahir = int(input("Masukkan tahun lahir Anda: "))
usia = date.today().year - tahun_lahir
print(f"Perkiraan usia Anda saat ini {usia} tahun.")
print("Semoga sukses!")
