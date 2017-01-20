from Tkinter import *

#start
root = Tk()
#



# a frame - invisible rectangle container that you can put things in
    # you can put widgets into the frame
topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

# widgets like button
    # Button (what frame?, what it says, foreground
button1 = Button(topFrame, text="tF Button", fg="#0066ff")
button2 = Button(topFrame, text="tF redButton", fg="red")
button3 = Button(topFrame, text="tF blueButton", fg="blue")
button4 = Button(bottomFrame, text="bF Button", fg="green")

# whenever you pack things in, it gets packed on top of each other
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)



# finish
root.mainloop()
