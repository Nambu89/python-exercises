import tkinter as tk 
from tkinter import messagebox

class libraryManagment:
    def __init__(self, master):
        self.master = master
        self.master.title('Library Management System')
        self.master.geometry("400x400")
        self.master.config(bg='#708090')

        self.books = []
        self.lend_list = []

        #labels
        self.login_label = tk.Label(self.master, text ='Library Management System', font=('Helvetica', 16), bg='#708090', fg='white')
        self.login_label.pack()
        self.username_label = tk.Label(self.master, text='Username', font=('Helvetica', 16), bg='#708090', fg='white',)
        self.username_label.pack()
        self.username_entry = tk.Entry(self.master, font=('helvetica', 16), show='*')
        self.username_entry.pack()

        #Password field
        self.password_label = tk.Label(self.master, text='Password', font=('Helvetica', 16), bg='#708090', fg='white',)
        self.password_label.pack()
        self.password_entry = tk.Entry(self.master, font=('helvetica', 16), show='*')
        self.password_entry.pack()

        #Login
        self.login_button = tk.Button(self.master, text='Login', command=self.login, font=('Helvetica', 12))
        self.login_button.pack()

        #Register
        self.register_button = tk.Button(self.master, text='Register', command=self.register, font=('Helvetica', 12))
        self.register_button.pack()

        self.username = ""
        self.password = ""
        self.librarians = []

    def login(self):
        self.username = self.username_entry.get()
        self.password = self.password_entry.get()
        for librarian in self.librarians:
            if self.username == librarian[0] and self.password == librarian[1]:
                self.username_entry.delete(0, tk.END)
                self.password_entry.delete(0, tk.END)
                self.login_label.destroy()
                self.username_label.destroy()
                self.username_entry.destroy()
                self.password_label.destroy()
                self.password_entry.destroy()
                self.login_button.destroy()
                self.register_button.destroy()
                self.library_management_screen()
                return
        messagebox.showerror('Error', 'Invalid username or password')
    
    def register(self):
        self.username = self.username_entry.get()
        self.password = self.password_entry.get()
        self.librarians.append([self.username, self.password])
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
    
    def library_management_screen(self):
        self.add_book_label = tk.Label(self.master, text='Add Book', font=('Helvetica', 16), bg='#708090', fg='white')
        self.add_book_label.pack()
        self.add_book_entry = tk.Entry(self.master, font=('Helvetica', 12))
        self.add_book_entry.pack()
        self.add_book_button = tk.Button(self.master, text='Add Book', command=self.add_book, font=("Helvetica", 16), bg="#708090", fg="white")
        self.add_book_button.pack()

        #... Repite este patrón para las otras funciones ...

    def add_book(self):
        book = self.add_book_entry.get()
        if book not in self.books:
            self.books.append(book)
            messagebox.showinfo("Success", "Book added successfully")
        else:
            messagebox.showerror("Error", "Book already exists")
        self.add_book_entry.delete(0, tk.END)

    #... Continúa con el resto de tus métodos ...

if __name__ == "__main__":
    root = tk.Tk()
    app = libraryManagment(root)
    root.mainloop()
