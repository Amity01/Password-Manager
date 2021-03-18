from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


#-----------------------Search FUnction_______________________________

def find_website():
    with open("data.json",'r') as data_file:
        data = json.load(data_file)
    website = website_input.get()
    try:
        email = data[website]["email"]
        password = data[website]["password"]
        messagebox.showinfo(title=website, message=f"email: {email}\npassword: {password} ")
    except KeyError:
        messagebox.showwarning(title="Website not found", message=f"No details for {website}")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project


def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list += [random.choice(letters) for i in range(nr_letters)]
    password_list += [random.choice(numbers) for i in range(nr_numbers)]
    password_list += [random.choice(symbols) for i in range(nr_symbols)]

    random.shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    website_name = website_input.get()
    email_id = username_input.get()
    password = password_input.get()
    new_data = {website_name:{
        "email":email_id,
        "password":password
    }}
    is_ok = False
    if len(website_name) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops!",message="Please make sure you haven't left any field empty")
    else:
        is_ok = messagebox.askokcancel(title=website_name, message=f"Do you want to save the informtion?\n{website_name}\n{username_input}\n{password}")

    if is_ok:
        try:
            with open("data.json", 'r') as data_file:
                data = json.load(data_file)
                data.update(new_data)
            with open ("data.json",'w') as data_file:
                json.dump(data, data_file, indent=4)
        except FileNotFoundError:
            with open ("data.json", 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)




# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")


window.config(padx=50, pady=50)
canvas = Canvas(height=200, width=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1, columnspan=2)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_input = Entry(width=21)
website_input.grid(row=1, column=1)
website_input.focus()

search_button = Button(text="Search", width=15, command=find_website)
search_button.grid(row=1, column=2)

username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)

username_input = Entry(width=40)
username_input.grid(row=2, column=1, columnspan=2)
username_input.insert(0, "andnajakd@gmail.com")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_input = Entry(width=21)
password_input.grid(row=3, column=1, columnspan=1)

generate_button = Button(text="Generate Password", command=password_generator, width=15)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", command=add, width=30)
add_button.grid(row=4, column=1, columnspan=2)
















window.mainloop()
