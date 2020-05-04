from tkinter import *
from tkinter import simpledialog, Button, messagebox
import os

root = Tk()
root.geometry("600x900")
root.title("Dictionary")
c = Canvas(root, width=600, height=133, bg="white", cursor="draft_large")
c.pack()

def submit():   
        s = e.get()
        if os.path.exists(s+".txt") == True:
                file1 = open(s+".txt", "r")
                contents = file1.read()
                global conts
                conts = Label(root, text=contents)
                conts.pack()
        
        else:
                messagebox.showinfo("ERROR", s+" does not exist in our database. Please fill out the following information")
                defi = simpledialog.askstring("Defention", "Please enter the defenition of "+s)
                fname = open(s+'.txt', 'w')
                fname.write(defi)
                messagebox.showinfo("Thanks", "Thank you for imporving our database!")
                messagebox.showinfo("Success", s+" has been succesfully created, with the defenition of: "+defi)


def clear():
    conts.forget()

def nwd():
        word = simpledialog.askstring("New Word", "Enter the word")
        if os.path.exists(word+'.txt') == False:
                defenition = simpledialog.askstring("New Word", "Enter defenition")
                wfile = open(word+'.txt', 'w')
                wfile.write(defenition)
                messagebox.showinfo("Thank You", "Thank you for helping us with out database")
        elif os.path.exists(word+'.txt') == True:
                messagebox.showerror('Exists', 'This word already exsits. You can find it by typing ' +word)
def about_us():
        text_window = Tk()
        text_window.title("About us")
        labels = Label(text_window, text='About Us')
        label2 = Label(text_window, text="This app was developed \n to establish a lightweight, dynamic dictionary for computer \n systems.")
        button = Button(text_window, command=exit, text="Exit")
        labels.pack()
        label2.pack()
        button.pack()

txt=c.create_text(112,19,fill="red",anchor='nw',font=("Arial 18"), text="Welcome To The DynamicDict App")
txt=c.create_text(112,49,fill="red",anchor='nw',font=("Arial 11"), text="Enter a word or phrase, if it does not exist in our libraries,")
txt=c.create_text(112,79,fill="red",anchor='nw',font=("Arial 11"), text="fill out the information that is asked.")

menubar = Menu(root)
menubar.add_command(label="Exit", command=exit)
menubar.add_command(label="About Us", command=about_us)


root.config(menu=menubar)
global e

e = Entry(root)
e.pack()


e.delete(0, END)
subbtn = Button(root, text="SUBMIT", command=submit, width=10, height=10)
subbtn.pack()
clearbtn = Button(root, text="CLEAR", command=clear, width=10, height=10)
clearbtn.pack()
newwd = Button(root, text="NEW WORD", command=nwd, width=10, height=10)
newwd.pack()
root.bind('enter', submit)
