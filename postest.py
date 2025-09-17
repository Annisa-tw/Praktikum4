# kasir_app.py

class Main:
    def main(self):
        pass

    def uiLogin(self):
        pass

    def uiMenu(self):
        pass

    def uiHitungPembayaran(self):
        pass

    def uiCetakStruk(self):
        pass


class LoginKasir:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    def validasiLogin(self):
        pass

    def logout(self):
        pass


class KoneksiDatabase:
    def __init__(self, host: str, database: str, username: str, password: str):
        self.host = host
        self.database = database
        self.username = username
        self.password = password

    def membukaKoneksi(self): pass
    def eksekusiQuerySelect(self): pass
    def eksekusiQueryInsert(self): pass
    def eksekusiQueryUpdate(self): pass
    def eksekusiQueryDelete(self): pass
    def tutupKoneksi(self): pass


class HitungPembayaran:
    def __init__(self, idMenu: str, namaMenu: str, harga: float, jumlah: int, totalHarga: float):
        self.idMenu = idMenu
        self.namaMenu = namaMenu
        self.harga = harga
        self.jumlah = jumlah
        self.totalHarga = totalHarga

    def insertPembayaran(self): pass
    def updatePembayaran(self): pass
    def deleteDataPembayaran(self): pass
    def cariDataPembayaranByIdMenu(self): pass


class PembayaranTunai:
    def hitungTotalHarga(self):
        pass


class PembayaranByCard:
    def hitungTotalHarga(self):
        pass


class CetakStruk:
    def cetakStruk(self):
        pass


class TabelHitungPembayaran:
    def __init__(self, idMenu: str, namaMenu: str, harga: float, jumlah: int, totalHarga: float):
        self.idMenu = idMenu
        self.namaMenu = namaMenu
        self.harga = harga
        self.jumlah = jumlah
        self.totalHarga = totalHarga

    def setIdMenu(self, idMenu): pass
    def getIdMenu(self): pass
    def setNamaMenu(self, namaMenu): pass
    def getNamaMenu(self): pass
    def setHarga(self, harga): pass
    def getHarga(self): pass
    def setJumlah(self, jumlah): pass
    def getJumlah(self): pass
    def setTotalHarga(self, totalHarga): pass
    def getTotalHarga(self): pass


class TabelPembayaranByCard:
    def __init__(self, idCard: str, jenisCard: str, namaBank: str, totalHarga: float):
        self.idCard = idCard
        self.jenisCard = jenisCard
        self.namaBank = namaBank
        self.totalHarga = totalHarga

    def setIdCard(self, idCard): pass
    def getIdCard(self): pass
    def setJenisCard(self, jenisCard): pass
    def getJenisCard(self): pass
    def setNamaBank(self, namaBank): pass
    def getNamaBank(self): pass
    def setTotalHarga(self, totalHarga): pass
    def getTotalHarga(self): pass


class CetakStrukDetail:
    def __init__(self, noStruk: str, totalHarga: float):
        self.noStruk = noStruk
        self.totalHarga = totalHarga


# =============================
# Buat objek dari setiap class
# =============================
if __name__ == "__main__":
    app = Main()
    kasir = LoginKasir("admin", "123")
    db = KoneksiDatabase("localhost", "dbkasir", "root", "")
    hitung = HitungPembayaran("M001", "Nasi Goreng", 15000, 2, 30000)
    bayarTunai = PembayaranTunai()
    bayarCard = PembayaranByCard()
    cetak = CetakStruk()
    tabelHitung = TabelHitungPembayaran("M001", "Nasi Goreng", 15000, 2, 30000)
    tabelCard = TabelPembayaranByCard("C001", "Debit", "BCA", 30000)
    detailStruk = CetakStrukDetail("S001", 30000)

    print("✅ Semua objek berhasil dibuat sesuai class diagram!")
