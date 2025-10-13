import customtkinter as ct

def ButtonCallBack() :
    print("button pressed")

app=ct.CTk()

app.title("NoteApp")
app.geometry("1000x600")

button = ct.CTkButton(app,text="my button",command=ButtonCallBack)
button.grid(row=0, column=0, padx=20,pady=20,sticky="ew")
app.grid_columnconfigure(0,weight=1)


app.mainloop()