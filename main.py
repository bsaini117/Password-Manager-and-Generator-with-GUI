from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project

def generate_pasword():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_symbol = [choice(symbols) for _ in range(randint(2, 4))]
    password_number = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_number + password_symbol + password_letter
    shuffle(password_list)

    # Convert list to string
    password = "".join(password_list)

    password_entry.insert(0, F"{password}")
    # Pyperclip module automatically copies the password after its generated
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="oops", message="Please dont leave any fields empty")

    else:
        # Creating dialouge box to appear that verifies and assures user that a task is done(password is saved)
        # askokcancel returns boolean, 0 if user press cancel and 1 if user press okay
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}"
                                                              f"\nPassword: {password} \nIs it okay to save?")
        if is_ok:
            with open("Pass_data.txt", "a") as f:
                f.write(f"{website} | {email} | {password}\n")
                # deleting the text on GUI after we add in file, FROM 0 index to END
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)


website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username")
email_label.grid(column=0, row=2)

password_label = Label(text="Password")
password_label.grid(column=0, row=3)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
website_entry.get()

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
# 0 means that the cursor will be before the text, END means the cursor will be at the end of the text in entry
email_entry.insert(0, "bsaini117@gmail.com")
email_entry.get()

password_entry = Entry(width=17)
password_entry.grid(column=1, row=3)
password_entry.get()


generate_button = Button(text="Generate Password", command=generate_pasword)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=30, command=save_data)
add_button.grid(row=4, column=1, columnspan=2)












window.mainloop()