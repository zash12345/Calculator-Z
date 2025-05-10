import tkinter as tk

# Fungsi saat tombol ditekan
def button_click(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Buat jendela
window = tk.Tk()
window.title("Calculator Z")
window.geometry("300x400")
window.configure(bg="#f0f0f0")

# Kolom input
entry = tk.Entry(window, font=("Arial", 18), bd=10, relief=tk.RIDGE, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

# Tombol
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', 'x'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

# Tambahkan tombol ke window
for i, row in enumerate(buttons):
    for j, btn_text in enumerate(row):
        if btn_text == '=':
            action = calculate
        else:
            action = lambda x=btn_text: button_click(x)
        tk.Button(
            window,
            text=btn_text,
            width=5,
            height=2,
            font=("Arial", 14),
            command=action,
            bg="#e6e6e6"
        ).grid(row=i+1, column=j, padx=5, pady=5)

# Tombol clear
tk.Button(
    window,
    text="C",
    width=10,
    height=2,
    font=("Arial", 14),
    bg="#ffcccc",
    command=clear
).grid(row=5, column=0, columnspan=4, padx=5, pady=10)

# Jalankan aplikasi
window.mainloop()
