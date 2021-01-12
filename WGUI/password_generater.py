from tkinter import*
from string import ascii_letters
from string import digits
from string import punctuation
import random
import pyperclip

root = Tk()
root.geometry("400x400")  
root.title("PG (Password Generator)")  

#root.configure(bg="blue")
#declare variables of string and int type to store generated password nd its length
password = StringVar()
pass_len = IntVar()
pass_len.set(4)

def selection():
    selection = choice.get()

#function to generate password
def generate_pass():
    poor=ascii_letters
    average=ascii_letters+digits
    advance=ascii_letters + digits + punctuation
    pswd=" "
    if choice.get() == 1:
        pswd="".join(random.sample(poor,pass_len.get()))
    elif choice.get() == 2:
        pswd="".join(random.sample(average, pass_len.get()))
    elif choice.get() == 3:
        pswd="".join(random.sample(advance, pass_len.get()))

    password.set(pswd)

# function to copy 
def copy_to_clipboard():
    random_password = password.get()
    pyperclip.copy(random_password)

Label(root, text="Password Generator Application", font="calibri 20 bold").pack()
Label(root, text="Enter password length").pack(pady=3)

# widget to take length from user
Spinbox(root,from_=0,to_=94,textvariable=pass_len,width=15).pack(pady=5)

Button(root, text="Generate Password", command=generate_pass).pack(pady=7)

# show password
Entry(root, textvariable=password).pack(pady=3)

Button(root, text="Copy to clipbord", command=copy_to_clipboard).pack(pady=7)

#variable to store value from radiobuttton
choice = IntVar()
choice.set(3)
R1 = Radiobutton(root, text="        POOR", variable=choice, value=1, command=selection).pack(anchor=CENTER,pady=7,padx="7")
R2 = Radiobutton(root, text="   AVERAGE", variable=choice, value=2, command=selection).pack(anchor=CENTER,pady=7)
R3 = Radiobutton(root, text="ADVANCED", variable=choice, value=3, command=selection).pack(anchor=CENTER,pady=7)
root.mainloop()