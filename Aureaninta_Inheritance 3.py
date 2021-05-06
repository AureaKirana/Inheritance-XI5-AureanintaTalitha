#Aureaninta TNKP (XI MIPA 5/06)

# super class / parent class
class Manusia:
    # konstruktor
    def __init__(self, nama, jk, usia):
        self.nama = nama
        self.jk = jk
        self.usia = usia
    
    def info(self):
        print("Nama : {}\nJenis Kelamin : {}\nUsia : {}".format(self.nama, self.jk, self.usia))
        print("---------------------------")
    
    def tidur(self):
        print("Sedang tidur")
        print("---------------------------")
 
# sub class / child class
class Pelajar(Manusia):
    # konstruktor anak
    def __init__(self, nama, jk, usia, nis, nilai):
        Manusia.__init__(self, nama, jk, usia)
        self.nis = nis
        self.nilai = nilai
 
    def tidur(self):
        print("{} Sedang tidur".format(self.nama))
        print("---------------------------")
 
    # methode overriding
    def mandi(self):
        print("{} masih tidur dan tidak mau mandi". format(self.nama))
        print("---------------------------")
 
# sub class / child class
class Pekerja(Manusia):
    # konstruktor anak
    def __init__(self, nama, jk, usia, nip, gaji):
        Manusia.__init__(self, nama, jk, usia)
        self.nip = nip
        self.gaji = gaji
 
    def bekerja(self):
        print("{} sedang sibuk mengerjakan tugas".format(self.nama))
        print("---------------------------")
 
# instansiasi objek
Wawak = Pelajar("Najwa", "Perempuan", 16, "16158", 90)
Puput = Pekerja("Kanjeng Putri", "Perempuan", 22,"1", 100000000)
 
#pemanggilan
Wawak.info()
Wawak.tidur()
Wawak.mandi() #memanggil methode anak
Puput.info()
Puput.bekerja()
Puput.tidur() # memanggil methode induk
