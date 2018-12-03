# -*- coding:utf-8 -*-

#************import***********
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
#***********~import***********

#*************App*************
class App(object):
    def __init__(self):
        self.root = tk.Tk()             # create an instance
        self.root.title("PC上位机")     # add a title
        self.root.resizable(0, 0)       # Disable resizing the GUI
        self.comment()

    def comment(self):                  # part of comment
        # scrolledtext
        self.scr = scrolledtext.ScrolledText(self.root, width=60, height=20, wrap=tk.WORD, bg='black')
        self.scr.grid(column=0, row=0, sticky='WE', rowspan=11, columnspan=8)

        # label1
        self.label1 = tk.Label(self.root, text="串口")
        self.label1.grid(column=8, row=1, sticky='E')
        # label2
        self.label2 = tk.Label(self.root, text="波特率")
        self.label2.grid(column=8, row=2, sticky='E')
        # label3
        self.label3 = tk.Label(self.root, text="数据位")
        self.label3.grid(column=8, row=3, sticky='E')
        # label4
        self.label4 = tk.Label(self.root, text="校验位")
        self.label4.grid(column=8, row=4, sticky='E')
        # label5
        self.label5 = tk.Label(self.root, text="停止位")
        self.label5.grid(column=8, row=5, sticky='E')

    def case1(self):                    # part of single sending
        pass
    
    def case2(self):                    # part of multi sending
        pass
    
    def case3(self):                    # part of statement
        pass


    def set_icon(self, addr):
        self.root.iconbitmap(addr)      # change the main windows icon
    
    def run(self):
        self.root.mainloop()            # start GUI

#************~App*************


#*************main************
def main():
    app = App()
    app.run()
#************~main************

#***********start*************
if __name__ == '__main__':
    main()
