# Mad Lib
# Create a story based on user input

from tkinter import *

class Application(Frame):
    """ GUI application which counts button clicks. """
    def __init__(self, master):
        """ Initialize the frame. """
        super(Application, self).__init__(master)
        self.grid()
        self.bttn_clicks = 0    # the number of button clicks
        self.create_widget()

    def create_widget(self):
        """ Create button which displays number of clicks. """
        self.bttn = Button(self)
        self.bttn["text"]= "Total Clicks: 0"
        self.bttn["command"] = self.update_count
        self.bttn.grid()

    def update_count(self):
        """ Increase click count and display new total. """
        self.bttn_clicks += 1
        self.bttn["text"] = "Total Clicks: " + str(self.bttn_clicks)

# main
root = Tk()
root.title("Простейший Gui")
root.geometry("500x400")

# внутри окна создается рамка для размещения других элементов
app = Frame(root)
app.grid()

# создание метки внутри рамки
lbl = Label(app, text = "Вот она я!")
lbl.grid()
# create a button in the frame
bttn1 = Button(app, text = "Вот она я!")
bttn1.grid()

app = Application(root)

root.mainloop()

# input("\n Нажмите ... ")
