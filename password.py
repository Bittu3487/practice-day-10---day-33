from tkinter import *
from tkinter import messagebox
from random import randint , choice , shuffle
def password_generate():
     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
     numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
     symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
     password_letter = [choice(letters) for _ in range(randint(8,10))]
     password_number = [choice(numbers) for _ in range(randint(8,10))]
     password_symbol = [choice(symbols) for _ in range(randint(8,10))]
     password_list = password_letter + password_number + password_symbol
     shuffle(password_list)
     password = "".join(password_list)
     password_entry.insert(0,password)
def save():
    password = password_entry.get()
    email = email_entry.get()
    website = website_entry.get()
    if len(password) == 0 or len(email) == 0 or len(website) == 0:
        messagebox.showinfo(title="oop" , message = "don't leave any field empty")
    else:
        is_ok = messagebox.askokcancel(title=website,message=f"is it okay\nyour password entered:{password}"
                                                              f"\nyou email is okay?{email}")
        if is_ok:
            with open("data entry.txt" , "a") as new_file:
                new_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0,END)
                password_entry.delete(0,END)

window = Tk()                                                   
window.title("password")
window.config(padx=50,pady=50)
canvas = Canvas(width=200,height=200)
password_image = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=password_image)
canvas.grid(row=0,column=1)
website_label = Label(text="Website Name:")
website_label.grid(row=1,column=0)
email_label = Label(text="Email/User name:")
email_label.grid(row=2,column=0)
password_label = Label(text="Password:")
password_label.grid(row=3,column=0)
website_entry = Entry()
website_entry.grid(row=1,column=1)
email_entry = Entry()
email_entry.grid(row=2,column=1)
password_entry = Entry()
password_entry.grid(row=3,column=1)
button =Button(text="Generate password",command=password_generate)
button.grid(row=3,column=2)
new_button = Button(text="Add" , command=save)
new_button.grid(row=4,column=1)
window.mainloop()