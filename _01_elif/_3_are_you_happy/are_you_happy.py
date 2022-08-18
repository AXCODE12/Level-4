from tkinter import Tk, simpledialog, messagebox


if __name__ == '__main__':
    # TODO: Look at the AreYouHappy.png image
    #       Use pop-ups to recreate the chart using if and elif statements
    que = simpledialog.askstring('q','Are you happy?')
    if que == 'yes':
        messagebox.showinfo('i','Keep doing whatever you are doing')
    elif que == 'no':
        que2 = simpledialog.askstring('q','Do you want to be happy?')
        if que2 == 'yes':
            messagebox.showinfo('i','Change Something')
        elif que == 'no':
            messagebox.showinfo('i','Keep doing whatever you are doing')
    pass
