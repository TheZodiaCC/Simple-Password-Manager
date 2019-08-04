import tkinter as tk
from tkinter import filedialog
import random
from cryptography.fernet import Fernet


class Manager:

    def __init__(self, root):
        root.title("Tiny Manager")
        #root.geometry("200x110")
        root.resizable(width=False, height=False)
        self.widgets()

    def widgets(self):
        tk.Button(root, text="Encrypt Password", command=self.encrypt_widget).grid(row=1, column=0, sticky="NWNESWSE")
        tk.Button(root, text="Decrypt Password", command=self.decrypt_widget).grid(row=2, column=0, sticky="NWNESWSE")
        tk.Button(root, text="Get Encryption Key", command=self.get_key).grid(row=3, column=0, sticky="NWNESWSE")
        tk.Button(root, text="Generate Password", command=self.gen_pass).grid(row=4, column=0, sticky="NWNESWSE")
        tk.Button(root, text="About", command=self.about).grid(row=5, column=0, sticky="NWNESWSE")

    def encrypt_widget(self):
        encrypt_widget = tk.Tk()

        encrypt_widget.resizable(width=False, height=False)
        encrypt_widget.geometry("680x85")
        encrypt_widget.title("Encrypt - TinyManager")

        self.encrypt_text = tk.Entry(encrypt_widget, width=65, font=("Ubuntu", 10))
        self.encrypt_text.grid(row=0, column=1, columnspan=6)
        self.encrypt_key = tk.Entry(encrypt_widget, width=50, font=("Ubuntu", 10))
        self.encrypt_key.grid(row=1, column=1, columnspan=6, sticky="W")

        tk.Button(encrypt_widget, text="Load Key", command=self.open_file).grid(row=1, column=5, sticky="E")

        tk.Label(encrypt_widget, text="Password", font="20").grid(row=0, column=0)
        tk.Label(encrypt_widget, text="Encryption Key", font="20").grid(row=1, column=0)

        tk.Button(encrypt_widget, text="Encrypt Password", command=self.encrypt).grid(row=2, column=0)

        self.encrypted_password = tk.Entry(encrypt_widget, width=65, font=("Ubuntu", 10))
        self.encrypted_password.grid(row=2, column=1, columnspan=5)

        self.encrypted_password.insert(0, "Your Encrypted Password Will Appear Here")

        encrypt_widget.mainloop()

    def decrypt_widget(self):
        decrypt_widget = tk.Tk()

        decrypt_widget.resizable(width=False, height=False)
        decrypt_widget.geometry("700x85")
        decrypt_widget.title("Decrypt - TinyManager")

        self.decrypt_text = tk.Entry(decrypt_widget, width=65, font=("Ubuntu", 10))
        self.decrypt_text.grid(row=0, column=1, columnspan=6)
        self.encrypt_key = tk.Entry(decrypt_widget, width=50, font=("Ubuntu", 10))
        self.encrypt_key.grid(row=1, column=1, columnspan=6, sticky="W")

        tk.Button(decrypt_widget, text="Load Key", command=self.open_file).grid(row=1, column=5, sticky="E")

        tk.Label(decrypt_widget, text="Encrypted Password", font="20").grid(row=0, column=0)
        tk.Label(decrypt_widget, text="Encryption Key", font="20").grid(row=1, column=0)

        tk.Button(decrypt_widget, text="Decrypt Password", command=self.decrypt).grid(row=2, column=0)

        self.decrypted_password = tk.Entry(decrypt_widget, width=65, font=("Ubuntu", 10))
        self.decrypted_password.grid(row=2, column=1, columnspan=5)

        self.decrypted_password.insert(0, "Your Decrypted Password Will Appear Here")

        decrypt_widget.mainloop()

    def encrypt(self):
        if self.encrypt_text.get() == "" and self.encrypt_key.get() == "":
            print("Can't be empty")

        else:
            try:
                fern = Fernet(self.encrypt_key.get())
                self.encrypted_password.delete(0, tk.END)
                self.encrypted_password.insert(0, fern.encrypt(self.encrypt_text.get().encode()))

                #print((fern.decrypt(self.encrypted_password.get().encode())).decode())

            except Exception as e:
                print(e)

    def decrypt(self):
        if self.decrypt_text.get() == "" and self.encrypt_key.get() == "":
            print("Can't be empty")

        else:
            try:
                fern = Fernet(self.encrypt_key.get())
                self.decrypted_password.delete(0, tk.END)
                self.decrypted_password.insert(0, (fern.decrypt(self.decrypt_text.get().encode())).decode())

            except Exception as e:
                print(e)

    def open_file(self):
        try:
            self.filename = filedialog.askopenfilename(defaultextension=".key", filetypes=[("Encrypted Key", "*.key*")])

            if self.filename:
                self.title = self.filename
                self.encrypt_key.delete(0, tk.END)

                with open(self.filename, "r") as file:
                    self.encrypt_key.insert(0, file.read())

        except Exception as e:
            print(e)

    def save_file(self):
        if self.key.get() == "":
            print("Can't be empty")

        else:

            try:
                file_name = filedialog.asksaveasfilename(initialfile="key.key", defaultextension=".key",
                                                         filetypes=[("Encryption Key", "*.key*")])

                content = self.key.get()

                with open(file_name, "w") as f:
                    f.write(content)

                print("Saved")

            except Exception as e:
                print(e)

    def get_key(self):
        get_key = tk.Tk()

        #get_key.geometry("350x150")
        get_key.resizable(width=False, height=False)
        get_key.title("Get Key - TinyManager")

        #print(Fernet.generate_key())
        self.key = tk.Entry(get_key, width=65, font=("Ubuntu", 9))
        self.key.grid(row=0, column=0, columnspan=6)
        tk.Button(get_key, text="Generate Key", command=self.gen_key).grid(row=1, column=0, sticky="W")
        tk.Button(get_key, text="Save Key to File", command=self.save_file).grid(row=1, column=1, sticky="E")

        get_key.mainloop()

    def gen_key(self):
        try:
            key = Fernet.generate_key()
            self.key.delete(0, tk.END)
            self.key.insert(0, key)

        except Exception as e:
            print(e)

    def gen_pass(self):
        gen_pass = tk.Tk()
        gen_pass.resizable(width=False, height=False)

        gen_pass.geometry("910x95")
        gen_pass.title("Generate Password - TinyManager")

        self.pass_entry = tk.Entry(gen_pass, width=60, font=("Ubuntu", 20))
        self.pass_entry.grid(row=0, column=0, columnspan=6)

        self.pass_len = tk.Entry(gen_pass, width=3)
        self.pass_len.grid(row=1, column=1)

        tk.Label(gen_pass, text="Password Length").grid(row=1, column=0, sticky="NWNESWSE")

        tk.Button(gen_pass, text="Generate Password", command=self.generate).grid(row=3, column=0)

        gen_pass.mainloop()

    def generate(self):
        try:
            chars = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZCVBNM1234567890!@#$%^&*()"
            password = ""

            for i in range(int(self.pass_len.get())):
                password += random.choice(chars)

            self.pass_entry.delete(0, tk.END)
            self.pass_entry.insert(0, password)

        except Exception as e:
            print(e)


    def about(self):
        about = tk.Tk()

        about.resizable(width=False, height=False)
        #about.geometry("250x100")
        about.title("About TinyManager")

        tk.Label(about, text="TinyManager v1 ~ 21.05.2019", font="20").grid(row=0,  column=0)
        tk.Label(about, text="Created by Zodiac", font="20").grid(row=1,  column=0)

        about.mainloop()


if __name__ == "__main__":

    root = tk.Tk()
    manager = Manager(root)
    root.mainloop()