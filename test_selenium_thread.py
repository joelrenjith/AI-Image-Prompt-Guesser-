import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
# dic = {'frixionmaster@gmail.com':'hello12345678','joelrenjith10@gmail.com':'JPYVDTLX','garimangangwani@gmail.com':'CJNYJAMN','diyx19@gmail.com':'JFLBAUEC'}
# ch = random.choice(list(dic))
# print(ch)
# df = pd.read_csv(r'Skribbl-words.csv')
# df_new = (df['word'])
# PATH = Service('C:\Program Files (x86)\chromedriver.exe')
# options = Options()
# options.binary_location = r'C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe'
# options.accept_insecure_certs = True
# options.headless = True
# driver = webdriver.Chrome( service = PATH,options = options)
# driver.get('https://freeimagegenerator.com/')
# print('opened website --> waiting for sign in')
# sign = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/nav/div[3]/div/div[2]/ul/li/a"))).click()
# art = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div/a[1]"))).click()
# user = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/form/div/div[1]/input"))).send_keys(ch)
# pswrd = driver.find_element(By.XPATH,"/html/body/div[2]/div/form/div/div[2]/input")
# pswrd.send_keys(dic[ch])
# login  =driver.find_element(By.XPATH,"/html/body/div[2]/div/form/div/div[3]/a")
# login.click()
# print('Sign-in done')
# head = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/header/div/div/div[1]/a[1]"))).click()
# prompt=  WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div/div[2]/div[2]/div[1]/div[1]/input")))
# l = list(df_new.sample(n=2))
# s=" ".join(l)
# s= s.lower()
# print(s)
# copy = ''
# prompt.send_keys(s)
# prompt.send_keys(Keys.ENTER)
# print('Enterred prompt')
# img = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div/div[2]/div[6]/button[1]"))).click()
# print('got results --> waiting for image')
# element = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div[2]/div[6]/a/img")))
# src  = driver.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div[6]/a/img").get_attribute("src")

# print(src+ "\n\n")
# import pandas as pd
# df = pd.read_csv(r'words&imgs.csv')
# # df1 = pd.DataFrame({'string':['apple'],'img_link': ['gay']})
# # df1.to_csv(r'words&imgs.csv',mode='a', index=False, header=False)
# print(df)
# df = df.drop(0)
# print("\n\n",df)
# df.to_csv(r'words&imgs.csv',index=False)
# # print

try:

    dic = {'frixionmaster@gmail.com':'hello12345678','joelrenjith10@gmail.com':'JPYVDTLX','garimangangwani@gmail.com':'CJNYJAMN','diyx19@gmail.com':'JFLBAUEC'}
    ch = random.choice(list(dic))

    df = pd.read_csv('Skribbl-words.csv')
    df_new = (df['word'])

    #df = pd.read_csv(r'words&imgs.csv')

    PATH = Service('C:\Program Files (x86)\chromedriver.exe')
    options = Options()
    #options.binary_location = r'C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe'
    options.accept_insecure_certs = True
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--allow-running-insecure-content')
    #options.headless = True
    driver = webdriver.Chrome( service = PATH,options = options)
    driver.get('https://freeimagegenerator.com/')
    print('opened website --> waiting for sign in')

    sign = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/nav/div[3]/div/div[2]/ul/li/a"))).click()
    art = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div/a[1]"))).click()
    user = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/form/div/div[1]/input"))).send_keys(ch)
    pswrd = driver.find_element(By.XPATH,"/html/body/div[2]/div/form/div/div[2]/input")
    pswrd.send_keys(dic[ch])
    login  =driver.find_element(By.XPATH,"/html/body/div[2]/div/form/div/div[3]/a")
    login.click()
    print('Sign-in done')

    head = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/header/div/div/div[1]/a[1]"))).click()

    i = 1
    temp =[]

    def generateString(x):
        l = list(x.sample(n=2))
        s=" ".join(l)
        return s

    while(i<5):
        s = generateString(df_new)
        if i>1:
            retry = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div[1]/div/a")))
            retry.click()
        prompt=  WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div/div[2]/div[2]/div[1]/div[1]/input")))
        prompt.send_keys(s)
        prompt.send_keys(Keys.ENTER)
        print('Enterred prompt')
        img = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div/div[2]/div[6]/button[1]"))).click()
        print('got results --> waiting for image')
        element = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div[2]/div[4]/a/img")))
        src  = driver.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div[4]/a/img").get_attribute("src")
        print(src+ "\n\n")
        #print(src+ "\n\n")
        entry = {'string':s,'link':src}
        temp.append(entry)
        df = pd.DataFrame(temp)
        df.to_csv('cn_project_1\words&imgs.csv',index=False)
        print(f'added image {i}')
        i+=1

except Exception as e:
    print(e)
