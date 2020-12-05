import tkinter as tk

window = tk.Tk()
window.geometry("306x245")
window.minsize(306, 245)
window.title('calculator')
window.configure(bg='gray20')

expression = ''
input_text = tk.StringVar()


def btn_click(item):
    """function continuously updates the input field whenever you enters a number"""
    global expression
    expression = expression + str(item)
    input_text.set(expression)


def btn_clear():
    """function clears the input field"""
    global expression
    expression = ""
    input_text.set("")


def btn_equal():
    """calculates the expression present in input field"""
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression = ""


# frame for the result and input field
input_frame = tk.Frame(window, bd=0, highlightbackground="gray15")
input_frame.pack(side='top', fill='both', padx=5, pady=(10, 3))

input_field = tk.Entry(input_frame, font=('monospace', 20, 'bold'),
                       textvariable=input_text, bg='gray15', fg='white', bd=0, justify='center')
input_field.pack(fill='both')

# buttons frame
btns_frame = tk.Frame(window, bg="gray17", bd=0)
btns_frame.pack(padx=3, pady=5)

# first row
btn_7 = tk.Button(btns_frame, text="7", fg="white", bd=0, bg="gray20", font=('monospace, 20'),
                  command=lambda: btn_click('7')).grid(row=0, column=0, padx=1, pady=1)
btn_8 = tk.Button(btns_frame, text="8", fg="white", bd=0, bg="gray20", font=('monospace, 20'),
                  command=lambda: btn_click('8')).grid(row=0, column=1, padx=1, pady=1)
btn_9 = tk.Button(btns_frame, text="9", fg="white", bd=0, bg="gray20", font=('monospace, 20'),
                  command=lambda: btn_click('9')).grid(row=0, column=2, padx=1, pady=1)
divide = tk.Button(btns_frame, text="➗", fg="white", bd=0, bg="gray20", font=('monospace, 20'),
                   command=lambda: btn_click('/')).grid(row=0, column=3, sticky='EWNS', padx=(10, 1), pady=1)
clear = tk.Button(btns_frame, text="clear", fg="white", bd=0, bg="gray20", font=('monospace, 20'),
                  command=lambda: btn_clear()).grid(row=0, column=4, columnspan=2, sticky='EWNS', padx=1, pady=1)


# second row
btn_4 = tk.Button(btns_frame, text="4", fg="white", bd=0, bg="gray20", font=('monospace, 20'),
                  command=lambda: btn_click('4')).grid(row=1, column=0, padx=1, pady=1)
btn_5 = tk.Button(btns_frame, text="5", fg="white", bd=0, bg="gray20", font=('monospace, 20'),
                  command=lambda: btn_click('5')).grid(row=1, column=1, padx=1, pady=1)
btn_6 = tk.Button(btns_frame, text="6", fg="white", bd=0, bg="gray20", font=('monospace, 20'),
                  command=lambda: btn_click('6')).grid(row=1, column=2, padx=1, pady=1)
multiply = tk.Button(btns_frame, text="✖", fg="white", bd=0, bg="gray20", font=('monospace, 20'),
                     command=lambda: btn_click('*')).grid(row=1, column=3, sticky='EWNS', padx=(10, 1), pady=1)
square = tk.Button(btns_frame, text="𝑥²", fg="white", bd=0, bg="gray20", font=('monospace, 20'),
                   command=lambda: btn_click('**2')).grid(row=1, column=4, sticky='EWNS', padx=1, pady=1)
cube = tk.Button(btns_frame, text="𝑥³", fg="white", bd=0, bg="gray20", font=('monospace, 20'),
                 command=lambda: btn_click('**3')).grid(row=1, column=5, sticky='EWNS', padx=1, pady=1)

# third row
btn_1 = tk.Button(btns_frame, text="1", fg="white", bd=0, bg="gray20", font=('monospace, 20'),
                  command=lambda: btn_click('1')).grid(row=2, column=0, padx=1, pady=1)
btn_2 = tk.Button(btns_frame, text="2", fg="white", bd=0, bg="gray20", font=('monospace, 20'),
                  command=lambda: btn_click('2')).grid(row=2, column=1, padx=1, pady=1)
btn_3 = tk.Button(btns_frame, text="3", fg="white", bd=0, bg="gray20", font=('monospace, 20'),
                  command=lambda: btn_click('3')).grid(row=2, column=2, padx=1, pady=1)
minus = tk.Button(btns_frame, text="‒", fg="white", bd=0, bg="gray20", font=('monospace, 20'),
                  command=lambda: btn_click('-')).grid(row=2, column=3, sticky='EWNS', padx=(10, 1), pady=1)
open_brkt = tk.Button(btns_frame, text="(", fg="white", bd=0, bg="gray20", font=('monospace, 20'),
                      command=lambda: btn_click('(')).grid(row=2, column=4, sticky='EWNS', padx=1, pady=1)
close_brkt = tk.Button(btns_frame, text=")", fg="white", bd=0, bg="gray20", font=('monospace, 20'),
                       command=lambda: btn_click(')')).grid(row=2, column=5, sticky='EWNS', padx=1, pady=1)

# forth row
btn_0 = tk.Button(btns_frame, text="0", fg="white", bd=0, bg="gray20", font=('monospace, 20'),
                  command=lambda: btn_click('0')).grid(row=3, column=0, sticky='EWNS', padx=1, pady=1)
dot = tk.Button(btns_frame, text="･", fg="white", bd=0, bg="gray20", font=('monospace, 20'),
                command=lambda: btn_click('.')).grid(row=3, column=1, sticky='EWNS', padx=1, pady=1,)
mod = tk.Button(btns_frame, text="ᶬ", fg="white", bd=0, bg="gray20", font=('monospace, bold', 20),
                command=lambda: btn_click('%')).grid(row=3, column=2, sticky='EWNS', padx=1, pady=1)
add = tk.Button(btns_frame, text="✚", fg="white", bd=0, bg="gray20", font=('monospace, 20'),
                command=lambda: btn_click('+')).grid(row=3, column=3, sticky='EWNS', padx=(10, 1), pady=1)
equal = tk.Button(btns_frame, text="＝", fg="white", bd=0, bg="gray20", font=('monospace, 20'),
                  command=lambda: btn_equal()).grid(row=3, column=4, columnspan=2, sticky='EWNS', padx=1, pady=1)
window.mainloop()
