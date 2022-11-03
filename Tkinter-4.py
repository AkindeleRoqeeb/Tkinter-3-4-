from tkinter import *

window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)

label = Label(text="This is old text")
label.config(text="This is new text", font= "bold")
label.pack()

# Button
def action():
    print("Do Something")

# Calls action

button = Button(text="Click Me And See", command=action)
button.pack()

# Entry
input = Entry(width=30)
# Add text
input.insert(END, string="Email Here........")
print(input.get())
input.pack()

# Text
text = Text(height=5, width=30)
text.focus()

text.insert(END, "Example of multi-line text entry...")

print(text.get("1.0", END))
text.pack()

def spinbox_used():
    # get current value
    print(spinbox_used())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

# Scale
def scale_used(value):
    print(value)

scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

def checkbutton_used():
    print(checked_state.get())

checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?",
                          variable=checked_state,
                          command=checkbutton_used)
checked_state.get()
checkbutton.pack()

def radio_used():
    print(radio_state.get())

radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1",
                           value=1,
                           variable=radio_state,
                           command=radio_used)

radiobutton2 = Radiobutton(text="Option2",
                           value=2,
                           variable=radio_state,
                           command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


def listbox_used(event):
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>",
             listbox_used)
listbox.pack()



window.mainloop()