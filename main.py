from tkinter import *


# root class
class MainWindow:
    def __init__(self, win):
        self.win = win
        self.clr = '#000080'
        self.create_widget()
        
    # create main widget
    def create_widget(self):
        self.top_frame = Frame(self.win)
        self.top_frame.pack(side=TOP, fill=X)
        self.lb_status = Label(self.top_frame, text=' Jonaki Computer Training Center', font='Cambria 28 bold', bg=self.clr, fg='white', anchor=W)
        self.lb_status.pack(side=LEFT, fill=X, expand=1)
        self.lb_status1 = Label(self.top_frame, text=u'\u232C'+' Registration '+u'\u232C', font='Cambria 28 bold', bg=self.clr, fg='white')
        self.lb_status1.pack(side=LEFT, fill=X, expand=1)
        self.bottom_frame = Frame(self.win)
        self.bottom_frame.pack(side=BOTTOM, fill=X)
        self.lb_status1 = Label(self.bottom_frame, text='[+880123456789] Rajshahi, Dhaka, Bangladesh [+880123456789]', font='Cambria 12 bold', bg=self.clr, fg='white')
        self.lb_status1.pack(side=TOP, fill=X, expand=1)
        self.lb_status2 = Label(self.bottom_frame, text='email.one@gmail.com, email.two@gmail.com', font='Cambria 10 bold', bg=self.clr, fg='white')
        self.lb_status2.pack(side=TOP, fill=X, expand=1)


# root
if __name__ == '__main__':
    win = Tk()
    win.title('Jonaki Computer Training Center')
    win.resizable(0, 0)
    app = MainWindow(win)
    win.mainloop()