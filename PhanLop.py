from tkinter import *
import tkinter.filedialog as tf
from tkinter import ttk
import tkinter.scrolledtext as tkst
import preprocess
import pickle,ast
import numpy as np
from Train import TRAIN
class TEST(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, bg ="white")
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("PHÂN LỚP")
        self.pack(fill=BOTH, expand=1)
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)
        lb1 = Label(self, text="CHỌN PHƯƠNG PHÁP", bg="white", font=('Helvetica', 11, 'bold'))
        lb1.place(x=10, y=10)
        lb2 = Label(self, text="PHÂN LỚP 1 MẪU", bg="white", font=('Helvetica', 11, 'bold'))
        lb2.place(x=10, y=70)
        lb3 = Label(self, text="PHÂN LỚP NHIỀU MẪU",bg = "white", font=('Helvetica', 11,'bold'))
        lb3.place(x=10, y=250)

        self.lb51 = Label(self, text="?", bg = "#DDA0DD")
        self.lb51.place(x = 180, y = 190)

        # Input thuộc tính
        self.txtInput = tkst.ScrolledText(self, height=3, width=120, bg="#B0E0E6")
        self.txtInput.place(x=10, y=130)
        aSampleButton = Button(self, text = "Kết quả", relief = RIDGE , height = 1, width = 20,command = self.aSamplePredict)
        aSampleButton.place(x=10, y = 190)
        #Xuat kết quả
        self.txtOut = tkst.ScrolledText(self, height=12, width=80, bg="#87CEFA")
        self.txtOut.place(x=10, y=330)
        # Xuất pre-recall
        txtPreRecall = tkst.ScrolledText(self, height=12, width=20, bg="#B0C4DE")
        txtPreRecall.place(x= 700, y=330)

        v = StringVar(self, "1")
        self.v = IntVar()
        self.v.set(0)
        self.rb1 = Radiobutton(self, text="KNN", bg="white", value=1, variable=self.v)
        self.rb2 = Radiobutton(self, text="SVM", bg="white", value=2, variable=self.v)
        self.rb3 = Radiobutton(self, text="Decision Tree", bg="white", value=3, variable=self.v)
        self.rb1.place(x=10, y=30)
        self.rb2.place(x=80, y=30)
        self.rb3.place(x=160, y=30)

        lb4 = Label(self, text="meanfreq,")
        lb4.place(x=10, y=100)
        lb5 = Label(self, text="sd,")
        lb5.place(x=70, y=100)
        lb6 = Label(self, text="median,")
        lb6.place(x=90, y=100)
        lb7 = Label(self, text="Q25,")
        lb7.place(x=140, y=100)
        lb8 = Label(self, text="Q75,")
        lb8.place(x=170, y=100)
        lb9 = Label(self, text="IQR,")
        lb9.place(x=200, y=100)
        lb10 = Label(self, text="skew,")
        lb10.place(x=230, y=100)
        lb11 = Label(self, text="kurt,")
        lb11.place(x=260, y=100)
        lb12 = Label(self, text="sp.ent,")
        lb12.place(x=290, y=100)
        lb13 = Label(self, text="sfm,")
        lb13.place(x=320, y=100)
        lb14 = Label(self, text="mode,")
        lb14.place(x=350, y=100)
        lb15 = Label(self, text="centroid,")
        lb15.place(x=390, y=100)
        lb16 = Label(self, text="meanfun,")
        lb16.place(x=450, y=100)
        lb17 = Label(self, text="minfun,")
        lb17.place(x=510, y=100)
        lb18 = Label(self, text="maxfun,")
        lb18.place(x=560, y=100)
        lb19 = Label(self, text="meandom,")
        lb19.place(x=620, y=100)
        lb20 = Label(self, text="mindom,")
        lb20.place(x=680, y=100)
        lb21 = Label(self, text="maxdom,")
        lb21.place(x=730, y=100)
        lb22 = Label(self, text="dfrange,")
        lb22.place(x=790, y=100)
        lb23 = Label(self, text="modindx,")
        lb23.place(x=850, y=100)
        lb24 = Label(self, text="label")
        lb24.place(x=900, y=100)


        #Xu ly
        bt1 = Button(self, text="Load Model", relief = GROOVE, command = self.loadmode) #reset làm trống các ô
        bt1.place(x=450, y = 40 )
        bt2 = Button(self, text = "File", relief = GROOVE, command = self.UpLoadData)
        bt2.place(x= 10, y = 290)
        bt3 = Button(self, text="Phân Lớp", relief=GROOVE, command = self.PredictFile)
        bt3.place(x=50, y=290)
        bt4 = Button(self, text="reset", relief=GROOVE, command = self.clearT)  # reset làm trống các ô
        bt4.place(x=550, y=40)
    def clearT(self):
        self.txtInput.delete('1.0',END)
    def loadmode(self):
        ftypes = [('model files', '*.sav'), ('All files', '*')]
        dlg = tf.Open(self, filetypes=ftypes)
        self.fl = dlg.show()
        return self.fl
    def aSamplePredict(self):

        stri=self.txtInput.get("1.0",END)
        arr= preprocess.convertStringToArray(stri)
        mau= np.array(arr)

        mau =mau.reshape(1,20)

        if (self.v.get() == 1):
            with open(TRAIN.save_model_knn, 'rb') as file:
                model = pickle.load(file)

        if (self.v.get() == 2):
            with open(TRAIN.save_model_svm, 'rb') as file:
                model = pickle.load(file)

        if (self.v.get() == 3):
            with open(TRAIN.save_model_dct, 'rb') as file:
                model = pickle.load(file)

        if(self.loadmode):
            with open(self.fl, 'rb') as file:
                model = pickle.load(file)
        label = model.predict(mau)
        a = label[0]
        if(a == 0):
            self.lb51.configure(text="female")
        else:
            self.lb51.configure(text ="male")

#upload file data
    def UpLoadData(self):
        ftypes = [('csv files', '*.csv'), ('All files', '*')]
        dlg = tf.Open(self, filetypes=ftypes)
        self.dt= dlg.show()
        return self.dt
#phân lớp nhiều mẫu

    def PredictFile(self):

        f_in = open(self.dt)
        fields = []
        arrKQ = []
        for line in f_in.readlines():
            fields.append([ast.literal_eval(item.strip('\n')) for item in line.split(',')])

        for field in fields:
            print(field)
            # fields = preprocess.convertStringToArray(fields)
            mau = np.array(field)
            mau = mau.reshape(1, 20)
            if (self.v.get() == 1):
                with open(TRAIN.save_model_knn, 'rb') as file:
                    model = pickle.load(file)

            if (self.v.get() == 2):
                with open(TRAIN.save_model_svm, 'rb') as file:
                    model = pickle.load(file)

            if (self.v.get() == 3):
                with open(TRAIN.save_model_dct, 'rb') as file:
                    model = pickle.load(file)

            if (self.loadmode):
                with open(self.fl, 'rb') as file:
                    model = pickle.load(file)
            label = model.predict(mau)

            if(label == 0):
                arrKQ.append('female')
            else:
                arrKQ.append('male')

        self.txtOut.insert(END, arrKQ)





def main():
    root = Tk()
    root.geometry("1050x550+100+100")
    app = TEST(root)
    root.mainloop()

if __name__ == '__main__':
    main()