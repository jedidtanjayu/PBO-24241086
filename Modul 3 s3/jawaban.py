# JAWABAN P1
# Pertanyaan & Jawaban:

# 1. Dari kode di atas, mana class induk (parent) dan mana class anak (child)?
#    -> Class induk (parent)  : Kendaraan
#    -> Class anak (child)    : Mobil (karena Mobil mewarisi Kendaraan)

# 2. Buat objek dari class Kendaraan!
#    -> Contoh:
#         motor = Kendaraan("Motor Mio")

# 3. Apakah objek yang dibuat dari class Kendaraan bisa mengakses method putar_AC()?
#    -> Tidak bisa.
#    -> Karena method putar_AC() hanya dimiliki oleh class Mobil, 
#       sedangkan class Kendaraan tidak punya fitur AC.

# 4. Apakah objek yang dibuat dari class Mobil bisa mengakses method maju()?
#    -> Ya, bisa.
#    -> Karena Mobil mewarisi semua method dari Kendaraan,
#       sehingga method maju() otomatis dimiliki oleh Mobil.

# 5. Mengapa pada class Mobil tidak perlu dibuat konstruktor?
#    -> Karena Mobil sudah mewarisi konstruktor (__init__) dari Kendaraan.
#    -> Selama class Mobil tidak perlu menambah atribut baru saat objek dibuat,
#       maka konstruktor parent sudah cukup untuk digunakan.
#    -> Konstruktor parent akan otomatis dijalankan ketika objek Mobil dibuat.



# JAWABAN P2
# Pertanyaan:
# 1. Apa yang terjadi jika super().__init__(nama) dihapus?
#    -> Jika baris tersebut dihapus, maka konstruktor parent (Kendaraan.__init__) tidak akan dijalankan.
#    -> Akibatnya atribut self.nama TIDAK dibuat, karena atribut itu didefinisikan di parent.
#    -> Objek Mobil tetap dibuat, tetapi tidak memiliki atribut 'nama'.

# 2. Jika error, apa penyebabnya?
#    -> Error yang muncul biasanya: AttributeError: 'Mobil' object has no attribute 'nama'
#    -> Penyebabnya: parent __init__ tidak dipanggil, sehingga atribut 'nama' tidak pernah diinisialisasi.

# 3. Apakah super() bisa dipakai child untuk memanggil method parent?
#    -> Ya, super() memang digunakan untuk memanggil method milik parent class.
#    -> Contohnya: super().maju() atau super().__init__(...)
#    -> super() membantu child menggunakan fitur parent tanpa menulis ulang kodenya.


# JAWABAN P3
# Pertanyaan:
# 1. Apa yang di-override oleh child class?
#    -> Child class (Hero_intelligent) melakukan override pada method showInfo().
#    -> Artinya, method showInfo() milik parent (Hero) diganti dengan versi baru
#       yang khusus untuk Hero_intelligent.

# 2. Jika kita ingin menggunakan method showInfo() pada parent class,
#    apa yang harus dilakukan?
#    -> Gunakan super().showInfo()
#    -> Contoh:
#         def showInfo(self):
#             super().showInfo()   # memanggil method showInfo milik parent
#             print("Info tambahan di subclass")


# JAWABAN P4
# Pertanyaan:
# Apa yang terjadi jika Ayah dan Ibu sama-sama punya method bernama mengasuh()?
# Versi siapa yang akan dipakai oleh Anak?

# Jawaban:
# -> Jika Ayah dan Ibu sama-sama memiliki method mengasuh(),
#    maka class Anak akan memakai method dari class yang
#    berada di urutan pertama pada pewarisan (class Anak(Ayah, Ibu)).
#
# -> Artinya, karena penulisan class Anak adalah:
#         class Anak(Ayah, Ibu)
#    maka method mengasuh() yang dipakai adalah milik Ayah.
#
# -> Ini terjadi karena Python mengikuti aturan MRO (Method Resolution Order),
#    yaitu mencari method dari kiri ke kanan pada daftar pewarisan.
#
# Kesimpulan:
# -> Yang dipakai = method mengasuh() milik Ayah.
