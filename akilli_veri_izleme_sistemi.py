# ==========================================
# PROJE: Akıllı Veri İzleme ve AI Bildirim Sistemi
# YAZAR: Aslı Hüma
# AMAÇ: Kritik veri değişimlerini AI yardımıyla anlık olarak tespit etmek.
# ==========================================

import pandas as pd

# 1. CANLI VERİ AKIŞI SİMÜLASYONU
veriler = {
    'Zaman': ['10:00', '10:05', '10:10', '10:15', '10:20'],
    'Sistem_Yuku': [45, 52, 98, 55, 48], # 98 değeri bir anormallik/spike
    'Kullanici_Sayisi': [120, 130, 450, 140, 135] # 450 değeri olağandışı
}

df = pd.DataFrame(veriler)

# 2. AI TABANLI ANORMALLİK TESPİTİ
def ai_anomali_kontrol(veri_noktasi, esik_deger):
    # Basit bir AI eşik kontrolü ve karar mekanizması
    if veri_noktasi > esik_deger:
        return "⚠️ KRİTİK UYARI: Olağandışı Hareket Tespit Edildi!"
    return "✅ Stabil"

# 3. OTOMATİK DENETLEME
print("--- AI Gözetim Sistemi Çalışıyor ---\n")
df['Durum'] = df['Sistem_Yuku'].apply(lambda x: ai_anomali_kontrol(x, 90))

# Sonuçları filtrele ve sadece uyarıları göster
uyarilar = df[df['Durum'].str.contains('KRİTİK')]

if not uyarilar.empty:
    print("AI TARAFINDAN YAKALANAN ANOMALİLER:")
    print(uyarilar[['Zaman', 'Sistem_Yuku', 'Durum']])
else:
    print("Sistemde herhangi bir sorun tespit edilmedi.")
