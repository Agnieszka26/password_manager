from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
import pyperclip

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
FONT_LABEL = ("Courier", 16, "bold")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    rand_letters = [choice(letters) for _ in range(randint(8, 10))]
    rand_symbols = [choice(symbols)for _ in range(randint(2, 4))]
    rand_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = rand_letters + rand_symbols + rand_numbers

    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(END, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    passw= password_input.get()
    email = email_input.get()
    website = website_input.get()

    if passw== "" or email =="" or website == "":
        messagebox.showinfo(title="Warning", message="You should not left any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"This are the details entered: \nEmail: {email} "
                                                      f"\nPassword: {passw}"
                                                      f"\n\nIs it ok to save?")
        if is_ok:
            with open("data_file.txt", mode="a") as file:
                file.write(f"{website} | {email} | {passw} \n")
            password_input.delete(0,END)
            email_input.delete(0, END)
            website_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=20)

logo = PhotoImage(file="logo.png")

canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1,row=0)

website_label = Label(text="Website:", font=FONT_LABEL)
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:", font= FONT_LABEL)
email_label.grid(column=0, row=2)

password_label = Label(text="Password:", font=FONT_LABEL)
password_label.grid(column=0, row=3)

website_input = Entry(width=55)
website_input.insert(END, string="www.example.pl")
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

email_input = Entry(width=55)
email_input.insert(END, string="email_example@example.com")
email_input.grid(column=1, row=2, columnspan= 2)

password_input= Entry(width=36)
password_input.grid(column=1, row=3)

generate_password_button = Button(text="generate password", command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="add", width=46, command=save_data)
add_button.grid(column=1, row=4, columnspan=2)



window.mainloop()
