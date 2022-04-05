from tkinter import font
import turtle
t = turtle.Turtle()
w = turtle.Screen()
w.title("Türk Bayrağımız")          # Başlık
w.setup(width=720,height=420)       # Pencere Boyutu
w.bgcolor('red')                    # Arka Plan Kırmızı Yap

# İlk Daire
t.up()
t.goto(-100,-100)                   # Fare İmleci Lokasyonu
t.color('white')                    # Beyaz Renk
t.begin_fill()                      # Beyaz Rengi Doldur
t.circle(120)                       # Çapı
t.end_fill()

# Hilal Yapabilmek İçin İkinci Daire
t.goto(-70,-80)                     # Fare İmleci Lokasyonu
t.color('red')                      # Kırmızı Renk
t.begin_fill()                      # Kırmızı Rengi Doldur
t.circle(100)                       # Çapı
t.end_fill()                        # Dolguyu Bitir

# Yıldız İçin Hazırlık
t.goto(0,35)
t.fillcolor("white")
t.begin_fill()

# Yıldız İçin Tekrar Eden Üçgen Çizimi
for i in range(5):
    t.forward(150)
    t.right(144)
t.end_fill()

t.goto(-130,-190)
t.color("white")
t.write("@maksatyazilim" , font=("verdana", 17, "bold"))

# Fare İmleci Ekranda Durup Görüntüyü Bozmasın Diye Uzaklaştırıyoruz :)
t.goto(-999,-0)

# Ekrana Tıklayınca Programın Kapanmasını Sağlar.
w.exitonclick()
