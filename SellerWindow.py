import tkinter as tk
from tkinter import messagebox, Label, Frame
import DBConnection as db
from datetime import datetime, timedelta
import pytz

tz_Kolkata = pytz.timezone('Asia/Kolkata')
datetime_Kol = datetime.now(tz_Kolkata).strftime('%Y-%m-%d %H:%M:%S')
final_time = (datetime.now() + timedelta(hours=12)).strftime('%Y-%m-%d %H:%M:%S')


def displayData(frame, rows):

    for widget in frame.winfo_children():
        widget.destroy()

    headers = ["Product ID ", "Product Name", "Category", "Initial Bid", "Maximum Bid", "Bid Closer Time", "Bidder Id"]
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



def open_seller_product_window(seller_window, seller_user_id):
    sPWRoot = tk.Toplevel(seller_window)
    sPWRoot.title('Your Products')
    sPWRoot.geometry('1080x600')
    sPWRoot.configure(background='#3C3E56')
    sPWRoot.resizable(False, False)

    frame = Frame(sPWRoot)
    frame.pack()

    def fetch_data():
        try:
            cursor = db.conn.cursor()
            cursor.execute("SELECT pid, pname, pcategory, initialBid, maxBid, finalTime, bidder_id FROM SellersProductDetails WHERE seller_id = ?", seller_user_id)
            rows = cursor.fetchall()
            displayData(frame, rows)
        except Exception as e:
            messagebox.showinfo('Error', e)
        finally:
            cursor.close()

    fetch_data()

    # Refresh button
    refresh_btn = tk.Button(sPWRoot, text="Refresh", bg='black', fg='white', command=fetch_data)
    refresh_btn.pack(pady=10)


def open_seller_window(seller_name, seller_user_id):
    seller_window = tk.Tk()
    seller_window.geometry('800x600')
    seller_window.title("Seller Dashboard")
    seller_window.configure(background='#3C3E56')
    seller_window.resizable(False, False)

    welcome_label = tk.Label(seller_window, text=f"Welcome, {seller_name} (User ID: {seller_user_id})!", font=('Arial', 20, 'bold'),
                             background='#3C3E56', foreground='white')
    welcome_label.pack(pady=20)

    # Set common margin values
    label_x = 250
    entry_x = 410
    common_width = 150

    # Product Name label
    product_name_label = tk.Label(seller_window, text="Product Name", font=('Arial', 12), background='#3C3E56', foreground='white')
    product_name_label.place(x=274, y=80, width=common_width)

    # Product Name entry box
    product_name_entry = tk.Entry(seller_window, font=('Arial', 14), width=20)
    product_name_entry.place(x=entry_x, y=80, width=100)

    # Product Category label
    product_category_label = tk.Label(seller_window, text="Product Category", font=('Arial', 12), background='#3C3E56', foreground='white')
    product_category_label.place(x=263, y=120, width=common_width)
    # Product Category dropdown menu
    category_var = tk.StringVar(seller_window)
    category_var.set("Select")  # Set default value
    product_category_menu = tk.OptionMenu(seller_window, category_var, "Luxury", "NonLuxury")
    product_category_menu.place(x=entry_x, y=120, width=100)

    # Initial Bid label
    initial_bid_label = tk.Label(seller_window, text="Initial Bid", font=('Arial', 12), background='#3C3E56',
                                 foreground='white')
    initial_bid_label.place(x=290, y=160, width=common_width)

    # Initial Bid entry box
    initial_bid_entry = tk.Entry(seller_window, font=('Arial', 14), width=20)
    initial_bid_entry.place(x=entry_x, y=160, width=100)

    ''''' end_time_label = tk.Label(seller_window, text="Initial Bid", font=('Arial', 12), background='#3C3E56',
                                 foreground='white')
    end_time_label.place(x=400, y=160, width=common_width)

    # Initial Bid entry box
    end_time_entry = tk.Entry(seller_window, font=('Arial', 14), width=20)
    end_time_entry.place(x=entry_x, y=160, width=100) '''''''''
    # Submit button
    submit_btn = tk.Button(seller_window, text="Submit", bg='black', fg='white',
                           command=lambda: submit_product(product_name_entry, category_var, initial_bid_entry, seller_user_id))
    submit_btn.place(x=310, y=200)
    logout_btn = tk.Button(seller_window, text="Logout", bg='black', fg='white', command=lambda: logout(seller_window))
    logout_btn.place(x=370, y=200)
    logout_btn = tk.Button(seller_window, text="Show products", bg='black', fg='white', command=lambda: open_seller_product_window(seller_window, seller_user_id))
    logout_btn.place(x=430, y=200)

    seller_window.mainloop()

def logout(window):
    window.destroy()
    import main
    main.root.deiconify()

def submit_product(product_name_entry, category_var, initial_bid_entry, seller_user_id):
    try:
        cursor = db.conn.cursor()
        cursor.execute(f"""
                INSERT INTO SellersProductDetails (pname, pcategory, initialBid, maxBid, seller_id, initialTime,finalTime)
                VALUES ('{product_name_entry.get()}', '{category_var.get()}', {initial_bid_entry.get()},{initial_bid_entry.get()}, '{seller_user_id}','{datetime_Kol}', '{final_time}');
            """)
        db.conn.commit()
        tk.messagebox.showinfo("Success", "Product registered successfully")
    except Exception:
        messagebox.showerror("Error", "Something went wrong, try checking if all inputs are properly given.")
    finally:
        cursor.close()