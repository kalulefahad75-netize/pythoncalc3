from tkinter import *

class calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("615x690+400+100")
        self.root.configure(bg='cadet blue')

        self.MainFrame = Frame(self.root, bd=18, width=600, height=670, relief=RIDGE, bg='powder blue')
        self.MainFrame.grid()

        self.widgetFrame = Frame(self.MainFrame, bd=18, width=590, height=660, relief=RIDGE, bg='cadet blue')
        self.widgetFrame.grid()

        self.LblDisplay = Label(self.widgetFrame, width=30, height=2, bg="white", font=('arial', 20, "bold"), anchor='e')
        self.LblDisplay.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        self.input_button = ""
        
        buttons = [
            ("←", 1, 0), ("CE", 1, 1), ("C", 1, 2), ("±", 1, 3),
            ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("+", 2, 3),
            ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
            ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("*", 4, 3),
            ("0", 5, 0), (".", 5, 1), ("/", 5, 2), ("=", 5, 3)
        ]

        for (text, r, c) in buttons:
            self.create_button(text, r, c)

    def create_button(self, text, row, column):
        btnwidge = Button(self.widgetFrame, text=text, width=5, height=2, bd=4, bg="powder blue", font=('arial', 20, "bold"),
                          command=lambda: self.button_click(text))
        btnwidge.grid(row=row, column=column, padx=5, pady=5)

    def button_click(self, text):
        if text == "←": 
            self.input_button = self.input_button[:-1] 
        elif text == "CE" or text == "C":
            self.input_button = ""
        elif text == "=":
            try:
                
                if self.input_button:
                    self.input_button = str(eval(self.input_button))
            except:
                self.input_button = "Error"
        elif text == "±":
            try:
                if self.input_button:
                    self.input_button = str(float(self.input_button) * -1)
            except:
                self.input_button = "Error"
        else:
            self.input_button += text
        
        self.LblDisplay.config(text=self.input_button)

if __name__ == "__main__":
    root = Tk()
    App = calculator(root)
    root.mainloop()