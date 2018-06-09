from keras.models import load_model
import cv2
import numpy as np
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter import StringVar
from tkinter import Entry

#This creates the main window of an application
window = tk.Tk()
window.title("Join")
window.geometry("900x900")
window.configure(background='grey')

frame = tk.Frame(window, bg='black')
frame.pack(fill='both', expand='yes')

path = filedialog.askopenfilename()
img = ImageTk.PhotoImage(Image.open(path))

#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(frame, image = img)
panel.place(x=100,y=20)
#The Pack geometry manager packs widgets in rows or columns.
#panel.pack(side = "bottom", fill = "both", expand = "yes")
#mainFrame = tk.Frame(window)
#mainFrame.grid()
#entryFrame = tk.Frame(mainFrame, width=454, height=20)
#entryFrame.grid(row=0, column=1)



#v = StringVar()
#e = Entry(frame, textvariable=v, width=200)
#e.place(x=20,y=700)
#e.pack(ipady=3)

model = load_model('model3.h5')

model.compile(loss='categorical_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

# Set the path of the image to be classified
img1 = cv2.imread(path)
font = cv2.FONT_HERSHEY_SIMPLEX

while True:
    cv2.namedWindow("show",0)
    new_img = img1.copy()
    new_img = cv2.resize(new_img,(150,150))
    new_img = np.reshape(new_img,[1,150,150,3])
    cv2.putText(img1,'OpenCV',(5,160), font, 0.5,(255,0,0),1,cv2.LINE_AA)
    cla = model.predict_classes(new_img)
    #v.set("a default value")
    print (cla[0])
    if(cla[0] == 1):
        label = tk.Label(frame, text="Alert! You're turning towards the right & texting instead of concentrating on driving straight.  ")
        label.place(x=100, y=600)
        #v.set ("This image can be described as a bar chart which represents data with rectangular bars with heights proportional to the values that they represent.")
    elif(cla[0] == 2):
        label = tk.Label(frame, text="Alert! You're turning towards the right & talking over phone instead of concentrating on driving straight.")
        label.place(x=100, y=600)
        #v.set ("This image is a graph of a function. It has x and y axes with curves and lines depicting a function.")
    elif(cla[0] == 3):
        label = tk.Label(frame, text="Alert! You're turning towards the left & texting instead of concentrating on driving straight.")
        label.place(x=100, y=600)
        #v.set ("This image has a geometrical figure.")
    elif(cla[0] == 4):
        label = tk.Label(frame, text="Alert! You're turning towards the left & talking over phone instead of concentrating on driving straight.")
        label.place(x=100, y=600)
        #v.set ("This image is a line graph in which information is displayed as a series of data points connected by straight line segments.")
    elif(cla[0] == 5):
        label = tk.Label(frame, text="Alert! You're operating on the radio instead of concentrating on driving straight. ")
        label.place(x=100,y=600)
        #v.set ("This image is a mapping of function which shows the relations of inputs and output in form of ordered pair. ")
    elif(cla[0] == 6):
        label = tk.Label(frame, text="Alert! You're drinking instead of concentrating on driving straight.")
        label.place(x=100, y=600)
        #v.set ("This image doesnot belong to any mathematical representation or figures.")                                                                                   
    elif(cla[0] == 7):
        label = tk.Label(frame, text="Alert! You're reaching behind instead of concentrating on driving straight.")
        label.place(x=100, y=600)
        #v.set ("This image is a pie chart, a circle which is divided into sectors that each represent a proportion of the whole.")
    elif(cla[0] == 8):
        label = tk.Label(frame, text="Alert! You're preoccupied with the mirror instead of concentrating on driving straight.")
        label.place(x=100, y=600)
        #v.set ("This image is a graph with x and y axes where points are plotted and drawn.")
    elif(cla[0] == 9):
        label = tk.Label(frame, text="Alert! You're talking with the passenger instead of concentrating on driving straight.")
        label.place(x=100, y=600)
    elif(cla[0] == 0):
        label = tk.Label(frame, text="You're driving attentively.")
        label.place(x=350, y=600)
        #v.set ("This image is a venn diagram in which logical sets represented as circles or closed curves within an enclosing rectangle,the universal set.")
    cv2.imshow("show",img1)

    #Start the GUI
    window.mainloop()
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break

def write(string):
    text_box.config(state=Tkinter.NORMAL)
    text_box.insert("end", string + "\n")
    text_box.see("end")
    text_box.config(state=Tkinter.DISABLED)