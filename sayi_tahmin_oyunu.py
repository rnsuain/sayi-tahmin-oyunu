import random 

print("Sayı Tahmin Oyununa Hoş Geldinn!")

while True:

 hak=10

 print("Zorluk Seç: ")
 print("1- Kolay (1-50)")
 print("2- Orta(1-100)")
 print("3-Zor (1-500)")

 secim=input("Seçimin: ")

 if secim =="1":
    tutulan_sayi=random.randint(1,50)
 elif secim =="2":
    tutulan_sayi=random.randint(1,100)
 elif secim =="3":
    tutulan_sayi=random.randint(1,500)
 else:
    print("Geçersiz seçim,orta seviye seçildi.")  
    tutulan_sayi=random.randint(1,100)
 tahmin=int(input("Seçmiş olduğunuz seviye aralığında sayı giriniz: "))  

 deneme=0

 while tahmin!=tutulan_sayi and hak > 0:
    deneme+=1

    hak -=1

    if tahmin < tutulan_sayi:
        print("Daha büyük bir değer giriniz.")
    elif tahmin > tutulan_sayi:
        print("Daha küçük bir değer giriniz.") 

    print("Kalan hak:",hak)  

    if hak>0:
        tahmin=int(input("Tekrar tahmin ediniz: "))

 deneme +=1     
 if tahmin ==tutulan_sayi:
    print("Tebrikler!",deneme,"denemede bildiniz.")        
 else:
    print("Hakkın bitti! Sayı:",tutulan_sayi)



 tekrar=input("Tekrar oynamak ister misin? (e/h): ")

 if tekrar =="h":
    print("Oyun bitti.")
    break