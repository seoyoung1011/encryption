from tkinter import *
import random, engine
from tkinter import messagebox


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
        Frame.__init__(self, master, width=400, height=300, bg="#FFCDD9")
        self.makePWbtn = PhotoImage(file="other/makePWbtn.png").subsample(2)
        self.lookupBtn = PhotoImage(file="other/makePWlookup.png").subsample(2)
        self.encryptionBtn = PhotoImage(file="other/encryptionBtn.png").subsample(2)
        self.decryptionBtn = PhotoImage(file="other/decryptionBtn.png").subsample(2)
        Button(self, text="", image=self.makePWbtn, command=lambda: master.switch_frame(makePW)).place(x="60", y="60")
        Button(self, text="", image=self.lookupBtn,
               command=lambda: master.switch_frame(lookup_PW)).place(x="220", y="60")
        Button(self, text="", image=self.encryptionBtn,
               command=lambda: master.switch_frame(Encryption)).place(x="60", y="145")
        Button(self, text="", image=self.decryptionBtn,
               command=lambda: master.switch_frame(Decryption)).place(x="220", y="145")
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
        Button(self, text="비밀번호 저장하기", command=self.save_window).place(x="270", y="250")
        self.propagate(0)

    def go(self):
        plain_text = Entry.get(self.PW)
        key = Entry.get(self.PWKEY)
        tmp = engine.encryption(plain_text, key)
        self.result.delete(0, "end")
        self.result.insert(0, tmp)

    def save_window(self):
        if Entry.get(self.PW).replace(" ", "") == "":
            messagebox.showwarning("!", "비밀번호를 입력하세요!")
        elif Entry.get(self.PWKEY).replace(" ", "") == "":
            messagebox.showwarning("!", "암호키를 입력하세요!")
        elif Entry.get(self.result).replace(" ", "") == "":
            messagebox.showwarning("!", "비밀번호를 생성하세요!")
        else:
            self.new_window = Toplevel(self)
            self.new_window.title("비밀번호 저장하기")
            self.new_window.geometry("200x80+500+300")
            Label(self.new_window, text="저장명", anchor="w").place(x="15", y="15")
            self.save_name = Entry(self.new_window, width=15)
            self.save_name.place(x="65", y="15")
            Button(self.new_window, text="저장하기", command=self.save).place(x="130", y="45")

    def save(self):
        if Entry.get(self.save_name).replace(" ", "") == "":
            messagebox.showwarning("!", "저장명을 입력하세요!")
        else:
            f = open('Other/save.txt', 'at')
            f.write(f'{Entry.get(self.save_name)}\t\t{Entry.get(self.result)}\t\t{Entry.get(self.PWKEY)}\n')
            f.close()
            self.new_window.destroy()


class lookup_PW(Frame):
    def __init__(self, master):
        Frame.__init__(self, master, width=400, height=300)
        self.back = PhotoImage(file="other/icon_back.png").subsample(25)
        Button(self, text=" ", image=self.back, command=lambda: master.switch_frame(main)).place(x="0", y="0")
        Label(self, text="저장명\t\t비밀번호\t\t암호키", anchor="w").place(x="30", y="30")
        list = open('Other/save.txt', 'rt').read().split('\n')
        tmp = Text(self, width="45", height="10")
        for x in list:
            tmp.insert(END, x + "\n")
        tmp.place(x="30", y="50")
        self.propagate(0)


class Encryption(Frame):
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
        tmp = engine.encryption(plainText, key)
        self.result.delete(0, "end")
        self.result.insert(0, tmp)
        self.useKey.config(text=key)

    def getKey(self):
        keys = open('other/key.txt', 'r').read().split('\n')
        key = random.choice(keys)

        return key


class Decryption(Frame):
    def __init__(self, master):
        Frame.__init__(self, master, width=400, height=300)
        self.back = PhotoImage(file="other/icon_back.png").subsample(25)
        Button(self, text=" ", image=self.back, command=lambda: master.switch_frame(main)).place(x="0", y="0")
        Label(self, text="암호문 입력").place(x="50", y="60")
        self.PW = Entry(self, width=30)
        self.PW.place(x="140", y="60")
        Label(self, text="암호키 입력").place(x="50", y="90")
        self.PWKEY = Entry(self, width=30)
        self.PWKEY.place(x="140", y="90")
        Button(self, text="복호화 하기", command=self.go).place(x="280", y="120")
        Label(self, text="결과").place(x="50", y="160")
        self.result = Entry(self, width=30)
        self.result.place(x="140", y="160")
        Label(self, text="결과는 정확하지 않으며 띄어쓰기가 없고 Z가 Q로 나옵니다.").place(x="40", y="200")
        self.propagate(0)

    def go(self):
        text = Entry.get(self.PW)
        key = Entry.get(self.PWKEY)
        tmp = engine.Decryption(text, key)
        self.result.delete(0, "end")
        self.result.insert(0, tmp)


if __name__ == "__main__":
    app = APP()
    app.mainloop()