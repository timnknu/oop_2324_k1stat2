import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("My Timer")
        #setting window size
        width=348
        height=192
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        #root.resizable(width=False, height=False)

        time_entry = tk.Entry(root, text = "0")
        time_entry.place(x=70,y=40,width=186)

        lbl1 = tk.Label(root, text = "Кількість секунд")
        lbl1.place(x=20,y=20)

        start_btn = tk.Button(root, text = "Пуск",
                              command = self.start_bnt_onclick)
        start_btn.place(x=30,y=110,width=70,height=25)

        stop_btn = tk.Button(root, text = "Стоп",
                             command = self.stop_btn_onclick)
        stop_btn.place(x=220,y=110,width=70,height=25)

    def start_bnt_onclick(self):
        print("command 123")


    def stop_btn_onclick(self):
        print("command 345")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
#        ft = tkFont.Font(family='Times',size=10)
