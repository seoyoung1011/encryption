from tkinter import *
import random, engine


class APP(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.frame = None
        self.title("집에 보내줘")
        self.iconbitmap('other/icon_key.ico')
        self.geometry("400x300+400+200")
        self.resizable(0, 0)
        self.switch_frame(main)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self.frame is not None:
            self.frame.destroy()
        self.frame = new_frame
        self.frame.pack()
        self.propagate(0)


class main(Frame):
    def __init__(self, master):
        Frame.__init__(self, master, width=400, height=300)
        Button(self, text="비밀번호 생성하기", font=('맑은 고딕', 15), command=lambda: master.switch_frame(makePW)).place(x="110", y="70")
        Button(self, text="암호화하기", font=('맑은 고딕', 15), command=lambda: master.switch_frame(encryption)).place(x="140", y="150")
        self.propagate(0)


class makePW(Frame):
    def __init__(self, master):
        Frame.__init__(self, master, width=400, height=300)
        self.back = PhotoImage(file="other/icon_back.png").subsample(25)
        Button(self, text=" ", image=self.back, command=lambda: master.switch_frame(main)).place(x="0", y="0")
        Label(self, text="비밀번호 입력").place(x="50", y="60")
        self.PW = Entry(self, width=30)
        self.PW.place(x="140", y="60")
        Label(self, text="암호키 입력").place(x="50", y="90")
        self.PWKEY = Entry(self, width=30)
        self.PWKEY.place(x="140", y="90")
        Button(self, text="암호화 하기", command=self.go).place(x="280", y="120")
        Label(self, text="결과").place(x="50", y="160")
        self.result = Entry(self, width=30)
        self.result.place(x="140", y="160")
        self.propagate(0)

    def go(self):
        plainText = Entry.get(self.PW)
        key = Entry.get(self.PWKEY)
        tmp = engine.쌍자치환(plainText, key)
        self.result.delete(0, "end")
        self.result.insert(0, tmp)


class encryption(Frame):
    def __init__(self, master):
        Frame.__init__(self, master, width=400, height=300)
        self.back = PhotoImage(file="other/icon_back.png").subsample(25)
        Button(self, text=" ", image=self.back, command=lambda: master.switch_frame(main)).place(x="0", y="0")
        Label(self, text="평문 입력").place(x="50", y="60")
        self.text = Entry(self, width=30)
        self.text.place(x="140", y="60")
        Button(self, text="암호화 하기", command=self.go).place(x="280", y="90")
        Label(self, text="결과").place(x="50", y="130")
        self.result = Entry(self, width=30)
        self.result.place(x="140", y="130")
        Label(self, text="사용된 암호키").place(x="50", y="160")
        self.useKey = Label(self, text="", width=30, anchor="w")
        self.useKey.place(x="140", y="160")
        self.propagate(0)

    def go(self):
        plainText = Entry.get(self.text)
        key = self.getKey()
        tmp = engine.쌍자치환(plainText, key)
        self.result.delete(0, "end")
        self.result.insert(0, tmp)
        self.useKey.config(text=key)

    def getKey(self):
        keys = open('other/key.txt', 'r').read().split('\n')
        key = random.choice(keys)

        return key


if __name__ == "__main__":
    app = APP()
    app.mainloop()