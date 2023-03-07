
from bs4 import BeautifulSoup
import requests
from tkinter import *
from PIL import ImageTk,Image
import datetime


url = 'https://weather.com/tr-TR/weather/today/l/448d7162c387dbf15f6965ed6ac4caa1d6f11ee0aeed16ffa29858a55fcc6e1c'
r = requests.get(url)
html = r.text
soup = BeautifulSoup(html, 'html.parser')


app = Tk()
app.geometry('830x380')
app.title('Ankara Hava Durumu')
app.iconbitmap(r'C:\Users\Madara\wet.ico')


durum = soup.select_one('div[class^="CurrentConditions--phraseValue--mZC_p"]').text
sıcaklık = soup.select_one('span[class^="CurrentConditions--tempValue--MHmYY"]').text
zaman = datetime.datetime.now().strftime("%x-%X")


url2 = 'https://weather.com/tr-TR/weather/tenday/l/448d7162c387dbf15f6965ed6ac4caa1d6f11ee0aeed16ffa29858a55fcc6e1c'
r2 = requests.get(url2)
html2 = r2.text
soup2 = BeautifulSoup(html2, 'html.parser')


gün2 = soup2.select('h3', class_='DetailsSummary--daypartName--kbngc')
sıcaklık2 = soup2.select('span[class^="DetailsSummary--highTempValue--3PjlX"]')
durum2 = soup2.select('span[class^="DetailsSummary--extendedData--307Ax"]')

gün2txt = gün2[3].text
gün3txt = gün2[6].text
gün4txt = gün2[9].text
gün5txt = gün2[12].text
gün6txt = gün2[15].text
gün7txt = gün2[18].text
gün8txt = gün2[21].text

durum2txt = durum2[1].text
durum3txt = durum2[2].text
durum4txt = durum2[3].text
durum5txt = durum2[4].text
durum6txt = durum2[5].text
durum7txt = durum2[6].text
durum8txt = durum2[7].text

sıcaklık2text = sıcaklık2[1].text
sıcaklık3text = sıcaklık2[2].text
sıcaklık4text = sıcaklık2[3].text
sıcaklık5text = sıcaklık2[4].text
sıcaklık6text = sıcaklık2[5].text
sıcaklık7text = sıcaklık2[6].text
sıcaklık8text = sıcaklık2[7].text

if durum == 'Parçalı Bulutlu':

    img = PhotoImage(file="bulut.png")
    width, height = img.width(), img.height()
    canvas = Canvas(app, width=width, height=height)
    canvas.pack()
    canvas.create_image((0, 0), image=img, anchor="nw")
    canvas.create_text(150, 18, text='Ankara Hava Durumu', font = ('Franklin Gothic', 22), fill = 'black')
    canvas.create_text(696,20, text = zaman, font = ('Franklin Gothic', 22), fill = 'black')
    img2= ImageTk.PhotoImage(Image.open("pngegg.png"))
    canvas.create_image(120,70,anchor=NW,image=img2)
    canvas.create_text(520,155, text = durum, font = ('Franklin Gothic', 22), fill = 'black')
    canvas.create_text(520,205, text = sıcaklık, font = ('Franklin Gothic', 22), fill = 'black')
    canvas.create_text(65,315, text = gün2txt, font = ('Franklin Gothic', 11), fill = 'black')
    canvas.create_text(65,335, text = durum2txt, font = ('Franklin Gothic', 8), fill = 'black')
    canvas.create_text(65,352, text = sıcaklık2text, font = ('Franklin Gothic', 10), fill = 'black')
    canvas.create_text(180,315, text = gün3txt, font = ('Franklin Gothic', 11), fill = 'black')
    canvas.create_text(180,335, text = durum3txt, font = ('Franklin Gothic', 8), fill = 'black')
    canvas.create_text(180,352, text = sıcaklık3text, font = ('Franklin Gothic', 10), fill = 'black')
    canvas.create_text(295,315, text = gün4txt, font = ('Franklin Gothic', 11), fill = 'black')
    canvas.create_text(295,335, text = durum4txt, font = ('Franklin Gothic', 8), fill = 'black')
    canvas.create_text(295,352, text = sıcaklık4text, font = ('Franklin Gothic', 10), fill = 'black')
    canvas.create_text(410,315, text = gün5txt, font = ('Franklin Gothic', 11), fill = 'black')
    canvas.create_text(410,335, text = durum5txt, font = ('Franklin Gothic', 8), fill = 'black')
    canvas.create_text(410,352, text = sıcaklık5text, font = ('Franklin Gothic', 10), fill = 'black')
    canvas.create_text(525,315, text = gün6txt, font = ('Franklin Gothic', 11), fill = 'black')
    canvas.create_text(525,335, text = durum6txt, font = ('Franklin Gothic', 8), fill = 'black')
    canvas.create_text(525,352, text = sıcaklık6text, font = ('Franklin Gothic', 10), fill = 'black')
    canvas.create_text(640,315, text = gün7txt, font = ('Franklin Gothic', 11), fill = 'black')
    canvas.create_text(640,335, text = durum7txt, font = ('Franklin Gothic', 8), fill = 'black')
    canvas.create_text(640,352, text = sıcaklık7text, font = ('Franklin Gothic', 10), fill = 'black')
    canvas.create_text(755,315, text = gün8txt, font = ('Franklin Gothic', 11), fill = 'black')
    canvas.create_text(755,335, text = durum8txt, font = ('Franklin Gothic', 8), fill = 'black')
    canvas.create_text(755,352, text = sıcaklık8text, font = ('Franklin Gothic', 10), fill = 'black')


if durum == 'Çoğunlukla Bulutlu':

    img = PhotoImage(file="bulut.png")
    width, height = img.width(), img.height()
    canvas = Canvas(app, width=width, height=height)
    canvas.pack()
    canvas.create_image((0, 0), image=img, anchor="nw")
    canvas.create_text(150, 18, text='Ankara Hava Durumu', font = ('Franklin Gothic', 22), fill = 'black')
    canvas.create_text(696,20, text = zaman, font = ('Franklin Gothic', 22), fill = 'black')
    img2= ImageTk.PhotoImage(Image.open("pngegg.png"))
    canvas.create_image(120,70,anchor=NW,image=img2)
    canvas.create_text(520,155, text = durum, font = ('Franklin Gothic', 22), fill = 'black')
    canvas.create_text(520,205, text = sıcaklık, font = ('Franklin Gothic', 22), fill = 'black')
    canvas.create_text(65,315, text = gün2txt, font = ('Franklin Gothic', 11), fill = 'black')
    canvas.create_text(65,335, text = durum2txt, font = ('Franklin Gothic', 8), fill = 'black')
    canvas.create_text(65,352, text = sıcaklık2text, font = ('Franklin Gothic', 10), fill = 'black')
    canvas.create_text(180,315, text = gün3txt, font = ('Franklin Gothic', 11), fill = 'black')
    canvas.create_text(180,335, text = durum3txt, font = ('Franklin Gothic', 8), fill = 'black')
    canvas.create_text(180,352, text = sıcaklık3text, font = ('Franklin Gothic', 10), fill = 'black')
    canvas.create_text(295,315, text = gün4txt, font = ('Franklin Gothic', 11), fill = 'black')
    canvas.create_text(295,335, text = durum4txt, font = ('Franklin Gothic', 8), fill = 'black')
    canvas.create_text(295,352, text = sıcaklık4text, font = ('Franklin Gothic', 10), fill = 'black')
    canvas.create_text(410,315, text = gün5txt, font = ('Franklin Gothic', 11), fill = 'black')
    canvas.create_text(410,335, text = durum5txt, font = ('Franklin Gothic', 8), fill = 'black')
    canvas.create_text(410,352, text = sıcaklık5text, font = ('Franklin Gothic', 10), fill = 'black')
    canvas.create_text(525,315, text = gün6txt, font = ('Franklin Gothic', 11), fill = 'black')
    canvas.create_text(525,335, text = durum6txt, font = ('Franklin Gothic', 8), fill = 'black')
    canvas.create_text(525,352, text = sıcaklık6text, font = ('Franklin Gothic', 10), fill = 'black')
    canvas.create_text(640,315, text = gün7txt, font = ('Franklin Gothic', 11), fill = 'black')
    canvas.create_text(640,335, text = durum7txt, font = ('Franklin Gothic', 8), fill = 'black')
    canvas.create_text(640,352, text = sıcaklık7text, font = ('Franklin Gothic', 10), fill = 'black')
    canvas.create_text(755,315, text = gün8txt, font = ('Franklin Gothic', 11), fill = 'black')
    canvas.create_text(755,335, text = durum8txt, font = ('Franklin Gothic', 8), fill = 'black')
    canvas.create_text(755,352, text = sıcaklık8text, font = ('Franklin Gothic', 10), fill = 'black')

if durum == 'Güneşli':

    img = PhotoImage(file="güneş.png")
    width, height = img.width(), img.height()
    canvas = Canvas(app, width=width, height=height)
    canvas.pack()
    canvas.create_image((0, 0), image=img, anchor="nw")
    canvas.create_text(150, 18, text='Ankara Hava Durumu', font = ('Lucida Console', 22), fill = 'black')
    canvas.create_text(670,20, text = zaman, font = ('Lucida Console', 22), fill = 'black')
    img2= ImageTk.PhotoImage(Image.open("pngegg3.png"))
    canvas.create_image(120,70,anchor=NW,image=img2)
    canvas.create_text(520,155, text = durum, font = ('Franklin Gothic', 22), fill = 'black')
    canvas.create_text(520,205, text = sıcaklık, font = ('Franklin Gothic', 22), fill = 'black')
    canvas.create_text(65,315, text = gün2txt, font = ('Franklin Gothic', 11), fill = 'black')
    canvas.create_text(65,335, text = durum2txt, font = ('Franklin Gothic', 8), fill = 'black')
    canvas.create_text(65,352, text = sıcaklık2text, font = ('Franklin Gothic', 10), fill = 'black')
    canvas.create_text(180,315, text = gün3txt, font = ('Franklin Gothic', 11), fill = 'black')
    canvas.create_text(180,335, text = durum3txt, font = ('Franklin Gothic', 8), fill = 'black')
    canvas.create_text(180,352, text = sıcaklık3text, font = ('Franklin Gothic', 10), fill = 'black')
    canvas.create_text(295,315, text = gün4txt, font = ('Franklin Gothic', 11), fill = 'black')
    canvas.create_text(295,335, text = durum4txt, font = ('Franklin Gothic', 8), fill = 'black')
    canvas.create_text(295,352, text = sıcaklık4text, font = ('Franklin Gothic', 10), fill = 'black')
    canvas.create_text(410,315, text = gün5txt, font = ('Franklin Gothic', 11), fill = 'black')
    canvas.create_text(410,335, text = durum5txt, font = ('Franklin Gothic', 8), fill = 'black')
    canvas.create_text(410,352, text = sıcaklık5text, font = ('Franklin Gothic', 10), fill = 'black')
    canvas.create_text(525,315, text = gün6txt, font = ('Franklin Gothic', 11), fill = 'black')
    canvas.create_text(525,335, text = durum6txt, font = ('Franklin Gothic', 8), fill = 'black')
    canvas.create_text(525,352, text = sıcaklık6text, font = ('Franklin Gothic', 10), fill = 'black')
    canvas.create_text(640,315, text = gün7txt, font = ('Franklin Gothic', 11), fill = 'black')
    canvas.create_text(640,335, text = durum7txt, font = ('Franklin Gothic', 8), fill = 'black')
    canvas.create_text(640,352, text = sıcaklık7text, font = ('Franklin Gothic', 10), fill = 'black')
    canvas.create_text(755,315, text = gün8txt, font = ('Franklin Gothic', 11), fill = 'black')
    canvas.create_text(755,335, text = durum8txt, font = ('Franklin Gothic', 8), fill = 'black')
    canvas.create_text(755,352, text = sıcaklık8text, font = ('Franklin Gothic', 10), fill = 'black')



if durum == 'Sağanak yağışlı':

    img = PhotoImage(file="yağmur.png")
    width, height = img.width(), img.height()
    canvas = Canvas(app, width=width, height=height)
    canvas.pack()
    canvas.create_image((0, 0), image=img, anchor="nw")
    canvas.create_text(150, 18, text='Ankara Hava Durumu', font = ('Lucida Console', 22), fill = 'black')
    canvas.create_text(670,20, text = zaman, font = ('Lucida Console', 22), fill = 'black')
    img2= ImageTk.PhotoImage(Image.open("yağmur1.png"))
    canvas.create_image(120,70,anchor=NW,image=img2)
    canvas.create_text(520,155, text = durum, font = ('Franklin Gothic', 22), fill = 'black')
    canvas.create_text(520,205, text = sıcaklık, font = ('Franklin Gothic', 22), fill = 'black')
    canvas.create_text(65,315, text = gün2txt, font = ('Franklin Gothic', 11), fill = 'black')
    canvas.create_text(65,335, text = durum2txt, font = ('Franklin Gothic', 8), fill = 'black')
    canvas.create_text(65,352, text = sıcaklık2text, font = ('Franklin Gothic', 10), fill = 'black')
    canvas.create_text(180,315, text = gün3txt, font = ('Franklin Gothic', 11), fill = 'black')
    canvas.create_text(180,335, text = durum3txt, font = ('Franklin Gothic', 8), fill = 'black')
    canvas.create_text(180,352, text = sıcaklık3text, font = ('Franklin Gothic', 10), fill = 'black')
    canvas.create_text(295,315, text = gün4txt, font = ('Franklin Gothic', 11), fill = 'black')
    canvas.create_text(295,335, text = durum4txt, font = ('Franklin Gothic', 8), fill = 'black')
    canvas.create_text(295,352, text = sıcaklık4text, font = ('Franklin Gothic', 10), fill = 'black')
    canvas.create_text(410,315, text = gün5txt, font = ('Franklin Gothic', 11), fill = 'black')
    canvas.create_text(410,335, text = durum5txt, font = ('Franklin Gothic', 8), fill = 'black')
    canvas.create_text(410,352, text = sıcaklık5text, font = ('Franklin Gothic', 10), fill = 'black')
    canvas.create_text(525,315, text = gün6txt, font = ('Franklin Gothic', 11), fill = 'black')
    canvas.create_text(525,335, text = durum6txt, font = ('Franklin Gothic', 8), fill = 'black')
    canvas.create_text(525,352, text = sıcaklık6text, font = ('Franklin Gothic', 10), fill = 'black')
    canvas.create_text(640,315, text = gün7txt, font = ('Franklin Gothic', 11), fill = 'black')
    canvas.create_text(640,335, text = durum7txt, font = ('Franklin Gothic', 8), fill = 'black')
    canvas.create_text(640,352, text = sıcaklık7text, font = ('Franklin Gothic', 10), fill = 'black')
    canvas.create_text(755,315, text = gün8txt, font = ('Franklin Gothic', 11), fill = 'black')
    canvas.create_text(755,335, text = durum8txt, font = ('Franklin Gothic', 8), fill = 'black')
    canvas.create_text(755,352, text = sıcaklık8text, font = ('Franklin Gothic', 10), fill = 'black')
 


if durum == 'ÖS Yağmur Geçişleri':
    img = PhotoImage(file="yağmur.png")
    width, height = img.width(), img.height()
    canvas = Canvas(app, width=width, height=height)
    canvas.pack()
    canvas.create_image((0, 0), image=img, anchor="nw")
    canvas.create_text(150, 18, text='Ankara Hava Durumu', font = ('Lucida Console', 22), fill = 'black')
    canvas.create_text(670,20, text = zaman, font = ('Lucida Console', 22), fill = 'black')
    img2= ImageTk.PhotoImage(Image.open("yağmur1.png"))
    canvas.create_image(120,70,anchor=NW,image=img2)
    canvas.create_text(520,155, text = durum, font = ('Franklin Gothic', 22), fill = 'black')
    canvas.create_text(520,205, text = sıcaklık, font = ('Franklin Gothic', 22), fill = 'black')
    canvas.create_text(65,315, text = gün2txt, font = ('Franklin Gothic', 11), fill = 'black')
    canvas.create_text(65,335, text = durum2txt, font = ('Franklin Gothic', 8), fill = 'black')
    canvas.create_text(65,352, text = sıcaklık2text, font = ('Franklin Gothic', 10), fill = 'black')
    canvas.create_text(180,315, text = gün3txt, font = ('Franklin Gothic', 11), fill = 'black')
    canvas.create_text(180,335, text = durum3txt, font = ('Franklin Gothic', 8), fill = 'black')
    canvas.create_text(180,352, text = sıcaklık3text, font = ('Franklin Gothic', 10), fill = 'black')
    canvas.create_text(295,315, text = gün4txt, font = ('Franklin Gothic', 11), fill = 'black')
    canvas.create_text(295,335, text = durum4txt, font = ('Franklin Gothic', 8), fill = 'black')
    canvas.create_text(295,352, text = sıcaklık4text, font = ('Franklin Gothic', 10), fill = 'black')
    canvas.create_text(410,315, text = gün5txt, font = ('Franklin Gothic', 11), fill = 'black')
    canvas.create_text(410,335, text = durum5txt, font = ('Franklin Gothic', 8), fill = 'black')
    canvas.create_text(410,352, text = sıcaklık5text, font = ('Franklin Gothic', 10), fill = 'black')
    canvas.create_text(525,315, text = gün6txt, font = ('Franklin Gothic', 11), fill = 'black')
    canvas.create_text(525,335, text = durum6txt, font = ('Franklin Gothic', 8), fill = 'black')
    canvas.create_text(525,352, text = sıcaklık6text, font = ('Franklin Gothic', 10), fill = 'black')
    canvas.create_text(640,315, text = gün7txt, font = ('Franklin Gothic', 11), fill = 'black')
    canvas.create_text(640,335, text = durum7txt, font = ('Franklin Gothic', 8), fill = 'black')
    canvas.create_text(640,352, text = sıcaklık7text, font = ('Franklin Gothic', 10), fill = 'black')
    canvas.create_text(755,315, text = gün8txt, font = ('Franklin Gothic', 11), fill = 'black')
    canvas.create_text(755,335, text = durum8txt, font = ('Franklin Gothic', 8), fill = 'black')
    canvas.create_text(755,352, text = sıcaklık8text, font = ('Franklin Gothic', 10), fill = 'black')


if durum == 'ÖÖ Yağmur Geçişleri':
    img = PhotoImage(file="yağmur.png")
    width, height = img.width(), img.height()
    canvas = Canvas(app, width=width, height=height)
    canvas.pack()
    canvas.create_image((0, 0), image=img, anchor="nw")
    canvas.create_text(150, 18, text='Ankara Hava Durumu', font = ('Lucida Console', 22), fill = 'black')
    canvas.create_text(670,20, text = zaman, font = ('Lucida Console', 22), fill = 'black')
    img2= ImageTk.PhotoImage(Image.open("yağmur1.png"))
    canvas.create_image(120,70,anchor=NW,image=img2)
    canvas.create_text(520,155, text = durum, font = ('Franklin Gothic', 22), fill = 'black')
    canvas.create_text(520,205, text = sıcaklık, font = ('Franklin Gothic', 22), fill = 'black')
    canvas.create_text(65,315, text = gün2txt, font = ('Franklin Gothic', 11), fill = 'black')
    canvas.create_text(65,335, text = durum2txt, font = ('Franklin Gothic', 8), fill = 'black')
    canvas.create_text(65,352, text = sıcaklık2text, font = ('Franklin Gothic', 10), fill = 'black')
    canvas.create_text(180,315, text = gün3txt, font = ('Franklin Gothic', 11), fill = 'black')
    canvas.create_text(180,335, text = durum3txt, font = ('Franklin Gothic', 8), fill = 'black')
    canvas.create_text(180,352, text = sıcaklık3text, font = ('Franklin Gothic', 10), fill = 'black')
    canvas.create_text(295,315, text = gün4txt, font = ('Franklin Gothic', 11), fill = 'black')
    canvas.create_text(295,335, text = durum4txt, font = ('Franklin Gothic', 8), fill = 'black')
    canvas.create_text(295,352, text = sıcaklık4text, font = ('Franklin Gothic', 10), fill = 'black')
    canvas.create_text(410,315, text = gün5txt, font = ('Franklin Gothic', 11), fill = 'black')
    canvas.create_text(410,335, text = durum5txt, font = ('Franklin Gothic', 8), fill = 'black')
    canvas.create_text(410,352, text = sıcaklık5text, font = ('Franklin Gothic', 10), fill = 'black')
    canvas.create_text(525,315, text = gün6txt, font = ('Franklin Gothic', 11), fill = 'black')
    canvas.create_text(525,335, text = durum6txt, font = ('Franklin Gothic', 8), fill = 'black')
    canvas.create_text(525,352, text = sıcaklık6text, font = ('Franklin Gothic', 10), fill = 'black')
    canvas.create_text(640,315, text = gün7txt, font = ('Franklin Gothic', 11), fill = 'black')
    canvas.create_text(640,335, text = durum7txt, font = ('Franklin Gothic', 8), fill = 'black')
    canvas.create_text(640,352, text = sıcaklık7text, font = ('Franklin Gothic', 10), fill = 'black')
    canvas.create_text(755,315, text = gün8txt, font = ('Franklin Gothic', 11), fill = 'black')
    canvas.create_text(755,335, text = durum8txt, font = ('Franklin Gothic', 8), fill = 'black')
    canvas.create_text(755,352, text = sıcaklık8text, font = ('Franklin Gothic', 10), fill = 'black')



app.resizable(False, False)
app.mainloop()








