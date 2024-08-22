import tkinter as tk
import DBConnection as db
from tkinter import messagebox


def open_bid_window(root, bidder_id):
    bid_window = tk.Toplevel(root)
    bid_window.geometry('800x500')
    bid_window.title("BIDDING WINDOW")
    bid_window.configure(background='#3C3E56')
    bid_window.resizable(False, False)
    welcome_label = tk.Label(bid_window, text="Place your Bid!",
                             font=('Arial', 20, 'bold'), background='#3C3E56', foreground='white')
    welcome_label.pack(pady=20)

    def submitBid():
        if pId.get() and bid.get():
            try:
                cursor = db.conn.cursor()
                if cursor:
                    cursor.execute("SELECT maxBid from sellersproductdetails where pid = ?", (pId.get()))
                    initialBid = cursor.fetchall()
                    print(initialBid[0][0])
                    if float(initialBid[0][0]) < float(bid.get()):
                        sql = "UPDATE sellersproductdetails SET maxBid = ?, bidder_id = ? WHERE pid = ?"
                        # Execute the query with parameters
                        cursor.execute(sql, (bid.get(), bidder_id, pId.get()))
                        cursor.commit()
                        messagebox.showinfo("Bid", "Your bid submitted successfully!")
                        bid_window.destroy()
                    else:
                        messagebox.showinfo("Bid", "Your bid is less than maximum bid")
                else:
                    messagebox.showinfo("Error", "Something went wrong!")
            except Exception as e:
                messagebox.showinfo("Error", e)
        else:
            messagebox.showinfo("Error", "Please enter your bid!")

    label_x = 200
    entry_x = 360
    width = 250
    height = 30

    product_id_label = tk.Label(bid_window, text="Product ID", font=('Arial', 13), background='#3C3E56', foreground='white')
    product_id_label.place(x=label_x, y=80, width=150, height=height)
    pId = tk.Entry(bid_window, font=('Arial', 14))
    pId.place(x=entry_x, y=80, width=width, height=height)

    your_bid_label = tk.Label(bid_window, text="Your Bid", font=('Arial', 13), background='#3C3E56',foreground='white')
    your_bid_label.place(x=label_x, y=120, width=150, height=height)
    bid = tk.Entry(bid_window, font=('Arial', 14))
    bid.place(x=entry_x, y=120, width=width, height=height)

    # Add the submit button
    submit_button = tk.Button(bid_window, text="Submit", font=('Arial', 13), background='#5A5C72', foreground='white',
                              command=submitBid)
    submit_button.place(x=360, y=280, width=100, height=30)

    bid_window.mainloop()
