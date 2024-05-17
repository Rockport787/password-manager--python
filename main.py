from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
import pyperclip
def clear_password():
    website_Pswrd.delete(0,END)
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]

    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)                                 # a random function normally called random.shuffle()

    password = "".join(password_list)

    website_Pswrd.insert(END, string=password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_details():
    pyperclip.copy(f"{website_Pswrd.get()}")
    if len(website_Input.get()) == 0 or len(website_Pswrd.get()) == 0:
        messagebox.showinfo(title="ERROR!", message="Please fill your fields before proceeding")

    else:
        final_check = messagebox.askokcancel(title="Final Confirmation", message=f" Website = {website_Input.get()} \n "
                                                                                 f"Email = {website_Email.get()} \n "
                                                                                 f"Password ={website_Pswrd.get()} \n"
                                                                                  "\nNote : Password is added to your Clipboard :)"  )
        if final_check:
            with open("storing_detail.txt", mode="a") as storage:
                storage.write(f"{website_Input.get()} | {website_Email.get()} | {website_Pswrd.get()} \n")

            website_Input.delete(0, END)
            website_Pswrd.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
#window
windows = Tk()
windows.title("Password Manager")
windows.config(padx=50, pady=50)

#canvas
canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

#Labels:
label_Website = Label(text="Website:")
label_Website.grid(row=1, column=0)

label_Email = Label(text="Email/Username:")
label_Email.grid(row=2, column=0)

label_Pswrd = Label(text="Password:")
label_Pswrd.grid(row=3, column=0)

#Entries
website_Input = Entry(width=40)
website_Input.insert(END, string="")
website_Input.focus()  #to put cursor on this entry whenever the program starts
website_Input.grid(row=1, column=1, columnspan=2)

website_Email = Entry(width=40)
website_Email.insert(END, string="richumathew1000@gmail.com")  #places default mail
website_Email.grid(row=2, column=1, columnspan=2)

website_Pswrd = Entry(width=21)
website_Pswrd.insert(END, string="")
website_Pswrd.grid(row=3, column=1, columnspan=1)

#Buttons
gen_pswrd = Button(text="Generate Password", command=generate_password)
gen_pswrd.grid(row=3, column=2)

add_pswrd = Button(text="Add", width=34, command=add_details)
add_pswrd.grid(row=5, column=1, columnspan=2)

clear_pswrd = Button(text="Clear password", width=18, command=clear_password)
clear_pswrd.grid(row=4, column=1, columnspan=1)
windows.mainloop()
