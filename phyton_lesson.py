y_n1=int(input("1. yazılı notunu giriniz: "))
y_n2=int(input("2. yazılı notunu giriniz: "))
s_n1=int(input("1. sözlü notunu giriniz: "))
s_n2=int(input("2. sözlü notunu giriniz: "))
ogrort=(((y_n1 + y_n2 + s_n1 +s_n2)/4))
print("öğrencinin not ortalaması=",ogrort)
if(ogrort<25):
    print("öğrencinin ders notu 1 dir")
elif(25<=ogrort<50):
    print("öğrencinin ders notu 2 dir")
elif(50<=ogrort<70):
    print("öğrencinin ders notu 3 tür")
elif(70<=ogrort<85):
    print("öğrencinin ders notu 4 tür")
else:
    print("öğrencinin ders notu 5 tir")