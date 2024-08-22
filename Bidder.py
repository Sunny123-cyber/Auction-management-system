import tkinter as tk
from tkinter import messagebox
import pyodbc

def bidderRegForm(root):
    # Create the bidder registration window
    root_bidder = tk.Toplevel(root)
    root_bidder.geometry('800x600')
    root_bidder.title("Auction Management System")
    root_bidder.configure(background='#3C3E56')
    root_bidder.resizable(False, False)

    # Add title label
    inWindowTitle = tk.Label(root_bidder, text="Auction Management System", font=('Arial', 20, 'bold'),
                             background='#3C3E56', foreground='white')
    inWindowTitle.pack(side="top", pady=25)

    # Function to handle form submission
    def submit_bidder_registration():
        try:
            conn_str = (
                "DRIVER={MySQL ODBC 8.4 ANSI Driver};"
                "SERVER=localhost;"
                "DATABASE=registration;"
                "USER=root;"
                "PASSWORD=Sunny@12345;"
                "PORT=3306;"
            )
            conn = pyodbc.connect(conn_str)
            cursor = conn.cursor()
            if cursor:
                cursor.execute(f"""
                INSERT INTO Bidders(name, address, phone_no, user_id, password)
                VALUES ('{bidder_name_entry.get()}', '{bidder_address_entry.get()}', '{bidder_phone_entry.get()}', '{bidder_userid_entry.get()}', '{bidder_password_entry.get()}')
                """)
                conn.commit()
                messagebox.showinfo("Success", "Registration successful")
                root_bidder.destroy()
                root.deiconify()
            else:
                messagebox.showinfo("Error", "Registration failed")
        except Exception as err:
            messagebox.showerror("Error", f"Error: {err}")

    # Function to create and place labels and entry boxes
    def create_label_entry(root, label_text, y_pos):
        label_x = 200
        entry_x = 360
        width = 250
        height = 30

        label = tk.Label(root, text=label_text, font=('Arial', 13), background='#3C3E56', foreground='white')
        label.place(x=label_x, y=y_pos, width=150, height=height)

        entry = tk.Entry(root, font=('Arial', 14))
        entry.place(x=entry_x, y=y_pos, width=width, height=height)

        return entry

    # Create labels and entry boxes
    bidder_name_entry = create_label_entry(root_bidder, "Bidder Name:", 80)
    bidder_address_entry = create_label_entry(root_bidder, "Bidder Address:", 120)
    bidder_phone_entry = create_label_entry(root_bidder, "Bidder Phone No:", 160)
    bidder_userid_entry = create_label_entry(root_bidder, "User Id:", 200)
    bidder_password_entry = create_label_entry(root_bidder, "Password:", 240)

    # Add the submit button
    submit_button = tk.Button(root_bidder, text="Submit", command=submit_bidder_registration, font=('Arial', 13), background='#5A5C72',
                              foreground='white')
    submit_button.place(x=360, y=280, width=100, height=30)

    # Add the back button
    back_button = tk.Button(root_bidder, text="Back", command=lambda: back_to_main(root_bidder, root), font=('Arial', 13), background='#5A5C72',
                            foreground='white')
    back_button.place(x=360, y=320, width=100, height=30)

    root_bidder.mainloop()

def back_to_main(current_window, main_root):
    current_window.destroy()
    main_root.deiconify()


