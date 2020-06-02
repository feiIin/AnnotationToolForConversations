from tkinter import *
from tkinter.filedialog import askopenfile
from tkinter.ttk import Progressbar

# Methods
def read_file():
    file_ = open("./files/cleaned_chats.txt")
    # create list of lines
    lines = file_.read().split('\n')
    # split every line in columns
    lines = [l.split(',') for l in lines]
    return lines


def next_line():
    global current_line # inform function to use global variable instead local because we will assign new value
    current_line += 1
    if current_line < len(all_lines):
        lbl0 = Label(window, text=all_lines[current_line][0], font=("Arial Bold", 13))
        lbl0.grid(row=1, column=1, columnspan=4, sticky=W + E + N + S, padx=5, pady=5)
    else:
        lbl0 = Label(window, text="The end", font=("Arial Bold", 13))
        lbl0.grid(row=1, column=1, columnspan=4, sticky=W + E + N + S, padx=5, pady=5)


all_lines = read_file()
current_line = 0

# Create tkinder gui as window
window = Tk()
textWidget = Text(window)
# Window settings
window.title("Annotation tool for conversations")
window.geometry('1000x500')


# Commands
def clicked():
    lbl1.configure(text="Button was clicked!")
    # lbl1.grid(column=2, row=2)


# Window content
lbl = Label(window, text="Your progress:", font=("Arial Bold", 13))
lbl.grid(column=0, row=0)

bar = Progressbar(window, length=200)
bar.grid(column=1, row=0)
bar['value'] = 70

lbl1 = Label(window, text="", font=("Arial Bold", 15))
lbl1.grid(column=2, row=3)

btn1 = Button(window, text="Next", bg="orange", command=next_line)  # fg="red")
btn1.grid(column=0, row=2)


# lists of intents
domain_specific_intents = ["Increment", "RequestIncrement", "YNQ", "WHQ", "YNResponse", "WHResponse", "IDKResponse",
                           "ExclaimNeg",
                           "ExclaimNPos", "Deflection", "Backtrace", "Clarification Request", "Clarification Response",
                           "Correction",
                           "StoryStartSignal", "StoryEndSignal", "AskIfEnded", "AskForStory", "StoryTransition",
                           "Comment", ]

generic_intents = ["Acceptance", "Rejection", "Thanking", "Greet", "ClosingPhrase"]

engagement_intents = ["FeedbackPrompt", "InclusionPrompt"]

# buttons for domain specific intents
lbl2 = Label(window, text="Domain specific Intents: ", font=("Arial Bold", 12), fg="red")
lbl2.grid(column=0, row=5)

column = 0
row = 6
for label in domain_specific_intents:
    btn = Button(window, text=label, bg="orange")  # fg="red")
    btn.grid(column=column, row=row, sticky="ew") # sticky="ew" to have same size buttons
    if column < 5:
        column += 1
    else:
        column = 0
        row += 1


# buttons for generic intents
lbl3 = Label(window, text="Generic Intents: ", font=("Arial Bold", 12), fg="red")
lbl3.grid(column=0, row=(row+2))

column = 0
row = row + 3
for label in generic_intents:
    btn = Button(window, text=label, bg="orange")  # fg="red")
    btn.grid(column=column, row=row, sticky="ew")
    if column < 5:
        column += 1
    else:
        column = 0
        row += 1

# buttons for engagement intents
lbl4 = Label(window, text="Engagement intents: ", font=("Arial Bold", 12), fg="red")
lbl4.grid(column=0, row=(row+2))

column = 0
row = row + 3
for label in engagement_intents:
    btn = Button(window, text=label, bg="orange")  # fg="red")
    btn.grid(column=column, row=row, sticky="ew")
    if column < 5:
        column += 1
    else:
        column = 0
        row += 1


## read file
# with open('./files/cleaned_chats.txt', 'r') as f:
#     lines = f.readlines()
#     new_file = []
#     for line in lines:
#         # Entry box
#         lbl0 = Label(window, text=line, font=("Arial Bold", 13))
#         lbl0.grid(row=1, column=1, columnspan=4, sticky=W + E + N + S, padx=5, pady=5)
#         btn1.wait_variable()


window.mainloop()
