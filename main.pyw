import tkinter as tk
import tkinter.ttk as ttk
import base64
import pyperclip

window = tk.Tk()
window.title('KRIPTER')
window.geometry("500x430")
window.resizable(False, False)

window.columnconfigure(1, weight=2)
window.columnconfigure(2, weight=2)

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' \
           'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ' \
           '.\\/[]{}()=-.,;:\'"1234567890~!`@#$%^&*<>?|=+_- '


def darkstyle(root):
    style = ttk.Style(root)
    root.tk.call('source', 'azure dark/azure dark.tcl')
    style.theme_use('azure')
    style.configure("Accentbutton", foreground='white')
    style.configure("Togglebutton", foreground='white')
    return style


def encrypt():
    string = decrypted.get("1.0", "end")

    string = string[::-1]

    result = ''
    for l in string:
        result = result + chr(ord(l)+10)
    string = result

    string = base64.b64encode(str.encode(string))

    encrypted.delete(1.0, "end")
    encrypted.insert(1.0, string)


def decrypt():
    string = encrypted.get("1.0", "end")

    string = base64.b64decode(string)

    string = string.decode('utf-8')

    result = ''
    for l in string:
        result = result + chr(ord(l)-10)
    string = result

    string = string[::-1]

    decrypted.delete(1.0, "end")
    decrypted.insert(1.0, string)


def copy_decrypted():
    string = decrypted.get("1.0", "end")
    pyperclip.copy(string)


def copy_encrypted():
    string = encrypted.get("1.0", "end")
    pyperclip.copy(string)


#def paste_decrypted():
#    decrypted.delete(1.0, "end")
#    decrypted.insert(1.0, pyperclip.paste())
#
#
#def paste_encrypted():
#    encrypted.delete(1.0, "end")
#    encrypted.insert(1.0, pyperclip.paste())


style = darkstyle(window)

decrypted = tk.Text(window, borderwidth=0, background='#262626')
encrypted = tk.Text(window, borderwidth=0, background='#262626')

encrypt = tk.Button(window, text='Зашифровать',
                    command=encrypt,
                    background='#393939',
                    borderwidth=0,
                    relief="solid")
decrypt = tk.Button(window, text='Расшифровать',
                    command=decrypt,
                    background='#393939',
                    borderwidth=0,
                    relief="solid")

copy_icon = tk.PhotoImage(file='copy-icon.png')
decrypt_copy = tk.Button(window,
                         image=copy_icon,
                         borderwidth=0,
                         background='#262626',
                         command=copy_decrypted)
encrypt_copy = tk.Button(window,
                         image=copy_icon,
                         borderwidth=0,
                         background='#262626',
                         command=copy_encrypted)

decrypted.configure(font=("Calibri", 16))
encrypted.configure(font=("Calibri", 16))

decrypt_copy.place(x=468, y=168,
                   width=32, height=32)
encrypt_copy.place(x=468, y=398,
                   width=32, height=32)

decrypted.place(x=0, y=0,
                width=500, height=200)
encrypted.place(x=0, y=230,
                width=500, height=200)

encrypt.place(x=125, y=200,
              width=100, height=30)
decrypt.place(x=250, y=200,
              width=100, height=30)

window.mainloop()
