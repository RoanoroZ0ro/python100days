from tkinter import *
from tkinter import font
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(1, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(1, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(1, 10))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)  # auto copy

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
 
    website = website_entry.get() 
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make suer you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \n "
                                                              f"Password: {password} \n Is it ok to save?")

        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="#FFFFFF")

# Fonts and Colors
label_font = font.Font(family="Arial", size=12, weight="bold")
entry_font = font.Font(family="Arial", size=10)
button_font = font.Font(family="Arial", size=10, weight="bold")
button_color = "#4CAF50"
button_fg_color = "#FFFFFF"

# Logo
canvas = Canvas(height=200, width=200, bg="#FFFFFF", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1, pady=(0, 20))

# Labels
website_label = Label(text="Website:", font=label_font, bg="#FFFFFF")
website_label.grid(row=1, column=0, sticky=W)

email_label = Label(text="Email/Username:", font=label_font, bg="#FFFFFF")
email_label.grid(row=2, column=0, sticky=W)

password_label = Label(text="Password:", font=label_font, bg="#FFFFFF")
password_label.grid(row=3, column=0, sticky=W)

# Entries
entry_width = 40

website_entry = Entry(width=entry_width, font=entry_font)
website_entry.grid(row=1, column=1, columnspan=2, pady=5, padx=5)
website_entry.focus()

email_entry = Entry(width=entry_width, font=entry_font)
email_entry.grid(row=2, column=1, columnspan=2, pady=5, padx=5)
email_entry.insert(0, "dummy@mail.com")

password_entry = Entry(width=entry_width, font=entry_font)
password_entry.grid(row=3, column=1, columnspan=2, pady=5, padx=5)

# Buttons
generate_password_button = Button(text="Generate Password", font=button_font, bg=button_color,
                                  fg=button_fg_color, command=generate_password)
generate_password_button.grid(row=3, column=3, padx=5)

add_button = Button(text="Add", width=36, font=button_font, bg=button_color, fg=button_fg_color, command=save)
add_button.grid(row=4, column=1, columnspan=3, pady=20)

window.mainloop()
