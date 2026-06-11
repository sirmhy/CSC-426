# Author: Lawrence Emmanuel
# CSC426  Assignment

import tkinter as tk


def button_click(item):
    current = display_var.get()
    display_var.set(current + str(item))

def button_clear():
    display_var.set("")

def button_equal():
    try:
        expression = display_var.get()
        # Convert custom symbols to Python operators
        expression = expression.replace('^', '**').replace('\\', '//')
        
        # Evaluate the math
        result = str(eval(expression))
        display_var.set(result)
    except Exception:
        display_var.set("Error")

# Main Window setup
root = tk.Tk()
root.title("CSC426 Calculator")
# Removed the fixed geometry so the window auto-sizes perfectly
root.configure(bg="#002135") 
root.resizable(0, 0)

display_var = tk.StringVar()

# Display Screen (Updated for dark mode)
display = tk.Entry(root, textvariable=display_var, font=('Arial', 24, 'bold'), 
                   bg="#002135", fg="white", bd=0, justify="right")
display.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=20, pady=10)

# Button Layout Matrix
buttons = [
    ('C', 1, 0), ('^', 1, 1), ('%', 1, 2), ('/', 1, 3),
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('*', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
    ('0', 5, 0), ('.', 5, 1), ('\\', 5, 2), ('=', 5, 3)
]


for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, font=('Arial', 14, 'bold'), bg="#4caf50", fg="white", height=2, width=5, command=button_equal)
    elif text == 'C':
        btn = tk.Button(root, text=text, font=('Arial', 14, 'bold'), bg="#f44336", fg="white", height=2, width=5, command=button_clear)
    else:
        # Standard buttons get a charcoal gray background
        btn = tk.Button(root, text=text, font=('Arial', 14, 'bold'), bg="#1e293b", fg="white", height=2, width=5, command=lambda t=text: button_click(t))
    
  
    btn.grid(row=row, column=col, padx=3, pady=3)

root.mainloop()