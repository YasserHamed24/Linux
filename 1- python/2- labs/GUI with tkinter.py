from tkinter import *

def func():
    print("Yasser was here!")

def ButtonPressTracker():
    ButtonPressTracker.counter +=1
    print("pressed : ", ButtonPressTracker.counter)

ButtonPressTracker.counter = 0

window_1 = Tk()

window_1.title("hello from tkinter")

window_1.geometry('400x400')

photo_1 = PhotoImage(file='jack.png')
photo_2 = PhotoImage(file='jack2.png')

photo_1 = photo_1.subsample(5,5)
photo_2 = photo_2.subsample(5,5)

# label_1 = Label(window_1 , text = "Yasser")
# label_2 = Label(window_1 , text = "Hamed")

# label_1.pack(side = TOP)
# label_2.pack(side = TOP)

b1 = Button(window_1 , text = "TOP" ,bd= '5' , command= window_1.destroy)

b2 = Button(window_1 ,bd= '10' , text = "BOTTOM" , command= func)

b3 = Button(window_1 , text = "LEFT" , bd= '3' , image = photo_1 , command= ButtonPressTracker)

b4 = Button(window_1 , text = "RIGHT" , bd= '3' , image = photo_1 , command= ButtonPressTracker)

b1.pack(side= TOP)
b2.pack(side= BOTTOM)
b3.pack(side= LEFT)
b4.pack(side= RIGHT)

window_1.mainloop()