class kendaraan:
    def __init__(self, nama):
        self.nama = nama
        print(f"sebuah kendaraan '{self.nama}' dibuat.")

    def maju(self):
        print(f"{self.nama} bergerak maju")

class mobil (kendaraan):
    def putar_ac(self):
        print(f"{self.nama}: ac dinyalakan, sejukk!")

print("--- membuat object mobil ---")
avanza = mobil("avanza")
avanza.maju()
avanza.putar_ac()

# contoh lain soalnya
#print("----------------------")
#mobil_2 = mobil("mercy")
#mobil_2.maju()
