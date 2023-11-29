import tkinter as tk
GX = 4
GY = 6
class CustomButton:
    def __init__(self,root,text,posx,posy):
        self.root = tk.Button(root.root,text=text,font = ('Arial',15))
        self.root.bind("<Button-1>",lambda s : root.ButtonHandler(s,text))
        self.root.place(relx=posx/GX,rely=posy/GY,relh = 1/GY,relw = 1/GX)
        root.Button.append(self)
    
#Calculator
#-PNum - main number
#-SNum - second number
#
class Calculator:
    def UpdateLabel(self,text):
        self.Label.config(text=text)
    def NumberHandler(self,num):
        if self.DecimalPlace == 0:
            self.PNum *= 10
            self.PNum += num
        else:
            if self.DecimalPlace < 6:
                self.PNum += num * (10**(-self.DecimalPlace))
                self.DecimalPlace += 1
        self.UpdateLabel(str(self.PNum))
    def resetP(self):
        self.PNum = 0
        self.DecimalPlace = 0
    def OpHandler(self,op):
        if self.SNum != 0 and self.rep == False:
            self.Evaluate()
        self.rep = False
        self.SNum = self.PNum
        self.resetP()
        self.op = op
    def Evaluate(self):
        if self.rep == False:
            self.PNum,self.SNum = self.SNum,self.PNum
        op = self.op
        if op == "+":
            self.PNum += self.SNum
        if op == "-":
            self.PNum -= self.SNum
        if op == "/":
            self.PNum /= self.SNum
        if op == "*":
            self.PNum *= self.SNum
        if op == "^":
            self.PNum =pow(self.PNum, self.SNum)
        #self.op = ""
        self.UpdateLabel(str(self.PNum))
        self.rep = True
    def ButtonHandler(self,event,text):
        if text.isnumeric():
            self.NumberHandler(int(text))
        elif text == ".":
            if self.DecimalPlace == 0:
                self.DecimalPlace = 1
        elif text == "C":
            self.PNum = 0
            self.UpdateLabel(str(self.PNum))
        elif text == "CE":
            self.initializeInternal()
            self.UpdateLabel(str(self.PNum))
        elif text == "Enter":
            self.Evaluate()
        elif text == "%":
            self.PNum /= 100
            self.UpdateLabel(str(self.PNum))
        else:
            self.OpHandler(text)


    def initializeInternal(self):
        self.DecimalPlace = 0
        self.PNum = 0
        self.SNum = 0
        self.op = ""
        self.rep = False
    def initializeWidget(self):
        self.Button = []
        CustomButton(self,"1",0,4)
        CustomButton(self,"2",1,4)
        CustomButton(self,"3",2,4)
        CustomButton(self,"4",0,3)
        CustomButton(self,"5",1,3)
        CustomButton(self,"6",2,3)
        CustomButton(self,"7",0,2)
        CustomButton(self,"8",1,2)
        CustomButton(self,"9",2,2)
        CustomButton(self,"0",1,5)
        CustomButton(self,"/",3,2)
        CustomButton(self,"+",3,3)
        CustomButton(self,"-",3,4)
        CustomButton(self,"*",3,5)
        CustomButton(self,".",0,5)
        CustomButton(self,"C",0,1)
        CustomButton(self,"CE",1,1)
        CustomButton(self,"%",2,1)
        CustomButton(self,"^",3,1)
        CustomButton(self,"Enter",2,5)

        self.Label = tk.Label(self.root,font = ("Arial",20))
        self.Label.place(relx = 0,rely=0,relh = 1/GY,relw = 1)
        self.Label.config(text = "0")

    
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("300x300")
        self.root.title("Calculator")
        self.initializeInternal()
        self.initializeWidget()
        self.root.mainloop()
    


Calculator()
