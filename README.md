# praktikum-python

Proyek praktikum Pemrograman Berorientasi Objek: program Python pertama,
virtual environment, dan repositori Git. Berisi `halo.py` (sapaan dan
perkiraan usia dari tahun lahir) dan `tampil.py` (tabel dengan paket rich).

## Membuat dan mengaktifkan virtual environment

Windows (PowerShell):

    py -m venv .venv
    .venv\Scripts\Activate.ps1

Windows (Command Prompt): `.venv\Scripts\activate.bat`

macOS / Linux:

    python3 -m venv .venv
    source .venv/bin/activate

Environment aktif jika prompt diawali `(.venv)`. Nonaktifkan dengan `deactivate`.

## Menginstal dependensi

    pip install -r requirements.txt

## Menjalankan program

    python halo.py
    python tampil.py

(Windows dapat memakai `py` sebagai pengganti `python`.)
