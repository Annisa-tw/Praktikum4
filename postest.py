class LoginKasir:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def validasiLogin(self):
        pass

    def logout(self):
        pass


class KoneksiDatabase:
    def __init__(self, host, database, userName, password):
        self.host = host
        self.database = database
        self.userName = userName
        self.password = password

    def membukaKoneksi(self):
        pass

    def eksekusiQuerySelect(self):
        pass

    def eksekusiQueryInsert(self):
        pass

    def eksekusiQueryUpdate(self):
        pass

    def eksekusiQueryDelete(self):
        pass

    def tutupKoneksi(self):
        pass


class HitungPembayaran:
    def __init__(self, idMenu, namaMenu, harga, jumlah, totalHarga):
        self.idMenu = idMenu
        self.namaMenu = namaMenu
        self.harga = harga
        self.jumlah = jumlah
        self.totalHarga = totalHarga

    def insertPembayaran(self):
        pass

    def updatePembayaran(self):
        pass

    def deletePembayaran(self):
        pass

    def cariDataPembayaranByIdMenu(self):
        pass


class TabelHitungPembayaran:
    def __init__(self, idMenu, namaMenu, harga, jumlah, totalHarga):
        self.idMenu = idMenu
        self.namaMenu = namaMenu
        self.harga = harga
        self.jumlah = jumlah
        self.totalHarga = totalHarga

    def setIdMenu(self):
        pass

    def getIdMenu(self):
        pass

    def setNamaMenu(self):
        pass

    def getNamaMenu(self):
        pass

    def setHarga(self):
        pass

    def getHarga(self):
        pass

    def setJumlah(self):
        pass

    def getJumlah(self):
        pass

    def setTotalHarga(self):
        pass

    def getTotalHarga(self):
        pass


class PembayaranTunai:
    def hitungTotalHarga(self):
        pass


class PembayaranByCard:
    def hitungTotalHarga(self):
        pass


class TabelPembayaranByCard:
    def __init__(self, idCard, jenisCard, namaBank, totalHarga):
        self.idCard = idCard
        self.jenisCard = jenisCard
        self.namaBank = namaBank
        self.totalHarga = totalHarga

    def setIdCard(self):
        pass

    def getIdCard(self):
        pass

    def setJenisCard(self):
        pass

    def getJenisCard(self):
        pass

    def setNamaBank(self):
        pass

    def getNamaBank(self):
        pass

    def setTotalHarga(self):
        pass

    def getTotalHarga(self):
        pass


class CetakStruk:
    def cetakStruk(self):
        pass


class TCetakStruk:
    def __init__(self, noStruk, totalHarga):
        self.noStruk = noStruk
        self.totalHarga = totalHarga
