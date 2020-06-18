from tkinter import *
import tkinter.filedialog as tf
from tkinter import ttk, messagebox
import tkinter.scrolledtext as tkst
import pandas as pd
import seaborn as sns
import numpy as np
np.set_printoptions(threshold=np.inf)  # Showing all the array in Console
import matplotlib.pyplot as plt
from sklearn import metrics
#from MainGui import Example
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from tkinter import filedialog
import pickle
import os

from preprocess import *
class TRAIN(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent, bg="white")
        #self.preprocessed = preprocessed
        self.parent = parent
        self.initUI()
    def initUI(self):
        self.parent.title("TRAIN")
        self.pack(fill=BOTH, expand=1)
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)

        # Huấn luyện mô hình
        lb1 = Label(self, text="CHỌN PHƯƠNG PHÁP", bg="white", font= ('Helvetica', 11, 'bold'))
        lb1.place(x=10, y=10)


        #Xuat ket qua
        self.tKQ = tkst.ScrolledText(self, height=10, width= 50, bg="#87CEFA")
        self.tKQ.place(x=10, y= 160)

        #Chon thuat toan
        self.v = IntVar()
        #self.v.set(0)
        self.rb1 = Radiobutton(self, text= "KNN", bg = "white", value = 1 , variable = self.v)
        self.rb2 = Radiobutton(self, text= "SVM", bg = "white", value = 2 , variable = self.v)
        self.rb3 = Radiobutton(self, text= " Decision Tree", bg = "white", value = 3, variable = self.v)
        self.rb1.place(x=10, y=30)
        self.rb2.place(x=10, y=50)
        self.rb3.place(x=10, y=70)


        #Xử lý
        bt1 = Button(self, text ="Train", relief =  GROOVE, height = 3, width = 10, command = self.TrainAndTest)
        bt1.place(x=10, y = 100)
        bt2 = Button(self, text="Lưu Model", relief=GROOVE, height = 3, width =10, command = self.saveModel)
        bt2.place(x=100, y=100)


    def TrainAndTest(self):
        dataset = pd.read_csv("voice.csv")
        dataset.corr()
        dataset.head()
        colormap = plt.cm.viridis
        plt.figure(figsize=(10, 10))
        plt.title('Pearson Correlation', y=1.05, size=15)
        plt.yticks(rotation=0)
        plt.xticks(rotation=90)
        sns.heatmap(dataset.iloc[:, :-1].astype(float).corr(), linewidths=0.3, vmax=1.0, square=True, cmap="YlGnBu",
                    linecolor='black', annot=True, annot_kws={"size": 7})
        #####################################################
        #	                                                 #
        #        Starting with Sets and Pre-Processing      #
        #	                                                 #
        #####################################################

        # ------ Separating the Independent and Dependent Variables
        # Getting all Columns, except the last one with the genders
        X = dataset.iloc[:, : -1].values
        # Getting the last column
        y = dataset.iloc[:, 20].values

        # ------ Checking the Number of Male and Females
        #txxt = "\nNumber of Males: {} \nNumber of Females: {}".format(dataset[dataset.label == 'male'].shape[
        #                                      0], dataset[dataset.label == 'female'].shape[0])  # shape returns the dimensions of the array. If Y has n rows and m columns, then Y.shape is (n,m). So Y.shape[0] is n.
        #self.tKQ.insert(END, txxt)
        # If we don´t know the labels or they are too many, we can use 'dataset["label"].value_counts()'

        # ------ Encoding Categorical Data of the Dependent Variable
        # male -> 1
        # female -> 0
        from sklearn.preprocessing import LabelEncoder

        labelencoder_y = LabelEncoder()
        y = labelencoder_y.fit_transform(y)

        # ------ Splitting the Dataset into the Training Set and Test Set
        from sklearn.model_selection import train_test_split

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=0)

        # ------- Feature Scaling
        from sklearn.preprocessing import StandardScaler

        sc_X = StandardScaler()
        X_train = sc_X.fit_transform(X_train)
        X_test = sc_X.transform(X_test)

        # Creating a Dictionaire
        model_accuracy = {}
        if (self.v.get() == 1):
            classifier = KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2)
            self.model_knn = classifier.fit(X_train, y_train)

            # Predicting the Test set results
            y_pred= classifier.predict(X_test)

            messagebox.showinfo("Huấn luyện", "Thành Công!")
            txtAcKNN = "\nAccuracy of KNN: {}".format(metrics.accuracy_score(y_test, y_pred))
            self.tKQ.insert("end", txtAcKNN)

        elif (self.v.get() == 2):
            from sklearn.svm import SVC
            classifier = SVC(kernel='rbf', random_state=0)
            self.model_svm = classifier.fit(X_train, y_train)

            # Predicting the Test set results
            y_pred= classifier.predict(X_test)

            messagebox.showinfo("Huấn luyện", "Thành Công!")
            txtAcSVM = "\nAccuracy of SVM: {}".format(metrics.accuracy_score(y_test, y_pred))
            self.tKQ.insert("end", txtAcSVM)

        elif(self.v.get() == 3):
            from sklearn.tree import DecisionTreeClassifier
            classifier = DecisionTreeClassifier(criterion='entropy', random_state=0)
            self.model_decisionTree = classifier.fit(X_train, y_train)
            y_pred = classifier.predict(X_test)
            messagebox.showinfo("Huấn luyện", "Thành Công!")
            txtAcDT = "\nAccuracy of Decision Tree: {}".format(metrics.accuracy_score(y_test, y_pred))
            self.tKQ.insert("end", txtAcDT)


    def outPut1(self):
        pass
    def saveModel(self):
        if (self.v.get() == 1):
            self.save_model_knn = filedialog.asksaveasfilename(filetypes=[("Save Model KNN", ".sav")],
                                         defaultextension=".sav")
            pickle.dump(self.model_knn, open(self.save_model_knn, 'wb'))
            messagebox.showinfo("Lưu Model", "Thành Công!")
        if (self.v.get() == 2):
            self.save_model_svm = filedialog.asksaveasfilename(filetypes=[("Save Model SVM", ".sav")],
                                         defaultextension=".sav")
            pickle.dump(self.model_svm, open(self.save_model_svm, 'wb'))
            messagebox.showinfo("Lưu Model", "Thành Công!")
        if (self.v.get() == 3):
            self.save_model_dct = filedialog.asksaveasfilename(filetypes=[("Save Model Decision Tree", ".sav")],
                                         defaultextension=".sav")
            pickle.dump(self.model_decisionTree, open(self.save_model_dct, 'wb'))
            messagebox.showinfo("Lưu Model", "Thành Công!")
    def loadModel(self):
        pass # load model


def main():
    root = Tk()
    root.geometry("500x350+300+100")
    app = TRAIN(root)
    root.mainloop()

if __name__ == '__main__':
    main()