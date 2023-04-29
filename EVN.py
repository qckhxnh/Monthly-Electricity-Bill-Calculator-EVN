import tkinter as tk
import locale
from tkinter import messagebox
import sys
locale.setlocale(locale.LC_ALL, 'vi_VN')

def clear_entries():
    name_entry.delete(0, tk.END)
    month_entry.delete(0, tk.END)
    old_kwh_entry.delete(0, tk.END)
    new_kwh_entry.delete(0, tk.END)
    vat_entry.delete(0, tk.END)
    name_used_entry.delete(0, tk.END)
    month_used_entry.delete(0, tk.END)
    kwh_used_entry.delete(0,tk.END)
    cost_before_vat_entry.delete(0,tk.END)
    vat_amount_entry.delete(0,tk.END)
    total_cost_entry.delete(0,tk.END)

def show_message():
    messagebox.showinfo("Bảng giá điện bậc thang", "Bậc 1 :   00 - 50 kw = 1.678 đ \nBậc 2 :   51-100 kw = 1.734 đ \nBậc 3 : 101-200 kw = 2.014 đ \nBậc 4 : 201-300 kw = 2.536 đ \nBậc 5 : 301-400 kw = 2.834 đ \nBậc 6 :     > 401 kw = 2.927 đ")

def calculate():
    # Lấy giá trị từ các đối tượng nhập liệu
    name = name_entry.get()
    month = int(month_entry.get())
    old_kwh = int(old_kwh_entry.get())
    new_kwh = int(new_kwh_entry.get())
    vat = float(vat_entry.get())




    # Tính toán các giá trị cần thiết

    bac_thang = ["1678","1734","2014","2536","2834","2927"]
    thang_list = ["1","2","3","4","5","6","7","8","9","10","11","12"]




    if (old_kwh < 0) or (new_kwh - old_kwh <= 0) :
        messagebox.showerror("Thông báo", "Nhập sai chỉ số điện . Vui lòng nhập lại")

    else:

        kwh_used = new_kwh - old_kwh

        if kwh_used <= 50:
            cost_before_vat = kwh_used*int(bac_thang[0])
        elif kwh_used <= 100:
            cost_before_vat = 50*int(bac_thang[0]) + (kwh_used-50)*int(bac_thang[1])
        elif kwh_used <= 200:
            cost_before_vat = 50*int(bac_thang[0]) + 50*int(bac_thang[1]) + ((kwh_used-100)*int(bac_thang[2]))
        elif kwh_used < 300:
            cost_before_vat = 50*int(bac_thang[0]) + 50*int(bac_thang[1]) + 100*int(bac_thang[2]) + ((kwh_used-200)*int(bac_thang[3]))
        elif kwh_used <= 400:
            cost_before_vat = 50*int(bac_thang[0]) + 50*int(bac_thang[1]) + 100*int(bac_thang[2]) + 100*int(bac_thang[3]) + ((kwh_used-300)*int(bac_thang[4]))
        else :
            cost_before_vat = 50*int(bac_thang[0]) + 50*int(bac_thang[1]) + 100*int(bac_thang[2]) + 100*int(bac_thang[3]) + 100*int(bac_thang[4]) + ((kwh_used-400)*int(bac_thang[5]))

    vat_amount = cost_before_vat * vat / 100
    total_cost = cost_before_vat + vat_amount

    # Hiển thị kiểu giá trị VNĐ

    amount = cost_before_vat 
    formatted_amount = locale.currency(amount, grouping=True)

    amount_1 =  vat_amount
    formatted_amount_1 = locale.currency(amount_1, grouping=True)

    amount_2 = cost_before_vat + vat_amount
    formatted_amount_2 = locale.currency(amount_2, grouping=True)



    
    # Cập nhật giá trị vào các đối tượng hiển thị kết quả
    if len(name) == 0:
    	messagebox.showerror("Thông báo", "Bạn chưa nhập tên")
    else:
        name_used_entry.delete(0, tk.END)
        name_used_entry.insert(0, str(name))

    if month > 12 or month < 1 :
       messagebox.showerror("Thông báo", "Nhập lại tháng từ 1 - 12")
    else: 
    	month_used_entry.delete(0, tk.END)
    	month_used_entry.insert(0, str(month))

    kwh_used_entry.delete(0, tk.END)
    kwh_used_entry.insert(0, str(kwh_used))

    cost_before_vat_entry.delete(0, tk.END)
    cost_before_vat_entry.insert(0, str(formatted_amount))

    vat_amount_entry.delete(0, tk.END)
    vat_amount_entry.insert(0, str(formatted_amount_1))

    total_cost_entry.delete(0, tk.END)
    total_cost_entry.insert(0, str(formatted_amount_2))

# Tạo một đối tượng Tkinter window
window = tk.Tk()
window.title("Tính tiền điện")

# Tạo một khung nhập liệu
entry_frame = tk.Frame(window, padx=10, pady=10)
entry_frame.pack(side=tk.LEFT, padx=5, pady=5)

# Tạo một nhãn cho khung nhập liệu tên
name_label = tk.Label(entry_frame, text="Tên người dùng ")
name_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

# Tạo một đối tượng nhập liệu tên
name_entry = tk.Entry(entry_frame)
name_entry.grid(row=0, column=1, padx=5, pady=5)

# Tạo một nhãn cho khung nhập liệu tháng
month_label = tk.Label(entry_frame, text="Nhập tháng dùng ")
month_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

# Tạo một đối tượng nhập liệu tháng

month_entry = tk.Entry(entry_frame)
month_entry.grid(row=1, column=1, padx=5, pady=5)

# Tạo một nhãn cho khung nhập liệu số kw cũ
old_kwh_label = tk.Label(entry_frame, text="Nhập số kWh cũ")
old_kwh_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")

# Tạo một đối tượng nhập liệu số kw cũ
old_kwh_entry = tk.Entry(entry_frame)
old_kwh_entry.grid(row=2, column=1, padx=5, pady=5)

# Tạo một nhãn cho khung nhập liệu số kw mới
new_kwh_label = tk.Label(entry_frame, text="Nhập số kWh mới")
new_kwh_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")

# Tạo một đối tượng nhập liệu số kw mới
new_kwh_entry = tk.Entry(entry_frame)
new_kwh_entry.grid(row=3, column=1, padx=5, pady=5)

# Tạo một nhãn cho khung nhập liệu VAT
vat_label = tk.Label(entry_frame, text="Nhập VAT (8-10%)")
vat_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")

# Tạo một đối tượng nhập liệu VAT
vat_entry = tk.Entry(entry_frame)
vat_entry.grid(row=4, column=1, padx=5, pady=5)


# Tạo một nút reset all
reset_button = tk.Button(entry_frame, text="Reset All", command=clear_entries)
reset_button.grid(row=5, column=1, padx=0, pady=0)

# Tạo một nút bảng giá
bacthang_button = tk.Button(entry_frame, text="Price list ", command=show_message)
bacthang_button.grid(row=5, column=0, padx=0, pady=0)

# Tạo một nút tính toán
calculate_button = tk.Button(entry_frame, text="Calculator", command=calculate)
calculate_button.grid(row=5, column=2, padx=0, pady=0)


# Tạo một khung hiển thị kết quả
result_frame = tk.Frame(window, padx=10, pady=10)
result_frame.pack(side=tk.LEFT, padx=5, pady=5)

# Tạo một nhãn cho khung hiển thị số kWh đã sử dụng
name_used_label = tk.Label(result_frame, text="Tên người dùng")
name_used_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

# Tạo một đối tượng hiển thị số kWh đã sử dụng
name_used_entry = tk.Entry(result_frame)
name_used_entry.grid(row=0, column=1, padx=5, pady=5)

# Tạo một nhãn cho khung hiển thị tháng sử dụng
month_used_label = tk.Label(result_frame, text="Tháng sử dụng")
month_used_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

# Tạo một đối tượng hiển thị tháng sử dụng
month_used_entry = tk.Entry(result_frame)
month_used_entry.grid(row=1, column=1, padx=5, pady=5)

# Tạo một nhãn cho khung hiển thị số kWh đã sử dụng
kwh_used_label = tk.Label(result_frame, text="kWh đã sử dụng")
kwh_used_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")

# Tạo một đối tượng hiển thị số kWh đã sử dụng
kwh_used_entry = tk.Entry(result_frame)
kwh_used_entry.grid(row=2, column=1, padx=5, pady=5)

# Tạo một nhãn cho khung hiển thị số tiền chưa VAT
cost_before_vat_label = tk.Label(result_frame, text="Tổng tiền điện ")
cost_before_vat_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")

# Tạo một đối tượng hiển thị số tiền chưa VAT
cost_before_vat_entry = tk.Entry(result_frame)
cost_before_vat_entry.grid(row=3, column=1, padx=5, pady=5)

# Tạo một nhãn cho khung hiển thị số tiền VAT
vat_amount_label = tk.Label(result_frame, text="Tổng tiền VAT ")
vat_amount_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")

# Tạo một đối tượng hiển thị số tiền VAT
vat_amount_entry = tk.Entry(result_frame)
vat_amount_entry.grid(row=4, column=1, padx=5, pady=5)

# Tạo một nhãn cho khung hiển thị tổng số tiền
total_cost_label = tk.Label(result_frame, text="Số tiền phải trả ")
total_cost_label.grid(row=5, column=0, padx=5, pady=5, sticky="w")

# Tạo một đối tượng hiển thị tổng số tiền
total_cost_entry = tk.Entry(result_frame)
total_cost_entry.grid(row=5, column=1, padx=5, pady=5)

# Chạy vòng lặp chính của ứng dụng
window.mainloop()
