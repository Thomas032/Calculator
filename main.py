from tkinter import *
from playsound import playsound


class Window:
    def __init__(self, master, title):
        self.master = master
        self.title = title
        self.master.title(self.title)
        self.master.geometry("475x270+10+10")

        # Content of the window

        self.master.greetings = Label(self.master, text="Calculator", font="Times 20")
        self.master.entry_win = Entry(self.master, font="Helvetica 25 ", justify="center")
        self.master.equal = Button(self.master, text="=", font="System 15", width="30", bg="green",
                                   command=self.calculate)
        self.show_nums()
        self.show_signs()
        self.master.entry_win.grid(column=1, row=1, columnspan=3)
        self.master.greetings.grid(column=1, row=0, columnspan=3)
        self.master.equal.grid(column=2, row=5, columnspan=2)

        # Variables

        self.user_in = ""
        self.solved = False
    def update_entry(self):
        entry = self.master.entry_win
        entry.delete(0, END)
        entry.insert(0, self.user_in)
    def play(self, category):
        if category == "success":
            playsound()
    def show_nums(self):  # handle numbers
        row_num = 2
        col_num = 0
        paddings = {'padx': 10, 'pady': 10}
        for i in range(1, 11):

            def add_num(num=i):
                if num == 10:
                    num = str(0)
                else:
                    num = str(num)
                if self.user_in != "ERROR" :
                    self.user_in += num
                    self.update_entry()
                else:
                    self.user_in = ""
                    self.user_in += num
                self.update_entry()

            text = i
            if i == 4 or i == 7 or i == 10:
                row_num += 1
                col_num = 0
            if i == 10:
                col_num = 1
                text = 0
            else:
                col_num += 1

            globals()['self.number_button' + str(i)] = Button(self.master, text=text, width="15", command=add_num)
            globals()['self.number_button' + str(i)].grid(row=row_num, column=col_num, **paddings)

    def show_signs(self):
        signs = ['C', '+', '-', '*', '/']
        paddings = {'padx': 10, 'pady': 10}
        row_num = 1
        for i in range(len(signs)):
            def add_sign(x=signs[i]):
                if x == "C":
                    self.user_in = ""
                    self.update_entry()
                else:
                    self.user_in += x
                    self.update_entry()

            globals()["self.master.sign-" + signs[i]] = Button(self.master, text=signs[i], width="5", bg="black",
                                                               fg="white", font="System 10", command=add_sign)
            globals()["self.master.sign-" + signs[i]].grid(row=row_num + i, column=4, **paddings)

    def calculate(self):
        signs = ['C', '+', '-', '*', '/']
        numbers = []
        used_signs = []
        cur = 0
        entry = self.master.entry_win
        text = entry.get()
        if text != "" :
            if text[0] not in signs:
                splitted = list(text)
                for s in splitted:
                    while s not in signs:
                        try:
                            numbers[cur] += s
                            break

                        except:
                            numbers.append("")
                            continue

                    else:
                        used_signs.append(s)
                        cur += 1

                problem = ""
                for i in range(len(numbers)):
                    problem += numbers[i]
                    try:
                        problem += used_signs[i]

                    except:
                        pass

                self.user_in = str(eval(problem))

                self.update_entry()


        else:
            self.user_in = "ERROR"
            self.update_entry()


if __name__ == "__main__":
    root = Tk()
    app = Window(root, "Calculator")
    root.mainloop()
