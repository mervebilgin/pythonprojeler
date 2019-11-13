"""
kullanıcıdan iki sayı alın ve bu sayının okunuşunu bulan bir fonksiyon yazın...
örn: 97----> doksan yedi

"""
birler = [" ","bir","iki","üç","dört","beş","altı","yedi","sekiz","dokuz"]
onlar = [" ","on","yirmi","otuz","kırk","elli","altmış","yetmiş","seksen","doksan"]

def okunus(sayı):
    birinci = sayı % 10
    ikinci = sayı // 10

    return onlar[ikinci] + " " +birler[birinci]

sayı = int(input("Sayı: "))
print(okunus(sayı))
