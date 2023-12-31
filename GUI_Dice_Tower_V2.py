import tkinter.messagebox
import customtkinter
from PIL import ImageTk, Image
import os
from DiceTower import *

#changes directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    dicetypes=["D4","D6","D8","D10","D12"]
    currentDice = 0
    DiceTypeVAL="D4"
    DamageModVAL = 0
    AttackModVAL = 0
    RolledString = ""

    #photos Import
    diceimagesize = 100
    DiceTypeImageD4 = customtkinter.CTkImage(light_image=Image.open(os.path.join("D4.png")), size=(diceimagesize , diceimagesize))
    DiceTypeImageD6 = customtkinter.CTkImage(light_image=Image.open(os.path.join("D6.png")), size=(diceimagesize , diceimagesize))
    DiceTypeImageD8 = customtkinter.CTkImage(light_image=Image.open(os.path.join("D8.png")), size=(diceimagesize , diceimagesize))
    DiceTypeImageD10 = customtkinter.CTkImage(light_image=Image.open(os.path.join("D10.png")), size=(diceimagesize , diceimagesize))
    DiceTypeImageD12 = customtkinter.CTkImage(light_image=Image.open(os.path.join("D12.png")), size=(diceimagesize , diceimagesize))

    #Dice Dic
    dice_image_dic = {
        "D4": DiceTypeImageD4,
        "D6": DiceTypeImageD6,
        "D8": DiceTypeImageD8,
        "D10": DiceTypeImageD10,
        "D12": DiceTypeImageD12
    }

    def __init__(self):
        super().__init__()
        self.Dt1 = DiceTower()

        # configure window
        self.title("CustomTkinter complex_example.py")
        self.geometry(f"{480}x{800}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        
        #creates spot for images
        self.rightImages = customtkinter.CTkFrame(self)
        self.rightImages.grid(row = 0,column = 1,)

        # create sidebar frame with widgets
        self.mainSection = customtkinter.CTkFrame(self, width=110, corner_radius=0)
        self.mainSection.grid(row=0, column=0, rowspan=7, sticky="nsew")
        self.mainSection.grid_rowconfigure(7, weight=1)

        #creat Title Bar
        self.TitleBar = customtkinter.CTkFrame(self, height= 70,width=480,fg_color="black",corner_radius=0)
        self.TitleBar.grid(row=0,column = 0,columnspan = 7,sticky ="n")
        self.TitleBarLable = customtkinter.CTkLabel(self.TitleBar,text_color= "Blue",text ="Auto Dice Tower",height=70,width=480,font=("Times",-60))
        self.TitleBarLable.grid(row=0,column = 0,columnspan = 7,sticky ="n")
        #Side bar buttons

        self.Roll = customtkinter.CTkButton(
            self.rightImages,
            command=self.RollDice,
            text="Roll",
            width=50,
            height=20,
            font=("Times",-50),
        )
        self.Roll.grid(row=2,column=0,pady=20,padx=20)
        
        self.spacertop = customtkinter.CTkLabel(self.rightImages, text="")
        self.spacertop.grid(row=0,column=0)
       
        self.spacerBottom = customtkinter.CTkLabel(self.rightImages, text="")
        self.spacerBottom.grid(row=4,column=0)

        self.RolledOut = customtkinter.CTkLabel(
            self.rightImages,
            text="No Roll Info",
            width=50,
            height=20,
            font=("Times",-25),
        )
        self.RolledOut.grid(row=3,column=0,pady=20,padx=20)
           
        #Dicetype
        self.dicetypedec = customtkinter.CTkButton(
            self.mainSection,
            command=self.DiceTypeDecButton,
            text="<",
            width=50,
            height=20,
            font=("Times",-50),
            )
        self.dicetypedec.grid(row=2,column=1, padx=10,pady=10)
        self.dicetypeinc = customtkinter.CTkButton(
            self.mainSection,
            command=self.DiceTypeIncButton,
            text=">",
            width=50,
            height=20,
            font=("Times",-50),
            )
        self.dicetypeinc.grid(row=2,column=3, padx=10,pady=10)

        #Attackmod
        self.AttackModdec = customtkinter.CTkButton(
            self.mainSection,
            command=self.AttackModDecButton,
            text="<",
            width=50,
            height=20,
            font=("Times",-50)
            )
        self.AttackModdec.grid(row=4,column=1, padx=10,pady=10)
        self.AttackModinc = customtkinter.CTkButton(
            self.mainSection,
            command=self.AttackModIncButton,
            text=">",
            width=50,
            height=20,
            font=("Times",-50)
            )
        self.AttackModinc.grid(row=4,column=3, padx=10,pady=10)

        #Damagemod
        self.DamageModdec = customtkinter.CTkButton(
            self.mainSection,
            command=self.DamageModDecButton,
            text="<",
            width=50,
            height=20,
            font=("Times",-50),
            anchor="e"
            )
        self.DamageModdec.grid(row=6,column=1, padx=10,pady=10)
        self.DammafeModinc = customtkinter.CTkButton(
            self.mainSection,
            command=self.DamageModIncButton,
            text=">",
            width=50,
            height=20,
            font=("Times",-50),
            anchor="w"
            )
        self.DammafeModinc.grid(row=6,column=3, padx=10,pady=10)

        #sidebartext
        #spacers
        self.spacerLable = customtkinter.CTkLabel(
            self.mainSection,
            text="",
            )
        self.spacerLable.grid(row=0,column=0,pady=20)
        self.spacerLeftSideLable = customtkinter.CTkLabel(
            self.mainSection,
            text="",
            )
        self.spacerLeftSideLable.grid(row=0,column=4,padx=10,rowspan=6)
        self.spacerRightSideLable = customtkinter.CTkLabel(
            self.mainSection,
            text="",
            )
        self.spacerRightSideLable.grid(row=0,column=0,padx=10,rowspan=6)
        #dicetype
        self.DiceTypeLable = customtkinter.CTkLabel(
            self.mainSection,
            text="Damage Dice",
            anchor="s",
            font=("Times",-30)
            )
        self.DiceTypeLable.grid(row=1,column=1,pady=10,columnspan=3)

        #Attack modifer
        self.AttackModLable = customtkinter.CTkLabel(
            self.mainSection,
            text="Attack Modifer",
            anchor="s",
            font=("Times",-30)
            )
        self.AttackModLable.grid(row=3,column=1,pady=10,columnspan=3)

        #Damage modifer
        self.DamageModLable = customtkinter.CTkLabel(
            self.mainSection,
            text="Damage Modifer",
            anchor="s",
            font=("Times",-30)
            )
        self.DamageModLable.grid(row=5,column=1,pady=10,columnspan=3)  

        #numbers for the 3 Values
        self.dicetypeValLable = customtkinter.CTkLabel(
            self.mainSection,
            text=self.DiceTypeVAL,
            font=("Times",-30)
        )
        self.dicetypeValLable.grid(row=2,column=2)

        self.DamageModValLable = customtkinter.CTkLabel(
            self.mainSection,
            text=self.DamageModVAL,
            font=("Times",-30)
        )
        self.DamageModValLable.grid(row=6,column=2)

        self.AttackModValLable = customtkinter.CTkLabel(
            self.mainSection,
            text=self.AttackModVAL,
            font=("Times",-30)
        )
        self.AttackModValLable.grid(row=4,column=2)

        #Dice Image
        #Set Start
        self.DiceTypeImageLable = customtkinter.CTkLabel(self.rightImages,image=self.DiceTypeImageD4, text='')
        self.DiceTypeImageLable.grid(column=0, row=1,pady=20,padx=20,stick="s")

        #Dice Changer
    def Change_diceimg(self,newDice):
            # Check if newDice is in the dictionary
        if newDice in self.dice_image_dic:
                # Configure diceImage_label with the corresponding image
            self.DiceTypeImageLable.configure(image=self.dice_image_dic[newDice])
        else:
            print("Error: Invalid dice type")
            self.DiceTypeImageLable.configure(image=self.DiceTypeImageD4)  # Fallback to D4 image
                    #Add an error image?

    def RollDice(self):
       self.Dt1.GetRoll()
       self.RolledString = str(self.Dt1)
       self.RolledOut.configure(text=self.RolledString)      
        
        #Button commands
    def DiceTypeIncButton(self):
        self.Dt1.IncDamDie()
        if (self.currentDice) >= 4:
            self.currentDice = 0
        else:
            self.currentDice += 1
        newdice = self.dicetypes[self.currentDice]
        self.dicetypeValLable.configure(text = (newdice))
        self.Change_diceimg(self.dicetypes[self.currentDice])

    def DiceTypeDecButton(self):
        self.Dt1.DeIncDamDie()
        if (self.currentDice) <= 0:
            self.currentDice = 4
        else:
            self.currentDice -= 1
        newdice = self.dicetypes[self.currentDice]
        self.dicetypeValLable.configure(text = (newdice))
        self.Change_diceimg(self.dicetypes[self.currentDice])


    def AttackModIncButton(self):
        self.AttackModVAL += 1
        self.Dt1.AddAtckMod()
        if self.AttackModVAL > 0:
            self.AttackModValLable.configure(text="+" + str(self.AttackModVAL))
        else:
            self.AttackModValLable.configure(text=self.AttackModVAL)

    def AttackModDecButton(self):
        self.AttackModVAL -= 1
        self.Dt1.SubAtckMod()
        if self.AttackModVAL > 0:
            self.AttackModValLable.configure(text="+" + str(self.AttackModVAL))
        else:
            self.AttackModValLable.configure(text=self.AttackModVAL)


    def DamageModIncButton(self):
        self.DamageModVAL += 1
        self.Dt1.AddDamMod()
        if self.DamageModVAL > 0:
            self.DamageModValLable.configure(text="+" + str(self.DamageModVAL))
        else:
            self.DamageModValLable.configure(text=self.DamageModVAL)

    def DamageModDecButton(self):
        self.Dt1.SubDamMod()
        self.DamageModVAL -= 1
        if self.DamageModVAL > 0:
            self.DamageModValLable.configure(text="+" + str(self.DamageModVAL))
        else:
            self.DamageModValLable.configure(text=self.DamageModVAL)

if __name__ == "__main__":
    app = App()
    app.mainloop()
