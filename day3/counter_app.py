import tkinter as tk

count = 0

def increase():
    global count
    count += 1
    label.config(text=str(count))

def decrease():
    global count
    count -= 1
    label.config(text=str(count))

root = tk.Tk()
root.title("숫자 증가/감소 앱")
root.geometry("300x150")

label = tk.Label(root, text="0", font=("Arial", 30))
label.pack(pady=10)

btn_frame = tk.Frame(root)
btn_frame.pack()

tk.Button(btn_frame, text="+", width=10, command=increase).pack(side="left", padx=5)
tk.Button(btn_frame, text="-", width=10, command=decrease).pack(side="right", padx=5)

root.mainloop()
