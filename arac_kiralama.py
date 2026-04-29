from abc import ABC, abstractmethod

# --- ENTITIES BÖLÜMÜ ---

# Parent Class: Arac (Abstract class!)
class Arac(ABC):
    def __init__(self, plaka, marka, model):
        self.plaka = plaka
        self.marka = marka
        self.model = model
        self.musait = True  # musait=True: Kiralanabilir, musait=False: Kiralanmış

    @abstractmethod
    def gunluk_ucret(self):
        """Her araç tipinde farklı değer döndürmeli"""
        pass

    def kirala(self):
        """Araç kiralandığında musait durumunu False yap"""
        if self.musait:
            self.musait = False
            return True
        return False

    def bilgileri_goster(self):
        """Araç bilgilerini ekrana yazdır"""
        durum = "Müsait" if self.musait else "Kiralanmış"
        print(f"Plaka: {self.plaka:12} | Marka: {self.marka:10} | Model: {self.model:10} | "
              f"Ücret: {self.gunluk_ucret():4} TL | Durum: {durum}")

# Child Classes (Her biri Arac'tan miras alır)
class Binek(Arac):
    def __init__(self, plaka, marka, model):
        # super().__init__() ile parent constructor çağrılmalı
        super().__init__(plaka, marka, model)

    def gunluk_ucret(self):
        return 1000

class Ticari(Arac):
    def __init__(self, plaka, marka, model):
        super().__init__(plaka, marka, model)

    def gunluk_ucret(self):
        return 1500

class Lux(Arac):
    def __init__(self, plaka, marka, model):
        super().__init__(plaka, marka, model)

    def gunluk_ucret(self):
        return 3000


# --- KULLANICI MENÜSÜ (main.py mantığı) ---

def ana_menu():
    # Başlangıç için örnek araçlar listesi
    arac_listesi = [
        Binek("34 ABC 123", "Toyota", "Corolla"),
        Ticari("35 XYZ 789", "Ford", "Transit"),
        Lux("06 LUX 001", "Mercedes", "S-Class"),
        Binek("34 DEF 456", "Renault", "Clio"),
        Ticari("16 TIC 016", "Fiat", "Doblo")
    ]

    while True:
        print("\n--- ARAÇ KİRALAMA SİSTEMİ ---")
        print("1. Kiralanabilir araçları listele")
        print("2. Araç kirala (plaka girerek)")
        print("3. Toplam günlük gelir hesapla (kiralanan araçlar)")
        print("4. Çıkış")
        
        secim = input("Seçiminiz (1-4): ")

        if secim == "1":
            print("\n--- KİRALANABİLİR ARAÇLAR ---")
            sayac = 0
            for arac in arac_listesi:
                if arac.musait:
                    arac.bilgileri_goster()
                    sayac += 1
            if sayac == 0:
                print("Müsait araç bulunmamaktadır.")

        elif secim == "2":
            hedef_plaka = input("Plaka girin: ").strip().upper()
            bulundu = False
            for arac in arac_listesi:
                if arac.plaka.upper() == hedef_plaka:
                    bulundu = True
                    if arac.kirala():
                        print(f"BAŞARILI: {hedef_plaka} kiralandı.")
                    else:
                        print(f"HATA: Bu araç zaten kiralanmış.")
                    break
            if not bulundu:
                print(f"HATA: Plaka bulunamadı.")

        elif secim == "3":
            toplam_gelir = sum(arac.gunluk_ucret() for arac in arac_listesi if not arac.musait)
            print(f"\nToplam Günlük Gelir: {toplam_gelir} TL")

        elif secim == "4":
            print("Çıkılıyor...")
            break
        else:
            print("Geçersiz seçim!")

if __name__ == "__main__":
    ana_menu()
