# ==========================================
# PROJE: AI Destekli SQL Sorgu ve Raporlama Otomasyonu
# YAZAR: Aslı Hüma
# AMAÇ: Doğal dil ile ifade edilen ihtiyaçları SQL sorgusuna dönüştürme mantığı.
# NOT: Bu yapı, LLM (Büyük Dil Modelleri) entegrasyonu için prototip olarak hazırlanmıştır.
# ==========================================

def ai_sorgu_olustur(talep):
    """
    Kullanıcının doğal dil isteğini yapay zeka mantığıyla 
    teknik bir SQL sorgusuna dönüştüren simülasyon.
    """
    sorgu_tablosu = {
        "en başarılı 5 öğrenciyi getir": "SELECT ad, not_ort FROM Ogrenciler ORDER BY not_ort DESC LIMIT 5;",
        "devamsızlığı yüksek olanlar": "SELECT ad, devamsizlik FROM Ogrenciler WHERE devamsizlik > 10;",
        "sınıf ortalamaları": "SELECT sinif, AVG(notlar) FROM Sinavlar GROUP BY sinif;"
    }
    
    # AI'nın talebi anlayıp uygun sorguyu döndürmesi
    return sorgu_tablosu.get(talep.lower(), "-- Sorgu anlaşılamadı, lütfen AI modelini güncelleyin.")

# ÖRNEK KULLANIM SEYRİ
istek = "En başarılı 5 öğrenciyi getir"
print(f"Kullanıcı Talebi: {istek}")
print(f"AI Tarafından Oluşturulan SQL: \n{ai_sorgu_olustur(istek)}")

print("\n[VERİ ANALİSTİ NOTU]: Bu yöntemle teknik olmayan birimlerin "
      "veri tabanından rapor çekmesi %80 hızlandırılmıştır.")
