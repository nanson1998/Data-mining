# from tkinter import Tk, Frame, BOTH, Button, Text, Menu, END
from tkinter import *
import tkinter.filedialog as tf
from tkinter import ttk, messagebox
import tkinter.scrolledtext as tkst
import csv
import pandas as pd
import Train, PhanLop,preprocess
from preprocess import *
class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, bg ="white")
        self.parent = parent
        self.initUI()
        self.preprocessed=''

    def initUI(self):
        self.parent.title("Voice Gender")
        self.pack(fill=BOTH, expand=1)
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)

        fileMenu = Menu(menubar)
        fileMenu.add_command(label="About Us", command = self.showInfo)
        fileMenu.add_command(label="Exit", command= quit)
        menubar.add_cascade(label="Home", menu=fileMenu)
        menubar.add_cascade(label="Training", command = self.onFrameTrain)
        menubar.add_cascade(label="Test", command = self.onFrameTest)
        menubar.add_cascade(label="Help")



        #Load file csv
        lb1 = Label(self, text = 'Load File', width = 6, bg = "white" )
        lb1.place(x = 10, y = 10)
        lb2 = Label(self, text = 'Số Thuộc Tính:', bg = 'white', width = 10)
        lb2.place(x = 10, y = 410)
        self.lb3 = Label(self, text = "?", bg = "#00FA9A")
        self.lb3.place(x = 100, y = 410)
        lb4 = Label(self, text="Số Mẫu:",bg = 'white', width = 15)
        lb4.place(x= 10, y=430)
        self.lb5 = Label(self, text="?", bg="SILVER")
        self.lb5.place(x=100, y=430)
        lb6 = Label(self, text = "DATA", fg = "#1E90FF", bg ="white")

        lb6.place(x = 950, y=40)

        cavas = Canvas(self)
        cavas.create_line(1, 10, 400, 10,  fill="#476042")
        # Show data:
        self.txtData = tkst.ScrolledText(self, height=20, width=120, bg="#87CEEB")
        self.txtData.place(x=10, y=65)



        loadButton = Button(self, text = 'UpFile', command = self.onOpen, relief = GROOVE)
        loadButton.place(x= 320, y = 30)

        bt2 = Button(self, text = "Tiền Xử Lý", relief = RIDGE , height = 2, width = 20,command = self.preprocessing)
        bt2.place(x= 20, y= 500)
        bt3 = Button(self, text="Clear", relief= RIDGE, command = self.clearText)
        bt3.place(x = 850, y = 410)
        self.var = IntVar()
        self.var.set(0)
        self.rb = Radiobutton(self, text = "Quick View", relief = GROOVE, value = 1, variable = self.var)
        self.rb.place(x = 900, y = 410)
        self.txt1 = Entry(self, bg ="white", width = 50)
        self.txt1.place(x = 10, y = 30)
        mb = Menubutton(self, text ="Output", relief = GROOVE, height = 3, width = 20)
        mb.place(x = 850, y= 450)
        mb.menu = Menu(mb)
        mb["menu"] = mb.menu
        mb.menu.add_checkbutton(label="File .log", variable=IntVar())
        mb.menu.add_checkbutton(label="File .csv", variable=IntVar())



    def onOpen(self):
        ftypes = [('csv files', '*.csv'), ('All files', '*')]
        dlg = tf.Open(self, filetypes=ftypes)
        fl = dlg.show()
        self.txt1.insert(END, fl)
        if fl != '':
            text = self.readFile(fl)
            if (self.var.get() == 0):
                text = self.readFile(fl)
            else:
                text = self.shortView(fl)
            self.txtData.insert(END, text)
    def readFile(self, filename):
        text = ''
        self.datafile = filename
        f = pd.read_csv(filename)
        f.head()
        self.lb5.configure(text=str(f.shape[0]))
        self.lb3.configure(text=str(f.shape[1]))
        text = '(' + str(f.shape[0]) +' , '+ str(f.shape[1]) +')' + '\n' + str(f.dtypes)
        somau = str(f.shape[0])
        return text
    #tien xu ly du lieu
    def preprocessing(self):
        self.preprocessed = preprocess.replaceValue(self.datafile).name
        return (self.preprocessed)
    def shortView(self, filename):
        text = pd.read_csv(filename)
        return text

    def clearText(self):
        self.txtData.delete(1.0, END)


    def onFrameTrain(self):
        root = Tk()
        root.geometry("500x350+300+100")

        ftrain = Train.TRAIN(root)
        root.mainloop()
    def onFrameTest(self):
        root = Tk()
        root.geometry("1050x550+50+100")
        ftrain = PhanLop.TEST(root)
        root.mainloop()
    def showInfo(self):
        messagebox.showinfo("Information",
                            'Đề tài: Phân loại giọng nói!  -Nhóm 16 \n'
                            'Môn: Khai Thác Dữ Liệu và Ứng Dụng \n'
                            'GV: Nguyễn Thị Anh Thư'
                            )


def main():
    root = Tk()
    root.geometry("1050x550+100+100")
    app = Example(root)
    root.mainloop()

if __name__ == '__main__':
    main()