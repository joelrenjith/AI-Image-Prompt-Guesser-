import pandas as pd
import urllib, requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import requests

try:
    dic = {'joelrenjith10@gmail.com':'SDDZFYUN','diyx19@gmail.com':'Joel1234','garimangangwani@gmail.com':'HHYUZCVU'}
    ch = random.choice(list(dic))
    print(ch)
    df = pd.read_csv(r'Skribbl-words.csv')
    df_new = (df['word'])
    PATH = Service('C:\Program Files (x86)\chromedriver.exe')
    options = Options()
    options.binary_location = r'C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe'
    options.accept_insecure_certs = True
    driver = webdriver.Chrome( service = PATH,options = options)
    driver.get('https://freeimagegenerator.com/')
    sign = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/nav/div[3]/div/div[2]/ul/li/a"))).click()
    art = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div/a[1]"))).click()
    user = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/form/div/div[1]/input"))).send_keys(ch)
    pswrd = driver.find_element(By.XPATH,"/html/body/div[2]/div/form/div/div[2]/input")
    pswrd.send_keys(dic[ch])
    login  =driver.find_element(By.XPATH,"/html/body/div[2]/div/form/div/div[3]/a")
    login.click()
    head = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/header/div/div/div[1]/a[1]"))).click()
    prompt=  WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div/div[2]/div[2]/div[1]/div[1]/input")))
    l = list(df_new.sample(n=2))
    s=" ".join(l)
    print(s)
    
    prompt.send_keys(s)
    prompt.send_keys(Keys.ENTER)
    img = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div/div[2]/div[6]/button[1]"))).click()
    element = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div[2]/div[4]/a/img")))
    src  = driver.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div[4]/a/img").get_attribute("src")
    print(src+ "\n\n")
    # with open('filename.png', 'wb') as file:
    #     file.write(driver.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div[4]/a/img').screenshot_as_png)
    # head = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/header/div/div/div[1]/a[1]"))).click()
    # prompt =  WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div/div[2]/div[2]/div[1]/div[1]/input")))
    data  = requests.get(src,stream=True)
    
    open('img.jpg','wb').write(data.content)
except Exception as e:
    print(e)
input()
driver.quit()
