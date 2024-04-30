import tkinter as tk

root = tk.Tk()

sel1 = tk.StringVar()
sel1.set('Fr')
tk.Radiobutton(root, variable=sel1, value="Fr", text="Fruits").pack()
tk.Radiobutton(root, variable=sel1, value="Vg", text="Vegetables").pack()
tk.Label(textvariable=sel1, bg='lime').pack()

agree_var = tk.BooleanVar()
tk.Checkbutton(root, text="I agree", variable=agree_var, onvalue=True, offvalue=False).pack()

root.mainloop()