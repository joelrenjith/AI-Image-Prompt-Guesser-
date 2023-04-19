import sys
from socket import socket, AF_INET, SOCK_DGRAM
import requests
import PIL.Image
from PIL import ImageTk
from tkinter import *
from tkinter import messagebox,ttk
import tkinter.font as tkFont
import time
import threading
I_C=-1
#SERVER_IP   = '192.168.11.197'
SERVER_IP   = '127.0.0.1'
PORT_NUMBER = 5000
SIZE = 1024
bit = 0
print ("Test client sending packets to IP {0}, via port {1}\n".format(SERVER_IP, PORT_NUMBER))

mySocket = socket( AF_INET, SOCK_DGRAM )
myMessage = "Hello!"
#myMessage1 = ""
#i = 0
# while i < 10:
#     mySocket.sendto(myMessage.encode('utf-8'),(SERVER_IP,PORT_NUMBER))
#     i = i + 1

# mySocket.sendto(myMessage.encode('utf-8'),(SERVER_IP,PORT_NUMBER))
# #mySocket.sendto(myMessage1.encode('utf-8'),(SERVER_IP,PORT_NUMBER))
# data,addr = mySocket.recvfrom(1024)
# print(data.decode())
# data,addr = mySocket.recvfrom(1024)
# img_link = data.decode()
# r = requests.get(img_link,allow_redirects=True)
# open('img.jpg','wb').write(r.content)
# ans,addr=mySocket.recvfrom(1024)
# print(ans.decode())
# print(1)


def listen():
    while(1):
        msg  = mySocket.recv(SIZE).decode()
        if(msg.isdigit()):
            num=int(msg)
            for i in range(0,num):
                players.insert(END,mySocket.recv(SIZE).decode())
        else:
            if(msg=='ready'):
                ind=int(mySocket.recv(SIZE).decode())
                players.itemconfig(ind,{'fg':'Green'})
            elif(msg=='__'):
                t=10
                temp= "Game starting in "
                tempend=" seconds"
                while(t!=0):
                    if(t==1):
                        tempend="second"
                    heading.set(temp+str(t)+tempend)
                    load.update()
                    time.sleep(1)
                    t=t-1
                return
            else:
                print('recieved name')
                players.insert(END,msg)
        

def load_dummyfunc(e):
    submituser()

def submit():
    global I_C
    I_C=I_C +1
    submitted=inp.get()
    mySocket.sendto(submitted.encode('utf-8'),(SERVER_IP,PORT_NUMBER))
    # bit,addr=mySocket.recvfrom(1024)
    msg,addr=mySocket.recvfrom(1024)
    msg = msg.decode()
    listbox.insert(END, msg)
    # print(msg ,"\n", inp.get())
    if msg!=submitted:
        global bit
        bit = 1
        listbox.itemconfig(I_C,{'fg':'Green'})
        correct,addr = mySocket.recvfrom(1024)
        messagebox.showinfo('Game over','Answer = '+correct.decode())
        root.destroy()
        quit()
    board ,addr = mySocket.recvfrom(1024)
    print("new =",board.decode())
    show_prmpt.set(board.decode())
    root.update()
    inp.delete(0, END)

def dummyfunc(e):
    submit()

def updatetime():
    global bit
    t = 90
    global my_var
    my_var.set(str(t))

    while(t!=0):
        if bit ==1:
            return
        root.update()
        t = t-1
        my_var.set(str(t))
        time.sleep(1)
    mySocket.sendto(('__').encode('utf-8'),(SERVER_IP,PORT_NUMBER))
    correct,addr = mySocket.recvfrom(1024)
    # correct = correct.decode()

    messagebox.showinfo('TIMES UP!','Answer = '+correct.decode()) 
    root.destroy()
    quit() 

def on_resize(e):
    ph = PIL.Image.open('background.png') # load the background image
    #l = Label(root)
    imgb = ph.resize((root.winfo_screenheight(), root.winfo_screenwidth()))# update the image of the label
    bgimg = ImageTk.PhotoImage(imgb)
    l = Label(root, image=bgimg)
    l.config(image=bgimg)
    print("///////////////////////////////////\n")
    print("The width of Root window:", root.winfo_width())
    print("\nThe height of Root window:", root.winfo_height())
    print("\n///////////////////////////////////\n")

def on_resize_loading(event):
    phl = PIL.Image.open('background.png') # load the background image
    #l = Label(root)
    imgbl = phl.resize((load.winfo_screenheight(), load.winfo_screenwidth()))# update the image of the label
    bgimgl = ImageTk.PhotoImage(imgbl)
    lo = Label(load, image=bgimgl)
    lo.config(image=bgimgl)
    print("///////////////////////////////////\n")
    print("The width of loading window:", load.winfo_width())
    print("\nThe height of loading window:", load.winfo_height())
    print("\n///////////////////////////////////\n")

def submituser():
    submitted=eyusn.get()
    mySocket.sendto(submitted.encode('utf-8'),(SERVER_IP,PORT_NUMBER))
    t1 = threading.Thread(target=listen)
    t1.start()
    t1.join()
    nextwindow()


def nextwindow():
    load.destroy()



    ##################################################################################

    '''






    Ongoing work: Loading Screen for multiplayer




    '''


load=Tk()
sz28 = tkFont.Font(size=28)
sz35 = tkFont.Font(size=35)
load.title("Waiting Stage")
load.geometry("848x666")
heading = StringVar()

phl = PIL.Image.open('background.png') # load the background image
#l = Label(root)
imgbl = phl.resize((load.winfo_screenheight(), load.winfo_screenwidth()))# update the image of the label
bgimgl = ImageTk.PhotoImage(imgbl)
lo = Label(load, image=bgimgl)
lo.config(image=bgimgl)
lo.place(x=0, y=0, relwidth=1, relheight=1) # make label l to fit the parent window always
lo.bind('<Configure>', on_resize_loading) # on_resize will be executed whenever label l is resized

heading.set("Guess the Prompt")

top_frame = Label(load, textvariable=heading, width=30, height=1,font=sz35) 
top_frame.grid(row=0, column=0, padx=15, pady=15)

inp_frame = LabelFrame(load, text="Enter Your Username", width=15, height=1)
inp_frame.grid(row=1, column=0, padx=15, pady=15)

eyusn=Entry(inp_frame, width=20)
Submit= Button(inp_frame,text="Submit", width=15, command=submituser)

load.bind('<Return>',load_dummyfunc)

eyusn.grid(row=0)
Submit.grid(row=1,pady=5)

subframe= Frame(load, width = 40, height= 40)
subframe.grid(row=2, column=0, padx=15, pady=15)

players = Listbox(subframe, width=55, height=30)
  
# Adding Listbox to the left
# side of root window
players.pack(side=LEFT, fill = BOTH, expand=True)
  
# Creating a Scrollbar and 
# attaching it to root window
scrollbar = Scrollbar(subframe)
  
# Adding Scrollbar to the right
# side of root window
scrollbar.pack(side = RIGHT, fill = BOTH) 
#scrollbar.grid(row=0, column=1, sticky=NS)


players.config(yscrollcommand = scrollbar.set)

scrollbar.config(command = players.yview)


ready=Button(load,text="Ready?",command=nextwindow,width=10)
ready.grid(row=3, column=0,padx=15,pady=15)
load.mainloop()

    #time.sleep(2)


    ##################################################################################


# root = Tk()  # create root window
# sz28 = tkFont.Font(size=28)
# sz35 = tkFont.Font(size=35)
# my_var = StringVar()
# show_prmpt = StringVar()
# root.title("Guess the Prompt")  # title of the GUI window
# root.maxsize(1300, 1300)  # specify the max size the window can expand to

# ph = PIL.Image.open('background.png') # load the background image
# #l = Label(root)
# imgb = ph.resize((root.winfo_screenheight(), root.winfo_screenwidth()))# update the image of the label
# bgimg = ImageTk.PhotoImage(imgb)
# l = Label(root, image=bgimg)
# l.config(image=bgimg)
# l.place(x=0, y=0, relwidth=1, relheight=1) # make label l to fit the parent window always
# l.bind('<Configure>', on_resize) # on_resize will be executed whenever label l is resized
#   # specify background color


# root.bind('<Return>',dummyfunc)
# # Create left,right and top frames
# top_frame = LabelFrame(root, text="Guess the Prompt", width=800, height=100) 
# top_frame.grid(row=0, column=0, padx=10, pady=10)

# subframe= Frame(root, width = 700, height= 400)
# subframe.grid(row=1, column=0, padx=10, pady=10)

# left_frame = LabelFrame(subframe, text="Image:", width=450, height=300)
# left_frame.grid(row=0, column=0, padx=2, pady=2)

# show_prmpt.set((ans.decode()))
# # load image to be "edited"
# image  = PIL.Image.open("img.jpg")
# resize_image = image.resize((450,500))
# img = ImageTk.PhotoImage(resize_image)
# print(ans.decode())
# # Display image in right_frame
# user_name = Label(top_frame,textvariable=show_prmpt, font=sz28).grid(row=0,column=0, padx=10, pady=10)

# timr = Label(top_frame,textvariable=my_var,fg='Red', font=sz35)
# timr.grid(row = 0,column=1, padx=10, pady=10)
# Label(left_frame, image=img).grid(row=0,column=0, padx=5, pady=5)

# right_frame = LabelFrame(subframe, text="Chat", width=200, height=500)
# right_frame.grid(row=0, column=1, padx=2, pady=2)

# history = Frame(right_frame, width=350, height=400, bg='#E2E5DE')
# history.grid(row=0, column=0)

# inpframe = Frame(right_frame, width=200, height=400)
# inpframe.grid(row=1, column=0, padx=1, pady=1)

# inp = Entry(inpframe, width=50)
# inp.grid(row=1, column=0, padx=1, pady=1)

# send = Button(inpframe, text="Submit", bg='#E2E5DE', command=submit)
# send.grid(row=1, column=1, padx=1, pady=1)




# listbox = Listbox(history, width=55, height=30)

# # Adding Listbox to the left
# # side of root window
# listbox.pack(side = LEFT, fill = BOTH, expand=True)

# # Creating a Scrollbar and 
# # attaching it to root window
# scrollbar = Scrollbar(history)

# # Adding Scrollbar to the right
# # side of root window
# scrollbar.pack(side = RIGHT, fill = BOTH) 
    
# listbox.config(yscrollcommand = scrollbar.set)

# scrollbar.config(command = listbox.yview)



# t1 = threading.Thread(target=updatetime)
# t1.start()
# root.mainloop()
