import tkinter as tk
from tkinter import Menu

class Calculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("320x480")
        self.root.resizable(True, True)
        self.root.title("Calculator GUI")

        # create a menubar
        menubar = Menu(self.root)
        self.root.config(menu=menubar)

        # create the file_menu
        file_menu = Menu(
            menubar,
            tearoff=0
        )

        # add menu items to the File menu
        file_menu.add_checkbutton(label="Standard Calculator", onvalue=1, offvalue=1)
        file_menu.add_command(label='Scientific Calculator')
        file_menu.add_command(label='Other Features')
        file_menu.add_separator()
        file_menu.add_command(label='Close', command=self.root.destroy)

        # create the file_menu
        about_menu = Menu(
            menubar,
            tearoff=0
        )

        # add the File menu to the menubar
        menubar.add_cascade(
            label="File",
            menu=file_menu
        )


        self.total_expression = ""
        self.current_expression = ""
        self.entry_frame = self.create_entry_frame()

        self.total_label, self.label = self.create_entry_labels()

        self.numbers = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), '.': (4, 1)
        }
        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "\u2212", "+": "+"}
        self.buttons_frame = self.create_buttons_frame()

        self.buttons_frame.rowconfigure(0, weight=1)
        for x in range(1, 5):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)
        self.create_number_buttons()
        self.create_operator_buttons()
        self.create_special_buttons()

    def create_special_buttons(self):
        self.create_clear_button()
        self.create_equals_button()
        self.create_delete_button()
        self.create_neg_button()

    def create_entry_labels(self):
        total_label = tk.Label(self.entry_frame, text=self.total_expression, anchor=tk.E, bg="#2E3649",
                               fg="#77F8D9", padx=24, font=("Rubik", 20))
        total_label.pack(expand=True, fill='both')

        label = tk.Label(self.entry_frame, text=self.current_expression, anchor=tk.E, bg="#2E3649",
                         fg="#77F8D9", padx=24, font=("Rubik", 40))
        label.pack(expand=True, fill='both')

        return total_label, label

    def create_entry_frame(self):
        frame = tk.Frame(self.root, height=221, bg="#636e72")
        frame.pack(expand=True, fill="both")
        return frame

    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.answer_label()

    def create_number_buttons(self):
        for number, grid_value in self.numbers.items():
            button = tk.Button(self.buttons_frame, text=str(number), bg="#374057", fg="#8A97BB", font=("Rubik", 22),
                               borderwidth=0, command=lambda x=number: self.add_to_expression(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def append_operator(self, operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.answer_total_label()
        self.answer_label()

    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg="#333B4D", fg="#8A97BB", font=("Rubik", 20),
                               borderwidth=0, command=lambda x=operator: self.append_operator(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1

    def clear(self):
        self.current_expression = ""
        self.total_expression = ""
        self.answer_label()
        self.answer_total_label()

    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text="C", bg="#B14562", fg="#FD8DA8", font=("Rubik", 20),
                           borderwidth=0, command=self.clear)
        button.grid(row=0, column=1, sticky=tk.NSEW)

    def delete(self):
        self.current_expression = "" + self.current_expression[0:-1]
        self.answer_label()

    def create_delete_button(self):
        button = tk.Button(self.buttons_frame, text="\u2B60", bg="#333B4D", fg="#8A97BB", font=("Rubik", 20),
                           borderwidth=0, command=self.delete)
        button.grid(row=0, column=2, sticky=tk.NSEW)

    def neg(self):
        self.current_expression = "-(" + self.current_expression + ")"
        self.total_expression = ""
        self.answer_label()

    def create_neg_button(self):
        button = tk.Button(self.buttons_frame, text="\u207A" + "\u2215" + "\u208B", bg="#333B4D", fg="#8A97BB", font=("Rubik", 20),
                           borderwidth=0, command=self.neg)
        button.grid(row=0, column=3, sticky=tk.NSEW)

    def evaluate(self):
        self.total_expression += self.current_expression
        self.answer_total_label()
        try:
            self.current_expression = str(eval(self.total_expression))

            self.total_expression = ""
        except Exception as e:
            self.current_expression = "Error"
        finally:
            self.answer_label()

    def create_equals_button(self):
        button = tk.Button(self.buttons_frame, text="=", bg='#77F8D9', fg="#374057", font=("Rubik", 30),
                           borderwidth=0, command=self.evaluate)
        button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)

    def create_buttons_frame(self):
        frame = tk.Frame(self.root)
        frame.pack(expand=True, fill="both")
        return frame

    def answer_total_label(self):
        expression = self.total_expression
        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f' {symbol} ')
        self.total_label.config(text=expression)

    def answer_label(self):
        self.label.config(text=self.current_expression[:11])

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = Calculator()
    app.run()
    