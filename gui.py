from tkinter import *
from tkinter.ttk import Progressbar


# Methods
def read_file():
    file = open("./files/example.txt")
    # create list of lines
    lines = file.readlines()
    # split every line in columns
    lines = [l.split('-') for l in lines]
    return lines


def write_new_file(new_path):
    with open(new_path, "w") as f:
        for line in new_file:
            f.writelines(str(line[0]))
    f.close()


def do_something():
    if current_line < len(all_lines):
        if "==" in all_lines[current_line][0] or "--" in all_lines[current_line][0]:
            next_line_no_annotation()
        elif "User" in all_lines[current_line][0]:
            userlbl = Label(window, text="___User:___", font=("Arial Bold", 13))
            new_file.append(all_lines[current_line])
            userlbl.grid(row=0, column=2)
            next_line_no_annotation()
        elif "Storytel" in all_lines[current_line][0]:
            userlbl = Label(window, text="Storyteller:", font=("Arial Bold", 13))
            userlbl.grid(row=0, column=2)
            new_file.append(all_lines[current_line])
            next_line_no_annotation()
        elif "Chat:" in all_lines[current_line][0]:
            chatlbl = Label(window, text=all_lines[current_line][0], font=("Arial Bold", 13), fg="blue")
            chatlbl.grid(row=1, column=0)
            new_file.append(all_lines[current_line])
            next_line_no_annotation()
        else:
            text = StringVar(value=all_lines[current_line][0])
            entry = Entry(window, textvariable=text, font=("Arial Bold", 13), state='readonly')
            scroll = Scrollbar(window, orient='horizontal', command=entry.xview)
            entry.config(xscrollcommand=scroll.set)
            entry.grid(row=1, column=1, columnspan=5, rowspan=2, sticky=W + E + N + S, padx=5, pady=5)
            scroll.grid(row=2, column=1, columnspan=5, sticky=W + E + N + S)
            new_file.append(all_lines[current_line])
    else:
        lbl0 = Label(window, text="Thanks! You can now close the window", font=("Arial Bold", 15), fg="red")
        lbl0.grid(row=1, column=1, columnspan=5, sticky=W + E + N + S, padx=5, pady=5)
        write_new_file("annotated_example.txt")


def create_buttons():
    btn1 = Button(window, text="Next", bg="orange", command=next_line_no_annotation)  # fg="red")
    btn1.grid(column=0, row=3)

    lbl2 = Label(window, text="Domain specific Intents: ", font=("Arial Bold", 12), fg="red")
    lbl2.grid(column=0, row=5)

    column = 0
    row = 6
    for label in domain_specific_intents:
        btn = Button(window, text=label, bg="orange", command=lambda label=label: next_line(label))  # fg="red")
        btn.grid(column=column, row=row, sticky="ew")  # sticky="ew" to have same size buttons
        if column < 5:
            column += 1
        else:
            column = 0
            row += 1

    # buttons for generic intents
    lbl3 = Label(window, text="Generic Intents: ", font=("Arial Bold", 12), fg="red")
    lbl3.grid(column=0, row=(row + 2))

    column = 0
    row = row + 3
    for label in generic_intents:
        btn = Button(window, text=label, bg="orange", command=lambda label=label: next_line(label))  # fg="red")
        btn.grid(column=column, row=row, sticky="ew")
        if column < 5:
            column += 1
        else:
            column = 0
            row += 1

    # buttons for engagement intents
    lbl4 = Label(window, text="Engagement intents: ", font=("Arial Bold", 12), fg="red")
    lbl4.grid(column=0, row=(row + 2))

    column = 0
    row = row + 3
    for label in engagement_intents:
        btn = Button(window, text=label, bg="orange", command=lambda label=label: next_line(label))  # fg="red")
        btn.grid(column=column, row=row, sticky="ew")
        if column < 5:
            column += 1
        else:
            column = 0
            row += 1


def start():
    # creates and display all the buttons needed to annotate
    create_buttons()
    # based on the first line of the txt, decide what to do
    do_something()
    # destroy 'start' button
    btn10.destroy()


def next_line_no_annotation():
    global current_line
    # if there aren't new lines, print message, else go to the next line and decide what to do
    if current_line == len(all_lines):
        print("You can now close the window")
    else:
        current_line += 1
        do_something()


def next_line(annotation):
    global current_line
    # if there aren't new lines, print message, else annotate the current line
    # and go to the next line to decide what to do
    if current_line == len(all_lines):
        print("You can now close the window")
    else:
        all_lines[current_line][0] = all_lines[current_line][0][:-1] + " (" + annotation + ")\n"
        current_line += 1
        do_something()


all_lines = read_file()
current_line = 0
new_file = []


# Create tkinder gui as window
window = Tk()
textWidget = Text(window)
# Window settings
window.title("Annotation tool for conversations")
window.geometry('1000x500')

userlbl = Label(window, text="----", font=("Arial Bold", 13))
userlbl.grid(row=1, column=0)


# Window content
lbl = Label(window, text="Your progress:", font=("Arial Bold", 13))
lbl.grid(column=0, row=0)

lbl1 = Label(window, text="", font=("Arial Bold", 15))
lbl1.grid(column=2, row=3)

btn10 = Button(window, text="Start", bg="orange", command=start)  # fg="red")
btn10.grid(column=0, row=2)


# lists of intents
domain_specific_intents = ["Increment", "RequestIncrement", "YNQ", "WHQ", "YNResponse", "WHResponse", "IDKResponse",
                           "ExclaimNeg",
                           "ExclaimPos", "Deflection", "Backtrace", "Clarification Request", "Clarification Response",
                           "Correction",
                           "StoryStartSignal", "StoryEndSignal", "AskIfEnded", "AskForStory", "StoryTransition",
                           "Comment", ]

generic_intents = ["Acceptance", "Rejection", "Thanking", "Greet", "ClosingPhrase"]

engagement_intents = ["FeedbackPrompt", "InclusionPrompt"]

# buttons for domain specific intents


window.mainloop()
