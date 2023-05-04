# import pandas as pd
# import urllib, requests
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
# import time
# import random
# from socket import socket, gethostbyname, AF_INET, SOCK_DGRAM
# import sys,re
# PORT_NUMBER = 5000
# SIZE = 1024
# hostName = gethostbyname( '0.0.0.0' )
# mySocket = socket( AF_INET, SOCK_DGRAM )
# mySocket.bind( (hostName, PORT_NUMBER) )


# print ("Test server listening on port {0}\n".format(PORT_NUMBER))
# s = "Hello Client"
def convert(copy):
    disp_ans =''
    for i in copy:
        if i == ' ':
            disp_ans+=i+' '
        disp_ans+=i+' '
    return disp_ans

# data,addr = mySocket.recvfrom(SIZE)
# mySocket.sendto('connected'.encode(),(addr))
# print(data.decode())
# print(addr)
# # mySocket.sendto(s.encode(),addr)
# try:
#     dic = {'frixionmaster@gmail.com':'hello12345678','joelrenjith10@gmail.com':'JPYVDTLX','garimangangwani@gmail.com':'CJNYJAMN','diyx19@gmail.com':'JFLBAUEC'}
#     ch = random.choice(list(dic))
#     print(ch)
#     df = pd.read_csv(r'Skribbl-words.csv')
#     df_new = (df['word'])
#     PATH = Service(r'C:\Users\joelr\Downloads\installers\chromedriver_win32\chromedriver.exe')
#     options = Options()
#     options.binary_location = r'C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe'
#     options.accept_insecure_certs = True
#     # options.headless = True
#     driver = webdriver.Chrome( service = PATH,options = options)
#     driver.get('https://freeimagegenerator.com/')
#     print('opened website --> waiting for sign in')
#     sign = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/nav/div[3]/div/div[2]/ul/li/a"))).click()
#     art = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div/a[1]"))).click()
#     user = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/form/div/div[1]/input"))).send_keys(ch)
#     pswrd = driver.find_element(By.XPATH,"/html/body/div[2]/div/form/div/div[2]/input")
#     pswrd.send_keys(dic[ch])
#     login  =driver.find_element(By.XPATH,"/html/body/div[2]/div/form/div/div[3]/a")
#     login.click()
#     print('Sign-in done')
#     head = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/header/div/div/div[1]/a[1]"))).click()
#     prompt=  WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div/div[2]/div[2]/div[1]/div[1]/input")))
#     l = list(df_new.sample(n=2))
#     s=" ".join(l)
#     s= s.lower()
#     print(s)
#     copy = ''
#     prompt.send_keys(s)
#     prompt.send_keys(Keys.ENTER)
#     print('Enterred prompt')
#     img = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div/div[2]/div[6]/button[1]"))).click()
#     print('got results --> waiting for image')
#     element = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div[2]/div[6]/a/img")))
#     src  = driver.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div[6]/a/img").get_attribute("src")

#     print(src+ "\n\n")
#     mySocket.sendto(src.encode('utf-8'),(addr))
#     print('sent img')
#     vowel = ['a','e','i','o','u']
#     s = s.lower()
#     for i in s:
#         if i != ' ':
#             if i not in vowel:
#                 copy+='_'
#             else:
#                 copy+=i
#         else:
#             copy+=i
        
#     print(convert(copy))
#     mySocket.sendto(convert(copy).encode('utf-8'),(addr))
#     print('Sent Prompt String')
#     # with open('filename.png', 'wb') as file:
#     #     file.write(driver.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div[4]/a/img').screenshot_as_png)
#     head =WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/header/div/div/div[1]/a[1]"))).click()
#     # prompt =   WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div/div[2]/div[2]/div[1]/div[1]/input")))
#     while(1):
#         check,addr = mySocket.recvfrom(SIZE)
#         check = check.decode().lower()
#         if check == '__':
#             mySocket.sendto(s.encode('utf-8'),(addr))
#             break
#         if check ==s:
#             msg = 'you goddit!!'
#             mySocket.sendto(msg.encode('utf-8'),(addr))
#             mySocket.sendto(s.encode('utf-8'),(addr))
#             break
#         else:
#             if check in s and len(check)>0:
#                 print(copy)
#                 for m in re.finditer(check, s):
#                     print(check, 'matched from position', m.start(), 'to', m.end())
#                 copy  = copy.replace(copy[m.start():m.end()],check)
#                 print(copy)
#             if copy == s:
#                 msg = 'you goddit!!'
#                 mySocket.sendto(msg.encode('utf-8'),(addr))
#                 mySocket.sendto(s.encode('utf-8'),(addr))
#                 break
#             mySocket.sendto(check.encode('utf-8'),(addr))
#             mySocket.sendto(convert(copy).encode('utf-8'),(addr))
#         # mySocket.sendto(bit.encode('utf-8'),(addr))
        



# except Exception as e:
#     print(e)

# driver.quit()
# quit()
