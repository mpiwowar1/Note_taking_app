import customtkinter as ct

class App(ct.CTk):
    def __init__(self):
        super().__init__()
        self.title("NoteApp")
        self.geometry("400x180")
        self.grid_columnconfigure((0,1),weight=1)
        self.grid_rowconfigure((0, 1), weight=1)

        self.button = ct.CTkButton(self,text="my button",command=self.ButtonCallBack)
        self.button.grid(row=2, column=0, padx=10,pady=10,sticky="ew",columnspan=2)

        self.checkbox_1 = ct.CTkCheckBox(self,text="checkbox1")
        self.checkbox_1.grid(row=0,column=0,padx=10,pady=(10,0),sticky="w")

        self.checkbox_2 = ct.CTkCheckBox(self,text="checkbox2")
        self.checkbox_2.grid(row=1, column=0, padx=10, pady=(10,0), sticky="w")
        self.grid_columnconfigure(0,weight=1)

    def ButtonCallBack(self) :
        print("button pressed")


app=App()
app.mainloop()



