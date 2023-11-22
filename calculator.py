from tkinter import *
import math

def click(value):
    ex = field.get()
    result = ' '

    try:

        if value == 'DEL':
            ex = ex[0:len(ex)-1]        #using slicing to delete last character
            field.delete(0,END)
            field.insert(0,ex)
            return

        elif value == 'CE':       #delete everything
            field.delete(0,END)

        elif value == '√':
            result = math.sqrt(eval(ex))    #evaluate int float everything

        elif value == 'π':
            result = math.pi

        elif value == 'cosθ':
            result = math.cos(math.radians(eval(ex)))
            result = round(result,2)

        elif value == 'tanθ':
            result = math.tan(math.radians(eval(ex)))
            result = round(result, 2)

        elif value == 'sinθ':
            result = math.sin(math.radians(eval(ex)))

        elif value == 'Sort':
            result = [int(x) for x in str(eval(ex))]
            result.sort()

        elif value == 'sin-1':
            result = math.asin(eval(ex))
            result = math.degrees(result)

        elif value == 'cos-1':
            result = math.acos(eval(ex))
            result = math.degrees(result)

        elif value == 'tan-1':
            result = math.atan(eval(ex))
            result = math.degrees(result)

        elif value == chr(8731):
            result = eval(ex) ** (1/3)

        elif value == 'x\u02b8':
            field.insert(END, '**')
            return

        elif value == 'x\u00B3':
            result = eval(ex) ** 3

        elif value == 'x\u00B2':
            result = eval(ex) ** 2

        elif value == 'ln':
            result = math.log2(eval(ex))
            result = round(result, 2)

        elif value == 'Deg':
            result = math.degrees(eval(ex))

        elif value == "Rad":
            result = math.radians(eval(ex))

        elif value == '%':
            result = eval(ex)/100

        elif value == 'Exp':
            result = math.e

        elif value == 'log₁₀':
            result = math.log10(eval(ex))

        elif value == 'x!':
            result = math.factorial(eval(ex))

        elif value == chr(247):
            field.insert(END, "/")
            return

        elif value == '=':
            result = eval(ex)

        elif value == 'D-Bin':
            result = bin(eval(ex)).replace("0b","")

        elif value == 'D-Hex':
            result = hex(eval(ex)).replace("0x","")

        elif value == 'D-Oct':
            result = oct(eval(ex)).replace("0o","")

        elif value == 'B-Dec':
            result = int(ex, 2)

        elif value == 'B-Hex':
            decimal = int(ex, 2)
            result = hex(decimal).replace("0x","")

        elif value == 'B-Oct':
            decimal = int(ex, 2)
            result = oct(decimal).replace("0o", "")

        elif value == 'H-Dec':
            result = int(ex, 16)

        elif value == 'H-Bin':
            decimal = int(ex, 16)
            result = bin(decimal).replace("0b","")

        elif value == 'H-Oct':
            decimal = int(ex, 16)
            result = oct(decimal).replace("0o", "")

        elif value == 'O-Dec':
            result = int(ex, 8)

        elif value == 'O-Bin':
            decimal = int(ex, 8)
            result = bin(decimal).replace("0b","")

        elif value == 'O-Hex':
            decimal = int(ex, 8)
            result = hex(decimal).replace("0x", "")

        elif value == 'x-1':
            result = 1/eval(ex)

        elif value == 'Abs':
            result = math.fabs(eval(ex))

        else:
            field.insert(END, value)
            return

        field.delete(0,END)
        field.insert(0,result)

    except SyntaxError:
        pass

root = Tk()     #Tk class object is root
root.title('Arbitrary Precision Calculator')
root.config(bg='white')
root.geometry('420x713+700+200')

field=Entry(root, font=('arial',18,'bold'), bg='black', fg='white', bd=15, relief=SUNKEN, width=25)        #fg means font color & Entry class's object is field
field.grid(row=0,column=0,columnspan=6)

button_text_list = ["D-Bin", "D-Hex", "D-Oct", "sinθ", "cosθ", "tanθ",
                    "B-Dec", "B-Hex", "B-Oct", "sin-1", "cos-1", "tan-1",
                    "H-Dec", "H-Bin", "H-Oct", "ln", "Deg", "Rad",
                    "O-Dec", "O-Bin", "O-Hex", "Sort", "(", ")",
                    "A", "B", "C", "%", "DEL", "CE",
                    "D", "E", "F",chr(247), "x-1", "x!",
                    "7", "8", "9", "*", "x\u02b8", "log₁₀",
                    "4", "5", "6", "+", "x\u00B2", "√",
                    "1", "2", "3", "-", "x\u00B3", chr(8731),
                    "0", ".", "π", "=", "Exp", "Abs"]

row_no = 1
column_no = 0
for i in button_text_list:
    button = Button(root, width=5, height=2, bd=2, relief=SUNKEN, text=i, bg='black', fg='white',
                    font=('arial', 14, 'bold'), activebackground='white',
                    command=lambda button=i:click(button))       #Button class object is button

    button.grid(row=row_no,column=column_no,pady=2)
    column_no = column_no + 1
    if column_no > 5:
        row_no = row_no + 1
        column_no = 0

root.mainloop()