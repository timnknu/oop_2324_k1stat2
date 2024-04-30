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

        GLineEdit_379=tk.Entry(root)
        GLineEdit_379["text"] = "0"
        GLineEdit_379.place(x=70,y=40,width=186,height=37)

        GLabel_966=tk.Label(root)
        GLabel_966["text"] = "Кількість секунд"
        GLabel_966.place(x=20,y=20,width=70,height=25)

        GButton_939=tk.Button(root)
        GButton_939["text"] = "Пуск"
        GButton_939.place(x=30,y=110,width=70,height=25)
        GButton_939["command"] = self.start_bnt_onclick

        GButton_533=tk.Button(root)
        GButton_533["text"] = "Стоп"
        GButton_533.place(x=220,y=110,width=70,height=25)
        GButton_533["command"] = self.GButton_533_command

    def start_bnt_onclick(self):
        print("command 123")


    def GButton_533_command(self):
        print("command 345")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
#        ft = tkFont.Font(family='Times',size=10)
