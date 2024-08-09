from tkinter import Tk, Entry, Button, StringVar

class Calculator:
    def __init__(self, master):
        master.title("Calculator")
        master.geometry('357x420+0+0')  # Use 'x' instead of '*' for size
        master.config(bg='gray')
        master.resizable(False, False)

        self.equation = StringVar()
        self.entry_value = ''

        # Entry widget
        Entry(master, width=17, bg='#fff', font=('Arial Bold', 28), textvariable=self.equation).place(x=0, y=0)

        # Button configuration
        button_texts = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        button_positions = [
            (0, 50), (90, 50), (180, 50), (270, 50),
            (0, 130), (90, 130), (180, 130), (270, 130),
            (0, 210), (90, 210), (180, 210), (270, 210),
            (0, 290), (90, 290), (180, 290), (270, 290)
        ]

        for (text, (x, y)) in zip(button_texts, button_positions):
            Button(master, text=text, width=5, height=2, command=lambda t=text: self.on_button_click(t)).place(x=x, y=y)

        # Clear button
        Button(master, text='C', width=5, height=2, command=self.clear).place(x=0, y=370)
        
    def on_button_click(self, value):
        if value == '=':
            self.solve()
        else:
            self.entry_value += str(value)
            self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def solve(self):
        try:
            result = eval(self.entry_value)
            self.equation.set(result)
            self.entry_value = str(result)
        except Exception as e:
            self.equation.set("Error")
            self.entry_value = ''

root = Tk()
calc = Calculator(root)
root.mainloop()
