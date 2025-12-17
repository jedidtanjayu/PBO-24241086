class Mahasiswa: 
    def __init__(self, name, nim, prodi): 
        self.name = name 
        self.nim = nim
        self.prodi = prodi


mhs1 = Mahasiswa("algi", "24241109", "PTI")
mhs2 = Mahasiswa("calgi", "24240911", "Sistem Informasi")


print("Nama:", mhs1.name)
print("NIM:", mhs1.nim)
print("Prodi:", mhs1.prodi)
print(mhs1.__dict__) 
print()
print("Nama:", mhs2.name)
print("NIM:", mhs2.nim)
print("Prodi:", mhs2.prodi)
print(mhs2.__dict__)