"""
random ve time modülüyle sayı tahmin oyunu
"""
import random # modülü içeri aktarıyoruz,artık bu modülün tüm fonksiyonlarını kullanabiliriz
import time

print("""**********
Sayı tahmin oyunu
1 ile 40 arasındaki sayıyı tahmin edin
************""")

rastgele_sayı = random.randint(1,40) # 1 ve 40 arasında rastgele sayı üretir
tahmin_hakkı = 7

while True:
    tahmin = int(input("Tahmininiz: "))

    if (tahmin < rastgele_sayı):
        print("bilgiler sorgulanıyor...")
        time.sleep(1) # program 1 saniye duracaktır...
        print("Daha yüksek bir sayı söyleyin")
        tahmin_hakkı -= 1

    elif (tahmin > rastgele_sayı):
        print("bilgiler sorgulanıyor...")
        time.sleep(1)  # program 1 saniye duracaktır...
        print("Daha düşük bir sayı söyleyin")
        tahmin_hakkı -= 1

    else:
        print("Bilgiler sorgulanıyor...")
        time.sleep(1)
        print("Tebrikler!Sayımız: ",rastgele_sayı)
        break

    if (tahmin_hakkı == 0):
        print("Tahmin hakkınız bitti...")
        print("Sayımız: ",rastgele_sayı)
        break

