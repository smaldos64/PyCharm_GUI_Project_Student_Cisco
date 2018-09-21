from tkinter import *
from enum import Enum

class Buttons(Enum):
    LEFTBUTTON = 1
    RIGHTBUTTON = 2
# Erklæringen herover bliver ikke brugt. Men er medtaget for at vise, at man også i Python
# kan bruge enums. Enums er rigtig gode at bruge for at gøre ens kode mere fleksibel og meget
# mere læsbar.

def UpdateAllInFrame(numberOfTimesButtonPressedFunction, buttonWidget, entryWidget):
    numberOfTimesButtonPressedFunction[0] += 1
    entryWidget.delete(0, END)
    # Slet tekst i entry widget først.
    entryWidget.insert(0, "%d" % (numberOfTimesButtonPressedFunction[0]))
    # Og indsæt derefter ny tekst.

    buttonWidget["text"] = "Gange trykket på knappen her %d" % numberOfTimesButtonPressedFunction[0]


if __name__ == '__main__':
    numberOfTimesButtonLeftPressed = [0]
    numberOfTimesButtonRightPressed = [0]

    root = Tk()

    textOnLeftEntryVariable = StringVar()
    textOnLeftEntryVariable.set("Nu starter opdateringsmaskinen snart !!!")
    textOnRightEntryVariable = StringVar()

    root.option_add("Button.Background", "blue")
    root.option_add("Button.Foreground", "yellow")
    # Specifikation af default forgrund og baggrund farve for alle buttons.

    root.title("h5id080118 Cisco Switch SW")
    root.geometry("800x600")
    # Definer størrelse af window til 800x600 pixels.
    root.resizable(0, 0)
    # Tillad ikke at større1sen af vindue ændrer sig i hverken x - eller y retning.

    leftFrame = Frame(root, width=400, height=600, bg='black')
    leftFrame.pack(side=LEFT)
    leftFrame.pack_propagate(0)
    # Tillad ikke widgets indeni leftFrame at bestemme størrelsen af Framens bredde-højde

    rightFrame = Frame(root, width=400, height=600, bg='red')
    rightFrame.pack(side=RIGHT)
    rightFrame.pack_propagate(0)
    # Tillad ikke widgets indeni rightFrame at bestemme størrelsen af Framens bredde-højde

    buttonInLeftFrame = Button(master=leftFrame, text="Gange trykket på knappen her (0)", bg="blue", fg="yellow",
                               command=lambda:UpdateAllInFrame(numberOfTimesButtonLeftPressed,
                                                               buttonInLeftFrame,
                                                               textBoxInLeftFrame))
    buttonInLeftFrame.pack(side = LEFT)

    textBoxInLeftFrame = Entry(master = leftFrame)
    textBoxInLeftFrame.pack(side = TOP)
    textBoxInLeftFrame.place(x=10, y=10, width=300)

    buttonInRightFrame = Button(master=rightFrame, text="Gange trykket på knappen her (0) !!!", bg="yellow", fg="blue",
                                command=lambda:UpdateAllInFrame(numberOfTimesButtonRightPressed,
                                                                buttonInRightFrame,
                                                                textBoxInRightFrame))
    buttonInRightFrame.pack(side = RIGHT)

    textBoxInRightFrame = Entry(master = rightFrame)
    textBoxInRightFrame.pack(side = TOP)
    textBoxInRightFrame.place(x=10, y=10, width=300)

    root.mainloop()  #uendelig løkke.
