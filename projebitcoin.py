from tkinter import *
from tkinter import messagebox
import os
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
import winsound


sayfa=Tk()
sayfa.title("Bitcoin Kontrol")
sayfa.geometry("800x400")


aralik=Label(sayfa,text="Aralık giriniz:",font=("Arial",25))
aralik.grid(row=0,column=0)

veri1=Entry(sayfa,width=15,font=("Arial",25))
veri1.grid(row=0,column=1)
veri1.insert(0,"0")

veri2=Entry(sayfa,width=15,font=("Arial",25))
veri2.grid(row=0,column=2)
veri2.insert(0,"0") 

def alarmCal():
    winsound.Beep(5000, 3000)
    #winsound.PlaySound(filename, winsound.SND_FILENAME)

def fun(i):   
    baslangic = float(veri1.get())
    bitis = float(veri2.get())
    if i >=baslangic and i <= bitis:
        alarmCal()
        sor = messagebox.askquestion("Önemli Uyarı", "Ürün "+str(i)+" değerinde. Satılsın mı?")         
        if sor == "yes":
            messagebox.showinfo("Bilgilendirme", "Ürün Satıldı!!!")
        else:
            messagebox.showinfo("Bilgilendirme", "Ürün satılmadı!!!")
    sayfa.mainloop()

def Bitcoin():

    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(options=options)
    driver.get("https://tr.tradingview.com/symbols/BTCUSD/?exchange=CRYPTO")
    for i in range(10):
        sleep(1)
        a=driver.find_element(By.XPATH,"/html/body/div[3]/div[4]/div[2]/header/div/div[3]/div[1]/div/div/div/div[1]/div[1]").text
        b=float(a)
        deger = b
        fun(b)
       


buton=Button(sayfa,text="Kontrol Et",command=Bitcoin)
buton.grid(row=1,column=1)

while True:
    Bitcoin()