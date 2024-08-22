import tkinter as tk
from tkinter import messagebox, ttk
import DBConnection as dbConnection


def open_seller_reg_form():
    import Seller
    root.withdraw()
    Seller.sellerRegForm(root)

def open_bidder_reg_form():
    import Bidder
    root.withdraw()
    Bidder.bidderRegForm(root)

# Initialize the main window
root = tk.Tk()
root.geometry('800x600')
root.title("Auction Management System")
root.configure(background='#3C3E56')
root.resizable(False, False)
inWindowTitle = tk.Label(root, text="Auction Management System", font=('Arial', 20, 'bold'),
                         background='#3C3E56', foreground='white')
inWindowTitle.pack(side="top", pady=25)
x = -20

def loginAct(from_whom):
    global _userId
    if len(user_id.get()) + len(passw.get()) != 0:
        _userId = user_id.get()
        _password = passw.get()
        try:

            cursor = dbConnection.conn.cursor()
            if cursor:
                print("Connection established")
                # Validate user credentials
                if from_whom == 1:
                    cursor.execute("SELECT name, user_id FROM Sellers WHERE user_id = ? AND password = ?", (_userId, _password))
                    seller = cursor.fetchone()
                    if seller:
                        root.destroy()
                        try:
                            import SellerWindow as sellerWindow
                            sellerWindow.open_seller_window(seller[0], seller[1])
                        except Exception as e:
                            print(e)
                    else:
                        messagebox.showerror("Error", "Invalid Seller credentials")
                elif from_whom == 2:
                    cursor.execute("SELECT name, user_id FROM Bidders WHERE user_id = ? AND password = ?", (_userId, _password))
                    bidder = cursor.fetchone()
                    root.destroy()
                    if bidder:
                        try:
                            import BidderWindow as bidderWindow
                            bidderWindow.open_bidder_window(bidder[0], bidder[1])
                        except Exception as e:
                            print(e)
                    else:
                        messagebox.showerror("Error", "Invalid Bidder credentials")
        except Exception as e:
            messagebox.showinfo("Error", e)
        finally:
            if cursor:
                cursor.close()
    else:
        messagebox.showinfo("Credentials Empty", "Please fill in the username and password before login.")

def registerAct(from_whom):
    if from_whom == 1:
        open_seller_reg_form()
    else:
        open_bidder_reg_form()

def main():
    global user_id, passw
    thirdrow = tk.Label(root, text="User ID", bg="#3C3E56", font=('Arial', 15, 'bold'), foreground='white')
    thirdrow.place(x=300, y=80, width=100)

    user_id = tk.Entry(root, width=35)
    user_id.place(x=410, y=85, width=100)

    forthrow = tk.Label(root, text="Password", bg="#3C3E56", font=('Arial', 15, 'bold'), foreground='white')
    forthrow.place(x=300, y=105, width=100)

    passw = tk.Entry(root, width=35, show='*')
    passw.place(x=410, y=110, width=100)

    seller_login_btn = tk.Button(root, text="Seller Login", bg='black', fg='white', command=lambda: loginAct(1))
    seller_login_btn.place(x=(250 + x), y=150)

    sellerRegBtn = tk.Button(root, text="Seller Register", bg='black', fg='white', command=lambda: registerAct(1))
    sellerRegBtn.place(x=330 + x, y=150)

    bidderLoginBtn = tk.Button(root, text="Bidder Login", bg='black', fg='white', command=lambda: loginAct(2))
    bidderLoginBtn.place(x=425 + x, y=150)

    bidderRegBtn = tk.Button(root, text="Bidder Register", bg='black', fg='white', command=lambda: registerAct(2))
    bidderRegBtn.place(x=510 + x, y=150)

    # Create and place the flashing label
    flashLabel = tk.Label(root, text="Bumper Auction Sale!", font=('Arial', 20, 'bold'), fg='red', bg='yellow')
    flashLabel.place(x=400, y=250, anchor="center")

    def flash_label():
        current_color = flashLabel.cget("foreground")
        next_color = "red" if current_color == "white" else "white"
        flashLabel.config(foreground=next_color)
        root.after(500, flash_label)  # Change the color every 500ms

    flash_label()
    root.mainloop()


main()

