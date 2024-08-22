import tkinter as tk
from tkinter import messagebox
import pyodbc

def sellerRegForm(main_window):
    root_seller = tk.Tk()
    root_seller.geometry('800x600')
    root_seller.title("Auction Management System")
    root_seller.configure(background='#3C3E56')
    root_seller.resizable(False, False)

    # Title label
    inWindowTitle = tk.Label(root_seller, text="Auction Management System", font=('Arial', 20, 'bold'),
                             background='#3C3E56', foreground='white')
    inWindowTitle.pack(side="top", pady=25)



    def back_to_main():
        root_seller.destroy()
        main_window.deiconify()

    def register_seller():
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
                INSERT INTO Sellers(name, address, phone_no, user_id, password)
                VALUES ('{seller_name_entry.get()}', '{seller_address_entry.get()}', '{seller_phone_entry.get()}', '{seller_userid_entry.get()}', '{seller_password_entry.get()}')
                """)
                cursor.commit()
                messagebox.showinfo("Success", "Registration successful")
                back_to_main()
            else:
                messagebox.showinfo("Error", "Registration failed")
        except Exception as err:
            messagebox.showerror("Error", f"Error: {err}")

    # Create a frame for the form
    form_frame = tk.Frame(root_seller, background='#3C3E56')
    form_frame.pack(pady=20)

    # Seller Name
    tk.Label(form_frame, text="Seller Name:", font=('Arial', 14), background='#3C3E56', foreground='white').grid(row=0, column=0, padx=10, pady=10, sticky='e')
    seller_name_entry = tk.Entry(form_frame, font=('Arial', 14), width=30)
    seller_name_entry.grid(row=0, column=1, padx=10, pady=10)

    # Seller Address
    tk.Label(form_frame, text="Seller Address:", font=('Arial', 14), background='#3C3E56', foreground='white').grid(row=1, column=0, padx=10, pady=10, sticky='e')
    seller_address_entry = tk.Entry(form_frame, font=('Arial', 14), width=30)
    seller_address_entry.grid(row=1, column=1, padx=10, pady=10)

    # Seller Phone No.
    tk.Label(form_frame, text="Seller Phone No:", font=('Arial', 14), background='#3C3E56', foreground='white').grid(row=2, column=0, padx=10, pady=10, sticky='e')
    seller_phone_entry = tk.Entry(form_frame, font=('Arial', 14), width=30)
    seller_phone_entry.grid(row=2, column=1, padx=10, pady=10)

    # Seller User ID
    tk.Label(form_frame, text="User Id:", font=('Arial', 14), background='#3C3E56', foreground='white').grid(row=3, column=0, padx=10, pady=10, sticky='e')
    seller_userid_entry = tk.Entry(form_frame, font=('Arial', 14), width=30)
    seller_userid_entry.grid(row=3, column=1, padx=10, pady=10)

    # Seller Password
    tk.Label(form_frame, text="Password:", font=('Arial', 14), background='#3C3E56', foreground='white').grid(row=4, column=0, padx=10, pady=10, sticky='e')
    seller_password_entry = tk.Entry(form_frame, font=('Arial', 14), width=30, show='*')
    seller_password_entry.grid(row=4, column=1, padx=10, pady=10)

    # Submit button
    seller_button = tk.Button(form_frame, text="Submit", command=register_seller,
                              font=('Arial', 14), background='#5A5C72', foreground='white')
    seller_button.grid(row=5, column=1, pady=20)

    # Back button
    back_button = tk.Button(form_frame, text="Back", command=back_to_main,
                            font=('Arial', 14), background='#5A5C72', foreground='white')
    back_button.grid(row=6, column=1, pady=20)

    # Start the main loop
    root_seller.mainloop()

