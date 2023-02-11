import random
import time
class Kumanda():
    def __init__(self,tv_durum = "Kapalı",tv_ses = 0, kanal_listesi = ["Trt"],kanal = "Trt"):
        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal
    
    def tv_ac(self):
        if self.tv_durum == "Açık":
            print("Televizyon zaten açık")
        else:
            print("Televizyon açılıyor...")
            time.sleep(1)
            self.tv_durum = "Açık"
            print("Televizyon açıldı.")


    def tv_kapat(self):
        if self.tv_durum =="Kapalı":
            print("Televizyon zaten kapalı.")
        else:
            print("Televizyon kapanıyor...")
            time.sleep(1)
            self.tv_durum ="Kapalı"
            print("Televizyon kapandı.")

    def ses_ayarlari(self):
        while True:
            cevap = input("Sesi Azalt:'<'\nSesi Arttır:'>'\nÇıkış: çıkış:")
            if cevap=="<":
                if self.tv_ses !=0:
                    self.tv_ses-=1
                    print("Ses:",self.tv_ses)
            elif cevap ==">":
                if self.tv_ses!= 31:
                    self.tv_ses+=1
                    print("Ses:",self.tv_ses)
            else:
                print("Ses güncellendi:",self.tv_ses)
                break

    def kanal_ekle(self,kanal_ismi):
        print("Kanal Ekleniyor...")
        time.sleep(1)
        self.kanal_listesi.append(kanal_ismi)
        print("Kanal eklendi.")

    def rasgele_kanal(self):
        rasgele = random.randint(0,len(self.kanal_listesi)-1)

        self.kanal = self.kanal_listesi[rasgele]
        print("Şu ankı kanal:",self.kanal)

    def __len__(self):
        return len(self.kanal_listesi)    
    
    def __str__(self):
        return "Tv Durumu: {}\nTv Ses {}\nKanal Listesi {}\nŞu Anki Kanal: {}\n".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal)
    

print("""
Televizyon Uygulaması:
1.Tv Aç
2.Tv Kapat
3.Ses Ayarları
4.Kanal Ekle
5.Kanal Sayısı Öğrenme
6.Rasgele Kanala Geçme
7.Televizyon Bilgileri
Çıkmak için 'q' tıklayınız
""")
kumanda = Kumanda()
while True:
    islem = input("Yapmak istediğiniz işlem numrasını giriniz:")
    if islem =="1":
        kumanda.tv_ac()
    elif islem =="2":
        kumanda.tv_kapat()
    elif islem =="3":
        kumanda.ses_ayarlari()
    elif islem =="4":
        kanal_eklee = input("Eklenecek olan kanal isimlerini ',' ile  giriniz:")
        kanal_listesi = kanal_eklee.split(",")
        for eklenecekler in kanal_listesi:
            kumanda.kanal_ekle(eklenecekler)
    elif islem =="5":
        print("Kanal sayısı:",len(kumanda))
    
    elif islem =="6":
        kumanda.rasgele_kanal()
    
    elif islem =="7":
        print("Televizyon bilgilerim:",kumanda)

    elif islem =="q":
        print("Televizyon kapatılıyor....")
        time.sleep(1)
        print("Televizyon kapandı.")
        break
        
    else:
        print("Geçersiz işlem...")
  