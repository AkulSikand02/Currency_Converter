from tkinter import * 
from tkinter import ttk
from tkinter.messagebox import OK
from typing import Dict

convert = Tk()
convert.geometry("600x400")
convert.title("Currency Conveter")

OPTIONS = {
    " Australian Doller ":56.43,
    " US Doller ":73.23,
    " Canadian Doller ":60.27,
    " UAE Dinar ":19.94,
    " BitCoin ":2607667.34,
    " Euro ":88.68,
    " Chinese Yen ":11.44,
    " Japanese Yen ":0.67,
    " Thai Baht ":2.36,
    " South African Rand ":5.34,
            }

def ok():
    price = rupees.get()
    answer = variable.get()
    DICT = OPTIONS.get(answer,None)
    converted = float(price)/float(DICT)
    result.delete(1.0,END)
    result.insert(INSERT,converted)    

appName = Label(convert, text="CURRENCY", font=("Areal",25,"bold",), fg="black")
appName.grid(row=0, column=0)

appName = Label(convert, text="",)
appName.grid(row=0, column=1)

appName = Label(convert, text="CONVETER", font=("Areal",25,"bold",), fg="black")
appName.grid(row=0, column=1)


indian = Label(convert, text="Indian Rupees: ", font=("Areal",25,"bold"), fg="black")
indian.grid(row=1, column=0)

rupees = Entry(convert, font="calibir")
rupees.grid(row=1, column=1)

choice = Label(convert, text="Choose Country: ", font=("Areal",20,"bold"), fg="black")
choice.grid(row=3, column=0)

variable = StringVar(convert)
variable.set(None)
option = OptionMenu(convert, variable, *OPTIONS)
option.grid(row=3, column=1, sticky="ew")

result = Text(convert, height=1, width=11 , font=("Areal",25))
result.grid(row=2, column=1)

button = Button(convert, text="Conveter", fg="black", font=("caliber",20), bg="powder blue", command=ok)
button.grid(row=3, column=2)



mainloop()
