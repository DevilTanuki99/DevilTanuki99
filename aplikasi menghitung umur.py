import datetime as dt

# -- Header --
print(6*'='  +  " APLIKASI MENGHITUNG UMUR " + 6*'=' + '\n')
nama = str(input("Masukkan nama anda : "))
tanggal = int(input("Tanggal Lahir \N: "))
bulan = int(input("Bulan Lahir\t : "))
tahun = int(input("Tahun Lahir\t : "))

# -- Fungsi --
lahir = dt.date(tahun,bulan,tanggal)
umur_1 = dt.date.today() - lahir
umur_2 = umur_1.days // 365
sisa = (umur_1.days % 365) // 31
online = dt.date.today() - lahir

# -- Output--
print('+' + 39*'-' + '+')
print(f"| Nama \t\t: {nama} \t|")
print(f"| Tanggal lahir : {lahir} \t\t|")
print(f"| Umur \t\t: {umur_2} Tahun {sisa} Bulan\t|")
print(f"| Online \t: {online} \t|")
print('+' + 39*'-' + '+')
