import tkinter as tk
from tkinter import messagebox, Label, Frame
import BidWindow
import DBConnection as db
from datetime import datetime, timedelta
import pytz

# get the current time
tz_Kolkata = pytz.timezone('Asia/Kolkata')
datetime_Kol = datetime.now(tz_Kolkata).strftime('%Y-%m-%d %H:%M:%S')
final_time = (datetime.now() + timedelta(hours=12)).strftime('%Y-%m-%d %H:%M:%S')


def displayData(frame, rows):
    for widget in frame.winfo_children():
        widget.destroy()

    headers = ["Product ID ", "Product Name", "Category", "Maximum Bid", "Seller ID", "Bid Closer Time"]
    for col, header in enumerate(headers):
        label = Label(frame, text=header,
                      font=("Arial", 12, "bold"), bg="white", fg="black", borderwidth=2, relief="solid", padx=5, pady=5)
        label.grid(row=0, column=col, sticky="nsew")

        for row_num, row in enumerate(rows, start=1):
            for col, value in enumerate(row):
                label = Label(frame, text=value, font=("Arial", 12),
                              borderwidth=1, relief="solid", padx=5, pady=5)
                label.grid(row=row_num, column=col, sticky="nsew")
    for i in range(len(rows[0])):
        frame.grid_columnconfigure(i, weight=1)
    for i in range(len(rows) + 1):
        frame.grid_rowconfigure(i, weight=1)


def open_bidder_window(bidder_name, bidder_user_id):
    bidder_window = tk.Tk()
    bidder_window.geometry('1000x600')
    bidder_window.title("Bidder Dashboard")
    bidder_window.configure(background='#3C3E56')
    bidder_window.resizable(False, False)

    welcome_label = tk.Label(bidder_window, text=f"Welcome, {bidder_name} (User ID: {bidder_user_id})!",
                             font=('Arial', 20, 'bold'),
                             background='#3C3E56', foreground='white')
    welcome_label.pack(pady=20)

    frame = Frame(bidder_window)
    frame.pack()

    def fetch_data():
        try:
            cursor = db.conn.cursor()
            cursor.execute("SELECT pid, pname, pcategory, maxBid, seller_id, finalTime FROM SellersProductDetails WHERE CURRENT_TIMESTAMP < finalTime")
            rows = cursor.fetchall()
            displayData(frame, rows)
        except Exception as e:
            messagebox.showerror("Error", f"Error fetching data: {e}")
        finally:
            cursor.close()

    # Fetch data initially
    fetch_data()


    refresh_btn = tk.Button(bidder_window, text="Refresh", bg='black', fg='white', command=fetch_data)
    place_bid_btn = tk.Button(bidder_window, text="place_bit", bg='black', fg='white', command=lambda: BidWindow.open_bid_window(bidder_window, bidder_user_id))
    logout_btn = tk.Button(bidder_window, text="Logout", bg='black', fg='white', command=lambda: logout(bidder_window))

    refresh_btn.pack(side='bottom', padx=10, pady=10)
    place_bid_btn.pack(side='bottom', padx=10, pady=10)
    logout_btn.pack(side='bottom', padx=10, pady=10)

    bidder_window.mainloop()

def logout(window):
    window.destroy()
    import main
    main.root.deiconify()
