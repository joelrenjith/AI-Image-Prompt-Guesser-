import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from csv import DictWriter
from socket import socket, gethostbyname, AF_INET, SOCK_DGRAM
import os
import pandas as pd
from test_selenium_thread import sel_thread
from threading import Thread
from server import convert
import re
PORT_NUMBER = 5000
SIZE = 1024

hostName = gethostbyname( '0.0.0.0' )
mySocket = socket( AF_INET, SOCK_DGRAM )
mySocket.bind( (hostName, PORT_NUMBER) )
print ("Test server listening on port {0}\n".format(PORT_NUMBER))
item = []
players = {}
bit  = 0
c = 0
ready_list = []
def listen():
    global bit,players
    while(1):
        if bit ==1:
            sendeveryone('__')
            return
        msg,id = mySocket.recvfrom(SIZE)
        msg = msg.decode()
        if bit ==0:
            if msg!='1':
                lobby(id,msg)
                if len(players) ==1:
                    t1 = Thread(target = img_get)
                    t1.start()
            else:
                ready(id)

def generateString(x):
                l = list(x.sample(n=2))
                s=" ".join(l)
                return s   
def img_get():
    global item
    try:
        PATH = Service('C:\Program Files (x86)\chromedriver.exe')
        options = Options()
        #options.binary_location = r'C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe'
        options.accept_insecure_certs = True
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--allow-running-insecure-content')
        options.binary_location = r'C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe'
    
       
        dic = {'frixionmaster@gmail.com':'hello12345678','joelrenjith10@gmail.com':'JPYVDTLX','garimangangwani@gmail.com':'CJNYJAMN','diyx19@gmail.com':'JFLBAUEC'}
        ch = random.choice(list(dic))

        df = pd.read_csv('Skribbl-words.csv')
        df_new = (df['word'])

        #df = pd.read_csv('cn_project_1\words&imgs.csv')
        titles = ['string','link']

        
        # options.headless = True
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
        

    
        for i in range(0,3):
            head = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/header/div/div/div[1]/a[1]"))).click()

            i = 1
            

            

            
            s = generateString(df_new)
            print(s)
            if i>1:
                retry = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div[1]/div/a")))
                retry.click()
            prompt=  WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div/div[2]/div[2]/div[1]/div[1]/input")))
            prompt.clear()
            prompt.send_keys(s)
            prompt.send_keys(Keys.ENTER)
            print('Enterred prompt')
            img = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div/div[2]/div[6]/button[1]"))).click()
            print('got results --> waiting for image')
            element = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div[2]/div[4]/a/img")))
            src  = driver.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div[4]/a/img").get_attribute("src")
            print(src+ "\n\n")
            #print(src+ "\n\n")
            # entry = {'string':s,'link':src}
            # # with open('words&imgs.csv','a',newline='') as f_object:
            # #         writerObject = DictWriter(f_object,fieldnames=titles)
            # #         writerObject.writerow(entry)
            # #         f_object.close()
            # # print(f'added image {i}')
            
            l  = [s,src]
            item.append(list(l))
            print(item)
    except Exception as e:
        print(e)
        return ('error occured on test_selenium_thread.py')
    driver.quit()
def sendeveryone(msg):
    global players
    for id in players:
        mySocket.sendto(msg.encode(),id)       
        

# def sel_thread():
    
#     try:

#         dic = {'frixionmaster@gmail.com':'hello12345678','joelrenjith10@gmail.com':'JPYVDTLX','garimangangwani@gmail.com':'CJNYJAMN','diyx19@gmail.com':'JFLBAUEC'}
#         ch = random.choice(list(dic))

#         df = pd.read_csv('Skribbl-words.csv')
#         df_new = (df['word'])

#         #df = pd.read_csv('cn_project_1\words&imgs.csv')
#         titles = ['string','link']

#         PATH = Service('C:\Program Files (x86)\chromedriver.exe')
#         options = Options()
#         #options.binary_location = r'C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe'
#         options.accept_insecure_certs = True
#         options.add_argument('--ignore-certificate-errors')
#         options.add_argument('--allow-running-insecure-content')
#         options.headless = True
#         driver = webdriver.Chrome( service = PATH,options = options)
#         driver.get('https://freeimagegenerator.com/')
#         print('opened website --> waiting for sign in')

#         sign = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/nav/div[3]/div/div[2]/ul/li/a"))).click()
#         art = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div/a[1]"))).click()
#         user = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/form/div/div[1]/input"))).send_keys(ch)
#         pswrd = driver.find_element(By.XPATH,"/html/body/div[2]/div/form/div/div[2]/input")
#         pswrd.send_keys(dic[ch])
#         login  =driver.find_element(By.XPATH,"/html/body/div[2]/div/form/div/div[3]/a")
#         login.click()
#         print('Sign-in done')

#         head = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/header/div/div/div[1]/a[1]"))).click()

#         i = 1
        

#         def generateString(x):
#             l = list(x.sample(n=2))
#             s=" ".join(l)
#             return s

#         while(i<3):
#             s = generateString(df_new)
#             print(s)
#             if i>1:
#                 retry = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div[1]/div/a")))
#                 retry.click()
#             prompt=  WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div/div[2]/div[2]/div[1]/div[1]/input")))
#             prompt.clear()
#             prompt.send_keys(s)
#             prompt.send_keys(Keys.ENTER)
#             print('Enterred prompt')
#             img = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div/div[2]/div[6]/button[1]"))).click()
#             print('got results --> waiting for image')
#             element = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div[2]/div[4]/a/img")))
#             src  = driver.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div[4]/a/img").get_attribute("src")
#             print(src+ "\n\n")
#             #print(src+ "\n\n")
#             entry = {'string':s,'link':src}
#             with open('words&imgs.csv','a',newline='') as f_object:
#                     writerObject = DictWriter(f_object,fieldnames=titles)
#                     writerObject.writerow(entry)
#                     f_object.close()
#             print(f'added image {i}')
#             i = i+1

#     except Exception as e:
#         print(e)
#         input()
#         driver.quit()


def lobby(id,username):
    global players
    if id not in players:
        mySocket.sendto(str(len(players)).encode(),id)
        for i in players:
            mySocket.sendto(players[i].encode(),id)
        mySocket.sendto(str(ready_list).encode(),id)

        players[id] = username
        # os.system('cls')

        
        print(id,':',username)
        sendeveryone(username)
        print('sent lobby')
        
       
        

def ready(id):
    global players,c,bit,ready_list
    print('recived a ready from',players[id])

    if id in players:
        c+=1
        sendeveryone('ready')
        sendeveryone(str(list(players).index(id)))
        ready_list.append(str(list(players).index(id)))
        if c == len(players):
            bit = 1

def start_game():
    global players,item
    
    leaderboard = {}
    for i in players:
        leaderboard[players[i]] = 0
    print('game started')
    df = pd.read_csv('words&imgs.csv')
    for x in range(0,3):
        # item = sel_thread()
        while(1):
            try:
                data = item[x]
            except Exception as e:

                continue
            else:
                break
        if type(item)==str:
            print(item)
            quit()
        print(item)
        point = len(players)
        s = data[0]
        # print(s)
        img_link = data[1]
        # print(img_link)
        copy = ''
        vowel = ['a','e','i','o','u']
        for i in s:
            if i != ' ':
                if i not in vowel:
                    copy+='_'
                else:
                    copy+=i
            else:
                copy+=i
        
        
        sendeveryone(img_link)
        print('sent img')
        sendeveryone(convert(copy))
        print('sent string')
        while(1):
            check,addr = mySocket.recvfrom(SIZE)
            check = check.decode().lower()
            if check == '__':
                sendeveryone("finish")
                sendeveryone(s)
                sendeveryone(str(leaderboard))
                break
            if check ==s:
                leaderboard[players[addr]] += point
                point = point - 1
                msg = players[addr]+' goddit!!'
                sendeveryone("goddit")
                sendeveryone(msg)
                # mySocket.sendto(s.encode('utf-8'),(addr))
                if point ==0:
                    sendeveryone("finish")
                    sendeveryone(s)
                    sendeveryone(str(leaderboard))
                    break
            else:
                if check in s and len(check)>0:
                    print(copy)
                    for m in re.finditer(check, s):
                        print(check, 'matched from position', m.start(), 'to', m.end())
                    copy  = copy.replace(copy[m.start():m.end()],check)
                    print(copy)
                if copy == s:
                    # mySocket.sendto(s.encode('utf-8'),(addr))
                    leaderboard[players[addr]] += point
                    point = point - 1
                    msg = players[addr]+' goddit!!'
                    sendeveryone("goddit")
                    sendeveryone(msg)
                    # mySocket.sendto(s.encode('utf-8'),(addr))
                    if point ==0:
                        sendeveryone("finish")
                        sendeveryone(s)
                        sendeveryone(str(leaderboard))
                        break
                else:
                    sendeveryone("msg")    
                    sendeveryone(players[addr]+' : '+check)
                mySocket.sendto("new_pr".encode('utf-8'),(addr))
                mySocket.sendto(convert(copy).encode('utf-8'),(addr))
    sendeveryone('!!')    
    
listen()
start_game()
    



