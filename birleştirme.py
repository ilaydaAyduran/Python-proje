while True:
    print("1- Kullanıcı işlemleri")
    print("2- Kitap işlemleri")
    sec = input("\nişlem yapmak istediğiniz türü seçin: ")
    if sec == "1":
        class Kullanici:  # Kullanıcı sınıfı, kullanıcı bilgilerini depolamak için kullanılır.
            def __init__(self, ad, soyad, telefon, email, adres):
                self.ad = ad
                self.soyad = soyad
                self.__telefon = telefon
                self.email = email
                self.__adres = adres

        class KullaniciYonetimi:  # Kullanıcı yönetimi sınıfı, kullanıcıları eklemek, silmek, listelemek ve bilgilerini aramak için kullanılır.
            def __init__(self):
                self.kullanicilar = []  # Boş bir kullanıcı listesi oluşturulur

            def kullanici_ekle(self, kullanici):
                self.kullanicilar.append(kullanici) # Yeni kullanıcı listeye eklenir
                print("Yeni kullanıcı eklendi: {} {}".format(kullanici.ad, kullanici.soyad))

            def kullanici_listele(self):
                for kullanici in self.kullanicilar:
                    print("{} {}, Email: {}".format(kullanici.ad, kullanici.soyad, kullanici.email))
                        # Tüm kullanıcıları listelemek için kullanicilar üzerinde döngü oluşturulur

            def kullanici_sil(self, ad, soyad):
                for kullanici in self.kullanicilar:
                    if kullanici.ad == ad and kullanici.soyad == soyad:
                        self.kullanicilar.remove(kullanici) # Kullanıcı listeden silinir
                        print("Kullanıcı silindi: {} {}".format(ad, soyad))
                        return
                print("Kullanıcı bulunamadı: {} {}".format(ad, soyad))
    
            def kullanici_bilgileri(self, ad, soyad): # Kullanıcı bilgilerini verilen ad ve soyadına göre ara
                for kullanici in self.kullanicilar:
                    if kullanici.ad == ad and kullanici.soyad == soyad:
                        print("{} {} kullanıcısının bilgileri:".format(ad, soyad))
                        print("Tel: {}, Email: {}, Adres: {}".format(kullanici.telefon, kullanici.email, kullanici.adres))
                        return
                        # Kullanıcı bulunamadığı durumda mesaj yazdır
                print("Kullanıcı bulunamadı: {} {}".format(ad, soyad))
    
        def ana_menu():    # Kullanıcıdan gerekli bilgileri alır ve bilgiler kullanıma hazır halde.
            print("Akıllı kütüphaneye hoşgeldiniz :)")
    
            ad= input("Adınızı girin : ")  # Kullanıcının adını al
            soyad= input("Soyadınızı girin :") # Kullanıcının soyadını al
            telefon= input("Telefon numarınızı girin : ") # Kullanıcının telefon numarasını al
            email= input("Email adresinizi girin : ") # Kullanıcının email adresini al
            adres= input("Adresinizi girin : ") # Kullanıcının adresini al
            yeni_kullanici= Kullanici(ad, soyad, telefon, email, adres ) # Yeni kullanıcı oluştur
    
            kullanici_yonetimi = KullaniciYonetimi() # Kullanıcı yönetimi nesnesi oluştur
            kullanici_yonetimi.kullanici_ekle(yeni_kullanici) # Yeni kullanıcıyı ekle
    
            while True:   # İşlem seçimini alır
                print("\nYapabileceğiniz işlemler:") # İşlem seçimini al
                print("1- Kullanıcı ekleme")
                print("2- Kullanıcı silme")
                print("3- Kullanıcıları listele ")
                print("4- Çıkış")
        
        
                secim = input("\nYapmak istediğiniz işlemi seçin: ")

                if secim == "1":
                    ad = input("\nAdı girin: ")
                    soyad = input("Soyadı girin: ")
                    telefon = input("Telefon numarası girin: ")
                    email = input("E-mail adresi girin: ")
                    adres = input("Adresi girin: ")

                    kullanici = Kullanici(ad, soyad, telefon, email, adres)
                    kullanici_yonetimi.kullanici_ekle(kullanici)   # Yeni kullanıcı ekleme işlemi yapar.
        
                elif secim == "2":
                    ad = input("\nSilmek istediğiniz kullanıcının adını girin: ")
                    soyad = input("Soyadını girin: ")
                    kullanici_yonetimi.kullanici_sil(ad, soyad) # Belirtilen ad ve soyada sahip kullanıcıyı silme işlemi yapar.
                elif secim == "3":
                    kullanici_yonetimi.kullanici_listele() #Kullanıcaları listeler
                elif secim == "4":
                    print("\nTeşekkürler, görüşmek üzere!")
                    break
                    # Çıkış seçeneği seçildiğinde teşekkür mesajı gösterilir ve döngüden çıkılır.
                else:
                    print("\nGeçersiz bir seçim yaptınız. Lütfen tekrar deneyin.")
                    # Geçersiz bir seçim yapıldığında kullanıcıya bilgilendirme yapılır.
            
        ana_menu()  # Ana menüyü çağırarak programı başlatırız. 
    
    if sec=="2":
        class kitaplar:
            def __init__(self,kitap, yazar,yayınevi,sayfa):
                self.kitap=kitap
                self.yazar=yazar
                self.yayınevi=yayınevi
                self.sayfa=sayfa
                self.ödünç_alınabilir_mi = True
            def __str__(self):
                return f"{self.kitap} - {self.yazar} - {self.sayfa} - {self.yayınevi}"
        while True:
                print("\nYapabileceğintiz işlemler:")
                print("1- Roman")
                print("2- Hikaye")
                print("3- Siir")
                print("4- Deneme")
                print("5- Kişisel Gelişim")
                tercih = input("\nişlem yapmak istediğiniz türü seçin: ")
                if tercih == "1":
                # Roman sınıfını tanımlıyoruz
                    class Roman:
                        def __init__(self):
                            self.romanlar= []  # Roman kitaplarını tutacak bir liste oluşturuyoruz
    
                        def roman_ekle(self,kitaplar):
                            self.romanlar.append(kitaplar)  # Yeni bir roman kitabını listeye ekliyoruz
                            print("Yeni roman eklendi {}-{}".format(kitaplar.kitap, kitaplar.yazar))
        
                        def roman_sil(self,kitap,yazar):
                            for kitaplar in self.romanlar:
                                if kitaplar.kitap == kitap and kitaplar.yazar == yazar:
                                    self.romanlar.remove(kitaplar)  # Kitabı listeden silme
                                    print("kitap silindi {} - {}".format(kitap,yazar))
                                    return
                            print("kitap bulunamadı: {} {}".format(kitap,yazar))
    
                        def roman_listele(self):
                            for kitaplar in self.romanlar:
                                print("{} - {} - {} - {} ".format(kitaplar.kitap, kitaplar.yazar, kitaplar.yayınevi, kitaplar.sayfa))
                                # Tüm şiirleri listelemek için  döngü oluşturulur
                        
                        def kitap_ara(self,kitap):
                            for kitaplar in self.romanlar:
                                if kitaplar.kitap == kitap:
                                    print(kitaplar)  # Aranan kitabın bilgilerini yazdırma
                                    break
                            else:
                                print("Kitap bulunamadı!")
    
                        def kitap_ödünç_al(self, kitap):
                            for kitaplar in self.romanlar:
                                if kitaplar.kitap == kitap:
                                    if kitaplar.ödünç_alınabilir_mi:
                                       kitaplar.ödünç_alınabilir_mi=False  # Kitabın ödünç alındığını anlamak için false değerini atadık
                                       print("Kitap başarıyla ödünç alındı!")
                                       break
                                    else:
                                        print("Bu kitap zaten ödünç alınmış!")
                                        break
                                else:
                                    print("Kitap bulunamadı!")
            
            
            
                    def ana_ekran():
                        roman=Roman() # Kullanıcıdan alınan bilgilerle bir Roman nesnesi oluşturulur
                        while True:
                            print("\nYapabileceğiniz işlemler:") # Kullanıcının yapabileceği işlemleri maddeleme 
                            print("1- Roman ekleme")
                            print("2- Roman silme")
                            print("3- Romanları listele ")
                            print("4- Roman ara")
                            print("5- Roman ödünç al")
                            print("6- Çıkış")
        
        
                            secim = input("\nYapmak istediğiniz işlemi seçin: ")
        
                            if secim == "1":
                                kitap = input("\nkitap adı girin: ")
                                yazar = input("yazar girin: ")
                                sayfa= input("sayfa sayısı girin: ")
                                yayınevi= input("yayınevi girin: ")

                                kitaplar_obj = kitaplar(kitap, yazar, sayfa, yayınevi)
                                roman.roman_ekle(kitaplar_obj)
                                # Roman kitabı eklemek için roman_ekle fonksiyonu çağırılır
            
                            elif secim == "2":
                                kitap = input("\nSilmek istediğiniz kitabın adını girin: ")
                                yazar = input("yazarı girin: ")
                                roman.roman_sil(kitap, yazar)
                                # Roman kitabı silmek için roman_sil fonksiyonu çağırılır
        
                            elif secim == "3":
                                roman.roman_listele()
                                # Tüm romanları listelemek için roman_listele() fonksiyonu çağırılır.
        
                            elif secim == "4":
                                kitap = input("\nAramak istediğiniz kitabın adını girin: ")
                                roman.kitap_ara(kitap)
                                # Romanlar arasında kitap aramak için roman_ara fonksiyonu çağırılır

                            elif secim == "5":
                                kitap = input("\nÖdünç almak istediğiniz kitabın adını girin: ")
                                roman.kitap_ödünç_al(kitap)
                                # Kitap ödünç almak için roman_ödünç_al fonksiyonu çağırılır
             
                            elif secim == "6":
                                print("\nTeşekkürler, görüşmek üzere!")
                                break
                                # Programdan çıkış yapılır.
                            else:
                                print("\nGeçersiz bir seçim yaptınız. Lütfen tekrar deneyin.")
                                # Geçersiz bir seçim yapıldığında kullanıcıya uyarı verilir.
            
                    ana_ekran()
        
                if tercih=="2":
                    class Hikaye:
                        def __init__(self):
                            self.hikayeler= [] # Hikaye kitaplarını tutacak bir liste oluşturuyoruz
    
                        def hikaye_ekle(self,kitaplar):
                            self.hikayeler.append(kitaplar)  # Yeni hikaye kitabı listeye eklenir
                            print("Yeni hikaye eklendi {}-{}".format(kitaplar.kitap, kitaplar.yazar))
        
                        def hikaye_sil(self,kitap,yazar):
                            for kitaplar in self.hikayeler:
                                if kitaplar.kitap == kitap and kitaplar.yazar == yazar:
                                    self.hikayeler.remove(kitaplar) # Hikaye kitabı listeden silinir
                                    print("kitap silindi {} - {}".format(kitap,yazar))
                                    return
                            print("kitap bulunamadı: {} {}".format(kitap,yazar))
    
                        def hikaye_listele(self):
                            for kitaplar in self.hikayeler:
                                print("{} - {} - {} - {} ".format(kitaplar.kitap, kitaplar.yazar, kitaplar.yayınevi, kitaplar.sayfa))
                                # Tüm hikaye kitaplarını listelemek için döngü oluşturulur
                         
                        def kitap_ara(self,kitap):
                            for kitaplar in self.hikayeler:
                                if kitaplar.kitap == kitap:
                                    print(kitaplar)  # Aranan kitap bilgileri ekrana yazdırılır
                                    break
                                else:
                                    print("Kitap bulunamadı!")
    
                        def kitap_ödünç_al(self, kitap):
                            for kitaplar in self.hikayeler:
                                if kitaplar.kitap == kitap:
                                    if kitaplar.ödünç_alınabilir_mi:
                                        kitaplar.ödünç_alınabilir_mi=False  # Kitap ödünç alınabildiğini anlamak için false değerini atadık 
                                        print("Kitap başarıyla ödünç alındı!")
                                        break
                                    else:
                                        print("Bu kitap zaten ödünç alınmış!")
                                        break
                                else:
                                    print("Kitap bulunamadı!")
            
            
            
                    def ana_ekran_hikaye():
                        hikaye=Hikaye()  # Hikaye sınıfından bir örnek oluşturuyoruz
                        while True:
                            print("\nYapabileceğiniz işlemler:")
                            print("1- Hikaye ekleme")
                            print("2- Hikaye silme")
                            print("3- Hikaye listele ")
                            print("4- Hikaye ara")
                            print("5- Hikaye ödünç al")
                            print("6- Çıkış")
        
        
                            secim = input("\nYapmak istediğiniz işlemi seçin: ")
        
                            if secim == "1":
                                kitap = input("\nkitap adı girin: ")
                                yazar = input("yazar girin: ")
                                sayfa= input("sayfa sayısı girin: ")
                                yayınevi= input("yayınevi girin: ")

                                kitaplar_obj = kitaplar(kitap, yazar, sayfa, yayınevi)
                                hikaye.hikaye_ekle(kitaplar_obj)
                         
                         
                            elif secim == "2":
                                kitap = input("\nSilmek istediğiniz kitabın adını girin: ")
                                yazar = input("yazarı girin: ")
                                hikaye.hikaye_sil(kitap, yazar)
                                # Kullanıcıdan alınan kitap adı ve yazar ile hikaye_sil() fonksiyonu çağırılır.
        
                            elif secim == "3":
                                hikaye.hikaye_listele()
                                # Hikaye listesini ekrana yazdırmak için hikaye_listele() fonksiyonu çağırılır.
        
                            elif secim == "4":
                                kitap = input("\nAramak istediğiniz kitabın adını girin: ")
                                hikaye.kitap_ara(kitap)
                                # Kullanıcıdan alınan kitap adı ile kitap_ara() fonksiyonu çağırılır.

                            elif secim == "5":
                                kitap = input("\nÖdünç almak istediğiniz kitabın adını girin: ")
                                hikaye.kitap_ödünç_al(kitap)
                                # Kullanıcıdan alınan kitap adı ile kitap_ödünç_al() fonksiyonu çağırılır.
             
                            elif secim == "6":
                                print("\nTeşekkürler, görüşmek üzere!")
                                break
                                # Programdan çıkış yapılır.
                            else:
                                print("\nGeçersiz bir seçim yaptınız. Lütfen tekrar deneyin.")
                                # Geçersiz bir seçim yapıldığında kullanıcıya uyarı verilir.
            
                    ana_ekran_hikaye()
                
                if tercih=="3":
            
                    class Siir:
                        def __init__(self):
                            self.siirler= [] # Boş bir şiir listesi oluşturulur
    
                        def siir_ekle(self,kitaplar):
                            self.siirler.append(kitaplar)  # Yeni şiir kitabı listeye eklenir
                            print("Yeni siir eklendi {}-{}".format(kitaplar.kitap, kitaplar.yazar))
        
                        def siir_sil(self,kitap,yazar):
                            for kitaplar in self.siirler:
                                if kitaplar.kitap == kitap and kitaplar.yazar == yazar:
                                    self.siirler.remove(kitaplar) # Şiir kitabı listeden silinir
                                    print("kitap silindi {} - {}".format(kitap,yazar))
                                    return
                            print("kitap bulunamadı: {} {}".format(kitap,yazar))
    
                        def siir_listele(self):
                            for kitaplar in self.siirler:
                                print("{} - {} - {} - {} ".format(kitaplar.kitap, kitaplar.yazar, kitaplar.yayınevi, kitaplar.sayfa))
                                # Tüm şiirleri listelemek için  döngü oluşturulur
            
                        def kitap_ara(self,kitap):
                            for kitaplar in self.siirler:
                                if kitaplar.kitap == kitap:
                                    print(kitaplar) # Aranan kitap bilgileri ekrana yazdırılır
                                    break
                            else:
                                    print("Kitap bulunamadı!")
    
                        def kitap_ödünç_al(self, kitap):
                            for kitaplar in self.siirler:
                                if kitaplar.kitap == kitap:
                                    if kitaplar.ödünç_alınabilir_mi:
                                        kitaplar.ödünç_alınabilir_mi=False # Kitap ödünç alınabildiğini anlamak için false değerini atadık
                                        print("Kitap başarıyla ödünç alındı!")
                                        break
                                    else:
                                        print("Bu kitap zaten ödünç alınmış!")
                                        break
                                else:
                                    print("Kitap bulunamadı!")
            
            
            
                    def ana_ekran_siir():
                        siir=Siir()  # Siir sınıfından bir örnek oluşturulur
                        while True:
                            print("\nYapabileceğiniz işlemler:")
                            print("1- Şiir ekleme")
                            print("2- Şiir silme")
                            print("3- Şiir listele ")
                            print("4- Şiir ara")
                            print("5- Şiir ödünç al")
                            print("6- Çıkış")
        
        
                            secim = input("\nYapmak istediğiniz işlemi seçin: ")
        
                            if secim == "1":
                                kitap = input("\nkitap adı girin: ")
                                yazar = input("yazar girin: ")
                                sayfa= input("sayfa sayısı girin: ")
                                yayınevi= input("yayınevi girin: ")

                                kitaplar_obj = kitaplar(kitap, yazar, sayfa, yayınevi)
                                siir.siir_ekle(kitaplar_obj)
                                # Kullanıcıdan alınan bilgilerle bir Siir nesnesi oluşturulur ve siir_ekle() fonksiyonu çağırılır.
            
                            elif secim == "2":
                                kitap = input("\nSilmek istediğiniz kitabın adını girin: ")
                                yazar = input("yazarı girin: ")
                                siir.siir_sil(kitap, yazar)
                                # Kullanıcıdan alınan kitap adı ve yazar ile siir_sil() fonksiyonu çağırılır.
        
                            elif secim == "3":
                                siir.siir_listele()
                                # Tüm şiirleri listelemek için siir_listele() fonksiyonu çağırılır.
        
                            elif secim == "4":
                                kitap = input("\nAramak istediğiniz kitabın adını girin: ")
                                siir.kitap_ara(kitap)
                                # Kullanıcıdan alınan kitap adı ile kitap_ara() fonksiyonu çağırılır.

                            elif secim == "5":
                                kitap = input("\nÖdünç almak istediğiniz kitabın adını girin: ")
                                siir.kitap_ödünç_al(kitap)
                                # Kullanıcıdan alınan kitap adı ile kitap_ödünç_al() fonksiyonu çağırılır.
             
                            elif secim == "6":
                                print("\nTeşekkürler, görüşmek üzere!")
                                break
                                # Programdan çıkış yapılır.
                            else:
                                print("\nGeçersiz bir seçim yaptınız. Lütfen tekrar deneyin.")
                                # Geçersiz bir seçim yapıldığında kullanıcıya uyarı verilir.
            
                    ana_ekran_siir()
                
                if tercih == "4":
        
                    class Deneme:
                        def __init__(self):
                            self.denemeler= [] # Boş bir deneme listesi oluşturulur
    
                        def deneme_ekle(self,kitaplar):
                            self.denemeler.append(kitaplar)  # Yeni deneme kitabı listeye eklenir
                            print("Yeni deneme eklendi {}-{}".format(kitaplar.kitap, kitaplar.yazar))
        
                        def deneme_sil(self,kitap,yazar):
                            for kitaplar in self.denemeler:
                                if kitaplar.kitap == kitap and kitaplar.yazar == yazar:
                                    self.denemeler.remove(kitaplar) # Deneme kitabı listeden silinir
                                    print("kitap silindi {} - {}".format(kitap,yazar))
                                    return
                            print("kitap bulunamadı: {} {}".format(kitap,yazar))
    
                        def deneme_listele(self):
                            for kitaplar in self.denemeler:
                                print("{} - {} - {} - {} ".format(kitaplar.kitap, kitaplar.yazar, kitaplar.yayınevi, kitaplar.sayfa))
                                # Tüm denemeleri listelemek için döngü oluşturulur
                          
                        def kitap_ara(self,kitap):
                            for kitaplar in self.denemeler:
                                if kitaplar.kitap == kitap:
                                    print(kitaplar) # Aranan kitap bilgileri ekrana yazdırılır
                                    break
                            else:
                                print("Kitap bulunamadı!")
    
                        def kitap_ödünç_al(self, kitap):
                            for kitaplar in self.denemeler:
                                if kitaplar.kitap == kitap:
                                    if kitaplar.ödünç_alınabilir_mi:
                                        kitaplar.ödünç_alınabilir_mi=False # Kitap ödünç alındığını anlamak için false değeri atadık
                                        print("Kitap başarıyla ödünç alındı!")
                                        break
                                    else:
                                        print("Bu kitap zaten ödünç alınmış!")
                                        break
                                else:
                                    print("Kitap bulunamadı!")
            
            
            
                    def ana_ekran_deneme():
                        deneme=Deneme() # Deneme sınıfından bir örnek oluşturulur
                        while True:
                            print("\nYapabileceğiniz işlemler:")
                            print("1- Deneme ekleme")
                            print("2- Deneme silme")
                            print("3- Deneme listele ")
                            print("4- Deneme ara")
                            print("5- Deneme ödünç al")
                            print("6- Çıkış")
        
        
                            secim = input("\nYapmak istediğiniz işlemi seçin: ")
        
                            if secim == "1":
                                kitap = input("\nkitap adı girin: ")
                                yazar = input("yazar girin: ")
                                sayfa= input("sayfa sayısı girin: ")
                                yayınevi= input("yayınevi girin: ")

                                kitaplar_obj = kitaplar(kitap, yazar, sayfa, yayınevi)
                                deneme.deneme_ekle(kitaplar_obj)
                                # Deneme kitabı eklemek için deneme_ekle fonksiyonu çağırılır
            
                            elif secim == "2":
                                kitap = input("\nSilmek istediğiniz kitabın adını girin: ")
                                yazar = input("yazarı girin: ")
                                deneme.deneme_sil(kitap, yazar)
                                # Deneme kitabı silmek için deneme_sil fonksiyonu çağırılır
        
                            elif secim == "3":
                                deneme.deneme_listele()
                                # Tüm denemeleri listelemek için deneme_listele fonksiyonu çağırılır
        
                            elif secim == "4":
                                kitap = input("\nAramak istediğiniz kitabın adını girin: ")
                                deneme.kitap_ara(kitap)
                                # Denemeler arasında kitap aramak için kitap_ara fonksiyonu çağırılır

                            elif secim == "5":
                                kitap = input("\nÖdünç almak istediğiniz kitabın adını girin: ")
                                deneme.kitap_ödünç_al(kitap)
                                # Kitap ödünç almak için kitap_ödünç_al fonksiyonu çağırılır
             
                            elif secim == "6":
                                print("\nTeşekkürler, görüşmek üzere!")
                                break
                                # Programdan çıkış yapılır
                            else:
                                print("\nGeçersiz bir seçim yaptınız. Lütfen tekrar deneyin.")
                                # Geçersiz bir seçim yapıldığında kullanıcıya uyarı verilir
            
                    ana_ekran_deneme()
                
                if tercih == "5":
        
                    class KisiselGelisim:
                        def __init__(self):
                            self.kgelisimler= []  # Boş bir kişisel gelişim listesi oluşturulur

                        def kgelisim_ekle(self,kitaplar):
                            self.kgelisimler.append(kitaplar) # Yeni kişisel gelişim kitabı listeye eklenir
                            print("Yeni deneme eklendi {}-{}".format(kitaplar.kitap, kitaplar.yazar))
        
                        def kgelisim_sil(self,kitap,yazar):
                            for kitaplar in self.kgelisimler:
                                if kitaplar.kitap == kitap and kitaplar.yazar == yazar:
                                    self.kgelisimler.remove(kitaplar) # Kişisel gelişim kitabı listeden silinir
                                    print("kitap silindi {} - {}".format(kitap,yazar))
                                    return
                            print("kitap bulunamadı: {} {}".format(kitap,yazar))
    
                        def kgelisim_listele(self):
                            for kitaplar in self.kgelisimler:
                                print("{} - {} - {} - {} ".format(kitaplar.kitap, kitaplar.yazar, kitaplar.yayınevi, kitaplar.sayfa))
                                # Tüm kişisel gelişimleri listelemek için döngü oluşturulur

                        def kgelisim_ara(self,kitap):
                            for kitaplar in self.kgelisimler:
                                if kitaplar.kitap == kitap:
                                    print(kitaplar) # Aranan kitap bilgileri ekrana yazdırılır
                                    break
                            else:
                                print("Kitap bulunamadı!")
    
                        def kitap_ödünç_al(self, kitap):
                            for kitaplar in self.kgelisimler:
                                if kitaplar.kitap == kitap:
                                    if kitaplar.ödünç_alınabilir_mi:
                                        kitaplar.ödünç_alınabilir_mi=False #Kitap ödünç alınabileceğini anlamak için false değerini atadık 
                                        print("Kitap başarıyla ödünç alındı!")
                                        break
                                    else:
                                        print("Bu kitap zaten ödünç alınmış!")
                                        break
                                else:
                                    print("Kitap bulunamadı!")
            
            
            
                    def ana_ekran_kgelisim():
                        kgelisim=KisiselGelisim() # KisiselGelisim sınıfından bir örnek oluşturulur
                        while True:
                            print("\nYapabileceğiniz işlemler:")
                            print("1- Kişisel Gelişim ekleme")
                            print("2- Kişisel Gelişim silme")
                            print("3- Kişisel Gelişim listele ")
                            print("4- Kişisel Gelişim ara")
                            print("5- Kişisel Gelişim ödünç al")
                            print("6- Çıkış")
        
        
                            secim = input("\nYapmak istediğiniz işlemi seçin: ")
        
                            if secim == "1":
                                kitap = input("\nkitap adı girin: ")
                                yazar = input("yazar girin: ")
                                sayfa= input("sayfa sayısı girin: ")
                                yayınevi= input("yayınevi girin: ")

                                kitaplar_obj = kitaplar(kitap, yazar, sayfa, yayınevi)
                                kgelisim.kgelisim_ekle(kitaplar_obj)
                                # Kişisel gelişim kitabı eklemek için kgelisim_ekle fonksiyonu çağırılır
            
                            elif secim == "2":
                                kitap = input("\nSilmek istediğiniz kitabın adını girin: ")
                                yazar = input("yazarı girin: ")
                                kgelisim.kgelisim_sil(kitap, yazar)
                                # Kişisel gelişim kitabı silmek için kgelisim_sil fonksiyonu çağırılır
        
                            elif secim == "3":
                                kgelisim.kgelisim_listele()
                                # Tüm kişisel gelişimleri listelemek için kgelisim_listele fonksiyonu çağırılır
        
                            elif secim == "4":
                                kitap = input("\nAramak istediğiniz kitabın adını girin: ")
                                kgelisim.kitap_ara(kitap)
                                # Kişisel gelişimler arasında kitap aramak için kgelisim_ara fonksiyonu çağırılır

                            elif secim == "5":
                                kitap = input("\nÖdünç almak istediğiniz kitabın adını girin: ")
                                kgelisim.kitap_ödünç_al(kitap)
                                # Kitap ödünç almak için kitap_ödünç_al fonksiyonu çağırılır
             
                            elif secim == "6":
                                print("\nTeşekkürler, görüşmek üzere!")
                                break
                                # Programdan çıkış yapılır.
                            else:
                                print("\nGeçersiz bir seçim yaptınız. Lütfen tekrar deneyin.")
                                # Geçersiz bir seçim yapıldığında kullanıcıya uyarı verilir.
            
                    ana_ekran_kgelisim()