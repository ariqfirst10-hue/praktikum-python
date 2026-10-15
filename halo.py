# halo.py - program Python pertama
from datetime import date

from colorama import Fore, Style, init

init(autoreset=True)

nama = input("Masukkan nama Anda: ")
print(Fore.GREEN + f"Halo, {nama}! Selamat datang di praktikum Python.")

tahun_ini = date.today().year
while True:
    try:
        tahun_lahir = int(input("Masukkan tahun lahir Anda: "))
    except ValueError:
        print(Fore.RED + "Input tidak valid. Masukkan tahun lahir dalam bentuk angka, contoh: 2004.")
        continue
    if tahun_lahir < 1900 or tahun_lahir > tahun_ini:
        print(Fore.RED + f"Tahun lahir harus antara 1900 dan {tahun_ini}.")
        continue
    break

usia = tahun_ini - tahun_lahir
print(Fore.CYAN + Style.BRIGHT + f"Perkiraan usia Anda saat ini {usia} tahun.")
print(Fore.YELLOW + "Semoga sukses!")
