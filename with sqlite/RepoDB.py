from tkinter import *
from db import Database
from tkinter import messagebox as mb
db = Database('store.db')

class gui(Tk):
    def __init__(self):
        super().__init__()
        #self.geometry('300x150')
        self.title('Repo Manager')

        #name
        Label( text='Name' ).grid(row=0,column=0)
        self.nVar = StringVar()
        self.nE=Entry(textvariable = self.nVar).grid(row=0,column=1, padx=10, pady=10)

        #id
        Label( text='ID NO' ).grid(row=0,column=2)
        self.idVar = StringVar()
        self.idE=Entry(textvariable = self.idVar).grid(row=0,column=3, padx=10, pady=10)

        #qnt
        Label( text='Quantity' ).grid(row=1,column=2)
        self.qVar = StringVar()
        self.qE =Entry(textvariable = self.qVar).grid(row=1,column=3, padx=10, pady=10)

        #price
        Label( text='Price' ).grid(row=1,column=0)
        self.pVar = StringVar()
        self.pE=Entry(textvariable = self.pVar).grid(row=1,column=1, padx=10, pady=10)


        #buttons
        Button(text='add New',command = self.new).grid(row=2,column=0, padx=10, pady=10)
        Button(text='Update',command = self.updateVal).grid(row=2,column=1, padx=10, pady=10)
        Button(text='delete',command = self.deleteVal).grid(row=2,column=2, padx=10, pady=10)
        Button(text='Save',command = self.save).grid(row=2,column=3, padx=10, pady=10)

        #list 
        # listbox
        self.scrollbar = Scrollbar()

        self.Box = Listbox(yscrollcommand=self.scrollbar.set, height=8, width=80)
        self.Box.grid(row=3, column=0, columnspan=4, padx=10, pady=10)
        self.Box.bind('<<ListboxSelect>>',self.select_item)

        self.scrollbar.config(command=self.Box.yview)
        
        self.addItem()

    def new(self):
        db.insert(self.nVar.get(),self.idVar.get(),self.pVar.get(),self.qVar.get())
        self.Box.delete(0,END)
        self.addItem()
        self.clear()
        
    def updateVal(self):
        db.update(self.selected_item[0],self.nVar.get(),self.idVar.get(),self.pVar.get(),self.qVar.get())
        self.addItem()
        self.clear()
        pass

    def deleteVal(self):
        db.remove(self.selected_item[0])
        self.addItem()
        self.clear()


    def save(self):
        self.clear()

    def addItem(self):
        self.Box.delete(0,END)
        for row in db.fetch():
            self.Box.insert(END ,row)

    def select_item(self,var):
        index = self.Box.curselection()[0]
        self.selected_item = self.Box.get(index)

        self.nVar.set(self.selected_item[1])
        self.idVar.set(self.selected_item[2])
        self.pVar.set(self.selected_item[3])
        self.qVar.set(self.selected_item[4])
        
    def clear(self):
        self.nVar.set('')
        self.idVar.set('')
        self.pVar.set('')
        self.qVar.set('')

gui().mainloop()