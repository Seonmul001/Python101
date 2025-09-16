import tkinter as tk
from tkinter import ttk, messagebox

# ------------------------------
# ฟังก์ชันหลัก
# ------------------------------
balance = 1000  # เงินตั้งต้น

def deposit():
    global balance
    try:
        amount = float(entry_amount.get())
        if amount <= 0:
            messagebox.showwarning("ผิดพลาด", "กรุณากรอกจำนวนเงินที่ถูกต้อง")
            return
        balance += amount
        update_balance()
        messagebox.showinfo("สำเร็จ", f"ฝากเงิน {amount:.2f} บาทเรียบร้อย")
        entry_amount.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("ผิดพลาด", "กรุณากรอกเป็นตัวเลข")

def withdraw():
    global balance
    try:
        amount = float(entry_amount.get())
        if amount <= 0:
            messagebox.showwarning("ผิดพลาด", "กรุณากรอกจำนวนเงินที่ถูกต้อง")
            return
        if amount > balance:
            messagebox.showerror("ผิดพลาด", "ยอดเงินไม่เพียงพอ")
            return
        balance -= amount
        update_balance()
        messagebox.showinfo("สำเร็จ", f"ถอนเงิน {amount:.2f} บาทเรียบร้อย")
        entry_amount.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("ผิดพลาด", "กรุณากรอกเป็นตัวเลข")

def update_balance():
    lbl_balance.config(text=f"{balance:,.2f} บาท")

# ------------------------------
# GUI หลัก
# ------------------------------
root = tk.Tk()
root.title("โปรแกรมจัดการบัญชี")
root.geometry("500x300")
root.configure(bg="#f4f6f7")

# ใช้ Style
style = ttk.Style()
style.configure("TButton", font=("Segoe UI", 12), padding=8)
style.configure("TLabel", font=("Segoe UI", 12))

# หัวข้อ
lbl_title = tk.Label(root, text="💰 ระบบจัดการบัญชีฝาก-ถอน", 
                     font=("Segoe UI", 18, "bold"), fg="white", bg="#2e86c1")
lbl_title.pack(fill="x", pady=5)

# แสดงยอดเงิน
frame_balance = tk.Frame(root, bg="#f4f6f7")
frame_balance.pack(pady=20)
tk.Label(frame_balance, text="ยอดเงินคงเหลือ:", font=("Segoe UI", 14), bg="#f4f6f7").grid(row=0, column=0, padx=10)
lbl_balance = tk.Label(frame_balance, text=f"{balance:,.2f} บาท", 
                       font=("Segoe UI", 14, "bold"), fg="green", bg="#f4f6f7")
lbl_balance.grid(row=0, column=1)

# กรอกจำนวนเงิน
frame_input = tk.Frame(root, bg="#f4f6f7")
frame_input.pack(pady=10)
tk.Label(frame_input, text="จำนวนเงิน:", font=("Segoe UI", 12), bg="#f4f6f7").grid(row=0, column=0, padx=5)
entry_amount = ttk.Entry(frame_input, width=20)
entry_amount.grid(row=0, column=1, padx=5)

# ปุ่ม
frame_buttons = tk.Frame(root, bg="#f4f6f7")
frame_buttons.pack(pady=20)
ttk.Button(frame_buttons, text="ฝากเงิน", command=deposit).grid(row=0, column=0, padx=10)
ttk.Button(frame_buttons, text="ถอนเงิน", command=withdraw).grid(row=0, column=1, padx=10)

root.mainloop()
