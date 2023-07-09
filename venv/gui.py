from tkinter import Tk, Text, messagebox, StringVar,Text,Frame
from tkinter.ttk import Label,Button
from tkinter.constants import *
import webbrowser, os

class GUI():
    def __init__(self, server):
        self.server = server
        self.window = Tk()
        self.window.title("Morse Code Typer")
        self.window.geometry('800x350')
        self.window.resizable = False
        self.window.iconbitmap(os.path.abspath(os.getcwd()) + '\static\icon.ico')
        self.isTypeOn = False
        self.add_widgets()

    def add_widgets(self):
        self.statusText = StringVar()
        self.statusText.set("Status:")
        self.status = Label(self.window,textvariable=self.statusText)
        self.status.pack(pady=(0,5))

        self.toggleTypeButton = Button(self.window, text="Toggle Keyboard",command=self.toggleType)
        self.toggleTypeButton.pack(pady=(5,20))

        self.sequence = Text(self.window,height=1, font="Helvetica 12")
        self.sequence.tag_configure('bold', font="Helvetica 12 bold")
        self.sequence.pack(padx=(10,10),pady=(0,20))
        self.addSequence('Sequence: ')

        self.letters = Text(self.window,height=10, font="Helvetica 12")
        self.letters.tag_configure('bold', font="Helvetica 12 bold")
        self.letters.pack(padx=(10,10),pady=(0,20))
        self.addLetters('Letters: ')

        self.buttonFrames = Frame(self.window)
        self.buttonFrames.pack()

        self.clearButton = Button(self.window, text="Clear", command=self.clear)
        self.clearButton.pack(in_=self.buttonFrames,side=LEFT,padx=(0,4))

        self.openMorseButton = Button(self.window, text="Morse Code",command=self.openMorse)
        self.openMorseButton.pack(in_=self.buttonFrames,side=RIGHT)

    def addSequence(self,text,bold=False):
        self.sequence.config(state=NORMAL)
        if bold: self.sequence.insert('end', text, 'bold')
        else: self.sequence.insert('end', text)
        self.sequence.config(state=DISABLED)
    
    def addLetters(self,text,bold=False):
        self.letters.config(state=NORMAL)
        if bold: self.letters.insert('end', text, 'bold')
        else: self.letters.insert('end', text)
        self.letters.config(state=DISABLED)
        
    def clear(self):
        self.sequence.config(state=NORMAL)
        self.sequence.delete('1.0',END)
        self.addSequence('Sequence: ')

        self.letters.config(state=NORMAL)
        self.letters.delete('1.0',END)
        self.addLetters('Letters: ')

    def clearSeq(self, clearSeq=True):
        self.sequence.config(state=NORMAL)
        self.sequence.delete('1.0',END)
        self.addSequence('Sequence: ')
        print("CLEAR")
        if clearSeq: self.server.clear()

    def toggleType(self):
        if self.isTypeOn:
            self.isTypeOn = False
            self.toggleTypeButton.config(text="Keyboard OFF")
        else:
            self.isTypeOn = True
            self.toggleTypeButton.config(text="Keyboard ON")

    def openMorse(self):
        webbrowser.open_new_tab('https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/International_Morse_Code.svg/315px-International_Morse_Code.svg.png')

    def run(self):
        self.window.mainloop()

    def userConfirmation(self,info):
        confirmation = messagebox.askyesno("New device connection", "A new device is wishing to connect:\n" + info)
        if confirmation:
            self.server.confirmUser()

if __name__ == "__main__":
    GUI().run()