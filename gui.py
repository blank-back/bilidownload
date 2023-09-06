import tkinter
import webbrowser
from tkinter import *
from dl import *



from tkinter import *
from tkinter.ttk import *
from typing import Dict


class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.__win()
        self.tk_label_la1 = self.__tk_label_la1(self)
        self.tk_label_la2 = self.__tk_label_la2(self)
        self.tk_input_en1 = self.__tk_input_en1(self)
        self.tk_button_button1 = self.__tk_button_button1(self)
        self.tk_text_txt1 = self.__tk_text_txt1(self)
        self.tk_button_button2 = self.__tk_button_button2(self)
        self.tk_text_link1 = self.__tk_text_link1(self)

    def __win(self):
        self.title("bilidownload")
        # 设置窗口大小、居中
        width = 900
        height = 600
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        self.resizable(width=False, height=False)
        # 自动隐藏滚动条

    def scrollbar_autohide(self, bar, widget):
        self.__scrollbar_hide(bar, widget)
        widget.bind("<Enter>", lambda e: self.__scrollbar_show(bar, widget))
        bar.bind("<Enter>", lambda e: self.__scrollbar_show(bar, widget))
        widget.bind("<Leave>", lambda e: self.__scrollbar_hide(bar, widget))
        bar.bind("<Leave>", lambda e: self.__scrollbar_hide(bar, widget))

    def __scrollbar_show(self, bar, widget):
        bar.lift(widget)

    def __scrollbar_hide(self, bar, widget):
        bar.lower(widget)

    def vbar(self, ele, x, y, w, h, parent):
        sw = 15  # Scrollbar 宽度
        x = x + w - sw
        vbar = Scrollbar(parent)
        ele.configure(yscrollcommand=vbar.set)
        vbar.config(command=ele.yview)
        vbar.place(x=x, y=y, width=sw, height=h)
        self.scrollbar_autohide(vbar, ele)

    def __tk_label_la1(self, parent):
        label = Label(parent, text="bilidownload", anchor="center", )
        label.place(x=200, y=20, width=500, height=80)
        label.config(background="red")
        return label

    def __tk_label_la2(self, parent):
        label = Label(parent, text="BV/au号", anchor="center", )
        label.place(x=20, y=140, width=320, height=60)
        label.config(background="pink")
        return label

    def __tk_input_en1(self, parent):
        ipt = Entry(parent, )
        ipt.place(x=560, y=140, width=320, height=60)
        return ipt

    def __tk_text_txt1(self, parent):
        text = Text(parent)
        text.place(x=200, y=330, width=500, height=200)
        self.vbar(text, 200, 330, 500, 200, parent)
        return text

    def finret(self):
        self.tk_text_txt1.config(state=NORMAL)
        self.tk_text_txt1.delete("1.0",END)
        self.tk_text_txt1.insert(tkinter.END, "正在解析")
        self.tk_text_txt1.config(state=DISABLED)
        str1 = self.tk_input_en1.get()
        try:
            if str1[0:2].lower() == "bv":
                str2 = 'https://www.bilibili.com/video/' + str1
                get_url_html(str2)
                self.tk_text_txt1.config(state=NORMAL)
                self.tk_text_txt1.delete("1.0", END)
                self.tk_text_txt1.insert(tkinter.END, "解析成功，已存放至当前目录下")
            elif str1[0:2].lower() == "au":
                str2 = 'https://www.bilibili.com/audio/' + str1
                get_url_audio(str2)
                self.tk_text_txt1.config(state=NORMAL)
                self.tk_text_txt1.delete("1.0", END)
                self.tk_text_txt1.insert(tkinter.END, "解析成功，已存放至当前目录下")
            else:
                self.tk_text_txt1.config(state=NORMAL)
                self.tk_text_txt1.delete("1.0", END)
                self.tk_text_txt1.insert(tkinter.END, "请检查输入是否正确")
        except:
            self.tk_text_txt1.config(state=NORMAL)
            self.tk_text_txt1.delete("1.0", END)
            self.tk_text_txt1.insert(tkinter.END, "解析失败，请自行检查后重试")
        self.tk_text_txt1.config(state=DISABLED)

    def __tk_button_button1(self, parent):
            btn = Button(parent, text="下载音频", takefocus=False, command=self.finret)
            btn.place(x=180, y=250, width=140, height=40)
            return btn

    def finretvd(self):
        self.tk_text_txt1.config(state=NORMAL)
        self.tk_text_txt1.delete("1.0",END)
        self.tk_text_txt1.insert(tkinter.END, "正在解析")
        self.tk_text_txt1.config(state=DISABLED)
        str1 = self.tk_input_en1.get()
        try:
            if str1[0:2].lower() == "bv":
                str2 = 'https://www.bilibili.com/video/' + str1
                get_url_html(str2, 1)
                self.tk_text_txt1.config(state=NORMAL)
                self.tk_text_txt1.delete("1.0", END)
                self.tk_text_txt1.insert(tkinter.END, "解析成功，已存放至当前目录下")
            else:
                self.tk_text_txt1.config(state=NORMAL)
                self.tk_text_txt1.delete("1.0", END)
                self.tk_text_txt1.insert(tkinter.END, "请检查输入是否正确")
        except:
            self.tk_text_txt1.config(state=NORMAL)
            self.tk_text_txt1.delete("1.0", END)
            self.tk_text_txt1.insert(tkinter.END, "解析失败，请自行检查后重试")
        self.tk_text_txt1.config(state=DISABLED)

    def __tk_button_button2(self, parent):
            btn = Button(parent, text="下载视频", takefocus=False, command=self.finretvd)
            btn.place(x=580, y=250, width=140, height=40)
            return btn

    def __tk_text_link1(self, parent):
        text = Text(parent)
        text.place(x=410, y=550, width=80, height=20)
        self.vbar(text, 410, 550, 80, 20, parent)
        text.tag_configure('link1', foreground='blue', underline=True)
        text.insert(END, '欢迎关注', 'link1')
        text.tag_bind('link1', '<Button-1>', lambda event: webbrowser.open('https://space.bilibili.com/628363349'))
        text.config(state=DISABLED)
        return text



class Win(WinGUI):
    def __init__(self):
        super().__init__()
        self.__event_bind()

    def __event_bind(self):
        self.tk_text_txt1.delete("1.0", END)
        self.tk_text_txt1.config(state=DISABLED)


if __name__ == "__main__":
    win = Win()
    win.mainloop()