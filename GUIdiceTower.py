from tkinter import *
from PIL import ImageTk, Image
import os

#changes directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#creat root window
root = Tk()

#photo library
diceimgd4 = ImageTk.PhotoImage(Image.open("D4.png"))
diceimgd6 = ImageTk.PhotoImage(Image.open("D6.png"))
diceimgd8 = ImageTk.PhotoImage(Image.open("D8.png"))
diceimgd10 = ImageTk.PhotoImage(Image.open("D10.png"))
diceimgd12 = ImageTk.PhotoImage(Image.open("D12.png"))
diceimgd20 = ImageTk.PhotoImage(Image.open("D20.png"))

#intergers
dicetype = ["D4","D6","D8","D10","D12"]
dicetypeselected = 0
Attackmod = 0
Damagemod = 0

#set up root window
root.title("Auto Dice Tower")
root.geometry('350x200')

#all widgers
Dice_Type_label = Label(root,text="Dice Type",font=("Arial",20))
Dice_Type_label.grid(column=2,row=0)
dicetype_label = Label(root, text=dicetype[dicetypeselected],font=("Arial",25))
dicetype_label.grid(column=2,row=1)
diceImage_label = Label(root,image = diceimgd4)
diceImage_label.grid(column=7,row=1)



atc_label = Label(root, text=Attackmod,font=("Arial",25))
atc_label.grid(column=2,row=3)

dam_label = Label(root, text=Damagemod,font=("Arial",25))
dam_label.grid(column=2,row=5)

#Change dice image
dice_image_dic = {"D4":diceimgd4,"D6": diceimgd6,"D8": diceimgd8,"D10": diceimgd10,"D12": diceimgd12}

def Change_diceimg(newDice):
    # Check if newDice is in the dictionary
    if newDice in dice_image_dic:
        # Configure diceImage_label with the corresponding image
        diceImage_label.configure(image=dice_image_dic[newDice])
    else:
        print("Error: Invalid dice type")
        diceImage_label.configure(image=diceimgd4)  # Fallback to D4 image
            #Add an error image?


#button click function
def dice_inc():
    global dicetype
    global dicetypeselected
    if dicetypeselected >= 4:
        dicetypeselected = 0
    else:
        dicetypeselected += 1
    dicetype_label.configure(text=dicetype[dicetypeselected])
    Change_diceimg(dicetype[dicetypeselected])

def dice_dec():
    global dicetype
    global dicetypeselected
    if dicetypeselected <= 0:
        dicetypeselected = 4
    else:
        dicetypeselected -= 1
    dicetype_label.configure(text=dicetype[dicetypeselected])
    Change_diceimg(dicetype[dicetypeselected])

def atc_inc():
    global Attackmod
    Attackmod += 1
    atc_label.configure(text=Attackmod)

def atc_dec():
    global Attackmod
    Attackmod -= 1
    atc_label.configure(text=Attackmod)

def mod_inc():
    global Damagemod
    Damagemod += 1
    dam_label.configure(text=Damagemod)

def mod_dec():
    global Damagemod
    Damagemod -= 1
    dam_label.configure(text=Damagemod)
    
#button
btn_inc_dice = Button(root, text = ">",fg= "blue", command=dice_inc,height= 1, width=3, font=("Arial",20))
btn_dec_dice = Button(root, text = "<",fg= "blue", command=dice_dec,height= 1, width=3, font=("Arial",20))

btn_inc_atc = Button(root, text = ">",fg= "blue", command=atc_inc,height= 1, width=3, font=("Arial",20))
btn_dec_atc = Button(root, text = "<",fg= "blue", command=atc_dec,height= 1, width=3, font=("Arial",20))

btn_inc_mod = Button(root, text = ">",fg= "blue", command=mod_inc,height= 1, width=3, font=("Arial",20))
btn_dec_mod = Button(root, text = "<",fg= "blue", command=mod_dec,height= 1, width=3, font=("Arial",20))

#set Button grid
btn_inc_dice.grid(column=3,row=1)
btn_dec_dice.grid(column=1,row=1)

btn_inc_atc.grid(column=3,row=3)
btn_dec_atc.grid(column=1,row=3)

btn_inc_mod.grid(column=3,row=5)
btn_dec_mod.grid(column=1,row=5)

#execute Tkinter
root.mainloop()
