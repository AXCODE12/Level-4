from tkinter import Tk, simpledialog, messagebox

# TODO Tell the user a story, but give them options so they can decide the
#  path of the plot.
#  Use pop-ups, if statements, and your imagination to make an interesting
#  story
win = Tk()
win.withdraw()


que = simpledialog.askstring('q', 'Does Bob go to the forest?')
if que == 'yes':
    messagebox.showinfo('i', 'He gets killed by a wolf')
elif que == 'no':
    que2 = simpledialog.askstring('q', 'Does he go home?')
    if que2 == 'yes':
        messagebox.showinfo('i', 'He sees his house is on fire')
    elif que == 'no':
        messagebox.showinfo('i', 'He dies')