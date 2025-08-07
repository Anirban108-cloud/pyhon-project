from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('700x550')
root.config(bg='#d3f3f5')
root.title('PythonGeeks Contact Book')
root.resizable(0, 0)

contactlist = [
    ['anirban ghosh', '369854712'],
    ['vaskar sarkar', '521155222'],
    ['swasti saran lal', '78945614'],
    ['raj paul', '58745246'],
    ['manab pal', '5846975'],
    ['joyeta mondal', '5647892'],
    ['sayan ghosh', '89685320'],
    ['kiron ghosh', '98564785'],
    ['ashish kumar ghosh', '85967412']
]

Name = StringVar()
Number = StringVar()

frame = Frame(root)
frame.pack(side=RIGHT)

scroll = Scrollbar(frame, orient=VERTICAL)
select = Listbox(frame, yscrollcommand=scroll.set, font=('Times new roman', 16), bg="#f0fffc", width=20, height=20, borderwidth=3, relief="groove")
scroll.config(command=select.yview)
scroll.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT, fill=BOTH, expand=1)

def Selected():
    if len(select.curselection()) == 0:
        messagebox.showerror("Error", "Please select a name")
        return None
    return int(select.curselection()[0])

def EntryReset():
    Name.set("")
    Number.set("")

def AddContact():
    if Name.get() != "" and Number.get() != "":
        contactlist.append([Name.get(), Number.get()])
        Select_set()
        EntryReset()
        messagebox.showinfo("Confirmation", "Successfully added new contact")
    else:
        messagebox.showerror("Error", "Please fill all the information")

def UpdateDetail():
    index = Selected()
    if index is not None and Name.get() and Number.get():
        contactlist[index] = [Name.get(), Number.get()]
        Select_set()
        EntryReset()
        messagebox.showinfo("Confirmation", "Successfully updated contact")
    elif index is None:
        messagebox.showerror("Error", "Please select a contact first")
    else:
        messagebox.showerror("Error", "Please fill in both Name and Contact Number")

def Delete_Entry():
    index = Selected()
    if index is not None:
        result = messagebox.askyesno('Confirmation', 'Do you want to delete the selected contact?')
        if result:
            del contactlist[index]
            Select_set()
            EntryReset()

def VIEW():
    index = Selected()
    if index is not None:
        NAME, PHONE = contactlist[index]
        Name.set(NAME)
        Number.set(PHONE)

def EXIT():
    root.destroy()

def Select_set():
    contactlist.sort()
    select.delete(0, END)
    for name, phone in contactlist:
        select.insert(END, name)

Select_set()

Label(root, text='Name', font=("Times new roman", 22, "bold"), bg='SlateGray3').place(x=30, y=20)
Entry(root, textvariable=Name, width=30).place(x=200, y=30)

Label(root, text='Contact No.', font=("Times new roman", 20, "bold"), bg='SlateGray3').place(x=30, y=70)
Entry(root, textvariable=Number, width=30).place(x=200, y=80)

Button(root, text="ADD", font='Helvetica 18 bold', bg='#e8c1c7', command=AddContact, padx=20).place(x=50, y=140)
Button(root, text="EDIT", font='Helvetica 18 bold', bg='#e8c1c7', command=UpdateDetail, padx=20).place(x=50, y=200)
Button(root, text="DELETE", font='Helvetica 18 bold', bg='#e8c1c7', command=Delete_Entry, padx=20).place(x=50, y=260)
Button(root, text="VIEW", font='Helvetica 18 bold', bg='#e8c1c7', command=VIEW).place(x=50, y=325)
Button(root, text="RESET", font='Helvetica 18 bold', bg='#e8c1c7', command=EntryReset).place(x=50, y=390)
Button(root, text="EXIT", font='Helvetica 24 bold', bg='tomato', command=EXIT).place(x=250, y=470)

root.mainloop()
