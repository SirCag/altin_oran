# -*- coding: utf-8 -*-
from math import sqrt
def runtime(): #ana fonksiyon
    fi = (sqrt(5)+1)/2 #altın oran
    print("Altın oran: {}".format(fi))
    def check_for_fi(x,y):
        print("Sayıların: {0} ve {1}.".format(a,b)) #kullanıcıya sayıları bildiriliyor
        #büyük sayının küçük sayıya oranı alınıyor
        if x > y:
            result = x/y
            print("Sayıların oranı: "+str(result))
            return abs(fi-result)
        elif x < y:
            result = y/x
            print("Sayıların oranı: "+str(result))
            return abs(fi-result)
    a = float(input("İlk sayıyı gir:\n"))
    b = float(input("İkinci sayıyı gir:\n"))
    print("Girilen değerlerin oranı altın orandan {} uzaktadır\n\n------------\n".format(check_for_fi(a,b))) #fark yazılıyor
    runtime() #programın tekrarlaması için
runtime()
