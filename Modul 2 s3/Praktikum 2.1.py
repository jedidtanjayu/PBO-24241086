class RekeningBank:
    def __init__(self, nama, saldo):
        self.nama = nama
        self__privatesaldo = saldo 


akun_budi = RekeningBank("Budi", 1000000)
print(f"Saldo awal Budi: {akun_budi.saldo}")
try
    print(f"Saldo akhir Budi: {akun_budi.saldo}")
akun_budi.saldo = -5000000
print(f"Saldo akhir Budi: {akun_budi.saldo}")