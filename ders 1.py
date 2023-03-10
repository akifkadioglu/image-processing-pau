import cv2
# verilen resmi okumak için imread fonksiyonu kullanılır, 0 yazarsak resmi siyah beyaz gösterir
img = cv2.imread("ornek_resim.jpg")

# okunan resmi göstermek için imshow fonksyionu kullanılır
cv2.imshow('Original Image', img) 

# yükseklik, genişlik ve kanal sayısını verir
print(img.shape)

# kanal sayısı yükseklik ve genişlik sayılarının çarpımını verir
print(img.size)

# (100,100) konumundaki pikselin mavi, kırmızı ve yeşil değerini verir
print(img.item(100,100,0)) #Blue
print(img.item(100,100,1)) #Red
print(img.item(100,100,2)) #Green

# veri tipini verir
print(img.dtype)

# split fonksiyonu 3 kanalı verir, her kanalı cv2.imshow() ile aynı normal resim gibi gösterebilirim
b,g,r=cv2.split(img)

# istediğim koordinatlardaki görüntüyü alabilmek için kullanabilirim
ROI = img[200:250,500:650]
cv2.imshow('roi',ROI)

# yeniden boyutlandırmak için resize fonksiyonu kullanılabilir
resize = cv2.resize(img,[1200,1200])

# dikdörtgen çerçeve eklemek için kullanılır x,y,rengi,kalınlık
cv2.rectangle(img, (100,150),(200,550),(0,255,255),1)

# çizgi çeker resim,(x,y),(x,y),renk,kalınlık
cv2.line(img,(0,0),(850,650),(255,255,0),2)

# çizgi çeker resim,(x,y),radius,renk,kalınlık
cv2.circle(img,(200,200),25,(255,255,0),2)

# yazı yazmak için kullanılır resim,yazı,(x,y),font,büyüklük,renk,kalınlık
cv2.putText(img,"naber",(200,200),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),cv2.LINE_4)

cv2.imshow('resim',img)

# iki resmi toplar binevi merge eder
cv2.add(img,img)

# iki resmi verilen ağırlıklarla toplar
cv2.addWeighted(img,12,img,51,0)

# iki resmi çıkarır
cv2.subtract(img,img)

# iki resmi çarpar
cv2.multiply(img,img)

# iki resmi böler
cv2.divide(img,img)

# pencere hemen kapanmasın diye waitKey fonksiyonu kullanılır 
cv2.waitKey(0)

# tüm pencereleri kapatmak için kullanılır
cv2.destroyAllWindows()