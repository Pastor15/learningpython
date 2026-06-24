from tkinter import *
from tkinter import messagebox
import base64

def encrypt():
    password = code.get()

    if password == "":
        messagebox.showerror("Input Error", "Please enter the secret value to encrypt the written message")
        return
    elif password != "1234":
        messagebox.showerror("Invalid", "You have entered the wrong code. Please enter the correct code to encrypt the written message")
        return

    screen1 = Toplevel(screen)
    screen1.title("encryption")
    screen1.geometry("400x200")
    screen1.configure(bg="#ed3833")

    message = text1.get("1.0", END)
    encoded_bytes = base64.b64encode(message.encode("ascii"))
    encrypted_text = encoded_bytes.decode("ascii")

    Label(screen1, text="ENCRYPT", font="arial", fg="white", bg="#ed3833").place(x=10, y=0)
    text2 = Text(screen1, font="arial 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text2.place(x=10, y=40, width=380, height=150)
    text2.insert(END, encrypted_text)


def decrypt():
    password = code.get()

    if password == "":
        messagebox.showerror("Input Error", "Please enter the secret value to decrypt the written message")
        return
    elif password != "1234":
        messagebox.showerror("Invalid", "You have entered the wrong code. Please enter the correct code to decrypt the written message")
        return

    screen2 = Toplevel(screen)
    screen2.title("decryption")
    screen2.geometry("400x200")
    screen2.configure(bg="#00bd56")

    message = text1.get("1.0", END).strip()
    try:
        decoded_bytes = base64.b64decode(message)
        decrypted_text = decoded_bytes.decode("ascii")
    except Exception:
        messagebox.showerror("Decryption Error", "The text in the box isn't valid base64.")
        return

    Label(screen2, text="DECRYPT", font="arial", fg="white", bg="#00bd56").place(x=10, y=0)
    text2 = Text(screen2, font="arial 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text2.place(x=10, y=40, width=380, height=150)
    text2.insert(END, decrypted_text)


def main_screen():
    global screen
    global code
    global text1

    screen = Tk()
    screen.geometry("365x398")

    def reset():
        code.set("")
        text1.delete("1.0", END)

    Label(text="Enter the text for encryption and decryption", fg="black", font=("calibri", 13)).place(x=10, y=10)
    text1 = Text(font="calibri 20", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=10, y=50, width=355, height=100)

    Label(text="Enter the secret value to read the written message", fg="black", font=("calibri", 13)).place(x=10, y=160)
    code = StringVar()
    Entry(textvariable=code, width=19, bd=0, font=("arial"), show="*").place(x=10, y=180)

    Button(text="ENCRYPT", height=2, width=23, bg="#ed3833", fg="white", bd=0, command=encrypt).place(x=10, y=250)
    Button(text="DECRYPT", height=2, width=23, bg="#00bd56", fg="white", bd=0, command=decrypt).place(x=200, y=250)
    Button(text="RESET", height=2, width=50, bg="#1089ff", fg="white", bd=0, command=reset).place(x=10, y=300)

    screen.mainloop()
    #copy the code on encrypt and paste it in decrypt to get the result of the original message
    #however edit how the the buttons are coded

main_screen()