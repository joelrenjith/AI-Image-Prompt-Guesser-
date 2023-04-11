from tkinter import *
mas = Tk()
# from time import time
import time
# start = time()
import threading

my_var = StringVar()
my_var1 = StringVar()
def tmr():
    t = 10
    my_var.set(str(t))
    label = Label(mas,textvariable=my_var,fg="red")
    label.pack()
    while(t!=0):
        mas.update()
        t = t-1
        my_var.set(str(t))
        time.sleep(1)

def rmt():
    t = 0
    my_var1.set(str(t))
    label1 = Label(mas,textvariable=my_var1,fg="red")
    label1.pack()
    while(t!=10):
        mas.update()
        t = t+1
        my_var1.set(str(t))
        time.sleep(1)
# label = Label(mas,text="Submit",command = cha
# label.pack()


 

    # creating thread
t1 = threading.Thread(target=tmr)
t2 = threading.Thread(target=rmt)

# starting thread 1
t1.start()
# starting thread 2
t2.start()

# wait until thread 1 is completely executed


# both threads completely executed
print("Done!")
mas.mainloop()