from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
import pyperclip
import json

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
FONT_LABEL = ("Courier", 16, "bold")

# ---------------------------- SEARCH WEBSITE NAME AND PRINT INTO MESSAGE BOX------------------------------- #
def search_website_name(website_name):
    if website_name != "":
        website_name=website_name.lower()
        try:
            file = open("data_file.json", "r")
        except FileNotFoundError:
            messagebox.showinfo(message="You should put any record first.", title="Warning")
            file = open("data_file.txt", "w")
        else:
            data = json.load(file)
            try:
                record = data[f"{website_name}"]
            except KeyError:
                messagebox.showinfo(message=f"Sorry, there is no website like: {website_name}")
            else:
                messagebox.showinfo(title=f"{website_name}", message=f"Your email: {record["email"]}\n"
                                                                 f"Your password: {record["password"]}")
        finally:
            file.close()
    else:
        messagebox.showinfo(message="Website field should not be empty.", title="Warning")


def handle_search_button():
    website = website_input.get()
    search_website_name(website)


# ---------------------------- CHECK DATA IS CORRECT (BETTER UI) ------------------------------- #
def check_data(passw, email,website):
    """Check if user write any values and if not show message, if user write data, user can confirm"""
    is_ok = False
    if passw == "" or email == "" or website == "":
        messagebox.showinfo(title="Warning", message="You should not left any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"This are the details entered: \nEmail: {email} "
                                                              f"\nPassword: {passw}"
                                                              f"\n\nIs it ok to save?")
    return is_ok

# ---------------------------- HANDLING STORAGE DATE ------------------------------- #
def handle_save_data_to_file(new_record):
    """Save data in json format to a file. If there is no file, create new file"""
    try:
        file = open("data_file.json", mode="r")
    except FileNotFoundError:
        file = open("data_file.json", mode="w")
        json.dump(new_record, file, indent=4)
    else:
        data = json.load(file)
        data.update(new_record)
        with open("data_file.json", mode="w") as file:
            json.dump(data, file, indent=4)
    finally:
        file.close()

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    """From set of letters, numbers and symbols chose randomly number of charts and save as password. It is
    refactored code from day 5th."""
    rand_letters = [choice(letters) for _ in range(randint(8, 10))]
    rand_symbols = [choice(symbols)for _ in range(randint(2, 4))]
    rand_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = rand_letters + rand_symbols + rand_numbers

    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(END, password)
    pyperclip.copy(password)

# ---------------------------- SAVE DATA ------------------------------- #
def save_data():
    passw= password_input.get()
    email = email_input.get()
    website = website_input.get().lower()

    new_data= {website:{
        "email": email,
        "password": passw
    }}
    is_ok = check_data(passw, email, website)
    if is_ok:
        handle_save_data_to_file(new_data)
        password_input.delete(0, END)
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

website_input = Entry(width=36)
website_input.grid(column=1, row=1)
website_input.focus()

email_input = Entry(width=55)
email_input.insert(END, string="email_example@example.com")
email_input.grid(column=1, row=2, columnspan= 2)

password_input= Entry(width=36)
password_input.grid(column=1, row=3)

generate_password_button = Button(text="generate password", command=generate_password)
generate_password_button.grid(column=2, row=3)

search_button = Button(text="search", command=handle_search_button, width=14)
search_button.grid(column=2, row=1)


add_button = Button(text="add", width=46, command=save_data)
add_button.grid(column=1, row=4, columnspan=2)



window.mainloop()
