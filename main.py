import tkinter
from tkinter import messagebox
import random
import json
import os


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    if password_input.get() != "":
        password_input.delete(0, tkinter.END)
    else:
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u',
                   'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
                   'P',
                   'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        password_list = []

        [password_list.append(random.choice(letters)) for char in range(random.randint(8, 10))]
        [password_list.append(random.choice(symbols)) for char in range(random.randint(2, 4))]
        [password_list.append(random.choice(numbers)) for char in range(random.randint(2, 4))]

        random.shuffle(password_list)

        password = "".join(password_list)

        password_input.insert(0, password)



# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_command():
    website = website_input.get().capitalize()
    try:
        with open("data.json", mode="r") as file:
            data = json.load(file)
            data = data[website]
    except FileNotFoundError:
        messagebox.showerror(title="Empty Database", message="No entries in the database")
    except KeyError:
        messagebox.showerror(title="Invalid Search", message="This website credentials don't exist in our database")
    else:
        email = data["email"]
        password = data["password"]
        messagebox.showinfo(title=website + " details", message=f"Email: {email} \n Password : {password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_entry():
    website = website_input.get().capitalize()
    email = username_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if website == "":
        messagebox.showerror(title="Incorrect Entry", message="Kindly provide correct website details")
    elif password == "":
        messagebox.showerror(title="Incorrect Entry", message="Invalid password credentials")
    else:
        should_proceed = messagebox.askokcancel(title="Kindly check details", message=f"Website: {website} \n "
                                                                                      f"Email: {email}\n "
                                                                                      f"password : {password}\n")
        if should_proceed:
            try:
                with open(file="data.json", mode="r") as file:
                    data = json.load(file)
                    data.update(new_data)

                with open(file="data.json", mode="w") as file:
                    json.dump(data, file, indent=4)

            except FileNotFoundError:
                with open(file="data.json", mode="w") as file:
                    json.dump(new_data, file, indent=4)

            finally:
                website_input.delete(0, tkinter.END)
                username_input.delete(0, tkinter.END)
                password_input.delete(0, tkinter.END)


# ---------------------------- UI SETUP ------------------------------- #
try:
    file_size = os.path.getsize('data.json')
    if file_size <= 2:
        os.remove('data.json')
except FileNotFoundError:
    pass

window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tkinter.Canvas(width=200, height=200, highlightthickness=0)
lock_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Labels
website_label = tkinter.Label(text="Website:")
website_label.grid(column=0, row=1)
username_label = tkinter.Label(text="Email/Username:")
username_label.grid(column=0, row=2)
password_label = tkinter.Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
website_input = tkinter.Entry(width=17)
website_input.grid(column=1, row=1)
website_input.focus()
username_input = tkinter.Entry(width=35)
username_input.grid(column=1, row=2, columnspan=2)
password_input = tkinter.Entry(width=17)
password_input.grid(column=1, row=3)

# Buttons
generate_password_button = tkinter.Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)
add_button = tkinter.Button(text="Add", width=30, command=save_entry)
add_button.grid(column=1, row=4, columnspan=2)
search_button = tkinter.Button(text="Search", command=search_command)
search_button.grid(column=2, row=1)

window.mainloop()
