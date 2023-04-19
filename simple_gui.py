# from tkinter import *

# root = Tk()  # create root window
# root.title("Basic GUI Layout")  # title of the GUI window
# root.maxsize(1300, 600)  # specify the max size the window can expand to
# root.config(bg="skyblue")  # specify background color

# # Create left and right frames
# left_frame = Frame(root, width=200, height=400, bg='#D3D3D3')
# left_frame.grid(row=0, column=0, padx=10, pady=5)

# right_frame = Frame(root, width=650, height=400, bg='#D3D3D3')
# right_frame.grid(row=0, column=1, padx=10, pady=5)

# # Create frames and labels in left_frame
# Label(left_frame, text="Original Image").grid(row=0, column=0, padx=5, pady=5)

# # load image to be "edited"
# image = PhotoImage(file="intermediate_python\images\harry_maguire.gif")
# original_image = image.subsample(3,3)  # resize image using subsample
# Label(left_frame, image=original_image).grid(row=1, column=0, padx=5, pady=5)

# # Display image in right_frame
# Label(right_frame, image=image).grid(row=0,column=0, padx=5, pady=5)

# # Create tool bar frame
# tool_bar = Frame(left_frame, width=180, height=185)
# tool_bar.grid(row=2, column=0, padx=5, pady=5)

# # Example labels that serve as placeholders for other widgets
# Label(tool_bar, text="Tools", relief=RAISED).grid(row=0, column=0, padx=5, pady=3, ipadx=10)  # ipadx is padding inside the Label widget
# Label(tool_bar, text="Filters", relief=RAISED).grid(row=0, column=1, padx=5, pady=3, ipadx=10)

# # Example labels that could be displayed under the "Tool" menu
# Label(tool_bar, text="Select").grid(row=1, column=0, padx=5, pady=5)
# Label(tool_bar, text="Crop").grid(row=2, column=0, padx=5, pady=5)
# Label(tool_bar, text="Rotate & Flip").grid(row=3, column=0, padx=5, pady=5)
# Label(tool_bar, text="Resize").grid(row=4, column=0, padx=5, pady=5)
# Label(tool_bar, text="Exposure").grid(row=5, column=0, padx=5, pady=5)
# root.mainloop()

import time
import PIL.Image
from PIL import Image, ImageTk
from tkinter import *
import tkinter.font as tkFont
from threading import Thread
ans = 'a__e_I a__e'
def addtohistory():
    listbox.insert(END, inp.get())
    inp.delete(0, END)

def updatetime():
    t = 60
    global my_var
    my_var.set(str(t))
   
    while(t!=0):
        root.update()
        t = t-1
        my_var.set(str(t))
        time.sleep(1)

def on_resize(event):
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
    print("The width of laoding window:", load.winfo_width())
    print("\nThe height of loading window:", load.winfo_height())
    print("\n///////////////////////////////////\n")
    
def nextwindow():
    load.destroy()

load=Tk()
sz28 = tkFont.Font(size=28)
sz35 = tkFont.Font(size=35)
load.title("Waiting Stage")
load.geometry("848x666")

phl = PIL.Image.open('background.png') # load the background image
#l = Label(root)
imgbl = phl.resize((load.winfo_screenheight(), load.winfo_screenwidth()))# update the image of the label
bgimgl = ImageTk.PhotoImage(imgbl)
lo = Label(load, image=bgimgl)
lo.config(image=bgimgl)
lo.place(x=0, y=0, relwidth=1, relheight=1) # make label l to fit the parent window always
lo.bind('<Configure>', on_resize_loading) # on_resize will be executed whenever label l is resized

top_frame = Label(load, text="Guess the Prompt", width=30, height=1,font=sz35) 
top_frame.grid(row=0, column=0, padx=15, pady=15)
subframe= Frame(load, width = 40, height= 40)
subframe.grid(row=1, column=0, padx=15, pady=15)

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
ready.grid(row=2, column=0,padx=15,pady=15)
load.mainloop()

time.sleep(2)


root = Tk()  # create root window
sz28 = tkFont.Font(size=28)
sz35 = tkFont.Font(size=35)
my_var = StringVar()
show_prmpt = StringVar()
root.title("Guess the Prompt")  # title of the GUI window
root.maxsize(1300, 1300)  # specify the max size the window can expand to


ph = PIL.Image.open('background.png') # load the background image
#l = Label(root)
imgb = ph.resize((root.winfo_screenheight(), root.winfo_screenwidth()))# update the image of the label
bgimg = ImageTk.PhotoImage(imgb)
l = Label(root, image=bgimg)
l.config(image=bgimg)
l.place(x=0, y=0, relwidth=1, relheight=1) # make label l to fit the parent window always
l.bind('<Configure>', on_resize) # on_resize will be executed whenever label l is resized


root.bind('<Return>',addtohistory)
# Create left,right and top frames
top_frame = LabelFrame(root, text="Guess the Prompt", width=800, height=100)
top_frame.grid(row=0, column=0, padx=10, pady=10)
user_name = Label(top_frame,text = ans, font=sz28).grid(row=0,column=0, padx=10, pady=10)
timr = Label(top_frame,textvariable=my_var,fg='Red', font=sz35)
timr.grid(row = 0,column=1, padx=10, pady=10)

subframe= Frame(root, width = 700, height= 400)
subframe.grid(row=1, column=0, padx=10, pady=10)

left_frame = LabelFrame(subframe, text="Image:", width=450, height=300)
left_frame.grid(row=0, column=0, padx=2, pady=2)

right_frame = LabelFrame(subframe, text="Chat", width=200, height=500)
right_frame.grid(row=0, column=1, padx=2, pady=2)

history = Frame(right_frame, width=350, height=400, bg='#E2E5DE')
history.grid(row=0, column=0)

inpframe = Frame(right_frame, width=200, height=400)
inpframe.grid(row=1, column=0, padx=1, pady=1)

inp = Entry(inpframe, width=50)
inp.grid(row=1, column=0, padx=1, pady=1)

send = Button(inpframe, text="Submit", bg='#E2E5DE', command=addtohistory)
send.grid(row=1, column=1, padx=1, pady=1)

# load image to be "edited"
image  = PIL.Image.open("img.jpg")
resize_image = image.resize((450,500))
img = ImageTk.PhotoImage(resize_image)
# Display image in right_frame
Label(left_frame, image=img).grid(row=0,column=0, padx=5, pady=5)


listbox = Listbox(history, width=55, height=30)
  
# Adding Listbox to the left
# side of root window
listbox.pack(side = LEFT, fill = BOTH, expand=True)
  
# Creating a Scrollbar and 
# attaching it to root window
scrollbar = Scrollbar(history)
  
# Adding Scrollbar to the right
# side of root window
scrollbar.pack(side = RIGHT, fill = BOTH) 
      
listbox.config(yscrollcommand = scrollbar.set)
  
scrollbar.config(command = listbox.yview)
t1 = Thread(target= updatetime)
t1.start()
root.mainloop()