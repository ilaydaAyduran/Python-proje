stok = []
sermaye = 10000  # Örnek bir başlangıç sermayesi
isim = "AY Market"

def urun_ekle(urun, birim_fiyat):
    global sermaye

    urun_id = urun["urun_id"]
    urun_adi = urun["urun_adi"]
    urun_fiyat = urun["urun_fiyat"]
    urun_miktar = urun["urun_miktar"]

    if urun_miktar <= 0:
        print(f"{urun_adi} eklenemedi: Ürün miktarı sıfır veya negatif olamaz.")
        return

    toplam_maliyet = urun_miktar * birim_fiyat
    if sermaye < toplam_maliyet:
        print(f"{urun_adi} eklenemedi: Yetersiz sermaye.")
        return

    for urun_stok in stok:
        if urun_stok["urun_id"] == urun_id:
            urun_stok["urun_miktar"] += urun_miktar
            sermaye -= toplam_maliyet
            print(f"{urun_adi} stok güncellendi. Yeni miktar: {urun_stok['urun_miktar']}")
            return

    urun_kopya = urun.copy()
    urun_kopya["urun_miktar"] = urun_miktar
    stok.append(urun_kopya)
    sermaye -= toplam_maliyet
    print(f"{urun_adi} stoklara eklendi. Kalan sermaye: {sermaye}")

def urun_sat(urun_id, urun_miktar):
    global sermaye

    for urun_stok in stok:
        if urun_stok["urun_id"] == urun_id:
            urun_adi = urun_stok["urun_adi"]
            urun_fiyat = urun_stok["urun_fiyat"]
            mevcut_miktar = urun_stok["urun_miktar"]

            if urun_miktar <= 0:
                print(f"{urun_adi} satılamadı: Geçersiz miktar.")
                return

            if mevcut_miktar < urun_miktar:
                print(f"{urun_adi} satılamadı: Stok yetersiz.")
                return

            toplam_gelir = urun_miktar * urun_fiyat
            urun_stok["urun_miktar"] -= urun_miktar
            sermaye += toplam_gelir
            print(f"{urun_adi} satıldı. Toplam gelir: {toplam_gelir}")
            return

    print("Ürün bulunamadı: Satış işlemi başarısız.")

def urunleri_goster():
    for urun_stok in stok:
        print(f"Ürün ID: {urun_stok['urun_id']}, Adı: {urun_stok['urun_adi']}, Fiyatı: {urun_stok['urun_fiyat']}, Miktarı: {urun_stok['urun_miktar']}")

def sermayeyi_gor():
    return sermaye

def sermayeyi_guncelle(yeni_sermaye):
    global sermaye
    sermaye = yeni_sermaye

def get_isim():
    return isim

# Kullanıcıdan giriş almak için input kullanımı:
while True:
    print("Hoş geldiniz,", get_isim())
    print("1. Ürün ekle")
    print("2. Ürün sat")
    print("3. Ürünleri göster")
    print("4. Sermayeyi göster")
    print("5. Sermaye güncelle")
    print("6. Çıkış")

    secim = input("Lütfen bir seçenek girin (1/2/3/4/5/6): ")

    if secim == "1":
        urun_id = int(input("Ürün ID'si: "))
        urun_adi = input("Ürün adı: ")
        urun_fiyat = float(input("Ürün fiyatı: "))
        urun_miktar = int(input("Ürün miktarı: "))
        urun = {
            "urun_id": urun_id,
            "urun_adi": urun_adi,
            "urun_fiyat": urun_fiyat,
            "urun_miktar": urun_miktar
        }
        birim_fiyat = float(input("Birim fiyat: "))
        urun_ekle(urun, birim_fiyat)

    elif secim == "2":
        urun_id = int(input("Ürün ID'si: "))
        urun_miktar = int(input("Satılacak miktar: "))
        urun_sat(urun_id, urun_miktar)

    elif secim == "3":
        urunleri_goster()

    elif secim == "4":
        print("Sermaye:", sermayeyi_gor())

    elif secim == "5":
        yeni_sermaye = float(input("Yeni sermaye miktarını girin: "))
        sermayeyi_guncelle(yeni_sermaye)

    elif secim == "6":
        print("Programdan çıkılıyor...")
        break

    else:
        print("Geçersiz seçenek. Lütfen tekrar deneyin.")
